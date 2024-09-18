# Hub to execute code

from budget_category import BudgetCategory

def run_budget_management():
    print("Personal Budget Management System")
    
    # Create an instance of BudgetCategory
    food_category = BudgetCategory("Food", 500)
    
    # Add an expense
    food_category.add_expense(100)
    
    # Display category summary
    food_category.display_category_summary()

if __name__ == "__main__":
    run_budget_management()
