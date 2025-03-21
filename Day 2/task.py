print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
percent_tip = tip/100
total_tip = percent_tip * bill
total_new_amount = total_tip + bill
split = round(total_new_amount/people,2)
each_person =(f"Each person should pay:{split}")
print (each_person)