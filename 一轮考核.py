print('模式1为加密，模式2为解密')
pattern=int(input('请输入模式几(1或2): '))
num=input('请输入偏移值： ')
x=int(num)
if pattern==1:
    with open('kaisa1.txt') as m:
        contents=m.read()
    print(contents,end=' ')   
    Plaintext=input('')
    print('密文为: ')
    R=''
    for i in range(0,len(Plaintext)):
        if Plaintext[i]==' ':
            print(' ',end='')
            r=' '
            R+=r
        if (65<= ord(Plaintext[i])<= (90-x)) or (97<=ord(Plaintext[i])<=(122-x)):
            print(chr(ord(Plaintext[i])+x),end='')
            r=chr(ord(Plaintext[i])+x)
            R+=r
        if ((90-x)<ord(Plaintext[i])<=90) or ((122-x)<ord(Plaintext[i])<=122):
            print(chr(ord(Plaintext[i])-26+x),end='')
            r=chr(ord(Plaintext[i])-26+x)
            R+=r
        filename='result.txt'
        with open(filename,'w')as file_obj:
            file_obj.write(R)
if pattern==2:
    with open('kaisa2.txt')as m:
        contents=m.read()
    print(contents,end=' ')
    Ciphertext=input('')
    print('明文为： ')
    R=''
    for i in range(0,len(Ciphertext)):
        if Ciphertext[i]==' ':
            print(' ',end='')
            r=' '
        if (65<= ord(Ciphertext[i])<=(65+x))or(97<=ord(Ciphertext[i])<=(97+x)):
            print(chr(ord(Ciphertext[i])+26-x),end='')
            r=chr(ord(Ciphertext[i])+26-x)
        if ((65+x)<ord(Ciphertext[i])<=90) or ((97+x)<ord(Ciphertext[i])<=122):
            print(chr(ord(Ciphertext[i])-x),end='')
            r=chr(ord(Ciphertext[i])-x)
        R+=r
        filename='result.txt'
        with open(filename,'w')as file_obj:
            file_obj.write(R)
            
    




