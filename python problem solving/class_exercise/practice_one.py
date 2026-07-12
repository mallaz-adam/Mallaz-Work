# Library Book System:
books = []
class Book:
    total_books = 0
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_pages = 0
        self.is_available = True
        Book.total_books += 1

    def read(self,pages):
        self.current_pages += pages
        
    def restart(self):
        self.current_pages = 0
    
    def borrow(self):
        if not self.is_available:
            print("---> This book can t be borrowed <---")
        else:
            choice = input(">>> are you sure about borrowing this book (Y/N) ? : ").upper().strip() == "Y"
            if choice:
                self.borrow = True
    
    def display_info(self):
        print(f"---> Title : {self.title} <---")
        print(f"---> Author : {self.author} <---")
        print(f"---> Progress : {self.current_pages} / {self.pages} <---")
        print(f"---> Status : {"Borrowed" if  not self.is_available else "Not borrowed"} <---")

# Admin part :
def Add_book(books):
    print("-"*30)
    print("---> Add book <---")
    book_name = input(">>> enter book name : ").strip()
    book_author = input(">>> enter book author : ").strip()
    book_pages = int(input(">>> enter book pages : "))
    new_book = Book(book_name,book_author,book_pages)
    books.append(new_book)
    print("---> The book was added <---")
    print("-"*30)


def remove_book(books):
    print("-"*30)
    print("---> Remove book <---")
    if len(books) > 0:
      book_title = input(">>> enter the book title you want to remove : ").strip().lower()
      while len(book_title) == 0:
        print("??? Wrong input , don t type empty title ???")
        book_title = input(">>> enter the book title you want to remove : ").strip().lower()
      found = False
      for i in range(len(books)):
        if books[i].title.lower() == book_title:
            save_index = i
            found = True
            break
      if found:
        print(f"---> Book founded : {books[save_index].title} <---")
        choice = input(">>> are you sure about removing this books (Y/N) ? :  ").upper().strip() == "Y"
        if choice:
            books.remove(books[save_index])
            print("---> The books was removed <---")
      else:
        print("??? Oops book not found ???")
    else:
       print("??? The list is empty ???")
    print("-"*30)
# costumer Side:

def borrow_book(books):
    print("-"*30)
    print("---> Borrow Book <---")
    
    print("-"*30)
   
    
        


