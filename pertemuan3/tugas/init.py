class Person:
  def __init__(self, name, age):
    #properti/atribut
    self.name = name
    self.age = age

#object dengan initial value
p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)

class Person:
  pass
#

#Mengatur properti object secara manual
p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)
#

class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)
#