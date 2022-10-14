from dogs import Dog

dog1 = Dog("milo", 'labrador', 13)
print(dog1.name)
print(dog1.breed)
print(dog1.age)
dog1.roll()
print('The name of my dog is ' + dog1.name.title() + ".")
print('She is an {0}. She is {1} years old. '
      .format(dog1.breed.title(), str(dog1.age)))

dog1.sit()
dog1.roll()
dog1.bark(10)
