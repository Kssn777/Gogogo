Plaintext=input('请输入明文： \n')
num=input('请输入偏移值： \n')
x=int(num)
print('密文为: ')
for i in range(0,len(Plaintext)):
    if Plaintext[i]==' ':
        print(' ',end= '')
    if (65<= ord(Plaintext[i])<= (90-x)) or (97<=ord(Plaintext[i])<=(122-x)):
        print(chr(ord(Plaintext[i])+x),end='')
    if ((90-x)<ord(Plaintext[i])<=90) or ((122-x)<ord(Plaintext[i])<=122):
        print(chr(ord(Plaintext[i])-26+x),end='')

