
t1 = "As inundações provocaram graves damnos na pharmácia batatas"
t2 = "As inundações provocaram graves danos na farmácia batats"

def find_corresp(t1,t2):
    dic = {}
    t1 = t1.split()
    t2 = t2.split()

    for i in range(len(t1)):
        if t1[i] != t2[i]:
            dic[t1[i]] = t2[i]
    print(dic)



find_corresp(t1,t2)