class Person:
      def __init__(self, firstname='Mr.', lastname='AROMA', age=27, country='South Sudan', city='Juba'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []
      def person_info(self):
          return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'
      def add_skill(self, skill):
         self.skills.append(skill) 
         
p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p1.add_skill('Python')
p1.add_skill('C')
p1.add_skill('Java')
p1.add_skill('SQL')

p2 = Person('John', 'Akech', 22, 'Rwanda', 'Kigali city')
print(p2.person_info)
print(p1.skills)
print(p2.skills)