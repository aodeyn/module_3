def get_multiplied_digits(namber):
    str_number = str(namber)
    first = int(str_number[0])
    if int(str_number) > 0 and len(str_number) >1:
        first = first * get_multiplied_digits(int(str_number[1:]))
    return (first)

result = get_multiplied_digits(40203)
print(result)