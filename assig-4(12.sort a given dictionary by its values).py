my_dict={'a':10,'b':20,'c':5,'d':15}
sorted_dict=dict(sorted(my_dict.items(),key=lambda item:item[1]))
print(sorted_dict)
