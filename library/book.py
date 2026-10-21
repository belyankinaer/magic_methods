class Book:
    def __init__(self, name: str, author: str, text: str):
        self.__name = name
        self.__author = author
        self.__text = text

    def get_name(self):
        if self.__name:
            return self.__name
