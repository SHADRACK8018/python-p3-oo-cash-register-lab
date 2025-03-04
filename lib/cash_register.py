class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []  # Track item titles
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        # Add an item with its price and quantity
        if isinstance(price, (int, float)) and price > 0:
            for _ in range(quantity):
                self.items.append(title)  # Store only the item title
            self.total += price * quantity
            self.last_transaction = price * quantity
        else:
            raise ValueError("Price must be a positive number.")

    def apply_discount(self):
        # Apply discount to the total
        if self.discount > 0:
            discount_amount = (self.total * self.discount) / 100
            self.total -= discount_amount
            
            # Print the updated total, remove decimal if it's an integer
            if self.total.is_integer():
                print(f"After the discount, the total comes to ${int(self.total)}.")
            else:
                print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Undo the last transaction
        self.total -= self.last_transaction
        self.last_transaction = 0

    def get_items(self):
        # Return the list of items added to the register
        return self.items
