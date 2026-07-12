text = input("Enter a string: ")

clean = text.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
