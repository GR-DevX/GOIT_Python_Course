# Каррінг
# def add(a):
#     def add_b(b):
#         return a+b
#     return add_b

# # add_5=add(5)
# # result=add_5(3)
# # print (result)

# print(add(5)(3))
def discount(d):
    k=(100-d)/100
    def dis(p):
        return int(p*k)
    return dis

prices=[100,120,500,300,160]
discount_10=discount(10)
for price in prices:
    print(discount_10(price))