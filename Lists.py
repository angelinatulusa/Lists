#3.Николай задумался о поиске «бесполезного» числа на основании списка. Суть оного в следующем: он берет произвольный список чисел, находит самое большое из них, а 







print()
print()
print()
#2. Напишите программу, которая меняет местами первый и последний элементы. (второй и предпоследний и т.д.). Количество меняемых местами элементов надо спросить у пользователя. В исходном списке минимум 2 элемента.
from random import *
spisok=[]
n=randint(2,20)
for i in range(n):
    spisok.append(randint(-50,50))
print(spisok)
while 1:
    try:
        k=int(input("Mitu positsioonist alustada vahetust? "))
        if k<=n//2:
            break
    except ValueError:
        print("Arv peab olema väiksem kui",n//2)
k-=1
for i in range(k,-1,-1):#k...0
    print(spisok[i],end="<->")
    print(spisok[n-i-1])
    a=spisok.pop(i)
    spisok.insert(n-i-1-1,a)
    a=spisok.pop(n-i-1)
    spisok.insert(i,a)
print(spisok)
print()
print()
print()
#3.Николай задумался о поиске «бесполезного» числа на основании списка. Суть оного в следующем: он берет произвольный список чисел, находит самое большое из них, а затем делит его на длину списка. Студент пока не придумал, где может пригодиться подобное значение, но ищет у вас помощи в реализации такой функции.
max=-50
for element in spisok:
    if element>max: max=element
new_max=max/n #len(spisok)
ind=spisok.index(max)
spisok.remove(max)
spisok.insert(ind,new_max)
print(spisok)
#4.Требуется создать программу, которая сортирует список чисел по убыванию/возрастанию их абсолютного значения.
print()
print()
print()
spisok2=[]
for e in spisok:
    spisok2.append(abs(e))
g=int(input("Po vozrastaniu(1) ili po ubivaniu(2)?"))
if g==1:
    print(spisok2.sort())
elif g==2:
    print(spisok2.sort(reverse=True))
else:
    print("sto-to ne tak!")





print()
print()
print()
#Задание 1: Почтовый индекс
maakonnad=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa , Lääne-Virumaa Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
while 1:
    try:
        index=int(input("Kirjuta oma indeks: "))
        if 10000<=index<=99999:
            break
    except ValueError:
        print("Vale index!")
index_1=index//10000
print(maakonnad[index_1-1])
if index<=3:
    print("Оставайтесь дома!")
else:
    print("Носите маски!")








print()
print()
print()
nimed=["Anna","Inna"]
for i in range(3):#sprasivaet ima tri raza i potom zapisivaet v spisok
    nimi=input("Sisesta nimi: ")
    nimed.append(nimi)
print(nimed)
nimed.sort(reverse=True)#otsortirovat v obratnom poradke
print(nimed)
nimed.insert(1,input("Sisesta veel nimi: "))#dobavlaet ese ima v spisok
print(nimed)
nimed.remove("Anna")
print(nimed)
nimed.pop(2)#esli nicego ne ukazat, to edalit poslednego v spiske
print(nimed)
print(len(nimed))
nimed.count(nimed[0])

