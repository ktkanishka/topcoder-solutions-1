def construct_suffix_array(string):
    return map(lambda x: len(string) - len(x), sorted([string[i:] for i in xrange(len(string))]))
