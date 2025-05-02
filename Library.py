# making a Node class for the books
class Node:
    def __init__(self, book):
        self.book = book
        self.next = None

# making a link list class to mange the books I add
class FavoriteBooks:
    def __init__(self):
        #starting with a clean slate
        self.head = None  
    #here is where I add books
    def add_book(self, book):
        new_node = Node(book)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            #this 'visits' each node until it gets to the end
            while current.next:
                current = current.next
            current.next = new_node
            #letting me know that it has been added.
        print(f"'{book}' has been added to your library.")
    #this is where I remove the books
    def remove_book(self, book):
        current = self.head
        prev = None
        while current:
            if current.book == book:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                    #letting me know the book has been removed
                print(f"'{book}' has been removed from your library.")
                return
            prev = current
            current = current.next
            #if the book isnt found it will print this
        print(f"'{book}' not found in your library list.")
    #this will show your list of books if you have one, if not you will get a message
    def show_books(self):
        if not self.head:
            print("Your book list is empty.")
        else:
            print("Your Books:")
            current = self.head
            idx = 1
            while current:
                print(f"{idx}. {current.book}")
                current = current.next
                idx += 1
#The main area
def main():
    favorites = FavoriteBooks()
    #your choices
    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Show your library")
        print("4. Exit")
        
        choice = input("Please select an option: ")
        
        if choice == '1':
            book = input("Enter the name of the book to add: ")
            favorites.add_book(book)
        elif choice == '2':
            book = input("Enter the name of the book to remove: ")
            favorites.remove_book(book)
        elif choice == '3':
            favorites.show_books()
        elif choice == '4':
            print("Have a good day!")
            break
        else:
            print("I do not know that choice, try again. Please select 1, 2, 3, or 4.")
#end of code
if __name__ == "__main__":
    main() 

