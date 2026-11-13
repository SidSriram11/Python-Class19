a = ["abc","cfc","xyz","aba","1221"]

count = 0

for i in a:
    if i[0] == i[-1]:
        count = count +1
        print(i)

print(f"The number of words starting and ending with the same letter/value is {count}")