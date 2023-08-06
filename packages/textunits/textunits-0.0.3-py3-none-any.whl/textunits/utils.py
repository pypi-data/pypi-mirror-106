# contain utilities function for different modules

def convert_regex_phrases(list_words: list,
                          leftwrap: str = None,
                          rightwrap: str = None,
                          textwrap: str = None,
                          ) -> str:
    """ Convert list_of_words into a "OR" regex phrase checking Expression"""
    leftwrap, rightwrap = (textwrap, textwrap) if textwrap else (
        leftwrap, rightwrap)

    def left_func(w): return str(leftwrap) + str(w) if leftwrap else str(w)

    def right_func(w): return str(w) + str(rightwrap) if rightwrap else str(w)

    for func in [left_func, right_func]:
        list_words = list(map(func, list_words))

    words = '|'.join(list_words)
    return '(' + words + ')'
