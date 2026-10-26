#1

Balance= 10000
attempt=2
correct_pin=1234
lst=[]
Pin= int(input("Enter PIN : "))
if correct_pin==Pin:
    while True:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        user= int(input("Enter your Query : "))
        if user==1:
            print("Your Current Balance is",Balance)
        elif user==2:
            print("Your Current Balance is",Balance)
            dep=int(input("Add amount : "))
            print("New Balance is : ",Balance+dep)
            Balance+=dep 
            lst.append("Deposit: ")
            lst.append(dep)
        elif user==3:
            print("Your Current Balance is",Balance)
            wit=int(input("Withdrawing Amount : "))
            if wit > Balance:
                print("Insufficient Balance")
            elif wit <=Balance:
                print("Withdrawal Successful")
                print("Remaining Balance : ", Balance-wit)
                lst.append("Withdraw: ")
                lst.append(wit)
                Balance-=wit 
        elif user==4:
            print("Thank you!")
            print("You can now safely remove your card")
            for i in range(len(lst)):
                if(i % 2 == 0):
                    print(lst[i],end="") 
                else :
                    print(lst[i])
            break;
        if user>4 or user<1:
            print("Invalid Input")
else:
    while True:
        attempt-=1
        print("Incorrect PIN,Try Again")
        print("You have",attempt+1,"Attempts left")
        Pin= int(input("Enter PIN : "))

        if attempt==0:
            print("You Ran out of attempts")
            print("Your card is temporarily blocked")
            break;
    
    

