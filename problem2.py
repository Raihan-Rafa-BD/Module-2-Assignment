#Problem 2: Simple File Writing

name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
print("Name saved successfully.")
file.close()