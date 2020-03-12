"""Project 4 for CPE 202
Search Engine
Author: Jae Park
"""

from hashtables import *

def main(dir_name):


class SearchEngine:
    def __init__(self, directory, stopwords):
        self.doc_length = HashTableSepchain()
        self.term_freqs = HashTableSepchain()
        self.stopwords = stopwords
        self.index_files(directory)

    def read_file(self, infile):
        with open() as infile:
            lines = infile.read()
        words = lines.split()
        words.strip()
        return words

    def parse_words(self, lines):
        pass
    def exclude_stopwords(self, words):
        pass
    def count_words(self, filename, words):
        pass
    def index_files(self, directory):
        """index all text files in a given directory
        Args:
            directory (str) : the path of a directory
        """
        pass
    def get_wf(self, tf):
        """computes the weighted frequency
        Args:
            tf (float) : term frequency
        Returns:
            float : the weighted frequency
        """
        if tf>0:
            wf = 1 + math.log(tf)
        else:
            wf = 0
        return wf
    def get_scores(self, terms):
        """creates a list of scores for each file in corpus
        The score = weighted frequency / the total word count in the file. Compute this score for each term in a query and sum all the scores.
        Args:
        terms (list) : a list of str
        Returns:
        list : a list of tuples, each containing the filename and its relevancy score
        """
        pass
    def rank(self, scores):
        """ranks files in the descending order of relevancy
        Args:
            scores(list) : a list of tuples: (filename, score)
        Returns:
            list : a list of tuples: (filename, score) sorted in descending order of relevancy
        """
    def search(self, query):
        """ search for the query terms in files
        Args:
            query (str) : query input
        Returns:
            list : list of files in descending order or relevancy
        """
