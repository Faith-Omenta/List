names=["Faith","Glenah","Darlene","Phylis","Melvin"]
first,second,third,*rest=names
print(first)
print(second)
print(*rest)

numbers=[25,64,876,93,26]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.pop()
print(numbers)


