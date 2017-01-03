class Acronyms(object):
    def acronize(document):
        pass

def split_sentences(string):
    current_sentence_start_index = 0
    sentences = []
    for index, char in enumerate(string):
        if char in ('\n', ' '):
            if string[index + 1] in ('\n', ' '):
                sentences.append(string[current_sentence_start_index:index])
                current_sentence_start_index += 2
    return sentences
