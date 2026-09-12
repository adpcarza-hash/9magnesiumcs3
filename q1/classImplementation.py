class Viand:
    def __init__(self, name: str, price: int, stock: int, calories: int):
        self.name = name
        self.price = price
        self.__stock = stock
        self.calories = calories

    def sellViand(self):
        if self.__stock > 0:
            self.__stock -= 1 
            print(f"One serving of {self.name} was sold. Remaining stock: {self.__stock}")
            return True
        else:
            print(f"{self.name} is out of stock.")
            return False 

    def serveViand(self, amount: int):
        if amount <= 0:
            print ("The amount to serve must be greater than zero.")
            return False

        if amount > self.__stock:
            print(f"Not enough stock to serve {amount} servings of {self.name}. Remaining stock: {self.__stock}")
            return False

        self.__stock -= amount 
        print(f"\n{amount} servings of {self.name} were served. Remaining stock: {self.__stock}")
        return True

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Price : ₱{self.price}")
        print(f"Stock : {self.__stock}")
        print(f"Calories : {self.calories}")

    def check_stock(self):
        return self.__stock

viand1 = Viand("Pork Sisig", 75, 250, 300)
viand2 = Viand("Pork Dinakdakan", 60, 200, 350)

print("---BEFORE---")
print(f"{viand1.name}'s Info:")
viand1.display_info()

print(f"\n{viand2.name}'s Info:")
viand2.display_info()

print("\nChoose a viand:")
print(f"1. {viand1.name}")
print(f"2. {viand2.name}")

choice = input("Enter 1 or 2: ")

if choice == "1":
    selected_viand = viand1
elif choice == "2":
    selected_viand = viand2
else:
    print("Invalid choice. Select from available viands only.")
    selected_viand = None

if selected_viand is not None:
    amount = int(
        input(
            f"How many portions of {selected_viand.name} "
            "do you want to serve? "
        )
    )
    selected_viand.serveViand(amount)

print("\n---AFTER---")
print(f"{viand1.name}'s Info:")
viand1.display_info()

print(f"\n{viand2.name}'s Info: ")
viand2.display_info()

