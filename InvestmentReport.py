print("\n--------Investment Report----------")
initial_investment = float(input("Initial Investment: "))
annual_interest_rate = float(input("Annual Interest Rate: "))
years = int(input("Number of Years: "))

interest_rate = annual_interest_rate / 100
investment_value = initial_investment

print("----------------------------")

for year in range(1, years + 1):
    investment_value += investment_value * interest_rate
    print("Year {}: ₹{:.2f}".format(year, investment_value))

final_amount = investment_value
growth = final_amount - initial_investment

print("----------------------------")
print("\nFinal Amount: ₹{:.2f}".format(final_amount))
print("Total Growth: ₹{:.2f}".format(growth))
print("----------------------------\n")
