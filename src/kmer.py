"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    >>> kmer('ACGTCC', 2)
    ['AC', 'CG', 'GT', 'TC', 'CC']
    """
    result = []
    for i in range(0, len(x)-k):
        result.append(x[i:i+k])
    return result


def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    >>> unique_kmers('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'gtc', 'tcg']

    >>> unique_kmers('AAATAAGAAC', 2)
    ['AA', 'AT', 'TA', 'AG', 'GA', 'AC']
    """
    result = []
    kmer_list = kmer(x, k)
    for i in range(0, len(kmer_list)):
        if kmer_list[i] not in result:
            result.append(kmer_list[i])
        else:
            continue
    return result



def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    >>> count_kmers('tttaaatttaaa', 3)
    {'ttt':2, 'tta':2, 'taa'=2, 'aaa'=2}
    """
    result = {}
    unique_kmer_list = unique_kmers(x, k)
    for i in range(0, len(unique_kmer_list)):
        search_kmer = unique_kmer_list[i]
        search_count = 0
        for i in range(0, len(x)-k):
            if search_kmer == x[i:i+k]:
                search_count += 1
        result[search_kmer] = search_count
    return result
            
