#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            dividend = my_list_1[i] if i < len(my_list_1) else 0
            divisor = my_list_2[i] if i < len(my_list_2) else 0

            if isinstance(dividend, (int, float)) and isinstance(divisor, (int, float)):
                if divisor == 0:
                    raise ZeroDivisionError
                result.append(dividend / divisor)
            else:
                print("wrong type")
                result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)

    return result
