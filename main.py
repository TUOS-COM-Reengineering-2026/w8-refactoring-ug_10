from collections import defaultdict
class CustomerManager:

    FUTURE_DISCOUNT = 300
    VIP = 1000
    PRIORITY = 800

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
        for c, p in self.customers.items():
            total_price = 0

            for item in p:
                if item['price'] > self.tax_threshold:
                    taxed_price = item['price'] * (1 + self.tax_rate)
                    total_price += taxed_price
                else:
                    total_price += item['price']

            print(c)

            self.customerBenefits(total_price)
      

    def customerBenefits(self, total_price):
        print(self.isDiscount(total_price))
        print(self.customerStatus(total_price))


    def isDiscount(self, total_price):
        if total_price > self.discount_threshold:
            return "Eligible for discount"
        else:
            return "Potential future discount customer" if total_price > self.FUTURE_DISCOUNT else "No discount"
        
    def isPriority(self, total_price):
        return "Priority Customer" if total_price > self.PRIORITY else ""
        
    def customerStatus(self, total_price):
        return "VIP Customer!" if total_price > self.VIP else self.isPriority(total_price)

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
