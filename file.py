file = (r"C:\Users\arnabdatta\Documents\name1= arnab.txt")

lines = 0
words = 0

with open(file, 'r') as f:
    for line in f:
        if not line.startswith('t'):
            lines += 1
            words += len(line.split())

print("Number of lines not starting with 't':", lines)
print("Number of words in the file:", words)
