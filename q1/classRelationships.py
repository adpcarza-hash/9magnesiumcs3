class Viand:

    def __init__(self, name: str, price: int, stock: int, calories: int):
        self.name = name
        self.price = price
        self.__stock = stock
        self.calories = calories

    def sellViand(self):
        if self.__stock > 0:
            self.__stock -= 1
            print(
                f"One serving of {self.name} was sold. "
                f"Remaining stock: {self.__stock}"
            )
            return True
        else:
            print(f"{self.name} is out of stock.")
            return False

    def serveViand(self, amount: int):
        if amount <= 0:
            print("The amount to serve must be greater than zero.")
            return False

        if amount > self.__stock:
            print(
                f"Not enough stock to serve {amount} servings "
                f"of {self.name}. Remaining stock: {self.__stock}"
            )
            return False

        self.__stock -= amount

        print(
            f"{amount} servings of {self.name} were served. "
            f"Remaining stock: {self.__stock}"
        )
        return True

    def display_info(self):
        print(f"Name     : {self.name}")
        print(f"Price    : ₱{self.price}")
        print(f"Stock    : {self.__stock}")
        print(f"Calories : {self.calories}")

    def check_stock(self):
        return self.__stock


class Beverage:

    def __init__(self, name: str, price: int, stock: int, size_ml: int):
        self.name = name
        self.price = price
        self.__stock = stock
        self.size_ml = size_ml

    def sellBeverage(self):
        if self.__stock > 0:
            self.__stock -= 1
            print(
                f"One serving of {self.name} was sold. "
                f"Remaining stock: {self.__stock}"
            )
            return True
        else:
            print(f"{self.name} is out of stock.")
            return False

    def serveBeverage(self, amount: int):
        if amount <= 0:
            print("The amount to serve must be greater than zero.")
            return False

        if amount > self.__stock:
            print(
                f"Not enough stock to serve {amount} servings "
                f"of {self.name}. Remaining stock: {self.__stock}"
            )
            return False

        self.__stock -= amount

        print(
            f"{amount} serving(s) of {self.name} were served. "
            f"Remaining stock: {self.__stock}"
        )
        return True

    def display_info(self):
        print(f"Name  : {self.name}")
        print(f"Price : ₱{self.price}")
        print(f"Stock : {self.__stock}")
        print(f"Size  : {self.size_ml} ml")

    def check_stock(self):
        return self.__stock


viand1 = Viand("Pork Sisig", 75, 250, 300)
viand2 = Viand("Pork Dinakdakan", 60, 200, 350)

beverage1 = Beverage("Iced Tea", 25, 100, 350)
beverage2 = Beverage("Milo Juice", 15, 80, 300)
beverage3 = Beverage("Bottled Water", 15, 150, 500)

beverage_menu = {
    "1": beverage1,
    "2": beverage2,
    "3": beverage3,
}

ordered_beverages = []  

print("--- BEFORE SERVING ---")

print(f"\n{viand1.name}'s Info:")
viand1.display_info()

print(f"\n{viand2.name}'s Info:")
viand2.display_info()

print(f"\n{beverage1.name}'s Info:")
beverage1.display_info()

print(f"\n{beverage2.name}'s Info:")
beverage2.display_info()

print(f"\n{beverage3.name}'s Info:")
beverage3.display_info()

print("\n--- CHOOSE A VIAND ---")
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

wants_beverage = input("\nDo you want a beverage? (yes/no): ")

if wants_beverage == "yes":
    while True:
        print("\n--- CHOOSE A BEVERAGE ---")
        print(f"1. {beverage1.name}")
        print(f"2. {beverage2.name}")
        print(f"3. {beverage3.name}")

        beverage_choice = input("Enter 1, 2, or 3: ")

        if beverage_choice in beverage_menu:
            selected_beverage = beverage_menu[beverage_choice]

            beverage_amount = int(
                input(
                    f"How many servings of "
                    f"{selected_beverage.name} "
                    "do you want to serve? "
                )
            )
            selected_beverage.serveBeverage(beverage_amount)
            ordered_beverages.append(selected_beverage)   
        else:
            print("Invalid beverage choice.")

        more = input("\nAdd another beverage? (yes/no): ")
        if more != "yes":
            break

elif wants_beverage == "no":
    print("No beverage selected.")

else:
    print("Please enter only yes or no.")

print("\n--- YOUR BEVERAGE ORDERS ---")       
for bev in ordered_beverages:
    print(f"{bev.name} - ₱{bev.price}")

total = sum(bev.price for bev in ordered_beverages)
print(f"Total: ₱{total}")

print("\n--- AFTER SERVING ---")

print(f"\n{viand1.name}'s Info:")
viand1.display_info()

print(f"\n{viand2.name}'s Info:")
viand2.display_info()

print(f"\n{beverage1.name}'s Info:")
beverage1.display_info()

print(f"\n{beverage2.name}'s Info:")
beverage2.display_info()

print(f"\n{beverage3.name}'s Info:")
beverage3.display_info()
