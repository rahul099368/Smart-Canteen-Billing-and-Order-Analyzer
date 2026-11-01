#Smart Canteen Billing and Order Analyzer
Veg_Sandwich = 60
Masala_Dosa = 80
Chole_Bhature = 90
Paneer_Roll = 100
Tea = 20

#for display menu
print(f"======SMART CANTEEN======")
print("1. Veg Sandwich - 60")
print("2. Masala Dosa - 80")
print("3. Chole Bhature - 90")
print("4. Paneer Roll - 100")
print("5. Tea - 20\n")

#for item choosen
sub_total = 0
count1 = 0
quantity1 = 0
count2 = 0
quantity2 = 0
count3 = 0
quantity3 = 0
count4 = 0
quantity4 = 0
count5 = 0
quantity5 = 0
while True:
    item = int(input("\nChoose item number: "))
    quantity = int(input("Enter quantity: "))
    if item == 1:
        print(f"Added: Veg Sandwich X {quantity} = RS {Veg_Sandwich*quantity}")
        sub_total += Veg_Sandwich*quantity
        count1 += 1
        quantity1 = quantity
    elif item == 2:
        print(f"Added: Masala Dosa X {quantity} = RS {Masala_Dosa*quantity}")
        sub_total += Masala_Dosa*quantity
        count2 += 1
        quantity2 = quantity
    elif item == 3:
        print(f"Added: Chole Bhature X {quantity} = RS {Chole_Bhature*quantity}")
        sub_total += Chole_Bhature*quantity
        count3 += 1
        quantity3 = quantity
    elif item == 4:
        print(f"Added: Paneer Roll X {quantity} = RS {Paneer_Roll*quantity}")
        sub_total += Paneer_Roll*quantity
        count4 += 1
        quantity4 = quantity
    elif item == 5:
        print(f"Added: Tea X {quantity} = Rs {Tea*quantity}")
        sub_total += Tea*quantity
        count5 += 1
        quantity5 = quantity
    else:
        print("this item is not in menu...\n")
    another_item = input("Add another item? (y/n):")
    if another_item == 'n':
        print("thanks for buying...\n")
        break
    elif another_item == 'y':
        continue
    else:
        while True:
            another_item = input("invalid operation, add another item? (y/n):")
            if another_item == 'n':
                print("thanks for buying...\n")
                break
            elif another_item == 'y':
                break
    if another_item == 'n':
        break
  
#for reciept
print("\n======RECEIPT======")
if count1 == 1:
    print(f"Veg Sandwich X {quantity1} = RS {Veg_Sandwich*quantity1}")
if count2 == 1:
    print(f"Masala Dosa X {quantity2} = RS {Masala_Dosa*quantity2}")
if count3 == 1:
   print(f"Chole Bhature X {quantity3} = RS {Chole_Bhature*quantity3}")
if count4 == 1:
    print(f"Paneer Roll X {quantity4} = RS {Paneer_Roll*quantity4}")
if count5 == 1:
    print(f"Tea X {quantity5} = Rs {Tea*quantity5}")
print(f"Sub Total: RS {sub_total}")
if sub_total >= 500:
    discount = (sub_total*10)/100
    print(f"Discount: RS {discount}")
    final_amount = sub_total - discount
    print(f"Final total: RS {final_amount}")
elif sub_total > 250 and sub_total <= 499.99:
    discount = (sub_total*5)/100
    print(f"Discount: RS {discount}")
    final_amount = sub_total - discount
    print(f"Final total: RS {final_amount}")
else:
    print(f"Discount: RS 0.00")
    print(f"final total: RS {sub_total}")
print("Thank you!")