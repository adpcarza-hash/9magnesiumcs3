# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

**Name:** Angela

**Section:** 9-Magnesium

**Last Name:** Carza

**Date:** August 20, 2026

---

### 1. Encapsulation
	
Encapsulation is the grouping of objects with their related information or function. In the Sari-Sari Store Inventory System situation, it can be applied by creating a product class that stores the product's name, price, and quantity together in one object. We can also use methods such as AddStock(), that can be used to modify the quantity instead of changing the data directly. Thus, by using this concept, we can prevent a disorganized program in which numerous variables are scattered throughout the code. Furthermore, this can decrease the possibility of errors in the code, and the program will appear more readable.

### 2. Abstraction

Abstraction is the concept of making the program appear much simpler by hiding the complex operations. In the Sari-Sari Store Inventory System situation, it can be applied by hiding the complicated processes involved in managing the inventory, like when the cashier uses the methods; AddItem(), RemoveItem(), and DisplayItems(), the exact process or how it works won’t be shown. Therefore, by using this concept, the system becomes much more simpler and easier to use. 

### 3. Inheritance
	
Inheritance is the concept of an object inheriting the product properties or information from the existing class/category that it belongs to, together with the similar products under that same class/category. In the Sari-Sari Store Inventory System situation, it can be applied by creating different product classes that inherit common properties from an existing product class. For example, FoodProduct and CleaningProduct inherits the product's name, price, and quantity, but it can also have their own additional properties, such as an expiration date or brand. By using this concept, we can decrease the repetition of code, thus allowing the program to be much more organized.

### 4. Polymorphism

Polymorphism is the concept of using a command that displays different information depending on what the product is. It basically uses the same operation, but gives different results due to the product’s difference in properties or information. In the Sari-Sari Store Inventory System situation, it can be applied by allowing different types of products to use the same method but perform it differently. For instance, both FoodProduct and CleaningProduct can have a DisplayInfo() method, but each can display information specific to its type such as the FoodProduct’s expiration date, and the CleaningProduct’s brand. By using this, the program becomes simpler and easier to use.

---

## Reflection
	
Among the 4 Pillars of OOP, I think encapsulation would be the most useful and fitting solution. The original scenario emphasizes the problem of having too many product variables, and indicated that most people would commonly use multiple variables for each item. However, it is stated that that isn’t the most optimal solution. Thus, with the help of encapsulation, these related pieces of information can be grouped and controlled through methods. This further makes the inventory system more organized, and easier to maintain.
