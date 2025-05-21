def write_file(text):
    with open('file.txt', 'w') as f:
        f.write(text)

def append_file(text):
    with open('file.txt', 'a') as f:
        f.write(text)
