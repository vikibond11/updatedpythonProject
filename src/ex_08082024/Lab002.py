print(2+2)
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", max(list1))
print("Largest element is:", min(list1))
# sorting the list
list1.sort()
print(list1)
print("Largest element is:", list1[-1])
list1.sort(reverse=True)
print(list1)
string = "one,two,three"
print(string.split(","))