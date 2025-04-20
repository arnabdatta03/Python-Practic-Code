str=input("Enter the string:")
count=0
vow="  "
for char in str:
    if char in 'aeiouAEIOU':
        vow += char
        count=count+1
        str=str.replace(char,"#")
print(str)
print("Vowels in the string is:", vow, count)