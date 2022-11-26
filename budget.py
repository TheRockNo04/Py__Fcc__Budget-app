def create_spend_chart(categories = list()):
	string = "Percentage spent by category"
	
	max_len = -1
	for e in categories:
		if len(e.name) > max_len:
			max_len = len(e.name)
	
	chart_width = len(categories)*3
	chart_y_axis_count = 100

	total = 0
	total_spent_list = list()
	for e in categories:
		category_spent = 0
		for i in e.ledger:
			if i["amount"] < 0:
				category_spent -= i["amount"]
				total -= i["amount"]
		total_spent_list.append(category_spent)

	persentage_spent = list()
	for e in total_spent_list:
		persentage = (e / total) * 100
		persentage_spent.append(persentage)

	# --- Top	
	chart_y_axis = ""

	for _ in range(11):
		chart_y_axis = chart_y_axis + "\n" + str(chart_y_axis_count).rjust(3) + "| "
		for i,e in enumerate(persentage_spent):
			if e >= chart_y_axis_count:
				chart_y_axis = chart_y_axis + "o  "
				persentage_spent[i] -= 10
			else: chart_y_axis = chart_y_axis + "   "
		chart_y_axis_count -= 10
	string = string + chart_y_axis + "\n"
	
	# --- Mid
	string = string + (" "*4) + ("-"*(chart_width+1))

	# --- Bottom
	for i in range(max_len):
		chart_x_axis = " ".rjust(5)
		for j in categories:
			try: chart_x_axis = chart_x_axis + j.name[i] + "".rjust(2)
			except IndexError: chart_x_axis = chart_x_axis + " ".rjust(2) + "".rjust(1)
		string = string + "\n" + chart_x_axis
	return string



class Category:
	balance = 0
	spent = 0

	def __init__(self, name):
		self.name = name
		self.ledger = list()

	def __repr__(self):
		# --- Category line
		stars = (30-len(self.name))/2
		first_line = f"{'''*''' * int(stars)}{self.name}{'''*''' * int(stars + (0.5 if stars > int(stars) else False))}"
		
		# --- Content of ledger
		second_line = ""
		list = []
		for i,e in enumerate(self.ledger):
			decimal = f"{e['amount']:.2f}"
			list.append(f"\n{decimal.rjust(30)}")
			list[i] = e["description"]
			second_line = second_line + "\n" + list[i][:23].ljust(23) + str(decimal).rjust(7)
		
		# Total balance
		total = f"\nTotal: {self.get_balance()}"

		return first_line + second_line + total
	
	def deposit(self, amount, description=""):
		self.amount = amount
		self.description = description
		self.ledger.append({"amount": amount, "description": description})
		self.balance += self.amount

	def withdraw(self, amount, description = ""):
		self.amount = amount
		if self.balance >= self.amount:
			self.balance -= self.amount
			self.ledger.append({"amount": (amount*-1), "description": description})
			return True
		else: 
			return False

	def transfer(self, amount, to):
		self.amount = amount
		transfer_to = to
		if self.check_funds(self.amount):
			self.withdraw(self.amount, f"Transfer to {transfer_to.name}")
			to.deposit(self.amount, f"Transfer from {self.name}")
			return True
		else:
			return False

	def get_balance(self):
		return self.balance

	def check_funds(self, amount):
		self.amount = amount
		if self.balance >= self.amount: return True
		else: return False
