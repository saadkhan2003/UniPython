my_list = ['orange', 'mango', 'banana', 'apple']
# print(my_list)
# print(type(my_list))



# print(my_list[3:5])


my_list2 = ['two','three']

# print(*(my_list + my_list2), sep ='\n')


my_list2.append('five')


my_list2.insert(0, 'one')
my_list2.insert(1, 'two')



print (my_list2.count('five'))
print (my_list2.count('one'))
print (my_list2.count('two'))

print (my_list2.index('five'))

my_list.extend(my_list2)
print(my_list)




