from ABS import ABS,abstractmethod
class Featureplan(ABS):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
class webapp(Featureplan):
    def login(self):
        print("Web Login is done")
    def logout(self):
        print("Web logout is done")
app=webapp()
app.login()
app.logout()
