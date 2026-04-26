from fastapi import APIRouter

router = APIRouter(prefix="/api/categories", tags=["categories"])

CATEGORIES = ["Yapay Zeka", "Teknoloji", "Haberler", "Kripto", "Finans", "Bilim", "Araştırma", "Siyaset"]

@router.get("/")
def list_categories():
    return {"categories": CATEGORIES}
