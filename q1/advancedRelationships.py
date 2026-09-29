class Canteen_menuItem:

    def __init__(self, name: str, price: int, stock: int):
        self.name = name
        self.price = price
        self._stock = stock

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Price : ₱{self.price}")
        print(f"Stock : {self._stock}")

    def check_stock(self):
        return self._stock


class Beverage(Canteen_menuItem):

    def __init__(
        self,
        name: str,
        price: int,
        stock: int,
        size_ml: int
    ):
        super().__init__(name, price, stock)
        self.size_ml = size_ml

    def sellBeverage(self):
        if self._stock > 0:
            self._stock -= 1
            print(
                f"One serving of {self.name} was sold. "
                f"Remaining stock: {self._stock}"
            )
            return True

        print(f"{self.name} is out of stock.")
        return False

    def serveBeverage(self, amount: int):
        if amount <= 0:
            print("The amount to serve must be greater than zero.")
            return False

        if amount > self._stock:
            print(
                f"Not enough stock to serve {amount} servings "
                f"of {self.name}. Remaining stock: {self._stock}"
            )
            return False

        self._stock -= amount

        print(
            f"{amount} serving(s) of {self.name} were served. "
            f"Remaining stock: {self._stock}"
        )
        return True

    def display_info(self):
        super().display_info()
        print(f"Size : {self.size_ml} ml")


class Viand(Canteen_menuItem):

    def __init__(
        self,
        name: str,
        price: int,
        stock: int,
        calories: int,
        paired_beverage: Beverage = None
    ):
        super().__init__(name, price, stock)
        self.calories = calories
        self.paired_beverage = paired_beverage

    def pair_beverage(self, beverage: Beverage):
        self.paired_beverage = beverage

    def sellViand(self):
        if self._stock > 0:
            self._stock -= 1
            print(
                f"One serving of {self.name} was sold. "
                f"Remaining stock: {self._stock}"
            )
            return True

        print(f"{self.name} is out of stock.")
        return False

    def serveViand(self, amount: int):
        if amount <= 0:
            print("The amount to serve must be greater than zero.")
            return False

        if amount > self._stock:
            print(
                f"Not enough stock to serve {amount} servings "
                f"of {self.name}. Remaining stock: {self._stock}"
            )
            return False

        self._stock -= amount

        print(
            f"{amount} servings of {self.name} were served. "
            f"Remaining stock: {self._stock}"
        )
        return True

    def display_info(self):
        super().display_info()
        print(f"Calories : {self.calories}")

        if self.paired_beverage:
            print(
                f"Recommended Pairing : "
                f"{self.paired_beverage.name} "
                f"(₱{self.paired_beverage.price})"
            )
        else:
            print("Recommended Pairing : None")


beverage1 = Beverage("Iced Tea", 25, 100, 350)
beverage2 = Beverage("Milo Juice", 15, 80, 300)
beverage3 = Beverage("Bottled Water", 15, 150, 500)

viand1 = Viand("Pork Sisig", 75, 250, 300)
viand2 = Viand("Pork Dinakdakan", 60, 200, 350)

viand1.pair_beverage(beverage1)
viand2.pair_beverage(beverage2)


beverage_menu = {
    "1": beverage1,
    "2": beverage2,
    "3": beverage3
}


ordered_viand = None
ordered_viand_amount = 0
ordered_beverages = []


print("--- BEFORE ORDERING ---")


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

print(f"1. {viand1.name} - ₱{viand1.price}")
print(f"2. {viand2.name} - ₱{viand2.price}")

choice = input("Enter 1 or 2: ")


if choice == "1":
    selected_viand = viand1

elif choice == "2":
    selected_viand = viand2

else:
    print("Invalid choice. Select from available viands only.")
    selected_viand = None


if selected_viand is not None:

    while True:

        try:
            amount = int(
                input(
                    f"How many portions of {selected_viand.name} "
                    "do you want to serve? "
                )
            )

        except ValueError:
            print("Please enter a whole number.")
            continue

        if selected_viand.serveViand(amount):
            ordered_viand = selected_viand
            ordered_viand_amount = amount
            break


wants_beverage = input(
    "\nDo you want a beverage? (yes/no): "
).lower()


if wants_beverage == "yes":

    while True:

        print("\n--- CHOOSE A BEVERAGE ---")

        print(f"1. {beverage1.name} - ₱{beverage1.price}")
        print(f"2. {beverage2.name} - ₱{beverage2.price}")
        print(f"3. {beverage3.name} - ₱{beverage3.price}")

        beverage_choice = input("Enter 1, 2, or 3: ")


        if beverage_choice in beverage_menu:

            selected_beverage = beverage_menu[beverage_choice]

            while True:

                try:
                    beverage_amount = int(
                        input(
                            f"How many servings of "
                            f"{selected_beverage.name} "
                            "do you want to serve? "
                        )
                    )

                except ValueError:
                    print("Please enter a whole number.")
                    continue

                if selected_beverage.serveBeverage(
                    beverage_amount
                ):

                    for counter in range(beverage_amount):
                        ordered_beverages.append(
                            selected_beverage
                        )

                    break

        else:
            print("Invalid beverage choice.")
            continue


        more = input(
            "\nAdd another beverage? (yes/no): "
        ).lower()

        if more != "yes":
            break


elif wants_beverage == "no":
    print("No beverage selected.")

else:
    print("Please enter only yes or no.")


print("\n--- YOUR ORDER ---")


viand_total = 0

if ordered_viand is not None:

    viand_total = (
        ordered_viand.price * ordered_viand_amount
    )

    print(
        f"{ordered_viand_amount} portion(s) of "
        f"{ordered_viand.name} - ₱{viand_total}"
    )

else:
    print("No viand ordered.")


beverage_total = 0

for beverage in ordered_beverages:

    print(
        f"1 serving of {beverage.name} "
        f"- ₱{beverage.price}"
    )

    beverage_total += beverage.price


total = viand_total + beverage_total

print(f"Total: ₱{total}")


print("\n--- AFTER ORDERING ---")


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
