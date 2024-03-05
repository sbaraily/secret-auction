from replit import clear
from art import logo

print(logo)
repeat = True
bidders = []

while repeat:
  name = input("What is your name?: ")
  bid_price = int(input("What's your bid?: $"))

  bidder_profile = {'name': name, 'bid': bid_price}
  other_bidders = input(
      "Are there any other bidders? Type 'yes' or 'no'. \n").lower()
  bidders.append(bidder_profile)

  if other_bidders == 'yes':
    clear()
  elif other_bidders == 'no':
    repeat = False
    bid_info = []
    for bidder in bidders:
      bid_info.append(bidder['bid'])
    max_bid = (max(bid_info))
    max_name = bid_info.index(max_bid)
    winner = bidders[max_name]['name']
    print(f"The winner is {winner} with a bid of ${max_bid}")
