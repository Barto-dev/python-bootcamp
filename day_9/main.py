from art import logo

print(logo)
print("Welcome to the secret auction program")

bidding_finished = False
bids = {}


def find_highest_bidder(bidding_records):
    winner_bid = 0
    winner_name = ''
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > winner_bid:
            winner_bid = bid_amount
            winner_name = bidder

    print(f"The winner is {winner_name} with a bid of ${winner_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'")

    if should_continue != 'yes':
        bidding_finished = True

find_highest_bidder(bids)
