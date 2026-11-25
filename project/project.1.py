#expense tracker:
expenses = []
print("Welcome To expense tracker:")

while True :    
    print("===MENU===")
    print("1.Add Expense:")
    print("2.View all expenses:")
    print("3.total expense:")
    print("4.EXIT")

    choice = int(input(" enter your choice:"))
    #ADD EXPENSE
    if(choice ==1):
        date = input("enter the date:")
        category = input("type of expense(eg.food ,travel,cloths):")
        des = input("enter description:")
        amount = float(input("enter the amount:"))


        expense = {
            "Date" : date,
            "Category" : category,
            "description":des,
            "Amount":amount


        }

        expenses.append(expense)
        print("\n expense added succesfully")



    elif(choice==2):
        if(len(expenses)==0):
            print("No expense is added. jao phela khrcha karoo")

        else:
            print("==Here is your all Expenses==")
            count = 1
            for money in expenses:
                print(f"expense no.{count}->{money["Date"]},{money["Category"]} ,{money["description"]},{money["Amount"]}")
                count+=1




    elif(choice==3):
        total = 0
        for money in expenses:
            total = total+money["Amount"]

        print("/n TOTAL MONEY SPENT=",total)



    elif(choice==4):
        print("/n<thankyou for using our system>")
        break


    else:
        print("wrong choice")

