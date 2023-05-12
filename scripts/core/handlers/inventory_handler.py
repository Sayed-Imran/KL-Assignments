from scripts.db.mongo.intern_b2_23.collections.inventory import Inventory
from scripts.config import MongoDB
from shortuuid import uuid
from datetime import datetime

class InventoryHandler:
    def __init__(self) -> None:
        self.uri = MongoDB().uri
        self.inventory = Inventory(uri=self.uri)
    
    def get_all_items(self):
        products = self.inventory.get_all_products()
        if not products:
            return []
        for product in products:
            del product["_id"] 
        return products

    def get_item(self, product_id: str):
        try:
            product = self.inventory.get_product_by_id(product_id)
            for x in product:
                del x["_id"]
            return x
        except Exception as e:
            return {"message": "Product not found"}
    
    def add_item(self, item: dict):
        item["product_id"] = uuid()[:8]
        item["created_at"] = datetime.now()
        item["updated_at"] = datetime.now()
        return self.inventory.insert_product(item)
    
    def update_item(self, product_id: str, item: dict):
        item["updated_at"] = datetime.now()
        self.inventory.update_product(product_id, item)
    
    def delete_item(self, product_id: str):
        self.inventory.delete_product(product_id)
    