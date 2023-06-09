from pydantic import BaseModel

class RequestSchema(BaseModel):
    product_name: str
    quantity: int
    price: float


class ResponseSchema(BaseModel):
    product_id: str
    product_name: str
    quantity: int
    price: float
