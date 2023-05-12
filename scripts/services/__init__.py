from scripts.core.handlers.inventory_handler import InventoryHandler
from fastapi import APIRouter, HTTPException, status
from scripts.constants.api_endpoints import APIEndpoints
from scripts.schemas import RequestSchema, ResponseSchema

inventory_router = APIRouter(prefix=APIEndpoints.api)

@inventory_router.get(APIEndpoints.get_all_items)
def get_all_items():
    try:
        print("get_all_items")
        return InventoryHandler().get_all_items()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e.args)
        ) from e

@inventory_router.get(APIEndpoints.get_item)
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
        InventoryHandler().add_item(product.dict())
        return {"message": "Product added successfully"}
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
