import random
secret=random.randint(1, 100)
print("你会读心术吗？我想到了一个1到100间的整数，你有六次机会说出我心里的数字！！")
tries=1
while tries<=6:
    guess=int(input("1-100的整数，这是你的第%d次机会，请输入答案："%(tries)))
    if guess == secret:
        print("wow！你真的会读心术！只用了%d次机会就说出了正确答案！"%(tries))
        break
    elif guess>secret:
        print("你猜的大了点")
    else:
        print("猜小了！！")
    tries+=1
else:
    print("原来你不会读心术，就这样吧，Bye bye!")
