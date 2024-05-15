# class person:
# from pip._vendor.rich import color

#     def __init__(self, fname, lname):
#         self.firstName = fname
#         self.lastName = lname
        
#     def abc(self):
#         print("My first name is ", self.firstName, " and last name is ", self.lastName)

        
# p1 = person("shubham","shinde")
# p1.abc()


# class animal:

#     def __init__(self, domestic, wild):
#         self.dom = domestic
#         self.wild = wild
        
        
#     def ani(self):
#         print("Domestic Animal: ", self.dom) #d)
      

# class info(animal):

#     def __init__(self, breed, color, weight, eyes):
#         self.b = breed
#         self.c = color
#         self.w = weight
#         self.e = eyes
        
#     def para(self):
#         print("Breed: ", self.b, "\ncolor: ", self.c, "\nWeight: ", self.w, "\nEyes: ", self.e)

        
# p1 = animal("Cat" , "nikhil")
# p2=info("German", "White", 30, "green")
# p1.ani()
# p2.para()

# print(r'foo\\bar\nbaz')


# class Vehicle:

#     def __init__(self, max_speed, mileage):
#         self.ms = max_speed
#         self.mil = mileage

#     def val(self):
#         print("maximum speed {} and mileage {} of vehicle".format(self.ms, self.mil))


# Obj = Vehicle(132, 50)
# Obj.val()


# class vehicle:
    
#     def __init__(self, max_speed, milease,name):
#         self.max_speed = max_speed
#         self.mileage = milease
#         self.name = name

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"  


# class bus(vehicle):
#     pass       

#     def seating_capacity(self, capacity=60):
#         return super().seating_capacity(capacity=60)
        

# obj = bus(132 , 50, "school volvo")
# print("Speed: ",obj.max_speed,   "Milease: ",obj.mileage,   "Name: ",obj.name)
# print(obj.seating_capacity())


# class vehicle:
#     color = "Black"
    
#     def __init__(self, name, max_speed, milease, model):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = milease
#         self.model = model
        


# class bus(vehicle):
#     pass


# class car(vehicle):
#     pass


# class Sports_car(vehicle):
#     pass


# class racers(vehicle):
#     pass


# race = racers("F-1", 350, 10, "MacQuin")
# print(race.color,race.name, race.max_speed,race.mileage,race.model)

# obj_car = car("Audi", 300, 12, "X3")
# print(obj_car.color,obj_car.name,obj_car.max_speed,obj_car.mileage,obj_car.model)


# class vehicle:

#     def __init__(self, name, milease, capacity):
#         self.name = name
#         self.mileage = milease
#         self.capacity= capacity

#     def cap(self):
#         return self.capacity*100
        
# class bus(vehicle):

#     def cap(self):
#         amount = super().cap()
#         amount += amount * 10 / 100
#         return amount


# school_bus = bus("Volvo", 18, 50)
# print("Amount: ", school_bus.cap())
# print(type(school_bus))
# print(isinstance(school_bus, vehicle))


# class abc:
#     var = 10 #CLASS VARIABLE 

    
# obj = abc()  #CLASS VARIABLE IS ACCESSED USING CLASS OBJECT
# print(obj.var)


# class abc:

#     def __init__(self, var):
#         print("In the class method......")
#         self.var = var
#         print("The value is: ", var)
        
# obj=abc(99197)


# class abc:
#     class_var=0
#     def __init__(self, var):
#         abc.class_var += 1
#         self.var = var
#         print("THE OBJECT VALUE IS : ", var)
#         print("The value of class variable is : ", abc.class_var)

        
# obj1 = abc(10)
# obj1 = abc(20)
# obj1 = abc(40)


# class evenOdd():
#     even = 0

#     def check(self, num):
#         if num % 2 == 0:
#             self.even = 1

#     def even_odd(self, num):
#         self.check(num)                                  
#         if self.even == 1:
#             print(num, "is even")
#         else:
#             print(num, "is odd")


# obj1 = evenOdd()
# obj1.even_odd(10)        


# class Check:

#     def __init__(self, num):
#         self.num = num
#         if num % 2 == 0:
#             print(num, "is even number")
#         else:
#             print(num, " is odd number")
        
# obj=Check(10)                                                                                                 



# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }

# a = person1["age"]
# print(key)
# print(a)

# import calendar

# print(calendar.calendar(2024))


# class Employee:

#     def get_data(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
        
#     def display_data(self):
#         print("Employee Name : {}\nEmplyee Age : {}\nEmployee Salary : {}".format(self.name, self.age, self.salary))

        
# obj1 = Employee()
# obj1.get_data("shubham", 27, 100000)
# obj1.display_data()


# class Employee:

#     def get_data(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
        
#     def display_data(self, name, age, salary):
#         print("Employee Name : {}\nEmplyee Age : {}\nEmployee Salary : {}".format(self.name, self.age, self.salary))

        
# obj1 = Employee()
# obj1.get_data("jindya", 26, 81500)
# obj1.display_data("susha", 27, 81000)


# print(-5//-3)



