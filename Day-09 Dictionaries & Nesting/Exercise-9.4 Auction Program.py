from replit import clear
bids = {}
highest_bid = 0
winner = ""
repeate = False
while not repeate:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    ask = input("Do you want to repeat? Yes or No? ").lower()
    if ask == "yes":
        clear()
    if ask == "no":
        for bidder in bids:
            bid_price = bids[bidder]
            if bid_price > highest_bid:
                highest_bid = bid_price
                winner = bidder
        print("Overall bid is:",bids)
        print(f"Winner is {winner} with a bid of ${highest_bid}")
        repeate = True

