import os
def Create_File(f):
        '''File Create Function , Tack A One Argument As File Name'''
        with open(f,"w") as f1:
            f1.write("Write Data")
            print("File Are Create successfully ")
            print()




def Write_Data(f,wr):
      '''File In Write Data Tack,  Tow Argument As File Name And Content Data '''
      try:
            if os.path.exists(f):
                  with open(f,"w") as f1:
                        f1.write(wr)
                        print("File In Data Written Successfuly ")
                        print()
            else:
                  raise FileExistsError            
      except FileExistsError:
            print("File Are Not Exists.. ! Please Create")

            
 


def Read_Data(f):
      '''File In Read Data , Tack A One Argument As File Name'''
      try:
            if os.path.exists(f):
                  with open(f,"r") as f1:
                        print(f1.read())
                        print()
            else:
                  raise FileExistsError            
      except FileExistsError:
            print("File Are Not Exists.. ! Please Create")                  

 

def Append_Data(f,wr):
      '''File In Append Data , Tack Tow Argument As File Name And Content Data'''
      try:
            if os.path.exists(f):
                  with open(f,"+a") as f1:
                        f1.write(wr)
                        print("File In Data Append Successfuly ") 
                        print()
            else:
                  raise FileExistsError            
      except FileExistsError:
            print("File Are Not Exists.. ! Please Create")      

       