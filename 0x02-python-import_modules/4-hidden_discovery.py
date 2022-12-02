#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    all_names = dir(hidden_4)
    for index in range(len(all_names)):
        if all_names[index][0] != '_' and all_names[index][1] != '_':
            print(all_names[index])
