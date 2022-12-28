#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for index in range(list_length):
        try:
            if ((type(my_list_1[index]) is int) or ((type(my_list_1[index]) is float)) and \
                ((type(my_list_2[index]) is int) or (type((my_list_2[index] is float))))):
                result = my_list_1[index] / my_list_2[index]
            else:
                raise(TypeError)
        except (IndexError):
            print("out of range")
            result = 0
        except (ZeroDivisionError):
            print("division by 0")
            result = 0
        except (TypeError):
            print("wrong type")
            result = 0
        finally:
            result_list.append(result)
    return (result_list)
