from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
# print(logo)
repeat = True
bidders = []

while repeat:
  name = input("What is your name?: ")
  bid_price = int(input("What's your bid?: $"))
  bidder_profile = {'name': name, 'bid': bid_price}
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n")

  if other_bidders == 'yes':
    bidders.append(bidder_profile)
    clear()
  elif other_bidders == 'no':
    bidders.append(bidder_profile)
    repeat = False
    bid_info = []
    for bidder in bidders:
      bid_info.append(bidder['bid'])
    max_bid = (max(bid_info))
    max_name = max_bid['name']
    print(f"The winner is {name} with a bid of ${max_bid}")
#     repeat = False
print(bidders)
