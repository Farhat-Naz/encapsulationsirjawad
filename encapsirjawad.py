class Library():
    def __init__(self, name, location):
        self.lib_name = name
        self.lib_location = location
        self.books = []
        
        self.__expenses = {'salaryExp':2322, 'KE_Bill':2222}


    def get_expenses(self):
        return self.__expenses
    
    def update_expenses(self, update_exp):
        self.__expenses = {'salaryse':44333, 'KE_Bill':324324}
        self.__expenses = update_exp
                
    def add_book(self, new_book_name):
         return self.books.append(new_book_name)
         
    def remove_book(self, remove_book):
        return self.books.remove(remove_book)
    
    def get_book(self):
        return self.books
    
mylib = Library("The library", 'karachi')    
mylib.add_book("thenation")
print(mylib.get_book())
print(mylib.get_expenses())

                   