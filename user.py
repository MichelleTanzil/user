class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
kobe = User("Kobe Bryant", "kobe@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(300)
guido.make_withdrawl(400)
guido.display_user_balance()

monty.make_deposit(50)
monty.make_deposit(150)
monty.make_withdrawl(25)
monty.make_withdrawl(15)
monty.display_user_balance()

kobe.make_deposit(500)
kobe.make_withdrawl(50)
kobe.make_withdrawl(50)
kobe.make_withdrawl(50)
kobe.display_user_balance()

guido.transfer_money(monty, 100)
