#Stack - млинці, останній прийшов - першим пішов, LIFO = FILO
def create_stack(): #створення стеку
    return [] # стек створюємо на основі списку

def is_empty(stack): #перевірка чи порожній
    return len(stack) == 0 # TRUE якщо порожній

def push(stack:list,item): # Додає елемент на вершину (в кінець) стеку
    stack.append(item)

def pop(stack:list): # повертає значення вершини і вилучає його
    if not is_empty(stack):
        return stack.pop()
    else:
        return None
    
def peak(stack:list): # повертає значення вершини
    if not is_empty(stack):
        return stack[-1]
    else:
        return None
    
if __name__=='__main__':
    mystack=create_stack()
    print('Стек створено:')
    print(mystack)#
    push(mystack,1)
    print('Стек після push:')
    print(mystack)#
    push(mystack,2)
    print('Стек після push:')
    print(mystack)#
    push(mystack,3)
    print('Стек після push:')
    print(mystack)#
    print(peak(mystack))
    print('Стек після peak:')
    print(mystack)#
    print(pop(mystack))
    print('Стек після pop:')
    print(mystack)#
    
