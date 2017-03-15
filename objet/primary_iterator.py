class PrimaryIterator:

    def __init__(self):
        self.__current = 1
        self.__premiers = []

    def __ispremier(self, value):
        for i in self.__premiers:
            if value % i == 0:
                return False
        self.__premiers.append(value)
        return True

    def ispremier(self, value):
        for i in range(2, value):
            if value % i == 0:
                return False
        return True

    def __iter__(self):
        return self

    def __next__(self):
        self.__current += 1
        while not self.__ispremier(self.__current):
            self.__current += 1
        return self.__current


if __name__ == '__main__':

    premiers = PrimaryIterator()

    for i in range(15):
        print(next(premiers))