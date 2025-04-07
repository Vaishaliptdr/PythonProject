class Login_page:

    def __init__(self,EmailId,Password,Age):
        self.email=EmailId
        self.password=Password
        self.age=Age

    def Login_confirm(self):
        if self.email=='vaishali@gmail.com' and self.password=='123':
            print('Login Successful')
        else:
            print('Not allowed')

    def is_eligible(self):
        if self.age>='18':
            print('Eligible for voting')
        else:
            print('Not eligible for voting')

email=input('Enter username: ')
password=input('Enter password: ')
age=input('Enter age: ')

login=Login_page(email,password,age)
login.Login_confirm()


login.is_eligible()

