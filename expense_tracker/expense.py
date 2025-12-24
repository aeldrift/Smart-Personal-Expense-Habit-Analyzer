
class Expense:
    def __init__(self, amount, category, note):
        self.amount = amount
        self.category = category
        self.note = note

expenses = []
# while True: or

n = int(input("How many expenses do you want to add?"))

for i in range(n):
    print(f"\nExpense {i+1}")
    amount = int(input("Enter amount: "))
    category = input("Enter category: ")
    note = input("Enter note: ")
