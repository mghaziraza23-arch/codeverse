print("Wlcome To Invoice Genrator")
print("Choose 1 type of Invoice")
print("Tip the commands are: Normal invoice, Grocery invoice and Grocery with Voucher invoice")
Invoices = input(" Normal Invoice, Grocery Invoice or Grocery With Voucher Invoice: ")
if Invoices == "Normal invoice":
  print("Here you go Fill The Details")
  Normal_Heading = input("Heading")
  Normal_Time = input("Timing")
  Normal_Date = input("Date")
  Normal_Details = input("Details")
  print(Normal_Heading)
  print(Normal_Time)
  print(Normal_Date)
  print(Normal_Details)
  

elif Invoices == "Grocery invoice":
 print("Here You Go Fill The Details")
 Grocery_Heading = input("Heading")
 Grocery_Time = input("Timing")
 Grocery_Date = input("Date")
 Grocery_Details = input("Details \n")
 item1 = input("Grocery item1. Write the in the next text box price")
 item1price = float(input("Grocery item1 price"))
 item2 = input("Grocery item2.  Write theh price in next")
 item2price = float(input("Grocery item2 price"))
 item3 = input("Grocery item3.  Write the price in next")
 item3price = float(input("Grocery item3 price"))
 item4 = input("Grocery item4.  Write the  price in the next one")
 item4price = float(input("Grocery item4 price"))
 item5 = input("Grocery item5.  Write in price the next ")
 item5price = float(input("Grocery item5 price"))
 if item1 == "":
  item1 = "No Item"
 if item2 == "":
  item2 = "No Item"
  if item3 == "":
   item3 = "No Item"
   if item4 == "":
     item4 = "No Item"
     if item5 == "":
      item5 = "No Item"
 Subtotal = item1price + item2price + item3price + item4price + item5price 
 Tax = float(1)
 result = item1price + item2price + item3price + item4price + item5price + Tax
 print(Grocery_Heading)
 print(Grocery_Time)
 print(Grocery_Date)
 print(Grocery_Details)
 print(item1)
 print(item2)
 print(item3)
 print(item4)
 print(item5, )
 print("Your Subtotal is:",Subtotal)
 print("Tax:",Tax)
 print("Final total is:", result)
elif Invoices == "Grocery with Voucher invoice":
 print("Here You Go Fill The Details")
 Voucher_Heading = input("Heading")
 Voucher_Time = input("Timing")
 Voucher_Date = input("Date")
 Voucher_Details = input("Details ")
 item1 = input("Grocery item 1")
 item1price = float(input("Grocery item1 price"))
 item2 = input("Grocery item 2")
 item2price = float(input("Grocery item2 price"))
 item3 = input("Grocery item 3")
 item3price = float(input("Grocery item3 price"))
 item4 = input("Grocery item 4")
 item4price = float(input("Grocery item4 price"))
 item5 = input("Grocery item 5")
 item5price = float(input("Grocery item5 price"))
 Discount1 = input("Voucher1")
 discounts = float(Discount1)
 VSubtotal = item1price + item2price + item3price + item4price + item5price 
 VTax = float(1)
 Vresult = item1price + item2price + item3price + item4price + item5price + VTax - discounts
 print(Voucher_Heading)
 print(Voucher_Time)
 print(Voucher_Date)
 print(Voucher_Details)
 print("Groceries")
 print(item1)
 print(item2)
 print(item3)
 print(item4)
 print(item5 )
 print("Discounts")
 print( "Subtotal:", VSubtotal)
 print("Tax:", VTax)
 print(" You got a", Discount1, "$ discount"  )
 print("Your total is :",Vresult)
 if item1 == "":
  item1 = "No Item"
 if item2 == "":
  item2 = "No Item"
  if item3 == "":
   item3 = "No Item"
   if item4 == "":
    item4 = "No Item"
    if item5 == "":
      item5 = "No Item"
Feedback = int(input("Pls Give a FeedBack 1 to 5 stars"))
if Feedback == 5:
 print("Thank you!!")
elif Feedback == 4:
 print("Thank you!!")
elif Feedback < 4:
 reason = input("May i know the reason? we will fix it soon!")
else:
 print("Thank you we will fix it soon!! :D") 

