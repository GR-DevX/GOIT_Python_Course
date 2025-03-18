import random
# dice=random.randint(1,6)
# print(f"dice: {dice}")

# f1=random.random()#  [0,1)
# print(f1)
# print(round(9*f1+1,2)) # [1,10)


# print(random.randrange(11)) # [0,10)
# print(random.randint(0,10)) # [0,10)

# cards=[2,3,4,5,6,7,8,9,'j','q','k','a']
# print(cards)
# for _ in range(10):
#     random.shuffle(cards)
# print(cards)

fruits=['apple', 'banana', 'orange', 'mango']
c_fruits={'apple':0, 'banana':0, 'orange':0, 'mango':0}
# for _ in range(1000):
    # chosen=random.choices(fruits,[100,10,10,1],k=7) #дає повтори при виборі
    # for f in chosen:
    #     c_fruits[f]+=1
# choice=random.sample(fruits,k=2)
#print(chosen)

# price=random.uniform(50,100)
# print(f'price: {price:.2f}')

# state=random.getstate()
# print(random.randint(1,5))
# print(state)
# random.setstate(state)
# print(random.randint(1,5))