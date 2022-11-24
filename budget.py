def create_spend_chart(categories = list()):
    return None



class Category:
    balance = 0
    spent = 0
    def __init__(self, name):
        self.name = name
        self.ledger = list()
    
    def deposit(amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(amount, description = ""):
        return None
    
    def transfer(amount, where):
        return None
    
    def get_balance():
        return None
    
    def check_funds():
        return None
