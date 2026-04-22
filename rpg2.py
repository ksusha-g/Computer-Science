class Book():

    def __init__(self, name: str, year: int) -> None: #аннотации типов используются всегда
        self.name = name
        self.year = year

book1 = Book('Война и мир', '1812')

# UML - unify Moduling Language

class Student:

    def __init__(self, name: str):
        self.name = name

class Teather:

    def __init__(self, name: str) -> None:
        self.name = name
        self.students = []

        def add_student(self, student: Student):
            self.students.append(student)





class Product:

    def __init__(self, name: str) -> None:
        self.name = name
        seld.orders = []

class Order:

    def __init__(self, id: int) -> None:
        self.id = id
        self.products = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)
        product.orders.append(self)
        
    
