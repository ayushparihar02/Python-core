#keyword arguments
def movie (name,rating):
    print (name,"rating is",rating)

movie (rating=9, name="pushpa")

#default argumments
def student (name, city="indore"):
    print(name, "lives in ", city)

student("rahul","mumbai")
student("priya")

#*args Unlimited inputs
def total_marks (*marks):
    print (marks)
total_marks (80,70,90,60)

#kwargs
def student_info(**data):
    print (data)
student_info(name="rahul", city="indore")

#return
def add(a,b):
    return a + b
result = add(10,20)
print (result)

#multiple return values

def student():
    return "rahul",21,"indore"
name,age,city = student()
print (name,age,city)

#scope in python
#local variable
def demo ():
    x = 10
    print (x)
demo()

#global variable
college = "Rays EdTech"
def show():
    print (college)
def display():
    print (college)
show()
display()