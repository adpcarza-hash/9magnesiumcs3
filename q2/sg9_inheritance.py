class Publication: #This line of code creates a class called Publication
    def __init__(self, title: str, author: str): #This line of code initializes the class with its attributes; title and author.
        self.__title = title #This line of code sets the title with an initial value.
        self.__author = author #This line of code sets the author with an initial value.

    @property #This line of code makes the method below it to function as an attribute.
    def get_title(self): #This line of code defines title as a method of the Publication class.
        return self.__title #This line of code returns the value of title.

    @property #This line of code makes the method below it to function as an attribute.
    def get_author(self): #This line of code defines author as a method of the Publication class.
        return self.__author #This line of code returns the value of author.

    def set_title(self, title): #This line of code defines a method to set the title.
        if title == "": #This line of code uses an if statement to check if the title is empty.
            raise ValueError("Title must be provided.") #This line of code raises an error if the title is empty.
        else: #This line of code is executed if the title is not empty.
            self.__title = title #This line of code sets the title with a new value.

    def set_author(self, author): #This line of code defines a method to set the author.
        if author == "": #This line of code uses an if statement to check if the author is empty.
            raise ValueError("The Author must be specified.") #This line of code raises an error if the author is empty.
        else: #This line of code is executed if the author is not empty.
            self.__author = author #This line of code sets the author with a new value.

    def display_info(self): #This line of code defines a method to display the informtion in the class Publication.)
        print(f"Title: {self.__title}") #This line of code prints the title.
        print(f"Author: {self.__author}") #This line of code prints the author.

class Book(Publication): #This line of code creates a Book class that inherits attributes from the Publication class.
    def __init__(self, title: str, author: str, number_of_pages: int): #This line of code initializes the class with its attributes; title, author, and number_of_pages.
        super().__init__(title, author) #This line of code calls the constructor of the parent class and initializes the title and author attributes.
        self.__number_of_pages = number_of_pages #This line of code sets the number_of_pages with an initial value.

    @property #This line of code makes the method below it to function as an attribute.
    def get_number_of_pages(self): #This line of code defines number_of_pages as a method of the Book class.
        return self.__number_of_pages #This line of code returns the value of number_of_pages.

    def set_number_of_pages(self, number_of_pages): #This line of code defines a method to set the number_of_pages.
        if number_of_pages <= 0: #This line of code uses an if statement to check if the number_of_pages is less than or equal to 0.
            print("Number of pages must be positive.") #This line of code prints a message if the number_of_pages is less than or equal to 0 to prevent negative values.
        else: #This line of code is executed if the number_of_pages is greater than 0.
            self.__number_of_pages = number_of_pages #This line of code sets the number_of_pages with a new value.

class Magazine(Publication): #This line of code creates a Magazine class that inherits attributes from the Publication class.
    def __init__(self, title: str, author: str, issue_number: int): #This line of code initializes the class with its attributes; title, author, and issue_number.
        super().__init__(title, author) #This line of code calls the constructor of the parent class and initializes the title and author attributes.
        self.__issue_number = issue_number #This line of code sets the issue_number with an initial value.

    @property #This line of code makes the method below it to function as an attribute.
    def get_issue_number(self): #This line of code defines issue_number as a method of the Magazine class.
        return self.__issue_number #This line of code returns the value of issue_number.

    def set_issue_number(self, issue_number): #This line of code defines a method to set the issue_number.
        if issue_number <= 0: #This line of code uses an if statement to check if the issue_number is less than or equal to 0.
            print("Issue number must be positive.") #This line of code prints a message if the issue_number is less than or equal to 0 to prevent negative values.
        else: #This line of code is executed if the issue_number is greater than 0.
            self.__issue_number = issue_number #This line of code sets the issue_number with a new value.

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & van Dongen, H.") 
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)
#The above lines of code creates instances of the Publication, Book, and Magazine classes.

print("Publication Information:")
pub1.display_info()
#The line of code above calls the display_info method of the Publication class and prints it.

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(f"Number of pages: {book1.get_number_of_pages}")
#The line of code above calls the display_info method of the Book class and prints it.

print("\nMagazine Information:")
mag1.display_info()
print(f"Issue number: {mag1.get_issue_number}")
#The line of code above calls the display_info method of the Magazine class and prints it.


#Lahat ng lines linagyan ko ng comment sir kasi di po ako sure if need lagyan lahat or hindi, so linahat ko nalang po just in case??
