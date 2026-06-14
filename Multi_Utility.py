from DateTime_And_Time_Operation import *
from File_Operation import *
import random
import string
import math
import uuid


def Compound_Interest():
    print()
    p = int(input("Enter Your Principal"))
    r = int(input("Enter Your Rate Of Interest (in %)"))
    n = int(input("Enter Your Time (Year)"))

    ci = p*(1+r/10*100)**n
    print("Compound Interest: ",ci)
    print()



def Trigonometric():
    num = int(input("Enter Your Number"))
    r = math.radians(num)
    print("Cos      :",math.cos(r))
    print("Sin:     ",math.sin(r))
    print("Tan:     ",math.tan(r))
    print("Degrees: ",math.degrees(r))
    print()




def Geometric_Shapes():
    num = int(input("Enter Your Number"))
    num1 = int(input("Enter Your Number"))
    print("Area Of square: ",num* num)
    print("Area Of Cricle: ",math.pi*math.radians(num)*2)
    print("Area of Ractangle :",num*2+num1*2)
    print()

while True:

    print("------------------------------------------")
    print("Welcome Multi Utility Toolkit")
    print("------------------------------------------")
    print("1. Datetime And Time Operation")
    print("2. Mathematical Oeration")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operation")
    print("6. Explore Module Attributes")
    print("7. Exit")

    ch = int(input("Enter Your Choice"))
    try:
     if ch <= 7:
        match ch:
            case 1:
                print("Datetme And Time Operation")
                print()
                while True:
                    print("---------------------------------------------")
                    print("1. Display Current Date And Time")
                    print("2. Calculate Difference Between Two Dates/Time")
                    print("3. Format Date Into Custom Format")
                    print("4. Stopwatch")
                    print("5.Countdown Timer")
                    print("6.Back To Main Menu")

                    ch1 = int(input("Enter Your Choice"))
                    print()
                    try:
                        if ch1 <= 6:
                            match ch1:
                                case 1:
                                    print("1. Display Current Date And Time")
                                    print()
                                    if __name__ == "__main__":
                                        Current_Date()    
                                        
                                case 2:
                                    print("2. Calculate Difference Between Two Dates/Time")
                                    print()
                                    s = input("Enter Staring Date [dd-mm-yyyy]")
                                    e = input("Enter Ending Date  [dd-mm-yyyy]")
                                    if __name__ == "__main__":
                                        Difference(s,e)
                                case 3:
                                    print("3. Format Date Into Custom Format")
                                    print()
                                    s = input("Enter Date [dd-mm-yyyy]")
                                    if __name__ == "__main__":
                                        Custome_Format(s)
                                case 4:  
                                    print("4. Stopwatch")
                                    print()
                                    if __name__ == "__main__":
                                        StopWatch()
                                case 5:    
                                    print("5.Countdown Timer")
                                    if __name__ == "__main__":
                                        CountDown_Timer()
                                    print() 
                                case 6:
                                    print()
                                    break 
                        else:
                            raise ValueError      
                    except ValueError:
                        print("------------------------------")
                        print("Invaild Choice.....")   
                        print()
                
            case 2:
                print("2.Mathematical Operation")
                print()
                while True:
                    print("------------------------------------")
                    print("1. Calculate Factorial ")
                    print("2. Solve Compound Interest")
                    print("3. Trigonometric Calculations")
                    print("4. Area of Geometric Shapes")
                    print("5. Back To Main Menu")

                    ch2 = int(input("Enter Your Choice"))
                    print()
                    try:
                        if ch2 < 6:
                            match ch2:
                                case 1:
                                    print("1. Calculate Factorial ")
                                    print()
                                    num = int(input("Enter Your Number"))
                                    print("Factorial",math.factorial(num))
                                    print()

                                case 2 :
                                    print("2. Solve Compound Interest")
                                    Compound_Interest()
                                case 3:
                                    print("3. Trigonometric Calculations")
                                    print()
                                    Trigonometric()
                                    
                                case 4:
                                    print("4. Area of Geometric Shapes")
                                    print()
                                    Geometric_Shapes()
                                    
                                case 5:
                                    print()
                                    break
                        else:
                            raise Exception            
                        
                    except Exception:
                        print("-------------------------------")
                        print("Invaild Choice..")  
                        print()                
                
            case 3:
                print("3.Random Data Generation")
                print()
                while True:
                    print("----------------------------------")
                    print("1. Generate Random Number")
                    print("2. Genrate Random List")
                    print("3. Create Random Password")
                    print("4. Generate Random OTP")
                    print("5. Back To Main Menu")

                    ch1 = int(input("Enter Your Choice"))
                    print()
                    try:
                        if ch1 <6:
                            match ch1:
                                case 1:
                                    print("1. Generate Random Number")
                                    print()
                                    print("Number",random.random())
                                case 2:
                                    print("2 . Genrate Random List")
                                    print()
                                    print(random.sample(range(1,20),10))
                                case 3:
                                    print("3 . Create Random Password")
                                    print()
                                    print("Password: ",''.join(random.sample(string.ascii_letters+string.digits,k=8)))
                                case 4:
                                    print("4. Generate Random OTP")
                                    print()
                                    l1 = 123456
                                    print("OTP: ",''.join(random.sample(string.digits,k=6)))
                                case 5:
                                    break        

                        else:
                            raise Exception            
                    except Exception:
                        print("-------------------------------")
                        print("Invaild Choice..")  
                        print()              


            case 4:
                print("4.Generate Unique Identifiers")
                print()
                print("Id",uuid.uuid8())
            case 5:
                print("5.File Operation")
                print()
                while True:
                    print("---------------------------------------")
                    print("1. Create A New File")
                    print("2. Write To A File")
                    print("3. Read From a File")
                    print("4. Append To A File")
                    print("5. Back To Main Menu")

                    ch3 = int(input("Enter Your Choice"))

                    print()
                    try:
                        if ch3 <6:
                            match ch3:
                                case 1:
                                    print("1. Create A New File")
                                    print()
                                    if __name__ == "__main__":
                                        file = input("Enter Your File Name")
                                        Create_File(file)
                                        print()
                                case 2:
                                    print("2. Write To A File")
                                    print()
                                    if __name__ == "__main__":
                                        file = input("Enter Your File Name")
                                        content = input("Enter Your File Content")
                                        Write_Data(file,content)
                                        print()
                                case 3:
                                    print("3. Read From a File")
                                    print()
                                    if __name__ == "__main__":
                                        file = input("Enter Your File Name")
                                        Read_Data(file)
                                        print()
                                case 4 :
                                    print("4. Append To A File")
                                    print()
                                    if __name__ == "__main__":
                                        file = input("Enter Your File Name")
                                        content = input("Enter Your File  Append Content")
                                        Append_Data(file,content)
                                        print()
                                case 5:
                                    print()
                                    break
                        
                        else:
                            raise Exception
                    except Exception:
                        print("-------------------------------")
                        print("Invaild Choice..")  
                        print()                


            case 6:
                print("6.Explore Module Attributes") 
                print()
                module = input("Enter Your Module")
                print(dir(module))
            case 7:
                print("---------------------------------------------")
                print("Thank You For Using Multi Utility Toolkit")
                print("-----------------------------------------------")
                print()
                exit()   
     else:
         raise Exception             
    except Exception:
        print("--------------------------------")
        print("Invalid Choice....")        
        
        print() 
        