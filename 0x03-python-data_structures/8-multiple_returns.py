#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    else:
        sentence_information = ((len(sentence)), sentence[0])
        return sentence_information
