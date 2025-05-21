with open("file.txt", "r") as f:
    print("Read mode:")
    print(f.read())

with open("file.txt", "w") as f:
    f.write("Written using 'w' mode\n")

with open("file.txt", "a") as f:
    f.write("Appended using 'a' mode\n")
