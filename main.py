from replit import clear
from art import logo


print(logo)

blind_auction_bids={}
highestBidder = ""
highestBid = 0

while True:
  bidderName = input("What is your name?: ")
  bidAmt = int(input("What's your bid?: "))
  flag = input("Are there any other bidders? Type 'yes' or 'no'.\n")

  if bidAmt > highestBid:
    highestBid = bidAmt
    highestBidder = bidderName

  if flag == "yes" :
    clear()
  elif flag == "no":
    print(f"The winner is {highestBidder} with a bid of {highestBid}")
    break
  
  blind_auction_bids[bidderName] = bidAmt


