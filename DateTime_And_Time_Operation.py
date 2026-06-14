from datetime import datetime
import time



def Current_Date():
    '''Current Data'''
    print(datetime.now())

  

def Difference(data1 , date2):
    '''Date Between Difference,  Tack Tow Argument As Date '''
    d = datetime.now().strptime(data1,"%d-%m-%Y")
    d1 = datetime.now().strptime(date2,"%d-%m-%Y")
    print("Difference Between Two Dates: ",d1-d)




def Custome_Format(date1):
    '''Coustom Date Formet , Tack One Argument As Date'''
    d = datetime.now().strptime(date1,"%d-%m-%Y")
    print(d.strftime("%D"))




def StopWatch():
    '''StopWatch Work'''
    end = int(input("Enter Stop Watch Second"))
    print("Current Time Watch Start")
    for i in range(1,end+1):
        print(datetime.now())
        time.sleep(1)
    print(f"After{end} Second Watch Stop")    


    

def CountDown_Timer():
    '''CountDown Timer Work'''
    start = int(input("Enter Your Counter Start"))
    end = int(input("Enter Your Counter End"))
    for i in reversed(range(start,end+1)):
        print(i)
        time.sleep(1)
    print("Go....")    

    

