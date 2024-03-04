# Checking whether a string is palindrome or not
string = input("Enter a string to checking if it is palindrome or not: ")
if string == string[::-1]:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")

# List Operations
lst = [20, 4, 65, 345, 34, 567, 324, 8, 42, 432, 86, 42, 5756]
print("lst =", lst)
lst.sort()
print("Sorted:", lst)
lst.pop(2)
print("lst.pop(2)", lst)
print("lst.index(8):", lst.index(8))
newlst = lst[2:7:2]
print("Slicing:", newlst)

# Use dictionaries to store and retrieve student grades.
stu_data = {}
n = int(input("Enter number of students you want to store the data of: "))
for _ in range(n):
    name = input("Enter the name: ")
    rollno = input("Enter the roll no: ")
    branch = input("Enter the branch: ")
    stu_data[rollno] = [name, branch]

search = input("Enter the roll no of the student you want to search: ")
run = True
while run:
    if search in list(stu_data.keys()):
        print(
            f"Name: {stu_data[search][0]}\nRoll No: {search}\nBranch: {stu_data[search][1]}"
        )
    else:
        print("404: Student Not Found!")
    run = int(input("Do you want to exit [1(yes)/0(no)]: "))
