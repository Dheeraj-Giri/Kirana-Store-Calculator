def ShreeRamKiranaStore():
    _sum = 0
    d = {}
    while (True):
        def check():
            inp = input("You want to Continue ! (Y/N): ")
            if inp == "y" or inp == "Y":
                ShreeRamKiranaStore()
            elif inp == "N" or inp == "n":
                print("Thanks For Comming.")
                exit()
            else:
                print("Invalid Input")
                exit()

        userInput = input("\nPress Y for Entering products and N for exiting (y/n): \t")
        if userInput == 'Y' or userInput == "y":
            key = input("Enter the product name : ").strip()
            if not (key.isalnum()):
                check()

            value = input("Enter the product price : ").strip()
            if not (value.isdigit()):
                check()
            d[key] = value
            _sum = _sum + int(value)

        elif userInput == "N" or userInput == "n":
            for i in d:
                print(f"\nName:{i}\t\tPrice:{d[i]}₹")

            print("\n***********************")
            print(f"your Total Amount: {_sum}₹.")
            print("***********************")
            break

        else:
            print("Invalid input")
            exit()


if __name__ == '__main__':

    Name = input("Enter Your Name:")
    print(f"\n--- Welcome {Name} To Shree Ram kirana Store ---")
    ShreeRamKiranaStore()
