from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    user_id: int
    movie: str
    review: str

