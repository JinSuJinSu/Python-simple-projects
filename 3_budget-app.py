class Category:

    def __init__(self,name):
        self.name = name
        self.ledger = []

    def get_balance(self):
        prices = []
        for i in self.ledger:
          prices.append(i["amount"])
        total_price = sum(prices)
        return total_price


    def check_funds(self,check_amount):
        if self.get_balance() >= check_amount:
            return True
        else:
            return False

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, withdraw_amount,description=''):
        if self.check_funds(withdraw_amount)==True:
            self.ledger.append({"amount": -withdraw_amount, "description": description})
            return True

        else:
            return False



    def transfer(self, transfer_amount, budget_category=''):
        if self.check_funds(transfer_amount)==True:
            self.withdraw(transfer_amount, description = "Transfer to " + budget_category.name)
            budget_category.deposit(transfer_amount, description = "Transfer from " + self.name)

        else:
            return False

    def __str__(self):
        table = self.name.center(30, "*") + "\n"
        for i in self.ledger:
          table += f"{i['description'][0:23].ljust(23)}{format(i['amount'], '.2f').rjust(7)}\n"
        table += f"Total: {format(self.get_balance(), '.2f')}"
        return table






































        






