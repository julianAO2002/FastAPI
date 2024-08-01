from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404: {"message": "producto no encontrado"}})

products_list = ["producto1",
                "producto2",
                "producto3"]

@router.get("/")
async def products():     
    return products_list

@router.get("/{id}")
async def products(id: int):     
    return products_list[id]