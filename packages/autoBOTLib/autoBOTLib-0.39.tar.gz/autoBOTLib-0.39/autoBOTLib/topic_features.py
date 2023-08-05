
import logging
from collections import defaultdict
logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
logging.getLogger().setLevel(logging.INFO)

import pandas as pd
import scipy.io
import numpy as np
from scipy.sparse import csgraph,csr_matrix
from sklearn.decomposition import TruncatedSVD
import matplotlib.pyplot as plt
import tqdm
from collections import OrderedDict
import gensim
import networkx as nx

class TopicDocs:

    def __init__(self, ndim = 128,
                 random_seed = 1965123,
                 verbose = True,
                 num_rep = 5,
                 targets = None):

        """
        Class initialization method.

        :param ndim: Number of latent dimensions
        :param targets: The target vector
        :param random_seed: The random seed used
        :param ed_cutoff: Cutoff for fuzzy string matching when comparing documents
        :param doc_limit: The max number of documents to be considered.
        :param verbose: Whether to have the printouts
        
        """
        
        self.ndim = ndim
        self.num_rep = num_rep
        self.verbose = verbose
        self.random_seed = random_seed

        
    def fit(self, text_list):

        """
        The fit method.

        :param text_list: List of input texts
        
        """

        if not type(text_list) == list:
            text_list = text_list.values.tolist()

        new_tlist = []
        for document in text_list:
            tokens = [x.lower() for x in document.strip().split(" ")]
            new_tlist.append(tokens)
            
        text_list = new_tlist
        del new_tlist
        dictionary = gensim.corpora.Dictionary(text_list)
        corpus = [dictionary.doc2bow(text) for text in text_list]
        ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = int(np.sqrt(self.ndim)), id2word = dictionary, passes=20)

        topics = ldamodel.print_topics(num_words = self.num_rep)
        for topic in topics:
            print(topic)

    def transform(self, new_documents):

        """
        Transform method.

        :param new_documents: The new set of documents to be transformed.
        :return all_embeddings: The final embedding matrix
        
        """

        if not type(new_documents) == list:
            text_list = new_documents.values.tolist()

        if self.verbose:
            logging.info("Transforming new documents.")
            
        

    def fit_transform(self, documents, b = None):

        """
        The sklearn-like fit-transform method.

        """
        
        self.fit(documents)
        return self.transform(documents)

    def get_feature_names(self):        
        return list(["topic_"+str(x) for x in range(self.ndim)])

if __name__ == "__main__":
    
    example_text = pd.read_csv("../data/pan-2017-age/train.tsv", sep="\t")['text_a']
    labels = pd.read_csv("../data/pan-2017-age/train.tsv", sep="\t")['label'].values.tolist()
    clx = TopicDocs()
    sim_features = clx.fit_transform(example_text)

    import matplotlib.pyplot as plt
    import seaborn as sns
    import operator
    
    from sklearn.linear_model import LogisticRegression
    from sentence_embeddings import *
    from sklearn.model_selection import cross_val_score
    from sklearn.dummy import DummyClassifier

    # dem = documentEmbedder()
    # dem_features = dem.fit_transform(example_text).todense()

    # clf = LogisticRegression()
    # lc = labels.copy()
    # cross_val_score = cross_val_score(clf, dem_features, lc, cv = 5)
    # print(np.mean(cross_val_score), "doc2vec")

    # clf = LogisticRegression()
    # lc = labels.copy()
    # cross_val_score = cross_val_score(clf, sim_features, lc, cv = 5)
    # print(np.mean(cross_val_score), "dsim")
