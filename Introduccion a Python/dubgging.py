result = None
a_number = 0
def a_function(a_number):
    if a_number % 2 == 0:

        if a_number % 10 == 0:
            result = a_number / 2
        elif a_number % 8 == 0:
            result = a_number / 4
        else:
            result = a_number - 1
    return result

#result_1 = a_function(20)
#print(result_1)