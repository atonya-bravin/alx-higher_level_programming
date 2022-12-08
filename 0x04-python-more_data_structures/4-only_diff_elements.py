#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    non_common_languages = []
    for set_1_language in set_1:
        if set_1_language not in set_2:
            non_common_languages.append(set_1_language)
    for set_2_language in set_2:
        if set_2_language not in set_1:
            non_common_languages.append(set_2_language)
    return non_common_languages
