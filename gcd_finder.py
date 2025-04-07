olma_narxlari = {
    "qizil_olma": 123,
    "yashil_olma":145,
    "sariq_olma": 112,
    "tosh_olma": 100
}
olmanarxlari = {}
for olmalar in olma_narxlari:
    narx = olma_narxlari[olmalar]
    if narx >=130:
        qale = olmanarxlari[olmalar] = "yaxshi narx"
        print(qale)
    elif narx >=120:
        olmanarxlari[olmalar] = "yaxshi narx"
    elif narx >=110:
        olmanarxlari[olmalar] = "yaxshi narx"
    else:
        olmanarxlari[olmalar] = "ota arzon"
        logo = r'''
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
name = input("Whats your name?\n")
price = input("whats the bid amount?\n$")
bids={}
bids[name] = price
def find_highest_bidder(bids):
    winner = ""
    highest_bid == 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
    print(f"The winner is {winner}" with the bid of {highest_bid})

continue_bidding = True
while continue_bidding:
    name = input("Whats your name?\n")
    price = input("whats the bid amount?\n$")
    bids[name] = price
    should_continue = input("Do you want to continue (y/n)?\n").lower()
    if should_continue =="no":



# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
Dictionary["name"] = name
# TODO-4: Compare bids in dictionary






