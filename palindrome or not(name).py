name = input("Enter a name: ")

reverse = name[::-1]

if name == reverse:
    print("Palindrome name")
else:
    print("Not a palindrome name")
