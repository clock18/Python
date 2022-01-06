# Visibility (가시성)

class Product(object):          
    pass

class Inventory(object):
    def __init__(self):
        self.__items = []

    def addNewItem(self,product):
        if type(product) == Product:
            self.__items.append(product)
            print('new item added')
        else:
            print('error')

    def getNumberofItems(self):
        return len(self.__items)