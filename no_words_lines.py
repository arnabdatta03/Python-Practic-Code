file_path = (r"C:\Users\arnabdatta\Documents\python-arnab.txt")

line_count = 0
word_count = 0

with open(file_path, 'r') as file:
    for line in file:
        line_count += 1
        words = line.split(' ')
        word_count += len(words)

print("Number of lines:", line_count)
print("Number of words:", word_count)
