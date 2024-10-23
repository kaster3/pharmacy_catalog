from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    name: str
    description: str


class Category(CategoryBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class CategoryCreate(CategoryBase):
    pass
