currentsalary = int(input("Enter Current Salay : "))
currentservice=int(input("Enter Service years : "))

if currentservice >= 5 and currentservice < 8:
    increase=currentsalary*0.10
    increment=increase+currentsalary
    print(f"Your Current Salary {currentsalary}")
    print(f"Incrasing Salary {increase}")
    print(f"After Increment your New Salary is {increment}")

elif currentservice == 4:
    increase=currentsalary*0.08
    increment=increase+currentsalary
    print(f"Your Current Salary {currentsalary}")
    print(f"Incrasing Salary {increase}")
    print(f"After Increment your New Salary is {increment}")

elif currentservice == 3:
    increase=currentsalary*0.06
    increment=increase+currentsalary
    print(f"Your Current Salary {currentsalary}")
    print(f"Incrasing Salary {increase}")
    print(f"After Increment your New Salary is {increment}")

elif currentservice == 2:
    increase=currentsalary*0.04
    increment=increase+currentsalary
    print(f"Your Current Salary {currentsalary}")
    print(f"Incrasing Salary {increase}")
    print(f"After Increment your New Salary is {increment}")    

elif currentservice == 1:
    increase=currentsalary*0.02
    increment=increase+currentsalary
    print(f"Your Current Salary {currentsalary}")
    print(f"Incrasing Salary {increase}")
    print(f"After Increment your New Salary is {increment}")
    
elif currentservice == 0:
    print("You're Junior")

else:
    print("You're Senior")
