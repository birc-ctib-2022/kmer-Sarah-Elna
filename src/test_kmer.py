# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from kmer import *

def test_kmer():
    assert kmer('accttga', 2) == ['ac', 'cc', 'ct', 'tt', 'tg', 'ga']

def test_unique_kmers():
    assert unique_kmers('accttaccga', 2) == {'ac', 'cc', 'ct', 'tt', 'ta', 'cg', 'ga'}

def test_count_kmers():
    assert count_kmers('acctacct', 2) == {'ac':2, 'cc':2, 'ct':2, 'ta':1}