from abc import ABC, abstractmethod

##  Person abstact class for student
class Person(ABC):
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

#getters for private attributes

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
#abstractmethod
    @abstractmethod
    def get_details(self):
        pass
        
## Child Class for Person to get marks 

class Student(Person):
        def __init__(self, name, age,student_class,maths,science,english):
         super().__init__(name,age)
         self.__student_class=student_class
         self.__maths=maths
         self.__science=science
         self.__english=english
         self.__average= (maths+science+english)/3

         ##getters to access the student attributes

        def get_maths(self):
             return self.__maths
         
        def get_student_class(self):
             return self.__student_class
         
        def get_science(self):
             return self.__science
        
        def get_english(self):
             return self.__english
        
        def get_average(self):
            return self.__average

        def get_details(self):
       
            print(f"Name: {self.get_name()}")
            print(f"Age: {self.get_age()}")
            print(f"Class: {self.get_student_class()}")
            print(f"Maths: {self.get_maths()}")
            print(f"Science: {self.get_science()}")
            print(f"English: {self.get_english()}")
            print(f"Average: {self.get_average()}")

           



def main():


    name= input("Enter your name: ")
           
    age=int(input("Enter your age : "))
          
    cls=input("Enter your class: ")
          
    maths=float(input("Enter your marks for maths :"))
        
    sci=float(input("Enter your marks for science : "))
           
    eng=float(input("Enter your marks for english : "))
            
    
        

    obj=Student(name,age,cls,maths,sci,eng)
    obj.get_details()

if __name__=="main":
    main()
  

        
     