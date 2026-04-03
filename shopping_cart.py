class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        total = 0
        for item in self.items:
            total = total + item["price"]
        
        return f"Cart with {len(self)} items, total: ${total:.2f}."

    def add(self, item):
        self.items.append(item)
    
    def get_expensive_items(self, threshold):
        return [item for item in self.items if item["price"] >= threshold]
