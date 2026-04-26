from pydantic import BaseModel

class CategorySelect(BaseModel):
    categories: list[str]
