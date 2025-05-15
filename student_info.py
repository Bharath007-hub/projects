def read_file():
    f = open("student_infor.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def write_file(lines):
    f = open("student_infor.txt", "w")
    f.writelines(lines)
    f.close()

lines = read_file()
lines[2] = "ID: 3, Name: Charles Lee, Age: 23, Grade: B+\n"
write_file(lines)

for line in lines:
    print(line.strip())
