def match(s1,s2):
    count=0
    for i in range(min(len(s1),len(s2))):
        if s1[i].lower()==s2[i].lower():
            count=count+1
    return count
S1="winter"
S2="summer"
print("Total number of matches:")
print(match(S1,S2))
