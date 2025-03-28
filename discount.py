def calculate_discount(price,  rate):
    return price - (price *rate/100)

price = int(input(("enter amount:")))

    

rate = int(input(("enter rate:")))

result = calculate_discount(price, rate)

if rate >= 20:
 print ("final amount is:", result)

else:
 print ("the amount is:", price ,"sorry no discount !!!")