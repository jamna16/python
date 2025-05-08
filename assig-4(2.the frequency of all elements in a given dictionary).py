my_dict={'a':2,'b':3,'c':2,'d':4,'e':3}
freq={}
for value in my_dict.values():
    if value in freq:
        freq[value]+=1
    else:
        freq[value]=1
print(freq)
                                                 
