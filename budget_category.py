# [ Task 1 ]

class BudgetCategory:
    def __init__(self, name, allocated_budget):
        self.__name = name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    # [ Getters ]
    def get_name(self):
        return self.__name

    def get_allocated_budget(self):
        return self.__allocated_budget

    # [ Setters ] 
    def set_name(self, name):

        self.__name = name

    def set_allocated_budget(self, budget):
        if budget >= 0:
            self.__allocated_budget = budget
            self.__remaining_budget = budget
        else:
            print("Budget must be a positive number.")

    # [ Methods ] 
    def add_expense(self, amount):
        if amount > 0 and amount <= self.__remaining_budget:
            self.__remaining_budget -= amount
        else:
            print("Invalid expense amount. Ensure it is positive and does not exceed remaining budget.")

    def display_category_summary(self):
        print(f"Category: {self.__name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Remaining Budget: ${self.__remaining_budget}")