# 1 topshiriq
class Book:
   def __init__(self,Creator,Name,Price):
    self.Muallif=Creator
    self.ism=Name
    self.narx=Price
     
   def __str__(self):
    return f'[{self.Muallif} ning kitobini ismi {self.ism} narxi esa {self.narx} ming turadi]'
Hamasi=Book("Qodiral_Bot","Besh Barmoqcha",1488)
print(Hamasi)
# 2 topshiriq
class Person:
   def __init__(self,Name,Age):
    self.ism=Name
    self.yosh=Age
   def __str__(self):
    return f'[Uning Ismi {self.ism} yoshi {self.yosh} da]'
Natija=Person("Qodiral",15)
print(Natija)
# 3 topshiriq
class Rectangle:
   def __init__(self,Length,width):
    self.Uzunligi=Length
    self.kengligi=width
   def __str__(self):
    return f'[maksimal sinfning uzunligi {self.Uzunligi}, maksimal sinfning kengligi {self.kengligi}]'
razmer=Rectangle(8,6)
print(razmer)
# 4 topshiriq
class Sinf:
      def __init__(self,school,letter,clas):
        self.maktab=school
        self.harf=letter
        self.sinf=clas
klass=Sinf(105,11,"E")
print(f'[{klass.maktab} maktab {klass.harf} {klass.sinf} sinf]')
# 5 topshiriq
class Makteb:
      def __init__(self,school,letter,clas):
        self.maktab=school
        self.harf=letter
        self.sinf=clas
      def __str__(self):
          return f'[{self.maktab} maktab {self.harf} {self.sinf} sinf]'
sing1=Makteb(89,8,"D")
print(sing1)
sing2=Makteb(89,10,"B")
print(sing2)