#sum and average of all

a = [4,7,2,4,2,5,61,2,3,4,5,9,0,12345]

sum = 0

for i in a:
    sum = sum + i
print(sum)

size = len(a)
print(f"The size of the list is : {size}")

average = sum/size
print(f"The average of your numbers is : {average}")

a.sort()
print(a)

print(f"The smallest element is {a[0]}")
print(f"The largest element is {a[-1]}")