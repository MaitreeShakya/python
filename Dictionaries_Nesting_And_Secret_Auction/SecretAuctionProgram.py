from os import system
from art import logo

print("***Welcome to the Secret Auction Program***")
print(logo)
bids = {}
continue_bidding = True


def find_highest_bidder(bidding_record):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder
    print(f"The highest bidder is {highest_bidder} with a bid of {highest_bid}")


while continue_bidding:
    bidder = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    bids[bidder] = bid
    more_bidding = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if more_bidding == "yes":
        system("cls")
        continue_bidding = True
    else:
        find_highest_bidder(bids)
        continue_bidding = False
