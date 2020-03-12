"""Project 4 for CPE 202
Search Engine
Author: Jae Park
"""

import os
import math
from hashtables import *

def main(dir_name):
    stoptable = HashTableSepchain()
    import_stopwords('stop_words.txt', stoptable)
    googleTM = SearchEngine(dir_name, stoptable)
    while True:
        query = input('Enter search query: ')
        if query.startswith('q'):
            break
        elif query.startswith('s:'):

            results = googleTM.search(query[2:])
            for file in results:
                print(file)
        else:
            print("I'm sorry; I can't do that for you.")



class SearchEngine:
    def __init__(self, directory, stopwords):
        self.doc_length = HashTableSepchain()
        self.term_freqs = HashTableSepchain()
        self.stopwords = stopwords
        self.index_files(directory)

    def read_file(self, infile_path):
        with open(infile_path) as infile:
            lines = infile.readlines()
        return lines

    def parse_words(self, lines):
        all_words = []
        for line in lines:
            words = line.split()
            for word in words:
                if word != "":
                    all_words.append(word.lower())
        return self.exclude_stopwords(all_words)

    def exclude_stopwords(self, all_words):
        words = []
        for word in all_words:
            if word not in self.stopwords:
                words.append(word)
        return words

    def count_words(self, filename, words):
        self.doc_length[filename] = len(words)
        for word in words:
            if word not in self.term_freqs:
                self.term_freqs[word] = HashTableSepchain()
            if filename not in self.term_freqs[word]:
                self.term_freqs[word][filename] = 1
            else:
                self.term_freqs[word][filename] += 1

    def index_files(self, directory):
        """index all text files in a given directory
        Args:
            directory (str) : the path of a directory
        """
        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)
            if os.path.isfile(path):
                parts = os.path.splitext(path)
                if parts[1] == '.txt':
                    lines = self.read_file(path)
                    words = self.parse_words(lines)
                    self.count_words(path, words)

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
        scores = HashTableSepchain()
        for t in terms:
            if t in self.term_freqs:
                t_table = self.term_freqs[t]
                for filename in t_table.keys():
                    if filename not in scores:
                        scores[filename] = 0
                    scores[filename] += self.get_wf(t_table[filename])
        scores_list = []
        for filename in scores.keys():
            score = scores[filename] / self.doc_length[filename]
            scores_list.append((filename, score))
        return scores_list

    def rank(self, scores):
        """ranks files in the descending order of relevancy
        Args:
            scores(list) : a list of tuples: (filename, score)
        Returns:
            list : a list of tuples: (filename, score) sorted in descending order of relevancy
        """
        self.rank_quick_sort(scores, 0, len(scores)-1)
        return scores

    def rank_quick_sort(self, items, lo, hi):
        """Author: Jae Park
        Quicksort algorthim that also counts number of comparisons.
        Args:
            items(list): list to be sorted
            lo(int): lower bound
            hi(int): upper bound
        Returns:
            int: number of comparisons
        """
        comparisons = 0
        if lo >= hi:
            return comparisons
        mid = (lo + hi) // 2
        pivot = items[mid][1]
        lt, gt, i = lo, hi, lo
        while i <= gt:
            if items[i][1] > pivot:
                temp = items[i]
                items[i] = items[lt]
                items[lt] = temp
                i += 1
                lt += 1
                comparisons += 1
            elif items[i][1] < pivot:
                temp = items[i]
                items[i] = items[gt]
                items[gt] = temp
                gt -= 1
                comparisons += 2
            else:
                i += 1
                comparisons += 2
        comparisons += self.rank_quick_sort(items, lo, lt - 1)
        comparisons += self.rank_quick_sort(items, gt + 1, hi)
        return comparisons

    def search(self, query):
        """ search for the query terms in files
        Args:
            query (str) : query input
        Returns:
            list : list of files in descending order or relevancy
        """
        terms = self.parse_words([query])
        search_map = HashTableSepchain()
        for term in terms:
            search_map[term] = 0
        search_list = self.get_scores(search_map.keys())
        search_list = self.rank(search_list)
        file_list = []
        for pair in search_list:
            file_list.append(pair[0] + ' (score: ' + str(pair[1]) + ')')
        return file_list


if __name__ == '__main__':
    main('docs')

