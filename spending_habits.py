# Micki Eustache
# Date: 09/05/24
# This program calculates weekly spending on lunch

PA_TAX = 0.06
PRICE_OF_MEAL = 12.49

MEALS_PER_WEEK = 5
MEAL_TAX = PRICE_OF_MEAL * PA_TAX

tot_without_tax = MEALS_PER_WEEK * PRICE_OF_MEAL
tot_w_tax = MEALS_PER_WEEK * (PRICE_OF_MEAL + MEAL_TAX)

print()
print("| Lunch Spending Habits |")
print("-------------------------")
print(f"Tax per meal: {MEAL_TAX}")
print(f"Total without tax: {tot_without_tax}")
print(f"Total with tax: {tot_w_tax}")
print("-------------------------")
print()