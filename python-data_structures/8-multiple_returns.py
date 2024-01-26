#!usr/bin/python3


def multiple_returns(sentence):
    if not sentence:
        f_char = None
        return (0, f_char)
    else:
        return (len(sentence), sentence[0])
