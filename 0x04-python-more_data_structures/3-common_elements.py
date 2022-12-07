#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_languages = []
    for set_1_language in set_1:
        for set_2_language in set_2:
            if set_1_language == set_2_language:
                common_languages.append(set_2_language)
    return common_languages
