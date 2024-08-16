'''x = 5
y = 8
x, y = y, x
print("x=",x,"y=",y)

Name="sivaramakrishnan"
Age=26
Salary=1000
#print(Name,Age,Salary)
"""print(Name)
print(Age)
print(Salary)

#print("Name:%s Age:%d Salary:%d"%(Name,Age,Salary))
print("Name:{} Age:{} Salary:{}".format(Name,Age,Salary))

a = int(input("The number is ="))
if a <= 30:
     print("True")
else:
   print("False")

a=10

if a==10:
    print("Ten")
elif a==25:
    print("twenty")
elif a==15:
    print("Thirty")
elif a==76:
    print("seventy six")
else:
    print("No data available")

(print("New world"), print("Siva")) if False else(print("Robo"),print("Rashid"))


print(list(range(5)))
print(list(range(1,10)))
print(list(range(1,10,2)))
print(list(range(0,10,2)))

for i in range(11,0,-2):
    print(i)

i=100
while i>=1:
    print(i)
    i=i-1

for i in range(0,50,2):
    print(i)

print(list(range(10)))

i=30
while i>=10:
      if i==12:
          continue
      print(i)
      i=i-1


x=10
print(float(x))

y=(150,175,299.87)
print(min(y))

for i in range(0,10,2):
    print(i)
for i in range(0,10):
    if i==4:
        break
    print(i)

for i in range(0,10):
    if i==4:
        continue
    print(i)

s= "Welcome to new world"

# converting string:
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())
s1=s.replace("new","siva")
print(s1)

s= "Welcome to new world"

#search strings
print(s.endswith("ld"))
print(s.startswith("a"))
print(s.find("W"))
print(s.rfind("w"))
print(s.count("o"))

#iteration
for i in s:
    print(s)
    print(i)

#membership operation
s= "Welcome to new world"
print("arr"not in s)
print("wel"in s)

print(s+" Hi")
print(s *2)

print(list(range(2)))
print(list())
list4 =list (["10", "22", "99"])
print(list4)
list8 = list(["siva", "stark"])
print(list8)
list6 = list("krishnan")
print(list6)


s=list([2,3,8])
print(7 in s)
print(max(s))
print(min(s))
print(len(s))
print(sum(s))

k=list([5,6,7,8,9])
print(k[1:3])
print(k[:4])
print(k[0:])

m=list([18,19,17])
print((k+m) *2)

m = list([18, 19, 17])
print(22 in m)
print(22 not in m)

m=list([1,2,3,4])
for i in m:
    print(i,end=" ")
for i in range(0,10,3):
    print(i,end=" ")

s=[7,8,7,4]
s.append(22)
print(s)
u=s.count(7)
print(u)
t=s.insert(2,87)
print(s)
b=s.remove(4)
print(s)
a=s.pop(2)
print(s)
#y=[1,8,655,765,45]
z=s.reverse()
print(s)
op=s.sort()
print(s)
indexing=s.index(22)
print(indexing,"siva")
add=[88,90]
adds=s.extend(add)
print(s,"you")

#List compression
#s=list([x+1 for x in range(10)])
#print(s)

u=[x for x in range(20) if x%2==0 ]
print(u)

for x in range(8):
    if x%2==0:
        print("Even =",x)
    elif x%3==0:
        print("Odd =",x)
    else:
        print("Neither even nor odd =",x)


#Dictionaries:

Team ={'siva':45, 'Ganesh':55, 'Natu':87}
print(Team)

# retrieving
print(Team['Natu'])

#adding

Team['solo']=99
print(Team)

#delete

Team ={'siva':45, 'Ganesh':55, 'Natu':87}
Team['solo']=98
print(Team)
del Team['solo']
print(Team)

Team['siva']=1001
print(Team)

Team ={'siva':45, 'Ganesh':55, 'Natu':87}
Team_1= {'siva':55, 'Ganesh':85, 'Natu':87}
#for y in Team:
   # print(y,":",Team[y])
print(Team!=Team_1)

Team ={'siva':45, 'Ganesh':55, 'Natu':87}
#print(Team.popitem())
#print(Team)
#print(Team.clear())
#print(Team)
print(Team.get('siva'))
#print(Team)
print(Team.values())
#print(Team)
print(Team.keys())
print(len(Team))
print(Team.pop('siva'))
print(Team)
print(Team.get(87))

t1=()
t2=(55,65,77)
t5=(87,98,108)
print(t1)
print(t2)
t3=([1,9,87,7])
print(t3)
t4=tuple("siva")
print(t4)

print(67 not in t3)

print(t3[1:4])

t7=[56,78,98]
#for z in t7:
    #print(z,end=" ")

print(max(t7))

# Fun

def siva(start,end):
    r = 0
    for i in range(start,end+1):
      r=r+i
    print(r)

siva(1,5)
def ram():
    pass

def srk(greeting,name):
    print(greeting,name)

srk("Welcome","sivaramakrishnan")
srk(greeting="Sky is",name="blue")


def sum(start, end):
    if (start > end):
        print("Start is greater")
        return
    result=0
    for i in range(start,end):
        result=result+i
    return result

s=sum(1,5)
print(s)

x=19

def fun():
    t=100
fun()

print(x)

ss=123

def siva():
    global ss
    ss=333
    print(ss)
siva()
print(ss)

def run(i,k=98):
    print(i,k)
run(87)

def clash(a,b):
    if(a>b):
        return a,b
    else:
        return b,a

s=clash(450,458)
print(s)
print(type(s))

#File handling
file = open('C:\\Users\\HUBINO\\Desktop\\Study\\Testdata.txt','a')
file.write("To be become limitless\n")
#file.write("On the sky\n")
file.close()

file = open('C:\\Users\\HUBINO\\Desktop\\Study\\Testdata.txt','r')
s=file.readlines()
print(s)
file.close()

# class and objects
a,b=10,20
class myclass():
    c,d=30,40

    def siva(self):
        pass
    def ran(self,x,y):
        print(x+y)

    def word(self,name):
        print("I am the freeman",name)

    def proc(self,e,f):
        print(a+b)
        print(self.c*self.d)
        print(e+f)

    def india(self):
        print("test for",globals()['a']+globals()['b'])

    @staticmethod
    def kamal():
        print("We are great")



on=myclass()
on.siva()
on.ran(10,15)
on.word("siva")
on.proc(50,60)
on.india()
myclass().kamal()
print(id("siva"))
print(id("kamal"))
off=myclass()
print(on is not off)
print(on is off)

#Constructor -20

class siva():
    def __init__(self):
        print("siva rocks")

    def srk(self):
        print("cat on the wall")

s=siva()
s.srk()

#Converting local variable into class variable
class siva():
    def __init__(self, x, y):
        print(x)
        print(y)
        self.x=x
        self.y=y

        print(self.x + self.y)  # class variable


ra=siva(10,15)


class apple():
    def math(self):
        print("new")
        self.sci("greats")

        print(self.name)

    def sci(self,name):
        print("new 3")
        self.name=name


u=apple()
u.math()

u.sci("rambo")

class names():
    na="sachin"
    def __init__(self,nam):
        print(nam)
        print(self.na)
x=names("moha")


class emp():
    def __init__(self,empid,empname,empsalary):
        self.empid=empid
        self.empname=empname
        self.empsalary=empsalary

    def display(self):
        print("EMPLOYID={} EMPLOYNAME={} EMPLOYSALARY={}".format(self.empid,self.empname,self.empsalary))
        self.empid="2"
        print(self.empid)

A=emp("148","SIVA","85000")
A.display()

class owner():

    def __str__(self):
        return "Welcome"
c=owner()
print(c)

class emp():
    def __init__(self,empid,empname,empsalary):
        self.empid=empid
        self.empname=empname
        self.empsalary=empsalary

    def __str__(self):
        return ("EMPLOYID={} EMPLOYNAME={} EMPLOYSALARY={}".format(self.empid,self.empname,self.empsalary))


A=emp("148","SIVA","85000")
print(A)
#__del__
class own():
    def __del__(self):
        print("we will")
o=own()

del o

class new():
    def tech(self):
        self.road("quick")
        print(self.name)


    def road(self,name):
        self.name = name
        print("The name is",name)

p=new()
p.tech()
p.road("food")

# Single inheritance

class fruit():
    def a1(self):
        print("Apple")

class tv(fruit):
    def a2(self):
        print("mango")

c=tv()
c.a1()
c.a2()
#mulilevel
class fruit():
    def a1(self):
        print("Apple")

class tv(fruit):
    def a2(self):
        print("mango")

class egg(tv):
    def a3(self):
        print("tomato")

c=egg()
c.a1()
c.a2()
c.a3()

#Hierchical
class fruit():
    def a1(self):
        print("Apple")

class tv(fruit):
    def a2(self):
        print("mango")

class egg(fruit):
    def a3(self):
        print("tomato")

c=egg()
c.a1()
#c.a2()
c.a3()
b=tv()
b.a1()
b.a2()

#Multiple
class fruit():
    def a1(self):
        print("Apple")

class tv():
    def a2(self):
        print("mango")

class egg(tv,fruit):
    def a3(self):
        print("tomato")

c=egg()
c.a1()
c.a2()
c.a3()

#super

class sun():
    def s1(self):
        print("next day")

class orange(sun):
    def moon(self):
        print("owl")
        super().s1()

srk=orange()
srk.moon()

class sun():
    a,b=10,20
class moon(sun):
    c,d=20,30
    def s3(self,x,y):
        print(x+y)
        print(self.c+self.d)
        print(self.a+self.b)
dog=moon()
dog.s3(17,18)

a,b=89,76
class sun():
    a,b=10,20
class moon(sun):
    a,b=20,30
    def s3(self,a,b):
        print(a+b) #local varibale
        print(self.a+self.b) #moon class variable
        print(super().a+super().b)#sun class variable
        print(globals()['a']+globals()['b'])

dog=moon()
dog.s3(17,18)

class rose():
    def __init__(self):
        print("sachin rocks")
class B(rose):
    def __init__(self):
        print("son of god")
        super().__init__()
        #rose().__init__()

c=B()

#polymorphism

#overriding
class animal():
    lion=10

class mamal(animal):
    lion=14

red=mamal()
print(red.lion)

class sky():
    def blue(self):
        return  15

class sea(sky):
    def solo(self):
        return 19

s1=sea()
print(s1.solo())
s2=sky()
print(s2.blue())

#overloading

class student:
    def stu(self,name=None):
        if name is None:
            print("Name is not available")
        else:
            print("Roars " + name)
ink=student()
ink.stu("Lion")
ink.stu()

#Encapsulation
#private variables can be accessed only within the methods

class animal():
    a=10
    __b=15
    def king(self):
        print(self.a)
        print(self.__b)

kn=animal()
kn.king()

print(animal.a)

#Private methods can be accessed only within the  methods

class tom():
    def __siva(self):
        print("Just wave your flag")
    def ram(self):
        print("Time to think")
        print(self.__siva())

ss=tom()
ss.ram()

class animal():

    __b=15
    def king(self):
        print(self.__b)

    def queen(self,c):
        print(c)
        self.__b=c

    def knight(self):
        print(self.__b)

army=animal()
army.king()
army.queen(88)
army.knight()

#Abstraction

from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def hero(self):
        None

class B(A):
    def hero(self):
        print("I am inevitable")

class C(A):
    def hero(self):
        print("I am the passer")

Bus=B()
Bus.hero()

Cat=C()
Cat.hero()

from abc import ABC,abstractmethod

class Maths(ABC):

    def __init__(self,value):
        self.value = value

    @abstractmethod
    def sum(self):
        pass
    @abstractmethod
    def sub(self):
        pass

class Great(Maths):
    def sum(self):
        print(self.value+89)

    def sub(self):
        print(self.value-17)

Gd=Great(200)
Gd.sum()
Gd.sub()

def sum(num1,num2):
     print(num1+num2)

def mul(num1,num2):
     print(num1*num2)

print("siva has stared exception handling")

try:
     print(10/2)
except TypeError:
     print("Enter the type error")
except ZeroDivisionError:
     print("Enter we have used Zero Division error")
else:
     print("We are rocking")
finally:
     print("we will rock you")


print("siva has closed")

def person_age(age):
     if age<0:
          raise ValueError("Only positivite numbers are allowed")
     if age%2==0:
          print("Age is even")
     else:
          print("Age is odd")
try:
     nu=-1
     person_age(nu)
except ValueError:
     print("Only positivite numbers are allowed")

try:
     number= one
     print("The number is",number)
except NameError as s:
     print("NameError",s)

s=lambda a:a+10
print(s(5))

s=lambda a,b:a+b
print(s(3,4))

s=lambda a,b,c:a*b*c
print(s(2,3,5))

def add(a):
     s=a+10
     return s
print("The number =",add(3))


def sum(*args):
    s = 10
    for i in args:
         s=s+i
         print(s)
sum(1,4,5)

def siva(a,b,c,d):
     print(a,b,c,d)
arg=[1,2,3,4]
siva(*arg)

def ram(a,c):
     print(a,c)

s={'a':"ss",'c':"RR"}

ram(**s)

def mat(**kw):
     for i,j in kw.items():
          print(i,j)
mat(name='siva',office='Hubino')


for i in range(2,204,4):
    print(i)




for i in range(2,100,4):
     print(i)

a=10
b=20
a,b=b,a
print("The value of a=",a)
print("The value of b=",b)'''

# noinspection PyTypeChecker
a=100
b=2
c=a+b
print(c)
print(type(c))
print(id(c))