my_list=[]
my_list.append(10)
my_list += [20, 30, 40]
my_list.insert(1,15)

another_list = [50, 60, 70]
my_list.extend(another_list)
my_list.pop()
my_list.sort()
indice = my_list.index(30)
print(indice)