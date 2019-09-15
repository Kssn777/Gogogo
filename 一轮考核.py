print('模式1为加密，模式2为解密')
print('明文或密文只能由字母组成，否则将重新输入！')
print('拥有密文或明文的.txt文件要自己创建')
print('记得路径最后要把文件名.txt都打出来哦')
filename1=input('请把文件路径输入到这，并且文件中要有明文或密文，再自行选择模式进行加密或者解密: ')
filename2=input('请把输出结果时，程序会把输出结果以result.txt形式输出在你的电脑上，请输入其路径： ')
pattern=int(input('请输入模式几(1或2): '))
num=input('请输入偏移值： ')
x=int(num)
lst=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
if pattern==1:
    with open(filename1)as L:
        G=L.read()
        Plaintext=G
    R=''
    for u in Plaintext:
        if u not in lst:
            Plaintext=input('检测到明文中有不含有字母的元素，请重新输入明文： ')
    for i in range(0,len(Plaintext)):
        if Plaintext[i]==' ':
            r=' '
            R+=r
        if (65<= ord(Plaintext[i])<= (90-x)) or (97<=ord(Plaintext[i])<=(122-x)):
            r=chr(ord(Plaintext[i])+x)
            R+=r
        if ((90-x)<ord(Plaintext[i])<=90) or ((122-x)<ord(Plaintext[i])<=122):
            r=chr(ord(Plaintext[i])-26+x)
            R+=r
        with open(filename2,'w')as file_obj:
            file_obj.write(R)
if pattern==2:
    with open(filename1)as L:
        G=L.read()
        Ciphertext=G
    R=''
    for u in Ciphertext:
        if u not in lst:
            Ciphertext=input('检测到密文中有不含有字母的元素，请重新输入密文： ')
    for i in range(0,len(Ciphertext)):
        if Ciphertext[i]==' ':
            r=' '
        if (65<= ord(Ciphertext[i])<=(65+x))or(97<=ord(Ciphertext[i])<=(97+x)):
            r=chr(ord(Ciphertext[i])+26-x)
        if ((65+x)<ord(Ciphertext[i])<=90) or ((97+x)<ord(Ciphertext[i])<=122):
            r=chr(ord(Ciphertext[i])-x)
        R+=r
        with open(filename2,'w')as file_obj:
            file_obj.write(R)
            
    




