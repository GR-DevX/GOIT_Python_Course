#lambada-функція
f=lambda x,y:x+y
# def g(x,y):
#     return x+y
print(f(3,5))
print((lambda x,y:x+y*x)(3,6))

nums=[i for i in range(10)]
print(nums)
def f(x):
    return -x
print(sorted(nums,key=f)) #lambda x:-x))