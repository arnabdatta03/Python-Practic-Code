f=open("find.txt","r")
d=f.read()
a_count = e_count = i_count = o_count = u_count = A_count = E_count = I_count = O_count = U_count = 0
for char in d:
    if char.lower() == 'a':
        a_count += 1
    elif char.lower() == 'e':
        e_count += 1
    elif char.lower() == 'i':
        i_count += 1
    elif char.lower() == 'o':
        o_count += 1
    elif char.lower() == 'u':
        u_count += 1
    if char.upper() == 'A':
        A_count += 1
    elif char.upper() == 'E':
        E_count += 1
    elif char.upper() == 'I':
        I_count += 1
    elif char.upper() == 'O':
        O_count += 1
    elif char.upper() == 'U':
        U_count += 1
print("Count of 'a':", a_count)
print("Count of 'e':", e_count)
print("Count of 'i':", i_count)
print("Count of 'o':", o_count)
print("Count of 'u':", u_count)
print("Count of 'A':", A_count)
print("Count of 'E':", E_count)
print("Count of 'I':", I_count)
print("Count of 'O':", O_count)
print("Count of 'U':", U_count)