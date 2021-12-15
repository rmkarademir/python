l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5,"c",[8,90,"at"],[11,12,13],[42,[43,[44,[45]]]]]
l2 = [[1, 2], [3, 4], [5, 6, 7,[8,9,10]]]

def flatten(l):
    newl = []
    x = True
    while (x):
        if type(l[-1])!=list:
            x = False
        for i in range(len(l)):
            if type(l[i])==list:
                x = True
                break
        for item in l:
            if type(item)==list:
                newl.extend(item)
            else:
                newl.append(item)
        l = newl.copy()
        newl = []
    print(l)

def returner(l):
    l = l[::-1]
    for i in range(len(l)):
        if(type(l[i])==list):
            l[i] = l[i][::-1]
            for j in range(len(l[i])):
                if(type(l[i][j])==list):
                    l[i][j] = l[i][j][::-1]                  
    print(l) 
    
flatten(l)
returner(l2)