
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

    e = Expense(amount, category, note)
    expenses.append(e)

    print("Expense added successfully")

    # choice = input("Do you want to add another expense? (y/n): ")
    # if choice.lower() != "y":
        break

print("\nAll Expenses:")
for e in expenses:
    print(e.amount, e.category, e.note) #Example: e1 =Expense(250, "food", "Lunch at canteen")



