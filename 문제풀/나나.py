from string import ascii_letters as ac


s = 'A High Point'

passwd = ac
passwd1, passwd2 = passwd[::2], passwd[1::2]
new_passwd = passwd1+passwd2
print(new_passwd)


result = ''
for elm in s:
    if elm==" ":result+=" "
    else:result += new_passwd[passwd.index(elm)]
print(result)