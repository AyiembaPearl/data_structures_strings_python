my_list = [ ]
print(my_list)

my_list = [ ]
numbers = [10, 20, 30, 40]
my_list.append(numbers)
print(my_list)

my_list = [10, 20, 30, 40]
my_list.insert(1, 15)
print(my_list)

my_list = [10, 15, 20, 30, 40]
num = [50, 60, 70]
my_list.extend(num)
print(my_list)

my_list = [10, 15, 20, 30, 40, 50, 60, 70]
my_list.pop()
print(my_list)

my_list = [10, 15, 20, 30, 40, 50, 60]
my_list.sort()
print(my_list)

my_list = [10, 15, 20, 30, 40, 50, 60]
print(my_list.index(30))