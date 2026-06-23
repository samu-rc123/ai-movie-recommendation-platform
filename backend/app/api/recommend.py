from fastapi import APIRouter

router = APIRouter()

@router.get("/recommend-test")
def recommend_test():
    return {
        "status": "recommend router loaded"
    }