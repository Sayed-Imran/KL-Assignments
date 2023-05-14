from scripts.constants import DataBases, Collections
from scripts.utils.mongo_utility import MongoUtility

class Inventory(MongoUtility):
    def __init__(self, uri):
        super().__init__(uri, DataBases.interns_b2_23, Collections.imran_inventory)

    def get_all_products(self):
        return self.get_all_documents()

    def get_product_by_id(self, product_id: str):
        return self.get_documents_by_query({"product_id": product_id})

    def insert_product(self, product: dict):
        return self.insert_document(product)

    def update_product(self, product_id: str, product: dict):
        self.update_document({"product_id": product_id}, product)
    
    def delete_product(self, product_id: str):
        self.delete_document({"product_id": product_id})
        
    def pipeline_aggregration(self, pipelines: list):
        return self.get_by_aggregation(pipelines=pipelines)
    