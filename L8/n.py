#any
#all

nums=[0,False,5,'']
print(any(nums))
print(all(nums))
nums=[1,2,3,4]
print(all(nums))
nums=[2,4,6,8]
words=['Hello','World','Python']
print(all(word.istitle() for word in words))
print(f"Even nums:{all(x%2==0 for x in nums)}")