"""
Interactive Calculator & Unit Converter
A beginner-friendly CLI program with:
  1. Basic arithmetic (+, -, *, /)
  2. Unit conversion (km <-> miles, Celsius <-> Fahrenheit)
  3. Currency conversion (fixed sample rates)
Input validation is done with while loops.
"""

# ---------- Settings ----------
# Sample exchange rates (1 unit of currency = X INR).
# These are fixed example values - edit them to match today's rates.
RATES_TO_INR = {
    "INR": 1.0,
    "USD": 85.0,
    "EUR": 92.0,
    "GBP": 108.0,
}


# ---------- Input helpers (validation with while loops) ----------
def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        text = input(prompt).strip()
        try:
            return float(text)
        except ValueError:
            print("  Invalid input. Please enter a number (e.g. 12 or 3.5).")


def get_choice(prompt, valid_choices):
    """Keep asking until the user enters one of the valid choices."""
    while True:
        choice = input(prompt).strip().upper()
        if choice in valid_choices:
            return choice
        print(f"  Invalid choice. Please pick one of: {', '.join(valid_choices)}")


def ask_yes_no(prompt):
    """Return True for yes, False for no. Repeats until valid."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("  Please type 'y' or 'n'.")


# ---------- Arithmetic functions ----------
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None  # signals "cannot divide by zero"
    return a / b


# ---------- Conversion functions ----------
def km_to_miles(km):
    return km * 0.621371


def miles_to_km(miles):
    return miles / 0.621371


def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def convert_currency(amount, from_cur, to_cur):
    amount_in_inr = amount * RATES_TO_INR[from_cur]
    return amount_in_inr / RATES_TO_INR[to_cur]


# ---------- Menu actions ----------
def calculator():
    print("\n--- Calculator ---")
    while True:
        a = get_number("Enter first number: ")
        op = get_choice("Choose operation (+, -, *, /): ", ["+", "-", "*", "/"])
        b = get_number("Enter second number: ")

        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = subtract(a, b)
        elif op == "*":
            result = multiply(a, b)
        else:
            result = divide(a, b)

        if result is None:
            print("  Error: You cannot divide by zero.")
        else:
            print(f"  Result: {a} {op} {b} = {result:.2f}")

        if not ask_yes_no("Do another calculation? (y/n): "):
            break


def unit_converter():
    print("\n--- Unit Converter ---")
    print("  1. Kilometers to Miles")
    print("  2. Miles to Kilometers")
    print("  3. Celsius to Fahrenheit")
    print("  4. Fahrenheit to Celsius")
    choice = get_choice("Choose (1-4): ", ["1", "2", "3", "4"])

    if choice == "1":
        value = get_number("Enter distance in km: ")
        print(f"  {value} km = {km_to_miles(value):.2f} miles")
    elif choice == "2":
        value = get_number("Enter distance in miles: ")
        print(f"  {value} miles = {miles_to_km(value):.2f} km")
    elif choice == "3":
        value = get_number("Enter temperature in °C: ")
        print(f"  {value}°C = {celsius_to_fahrenheit(value):.2f}°F")
    else:
        value = get_number("Enter temperature in °F: ")
        print(f"  {value}°F = {fahrenheit_to_celsius(value):.2f}°C")


def currency_converter():
    print("\n--- Currency Converter ---")
    currencies = list(RATES_TO_INR.keys())
    print(f"  Available currencies: {', '.join(currencies)}")

    from_cur = get_choice("Convert from: ", currencies)
    to_cur = get_choice("Convert to: ", currencies)

    # Amount must be positive
    while True:
        amount = get_number("Enter amount: ")
        if amount >= 0:
            break
        print("  Amount cannot be negative.")

    result = convert_currency(amount, from_cur, to_cur)
    print(f"  {amount:.2f} {from_cur} = {result:.2f} {to_cur}")
    print("  (Note: rates are fixed sample values.)")


# ---------- Main program ----------
def main():
    print("=" * 40)
    print("  Calculator & Unit Converter")
    print("=" * 40)

    while True:
        print("\nMain Menu")
        print("  1. Calculator")
        print("  2. Unit Converter")
        print("  3. Currency Converter")
        print("  4. Exit")
        choice = get_choice("Choose an option (1-4): ", ["1", "2", "3", "4"])

        if choice == "1":
            calculator()
        elif choice == "2":
            unit_converter()
        elif choice == "3":
            currency_converter()
        else:
            print("\nThank you for using the program. Goodbye!")
            break


if __name__ == "__main__":
    main()