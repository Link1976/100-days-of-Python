#from replit import clear

#HINT: You can call clear() to clear the output in the console.

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids_record = {}

def add_bids(person_name, bid_value):

  bids_record[name] = bid_value

def find_highest_bidder(all_bids):

  highest_bid = 0

  winner = ""

  for bidder in all_bids:

    bid_amount = all_bids[bidder]

    if bid_amount > highest_bid:

      highest_bid = bid_amount

      winner = bidder

  print("The winner is " + winner + " with a bid of $" + str(highest_bid) + ".")

keep_asking = True

while keep_asking:

  name = input("Please type your name: \n")

  bid = int(input("Please enter your bid: \n"))

  add_bids(name, bid)

  question = input("Any other user has a bid (y / n)? \n").lower()

  if question == "y":

    #clear()

    add_bids(name,bid)

  else:

    find_highest_bidder(bids_record)

    keep_asking = False

 

print(bids_record)