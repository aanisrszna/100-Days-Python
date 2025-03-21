# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)
print("Welcome to secret auction program.")

def highest(bidding_rec):
    highest_bid =0
    winner=""
    for bidder in bidding_rec:
        amount = bidding_rec[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner} with bid of ${highest_bid}")

bids={}
bidding_finished = False
while not bidding_finished:

    name = input("What is your name?:")
    bid = int(input("what's your bid?:"))

    bids[name]=bid
    additional = input("Are there any other biiders? Types 'yes' or 'no'").lower()

    if additional == "no":
        bidding_finished= True
        highest(bids)
    elif additional =="yes":
        bidding_finished= False
        print("\n"*20)