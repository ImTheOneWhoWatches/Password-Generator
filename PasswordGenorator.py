import random
import colorama
from colorama import Fore, Style
import time

def reset_script():
    global all, length, amount
    length = 20
    amount = 10

    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "123456789"
    symbols = "!@#$%^&*()_+-=~`:;{[}]:;>.<,?/"

    upper, lower, nums, syms = True, True, True, True

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += symbols

def print_banner():
    print(Fore.BLUE + """
     ______ __           ____               _       __  __          _       __          __           __
    /_  __// /_   ___   / __ \  ____   ___ | |     / / / /_   ____ | |     / / ____ _  / /_  _____  / /_   ___    _____
     / /  / __ \ / _ \ / / / / / __ \ / _ \| | /| / / / __ \ / __ \| | /| / / / __ `/ / __/ / ___/ / __ \ / _ \  / ___/
    / /  / / / //  __// /_/ / / / / //  __/| |/ |/ / / / / // /_/ /| |/ |/ / / /_/ / / /_  / /__  / / / //  __/ (__  )
   /_/  /_/ /_/ \___/ \____/ /_/ /_/ \___/ |__/|__/ /_/ /_/ \____/ |__/|__/  \__,_/  \__/  \___/ /_/ /_/ \___/ /____/
""" + Style.RESET_ALL)

def print_separator():
    print(Fore.GREEN + "========================================================================================================================" + Style.RESET_ALL)

def generate_password():
    global all, length, amount

    print_separator()
    print("Generated Passwords:")
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)

reset_script()

print_banner()

generate_password()

while True:
    user_input = input("\nType 'esc' to exit, or 'res' to reset: ")
    if user_input.lower() == "esc":
        print("Exiting the script.")
        time.sleep(2)
        break
    elif user_input.lower() == "res":
        print("Resetting...")
        reset_script()
        generate_password()
    else:
        print("Make sure you typed 'esc' or 'res' correctly")
