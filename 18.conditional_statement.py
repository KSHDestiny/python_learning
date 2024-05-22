diet_restrictions = set(['meat', 'cheese'])

# put more restrict condition to be higher
if 'meat' and 'cheese' in diet_restrictions:
    print("Get a vegan pizza.")
elif 'meat' in diet_restrictions:
    print("Get a cheese pizza.")
else:
    print("Get something else.")


def order_special(day):
    match day:
        case 'Sunday':
            return 'spinach pizza'
        case 'Monday':
            return 'mushroom pizza'
        case 'Tuesday':
            return 'pepperoni pizza'
        case 'Wednesday':
            return 'veggie pizza'
        case 'Thursday':
            return 'bbq chicken pizza'
        case 'Friday':
            return 'sausage pizza'
        case 'Saturday':
            return 'Hawaiian pizza'
        case _: # default condition
            print(f"There is no {day} special.")
            return None
        
today = 'Christmas'
special = order_special(today)
print(f"\nToday is {today}, and the special is {special}.\n")