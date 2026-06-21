from pydantic import BaseModel

class ReviewRequest(BaseModel):
    review: str


class ReviewsRequest(BaseModel):
    reviews: list[str]