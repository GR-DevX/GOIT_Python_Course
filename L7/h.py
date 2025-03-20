def sq_gen(n=10):
    i=0
    while i<n:
        i+=1
        yield i*i

def reader(filename:str):
    l=' '
    with open(filename,'r') as f:
        while l!='':
            l=f.readline().strip()
            yield l.split()

if __name__=='__main__':
    pass
    gen_sq=sq_gen(100000000)
    for k in range(99):
        next(gen_sq)
    print(next(gen_sq))
    # l=[i for i in sq_gen(1000)]
    # print(l)
    # print(sq_gen())
    # gen=reader('text.txt')
    # for line in gen:
    #     print(line)
    #     if line[0]=='To':
    #         break
    # print('-'*20)
    # # gen2=reader('text.txt')
    # for line in gen:#gen2:
    #     print(line)
    
    # print([i for i in reader('text.txt')])
    
    
    # comprehension
    l=tuple(n for n in sq_gen(100) if str(n)[-1]=='0')
    l2=[n for n in reader('text.txt')]
    print()