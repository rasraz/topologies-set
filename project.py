def find_in_set_T(item):
    # if len(item)==1:item=item
    find=next(filter(lambda x:x==item,T),False)
    return find

def community(family_list):
    society=family_list[0]
    if 1<len(family_list):
        for ItemFamily in family_list[1:]:
            society=society|set(ItemFamily)
    # print('community:',society)
    return society

def subscription(family_list):
    society=family_list[0]
    if 1<len(family_list):
        for ItemFamily in family_list[1:]:
            society=society&set(ItemFamily)
    # print('subscription:',society,end='\n\n')
    return society

def list_to_set(subset):
    list=[]       
    list_sets=[]
    for i in subset:
        for j in i:
            list_sets.append(set(j))
        list.append(list_sets)
        list_sets=[]
    return list

def get_subsets(fullset):
    listrep = list(fullset)
    n = len(listrep)
    return [[listrep[k] for k in range(n) if i&1<<k] for i in range(2**n)]

def topologies_on_set(X):
    all_T=[]
    global T
    subX=get_subsets(get_subsets(X)[1:-1])
    subX=list_to_set(subX)
    for i in subX:
        T=[set(),X]+i
        # print(T)
        # print(4*'\t',T)
        subT=get_subsets(T)[1:]
        for e in subT:
            # print(e)
            C=community(e)
            status_C=find_in_set_T(C)
            if status_C==False:
                # print('C failed')
                break
            S=subscription(e)
            status_S=find_in_set_T(S)
            if status_S==False:
                # print('S failed')
                break
        if (status_C!=False)&(status_S!=False):all_T.append(T)
        # print('************************************************************************')
    return all_T
    
X={'a','b','c'}
topologies=topologies_on_set(X)
print('number of all T:',len(topologies))
print('all T:',end='\n\n')
for T in topologies:
    print(T)
