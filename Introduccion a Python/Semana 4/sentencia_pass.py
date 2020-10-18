def a_function(x):
    result = 0
    if x > 0 and x < 5:
        result = x ** 2
    elif x >= 5 and x < 10:
        pass #no hace nada
    else:
        result = (x ** 4) + 1
    
    return result

print(a_function(2))
print(a_function(7))
print(a_function(12))