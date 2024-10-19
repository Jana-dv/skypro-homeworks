class User:
    def __init__(self, first_name, last_name):
        print("создан")
        self.firstName = first_name
        self.lastName = last_name

    def getName(self):
        print("Мое имя", self.firstName)
    
    def getSurname(self):
        print("Моя фамилия", self.lastName)

    def getNameSurname(self):
        print("Меня зовут", self.firstName, self.lastName)

alex = User("Brad", "Pitt")
alex.getName()
alex.getSurname()
alex.getNameSurname()
