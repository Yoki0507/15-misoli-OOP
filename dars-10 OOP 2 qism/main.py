# 1 topshiriq
class Car:
    wheels=4
    def __init__(self, color):
        self.color=color

mashina1=Car("Qizil")
mashina2=Car("Yashil")

print(mashina1.color)
print(mashina2.color)
# 2 topshiriq
class Student:
    school_name="New Uzbekistan School"
    def __init__(self, name):
        self.name=name

student1=Student("Ali")
student2=Student("Qodirali")

print(student1.name,student1.school_name)
print(student2.name,student2.school_name)
# 3 topshiriq
class Phone:
    country="China"
    def __init__(self, brand, price):
        self.brand=brand
        self.price=price

telefon1=Phone("Samsung",500)
telefon2=Phone("Xiaomi",300)
telefon3=Phone("iPhone",1000)

print(telefon1.brand,telefon1.price,Phone.country)
print(telefon2.brand,telefon2.price,Phone.country)
print(telefon3.brand,telefon3.price,Phone.country)
# 4 topshiriq
class Book:
    category="Education"
    def __init__(self,title,creator):
        self.title=title
        self.creator=creator

book = Book("Python-book","Mr.Qodirali")

print(book.title)
print(book.creator)
print(Book.category)
# 5 topshiriq
class Animal:
    kingdom="Animals"
    def __init__(self, name):
        self.name=name

hayvon1=Animal("Lion")
hayvon2=Animal("Tiger")

print(hayvon1.name,Animal.kingdom)
print(hayvon2.name,Animal.kingdom)
# 6 topshiriq
class Employee:
    company="TechCorp"
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

ex1=Employee("Aziz",3000)
ex2=Employee("Alibek",3500)

print(ex1.name,ex1.salary)
print(ex2.name,ex2.salary)
# 8 topshiriq
class Course:
    platform="Online"
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

c1=Course("Python","3 months")
c2=Course("Java","4 months")
c3=Course("Web","2 months")

print(c1.title,c1.duration,Course.platform)
print(c2.title,c2.duration,Course.platform)
print(c3.title,c3.duration,Course.platform)
# 9 topshiriq
class BankAccount:
    bank_name="National Bank"
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

bank1=BankAccount("Qodirali", 5000)
bank2=BankAccount("Alijon", 7000)

print(bank1.owner,bank1.balance)
print(bank2.owner,bank2.balance)
# 10 topshiriq
class Teacher:
    Profession="Teacher"
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def __str__(self):
          return f'[Ism {self.name}, Profession {self.subject} Ustoz]'

Teacher1=Teacher('Qodiral','Matematika')
Teacher2=Teacher('Bekzodbek','Ingliz Tili')
Teacher3=Teacher('Ali','Fizika')

print(Teacher1.name,Teacher1.subject)
print(Teacher2.name,Teacher2.subject)
print(Teacher3.name,Teacher3.subject)
# 11 topshiriq

class Counter:
    count=0
    def __init__(self):
        Counter.count=Counter.count+1

obj1=Counter()#1
obj2=Counter()#2
obj3=Counter()#3
obj4=Counter()#4
obj5=Counter()#5
print(Counter.count)

# 12 topshiriq
class total_users:
    username=0
    def __init__(self):
        total_users.username=total_users.username+1

obj1=total_users()#1
obj2=total_users()#2
obj3=total_users()#3
obj4=total_users()#4
obj5=total_users()#5
print(total_users.username)
# 13 topshiriq
class Product:
    currency="USD"

    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def usd_to_uzs(self):
        return f'Assalomu Alaykum {self.name}, sizning {self.price} {self.currency} o\'zbek so\'mida {self.price*12243.19} UZS '
onj1=Product("Qodirali",1500)
print(onj1.usd_to_uzs())
# 14 topshiriq
class Library:
    library_name="Central Library"
    def __init__(self,book_title,year):
        self.book_title=book_title
        self.year=year

b1=Library("Ajdar", 2024)
b2=Library("Beak", 2020)
b3=Library("qewd", 2025)

print(b1.book_title,b1.year)
print(b2.book_title,b2.year)
print(b3.book_title,b3.year)
print(Library.library_name)
# 15 topshiriq
class StudyBot:
    bot_name="StudyBot"

    def __init__(self, user_id, full_name):
        self.user_id=user_id
        self.full_name=full_name

    def __str__(self):
        return f"Bot {StudyBot.bot_name}, ID {self.user_id}, Ism {self.full_name}"

user1=StudyBot(1, "Ali Karimov")
user2=StudyBot(2, "Vali Abdullayev")
user3=StudyBot(3, "Dilshod Rustamov")
user4=StudyBot(4, "Madina Islomova")
user5=StudyBot(5, "Sardor Qodirov")

print(user1)
print(user2)
print(user3)
print(user4)
print(user5)