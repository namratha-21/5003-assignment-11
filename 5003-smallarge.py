NumList = []
Number = int(input("enter the total numbers: "))
for i in range(1, Number + 1):
    value = int(input(" enter the number of %d Element : " %i))
    NumList.append(value)

print("The Smallest Element in this List is : ", min(NumList))
print("The Largest Element in this List is : ", max(NumList))