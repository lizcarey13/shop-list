shop_list = []

def add_shop():
    global shop_list
    x = raw_input("What would you like to add? ")
    x = str.lower(x)
    if x in shop_list:
        return "You already have this in your list"
    shop_list.append(x)
    sort_alpha(shop_list)
    print shop_list

def rem_shop():
    global shop_list
    y = raw_input ("What would you like to remove? ")
    y = str.lower(y)
    if y in shop_list:
        shop_list.remove(y)
    else:
        print "That item isn't in your list!"
    shop_list.sort()
    print shop_list

def sort_alpha(list_name):
    return list_name.sort()

