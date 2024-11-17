calls = 0
def count_calls():
    global calls
    calls += 1
def  string_info(str_1):
    count_calls()
    tuple_string = int(len(str_1)), str_1.upper(),str_1.lower()
    return(tuple_string)

def is_contains(str_2, list_1):
    str_2 = str_2.lower()
    count_calls()
    for i in range(len(list_1)):
        list_1[i] = list_1[i].lower()
    if str_2 in list_1:
        return('True')
    else:
        return('False')

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
