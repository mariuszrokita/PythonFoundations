def get_order():
    print("[command] [item] (command is 'a' to add, 'd' to delete, 'q' to quit ")
    line = input()
    
    command = line[:1]      # get subtext (aka. text slicing)
    item = line[2:]
    return command, item    # pack variables into tuple and return


def add_to_cart(item, cart):
    if not item in cart:
        cart[item] = 0
    cart[item] += 1


def delete_from_cart(item, cart):
    if item in cart:
        cart[item] -= 1

    if cart[item] == 0:
        del cart[item]
        

def process_order(order, cart):
    command, item = order   # unpack tuple into variables

    if command == "a":
        add_to_cart(item, cart)
    elif command == "d" and item in cart:
        delete_from_cart(item, cart)
    elif command == "q":
        return False

    return True


# alist  = [1, 2, 3]    List is mutable, ordered
# atuple = (1, 2, 3)    Tuple is immutable
# aset = {1, 2, 3}      Set is an unordered collection with unique items.
#                       Set cannot be indexed.
#                       Cool operations:
#                           set1.difference(set2)
#                           set1 - set2   difference (short syntax)
#                           set2 - set1
#                           set1 & set2   intersection. elements that are in both sets
#                           set1 ^ set2   symmetric difference. returned set has elements that are unique in each set.
#                           set1 | set2   union
#
# adict = { "x1":"y1", "x2":"y2" }

def go_shopping():
    cart = dict()

    while True:
        order = get_order()
        if not process_order(order, cart):
            break

    print(cart)
    print("Finished!")

go_shopping()
