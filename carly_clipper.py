hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# First, let’s sum up all the prices of haircuts. Create a variable total_price, and set it to 0.
total_price = 0

# Iterate through the prices list and add each price to the variable total_price.
for price in prices:
  total_price+=price


# After your loop, create a variable called average_price that is the total_price divided by the number of prices.
# Print the value of average_price
average_price = total_price/len(prices)
print("Average Haircut Price: %s" %(average_price))


# That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.
new_prices = [price-5 for price in prices]
print(new_prices)


# Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.

# Create a variable called total_revenue and set it to 0.
total_revenue = 0


# Use a for loop to create a variable i that goes from 0 to len(hairstyles)
# Hint: You can use range() to do this!

# Add the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step.
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue:%s" %(total_revenue))

# Find the average daily revenue by dividing total_revenue by 7. Call this number average_daily_revenue and print it out.
average_daily_revenue = total_revenue/7
print(average_daily_revenue)


# Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.
# Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.
# You can use range() in your list comprehension to make i go from 0 to len(new_prices) - 1.
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
