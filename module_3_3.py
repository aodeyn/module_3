def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(12,True,'Hello!')
print_params(4,2)
print_params(3)
print_params()
print_params(b=25)
print_params(c = [1,2,3])
values_list = [8,'Hello!',[2,3,5]]
print_params(*values_list)
values_dict = {'a' : 7, 'b' : 9, 'c' : 13}
print_params(**values_dict)
values_list_2 = [45.64, 'Глубина погружения']
print_params(*values_list_2,60)

