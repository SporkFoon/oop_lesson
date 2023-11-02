class Account:
    def __init__(self, account_number, account_type, account_name, balance):
        self.account_number = account_number
        self.account_type = account_type
        self.account_name = account_name
        self.balance = balance

class AccountDatabase:
    def __init__(self):
        self.account_database = []

    def create_account(self, account_number, account_type, account_name, initial_balance):
        index = self.search_account(account_number)
        if index == -1:
            account = Account(account_number, account_type, account_name, initial_balance)
            self.account_database.append(account)
        else:
            print("Account", account_number, "already exists")

    def delete_account(self, account_number):
        index = self.search_account(account_number)
        if index != -1:
            print("Deleting account:", self.account_database[index].account_number)
            del self.account_database[index]
        else:
            print(account_number, "invalid account number; nothing to be deleted.")

    def search_account(self, account_number):
        for i in range(len(self.account_database)):
            if self.account_database[i].account_number == account_number:
                return i
        return -1

    def deposit(self, account_number, amount):
        index = self.search_account(account_number)
        if index != -1:
            print("Depositing", amount, "to", self.account_database[index].account_number)
            self.account_database[index].balance += amount
        else:
            print(account_number, "invalid account number; no deposit action performed.")

    def withdraw(self, account_number, amount):
        index = self.search_account(account_number)
        if index != -1:
            if self.account_database[index].balance >= amount:
                print("Withdrawing", amount, "from", self.account_database[index].account_number)
                self.account_database[index].balance -= amount
            else:
                print("Withdrawal amount", amount, "exceeds the balance of",
                      self.account_database[index].balance, "for", account_number, "account.")
        else:
            print(account_number, "invalid account number; no withdrawal action performed.")

    def show_account(self, account_number):
        index = self.search_account(account_number)
        if index != -1:
            print("Showing details for", self.account_database[index].account_number)
            print(vars(self.account_database[index]))
        else:
            print(account_number, "invalid account number; nothing to be shown for.")


account_db = AccountDatabase()

account_db.create_account("0000", "saving", "David Patterson", 1000)
account_db.create_account("0001", "checking", "John Hennessy", 2000)
account_db.create_account("0003", "saving", "Mark Hill", 3000)
account_db.create_account("0004", "saving", "David Wood", 4000)
account_db.create_account("0004", "saving", "David Wood", 4000)
print(account_db.account_database)

account_db.show_account('0003')
account_db.deposit('0003', 50)
account_db.show_account('0003')
account_db.withdraw('0003', 25)
account_db.show_account('0003')
account_db.delete_account('0003')
account_db.show_account('0003')
account_db.deposit('0003', 50)
account_db.withdraw('0001', 6000)