from collections import defaultdict
class CustomerManager:
    def __init__(self):
        self.customers = defaultdict(list)
        self.tax_rate = 0.2
        self.tax_threshold = 100
        self.discount_threshold = 500
    
    def add_customer(self, name, purchases):
        self.customers[name].extend(purchases)
    
    def add_purchases(self, name, purchases):
        self.add_customer(name, purchases)

    def generate_report(self):
        for y, x in self.customers.items():
            a = 0
            for z in x:
                if z['price'] > self.tax_threshold:
                    taxed_price = z['price'] * (1 + self.tax_rate)
                    a += taxed_price
                else:
                    a += z['price']
            print(y)
            if a > self.discount_threshold:
                print("Eligible for discount")
            else:
                if a > 300:
                    print("Potential future discount customer")
                else:
                    print("No discount")
            if a > 1000:
                print("VIP Customer!")
            else:
                if a > 800:
                    print("Priority Customer")

    def calculate_shipping_fee(self, purchases,check_for_fragile_items=False):
        heavy_item = False
        fragile_item = False

        for purchase in purchases:
            if purchase.get('weight', 0) > 20 :
                heavy_item = True
            if purchase.get('fragile', False):
                fragile_item = True
        if heavy_item:
            return 50
        elif fragile_item:
            return 60
        else:
            return 25 if check_for_fragile_items else 20



    flat_tax = 0.2