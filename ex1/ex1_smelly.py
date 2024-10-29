class OrderProcessor:
    def process_order(self, order):
        # Step 1: Validate order details
        self.validate_order(order)
        
        # Step 2: Calculate total price
        total_price = self.calculate_total_price(order)
        
        # Step 3: Apply discounts if applicable
        total_price = self.apply_discounts(total_price, order.get("discount_code"))
        
        # Step 4: Update inventory
        self.update_inventory(order)
        
        # Step 5: Generate receipt
        receipt = self.generate_receipt(order, total_price)
        
        # Step 6: Send confirmation email
        self.send_confirmation_email(order["customer_id"], receipt)
        
        return receipt

    def validate_order(self, order):
        if not order.get("customer_id"):
            raise ValueError("Customer ID is required.")
        if not order.get("items"):
            raise ValueError("Order must contain items.")

    def calculate_total_price(self, order):
        return sum(item["price"] * item["quantity"] for item in order["items"])

    def apply_discounts(self, total_price, discount_code):
        discounts = {"SUMMER20": 0.8, "WELCOME10": 0.9}
        return total_price * discounts.get(discount_code, 1.0)

    def update_inventory(self, order):
        for item in order["items"]:
            item_id = item["id"]
            quantity = item["quantity"]
            print(f"Updating inventory for item {item_id}, reducing stock by {quantity}.")

    def generate_receipt(self, order, total_price):
        receipt = f"Customer ID: {order['customer_id']}\nItems:\n"
        for item in order["items"]:
            receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
        receipt += f"Total: ${total_price:.2f}\n"
        return receipt

    def send_confirmation_email(self, customer_id, receipt):
        print(f"Sending email to customer {customer_id} with receipt:\n{receipt}")
