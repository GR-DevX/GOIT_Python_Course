from collections import Counter
marks=['4',2,'4',6,7,4,2,3,4,5,6,2,3,4,2,2,3,4,5,4]
# marks=[int(i) for i in marks]
marks_count=Counter(marks)
print(marks_count)
print(marks_count.most_common())
print(marks_count.most_common(1))
print(marks_count.most_common(2))
print(Counter('Hello world hello'))#.most_common(2))
print(Counter('some text is long, some is short, but long and short are not some'))
print(Counter('some text is long, some is short, but long and short are not some'.split()))