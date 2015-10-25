## Exam

def f(n):
    def g(m):
        m = 0
        for i in range(m):
            print i
            print m
    for i in range(n):
        print i
        g(n)


L = {'1':1, '2':2, '3':3}


L = [1,2,3]
d = {'a': 'b'}
def f(x):
    return 3


def sort1(lst):
    swapFlag = True
    iteration = 0
    count=0
    while swapFlag:
        swapFlag = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                count+=1
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
                swapFlag = True
        L = lst[:]  # the next 3 questions assume this line just executed
        if iteration ==3:
            print iteration
            print lst
            print L
        iteration += 1
    print "Count: "+str(count)
    return lst

def ser(limit,ascend):
    a=[]
    if ascend == True:
        for i in range(limit):
            a.append(i)
    else:
        for i in range(limit):
            a.append(limit-i-1)
    return a


def sort2(lst,n):
    count=0
    for iteration in range(len(lst)):
        minIndex = iteration
        minValue = lst[iteration]
        for j in range(iteration+1, len(lst)):
            if lst[j] < minValue:
                minIndex = j
                minValue = lst[j]
                count+=1
        temp = lst[iteration]
        lst[iteration] = minValue
        lst[minIndex] = temp

        L = lst[:]  # the next 3 questions assume this line just executed
        if iteration ==n:
            print iteration
            print L
            #print L
    return lst

def sort3(lst,n):
    count=0
    out = []
    for iteration in range(0,len(lst)):
        new = lst[iteration]
        inserted = False
        for j in range(len(out)):
            count += 1
            if new < out[j]:
                
                out.insert(j, new)
                inserted = True
                break
        if not inserted:
            count += 1
            out.append(new)

        L = out[:]  # the next 3 questions assume this line just executed
        if iteration ==n:
            print iteration
            print L

def sort4(lst,count=0):
    def unite(l1, l2):
        if len(l1) == 0:
            return l2
        elif len(l2) == 0:
            return l1
        elif l1[0] < l2[0]:
            return [l1[0]] + unite(l1[1:], l2)
        else:
            return [l2[0]] + unite(l1, l2[1:])

    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        count +=1
        front = sort4(lst[:len(lst)/2],count)
        back = sort4(lst[len(lst)/2:],count)
        print count
        L = lst[:]  # the next 3 questions assume this line just executed
        print front,back
        print L
        a = unite(front, back)
       
        return a


def unite(l1, l2):
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    elif l1[0] < l2[0]:
        return [l1[0]] + unite(l1[1:], l2)
    else:
        return [l2[0]] + unite(l1, l2[1:])

def getSublists(L,n):
    out=[]
    for i in range(len(L)-n+1):
        out.append(L[i:i+n])
    return out

L1 = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
L2= [1, 1, 1, 1, 4]

def longestRun(L):
    run=[]
    for i in range (len(L)):
        run.append(False)
        subLists=getSublists(L,i+1)
        for j in range(len(subLists)):
            if sorted(subLists[j])==subLists[j]:
                run.pop()
                run.append(True)
        if run[i]==False:
            run.pop()
            break
    return len(run)
