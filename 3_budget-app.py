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
            return True

        else:
            return False

    def __str__(self):
        table = self.name.center(30, "*") + "\n"
        for i in self.ledger:
          table += f"{i['description'][0:23].ljust(23)}{format(i['amount'], '.2f').rjust(7)}\n"
        table += f"Total: {format(self.get_balance(), '.2f')}"
        return table


def create_spend_chart(categories):
    names = []
    spents = []
    table_list = []
    dash_list = ['    ' + '---'*len(categories)+'-']

    percentages = []
    first_space_list = []
    second_space_list = []
    third_space_list = []

    first_name_list = []
    second_name_list = []
    third_name_list = []




    for i in range(100,-10,-10):
        table_list.append((str(i) + '|').rjust(4))

    for i in categories:
        names.append(i.name)
        spend = 0

        for j in i.ledger:
            if j["amount"]<0:
                spend -=j["amount"]

        spents.append(round(spend,2))

    sum_spents = sum(spents)


    for i in range(len(categories)):
        percent = (spents[i]/sum_spents)*100
        percentages.append(round(percent,0))


    # name length for calculation
    name_length = []

    for i in range(len(names)):
        name_length.append(len(names[i]))

    max_name_length = max(name_length)


    # first percantage list append

    for i in range(100,-10,-10):
        num1 = percentages[0]

        if num1 < i:
            first_space_list.append('   ')

        else:
            first_space_list.append(' o ')

    # second percantage list append

    for i in range(100,-10,-10):
        num2 = percentages[1]

        if num2 < i:
            second_space_list.append('   ')

        else:
            second_space_list.append(' o ')

    # third percantage list append
    for i in range(100,-10,-10):
        num3 = percentages[2]

        if num3 < i:
           third_space_list.append('    ')

        else:
           third_space_list.append(' o  ')


    # first name list append
    for i in range(max_name_length):
        if i < name_length[0]:
            first_name_list.append('     ' + names[0][i] + ' ')

        else:
            first_name_list.append('     ' + ' ' + ' ')

    # second name list append
    for i in range(max_name_length):
        if i < name_length[1]:
            second_name_list.append(' ' + names[1][i] + ' ')

        else:
            second_name_list.append(' ' + ' ' + ' ')

    # third name list append
    for i in range(max_name_length):
        if i < name_length[2]:
            third_name_list.append(' ' + names[2][i] + '  ')

        else:
            third_name_list.append(' ' + ' ' + '  ')

    
    # 1. frist result for return
    result1 = 'Percentage spent by category\n'


    # 2. second result for return
    result2 = ''
    for i in range(len(table_list)):
        result1 +=''.join(table_list[i]) + ''.join(first_space_list[i]) + ''.join(second_space_list[i]) + ''.join(third_space_list[i]) + '\n'


    # 3. third result for return
    result3 = ''.join(dash_list) + '\n'


    # 4. forth result for return
    result4 = ''
    for i in range(max_name_length):

        if i< max_name_length-1:
            result3 += ''.join(first_name_list[i]) + ''.join(second_name_list[i]) + ''.join(third_name_list[i]) + '\n'

        else:
            result3 += ''.join(first_name_list[i]) + ''.join(second_name_list[i]) + ''.join(third_name_list[i])



    #final result
    final_result = ''.join(result1) + ''.join(result2) + ''.join(result3) + ''.join(result4)


    return final_result

