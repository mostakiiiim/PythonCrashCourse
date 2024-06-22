numbers= [x for x in range(1,1000001)]

primeNumbers= [x%2!= 0 for x in numbers]


print(f"Minimum number is {min(numbers)}")
print(f"Minimum number is {max(numbers)}")
sum=0
for i in numbers:
    sum = sum + i
    i = i+1

print(sum)

#4-6
for i in range(1,20, 2):
    print(i)
#4-7

lists=[]
for i in range(3,31):
    list.append(i*3)

print(list)
