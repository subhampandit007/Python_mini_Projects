import os
#file manager
def creat_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"file {filename} created succesfully")
    except FileExistsError:
        print(f"file name {filename},already exixted!")

    except Exception:
        print("AN ERROR HAS OCCURED!") 



def view_all_files():
    files =os.listdir()
    if not files:
        print("NO FILE FOUND!")
    else:
        print("files in directory")    
        for file in files:
            print(file)




def delet_file(filename) :
    try:
        os.remove(filename)
        print(f"file named{filename} has been succesfully deleted:")
    except FileNotFoundError:
        print("file not found!")   
          
    except Exception as e:
        print("an error has occured!")


def read_file(filename):
    try:
        with open('sample.txt' , 'r') as f:
            content = f.read()
            print(f"content of {filename} :/n{content}")
    except FileNotFoundError:
        print(f"{filename} doesn't exixt!")
    except Exception as E:
        print("an error occured!")


def edit_file(filename):
    try:
        with open('sample.txt' , 'a') as f:
            content = input("enter data to add:")
            f.write(content + "/n")
            print(f"content added to {filename} succesfully")
    except FileNotFoundError:
        print(f"{filename} doesn't exixt!")
    except Exception as E:
        print("an error occured!")

def main():
    while True:
        print("file management app:") 
        print("1: creat file")       
        print("2: view all files")
        print("3: delet file")  
        print("4: read file")  
        print("5: edit file") 
        print("6: EXIT") 

        choice = int(input("enter your choice:"))  
        if choice == 1:
            filename = input("enter file-name you want to creat:")
            creat_file(filename)

        elif choice == 2:
            view_all_files()   

        elif choice== 3:
            filename = input("enter file name you want to delet:")
            delet_file(filename)   

        elif choice== 4:
            filename = input("enter file name you want to read:")
            read_file(filename)
        elif choice== 5:
            filename = input("enter name of file you want to edit:") 
            edit_file(filename)   
        elif choice== 6:
            print("closing the APP...")
            break    
          
        else:
            print("wrong entry!") 


if __name__ == "__main__":
    main()



          