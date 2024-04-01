MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10


def deposit():
    while True:
        amount = input("Would you like to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("too hemjee 0 eees ih baih ystoi shdee bro")
        else:
            print("Too oruulaa huu")
    return amount


def get_number_of_lines():
    while True:
        lines  = input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit:
            lines = int(lines)
            if 1<=lines<=3:
                break
            else:
                print("Enter a valid number")
        else:
            print("please enter a number")
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet? $: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Too oruulaa huu")
    return amount

def main():
    balance  = deposit()
    lines = get_number_of_lines()
    while True:              
        bet = get_bet()
        total_bet  = bet*lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, you current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equals to {total_bet}.")
main()