"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.
    k must be positive and not zero.
    k must also be smaller than the length of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    >>> kmer('ACGTCC', 2)
    ['AC', 'CG', 'GT', 'TC', 'CC']
    """
    if k <= 0 or k > len(x):
        raise Except('NO! Bad k.')
    result = []
    for i in range(0, len(x)-k+1):
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
    result = set()
    kmer_list = kmer(x, k)
    for kmer_i in kmer_list:
        if kmer_i not in result:
            result.add(kmer_i)
    return result



def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    >>> count_kmers('tttaaatttaaa', 3)
    {'ttt': 2, 'tta': 2, 'taa': 2, 'aaa': 2, 'aat': 1, 'att': 1}
    """
    result = {}
    unique_kmer_list = unique_kmers(x, k)
    for unique_kmer in unique_kmer_list:
        search_count = 0
        for i in range(0, len(x)-k+1):
            if unique_kmer == x[i:i+k]:
                search_count += 1
        result[unique_kmer] = search_count
    return result
            
