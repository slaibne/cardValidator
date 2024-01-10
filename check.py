# Identifies card type based on the prefix
def card_type(card_number):
    card_types = {
        "4": "Visa",
        "5": "Mastercard",
        "6": "Discover",
        "37": "American Express",
    }
    prefix = card_number[:1]
    return card_types.get(prefix, "Unknown")


# Validates number using the Luhn check
def luhn(n):
    r = [int(ch) for ch in str(n)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d * 2, 10)) for d in r[1::2])) % 10 == 0


def check_card(card_number):
    if 13 < len(card_number) > 16:  # checks number of digits
        return False
    validate = luhn(card_number)
    if validate == True:
        c_type = card_type(card_number)
        print("Card type:", c_type)
    else:
        print("Invalid")


card_number = input("Enter a credit card number: ")
check_card(card_number)
