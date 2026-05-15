'''
Welcome, manager, to your new place of employment: BrB_ Inc., the OFFICIAL manufacturer of bootleg Breaking Bad merchandise!
Naturally, it's a very competitive industry we find ourselves in. In order to keep up with the competition, we have to be on
top of every detail of our financial well-being, and this includes inventory! Your job is to determine how much inventory
value we have, how much of each product we have, which product has the highest contribution margin, and how our inventory would
be affected should we have a sale.

I never thought I would find myself coding an inventory management system for a Breaking Bad bootleg merch store. The places that
information systems takes you are extraordinary!

Inputs:
- What product do you want to take a look at? (str) (This assumes the user knows the names of all inventory items)
- Do you want to see overall inventory health? (str) (This will come after output for individual product selection)

Processing:
- Loop through collections until product type is identified, then specific product, then product price
- Contribution margin is calculated (price minus product type cost)
- Accumulator goes through collection prices until total value is determined

Output:
- Message containing identified product price, quantity, and contribution margin
- Message showing total inventory value, highest and lowest item value, and items that need to be reordered
'''

#Collection: gotta know inventory type, inventory type cost, specific product, and product price
#The inventory dictionary key items show inventory type, the inner inventory key items are item names, the first number in the
#tuple is price, and the second number in the tuple is stock

inventory = {
    "t-shirt":{"walter white shirt":(20,200),"jessie pinkman shirt":(20,95),"retro meth shirt":(30,70),"gus shirt":(25,88)},
    "plush":{"crossbow plush":(35,41),"heisenberg plush":(30,4),"meth van plush":(40,0)},
    "poster":{"blue meth poster":(15,76),"saul goodman 'objection!' poster":(22,67),"breaking bad all characters poster":(18,29)}
}
inventory_cost = {
    "t-shirt":8,
    "plush":15,
    "poster":4
}
item_list = ["walter white shirt","jessie pinkman shirt","retro meth shirt","gus shirt","crossbow plush","heisenberg plush",
             "meth van plush","blue meth poster","saul goodman 'objection!' poster","breaking bad all characters poster"]

#Inputs and input validation
merch_ok = False
while not merch_ok:
    merch = input("Which of your items would you like to take a better look at today? ").lower()
    for item in item_list:
        if merch == item:
            merch_ok = True
    if not merch_ok:
        print("That is not a valid item, please try again.")

if merch_ok == True:
    item_stats = []
    for category in inventory:
        for item in inventory[category]:
            if item == merch:
                item_stats.append(category)
                item_stats.append(item)
                item_stats.append(inventory[category][item][0])
                item_stats.append(inventory[category][item][1])
                for cost in inventory_cost:
                    if cost == category:
                        item_stats.append(inventory_cost[cost])
#In item_stats: item 0 = item type, item 1 = item name, item 2 = item price, item 3 = item stock, item 4 = item cost to manufacture
else:
    print("full stop")

C_margin = item_stats[2] - inventory_cost[item_stats[0]]

#Outputs 1
print(f"\nThe price of the {item_stats[1]} is ${item_stats[2]}. There are currently {item_stats[3]} in stock, and it"
      f" has a contribution margin of ${C_margin}.\n")

#Input 2 and Processing 2
report_yes = "N/A"
while report_yes != "no" and report_yes != "yes":
    report_yes = input("Would you like to look at an overall inventory report as well? y/n ").lower()
    if report_yes == "yes":
        inventory_total = 0
        inventory_high = 0
        IH_items = ""
        inventory_low = 1000
        IL_items = ""
        inventory_reorder = []
        for category in inventory:
            for item in inventory[category]:
                inventory_total += (inventory[category][item][0] * inventory[category][item][1])
                if inventory[category][item][0] > inventory_high:
                    inventory_high = inventory[category][item][0]
                    IH_items = item
                if inventory[category][item][0] < inventory_low:
                    inventory_low = inventory[category][item][0]
                    IL_items = item
                if inventory[category][item][1] < 30:
                    inventory_reorder.append(item)

        New_I = ", ".join(inventory_reorder)
        print(f"\nThe total value of your inventory is currently ${inventory_total}.")
        print(f"The highest value item is the {IH_items} which costs ${inventory_high}, and the lowest is the {IL_items} which costs ${inventory_low}.")
        print(f"It's wise to resupply when you have less than 30 of an item in stock. You currently have less than 30 of each of the following"
            f" items: {New_I}")
    elif report_yes == "no":
        print("Have a great day!")
    else:
        print("Please just type yes or no.")
    