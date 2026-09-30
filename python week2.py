def calculate_total(price: float, quantity: int) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")
    return price * quantity


def main() -> None:
    try:
        price = float(input("Enter the price of one item: "))
        quantity = int(input("Enter the quantity you want: "))
        total = calculate_total(price, quantity)
    except ValueError:
        print("Please enter valid numeric values.")
        return

    print(f"{quantity} items at {price:.2f} each = {total:.2f}")


if __name__ == "__main__":
    main()
