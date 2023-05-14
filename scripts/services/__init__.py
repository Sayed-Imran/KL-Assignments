from scripts.core.handlers.inventory_handler import InventoryHandler
from scripts.core.handlers.mail_handler import EmailHandler,Email
from fastapi import APIRouter, HTTPException, status
from scripts.constants.api_endpoints import APIEndpoints
from scripts.schemas import RequestSchema, ResponseSchema

inventory_router = APIRouter(prefix=APIEndpoints.api)

@inventory_router.get(APIEndpoints.get_all_items)
def get_all_items():
    try:
        return InventoryHandler().get_all_items()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e.args)
        ) from e

@inventory_router.get(APIEndpoints.get_item, response_model=ResponseSchema)
def get_item(product_id: str):
    try:
        return InventoryHandler().get_item(product_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e.args)
        ) from e

@inventory_router.post(APIEndpoints.create_item)
def add_item(product: RequestSchema):
    try:
        return InventoryHandler().add_item(product.dict())
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e.args)
        ) from e


@inventory_router.put(APIEndpoints.update_item)
def update_item(product_id: str, product: RequestSchema):
    try:
        return InventoryHandler().update_item(product_id, product.dict())
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e.args)
        ) from e
        
@inventory_router.delete(APIEndpoints.delete_item)
def delete_item(product_id: str):
    try:
        return InventoryHandler().delete_item(product_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e.args)
        ) from e

@inventory_router.get(APIEndpoints.inventory_price)
def get_inventory_price():
    try:
        return InventoryHandler().inventory_price()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e.args)
        ) from e

@inventory_router.post(APIEndpoints.mail)
def send_email(email: Email):
    try:
        return EmailHandler().send_email(email)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e.args)
        ) from e
