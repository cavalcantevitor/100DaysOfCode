# Blind Auction

import art
import clear

auction = True
bidders = {}
highest_bid = 0
highest_bidder = ''

print(art.logo)

while auction:
    name = input(
        "Welcome to the secret auction program. What is your name?:\n")
    bid = int(input("What's your bid?:\n$"))

    def add_bid(key, value):
        bidders[key] = value

    add_bid(name, bid)

    continue_auction = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n")

    if continue_auction.lower() == 'no':
        auction = False
    else:
        clear.clear()

for key in bidders:
    if bidders[key] > highest_bid:
        highest_bid = bidders[key]
        highest_bidder = key

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
