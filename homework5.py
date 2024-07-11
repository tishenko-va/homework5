immutable_var = 1, True, 'student', 2
print(immutable_var)
# immutable_var[0] = 300 не получается изменить, потому что кортеж не поддерживает обращение по элементам
mutable_list = [1, 2, 'work', 'hurd']
print(mutable_list)
mutable_list[0] = 100
mutable_list [2] = 'relax'
print(mutable_list)