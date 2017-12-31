class Cat:
  __egg = 7
  def print_egg(self):
    print(self.__egg)

s = Cat()
s.print_egg()
print(s._Cat__egg)
print(s.__egg)
