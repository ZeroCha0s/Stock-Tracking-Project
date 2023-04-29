# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:29:17 2023

@author: Devon King
"""

sum = 0
count = 0
full_name = input("What is your full name: ")
min_price = float(input("Enter the minimum price: "))
price_list = [69.8, 74.5, 84.5, 93.5, 67.4, 55.45, 35.0, 22.65, 89.6, 43.70]
for price in price_list:
    sum=sum+price
    if price > min_price:
        count=count+1
    


print('Hello ',full_name,"The minimum price is ", min_price)
print("There are ", count, "prices greater than the minimum price")
print("The total price for everything is ", sum)


