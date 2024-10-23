from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    category_id: int


class Product(ProductBase):
    # конвертирует бд модель в pydantic (json) модель для http ответа
    model_config = ConfigDict(from_attributes=True)
    id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductUpdatePartial(ProductBase):
    name: str | None = None
    description: str | None = None
    price: int | None = None
    category_id: int | None = None
