from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.services.report import (
    generate_report
)

router = APIRouter()

@router.post("/report")
def create_report(payload: dict):

    filename = "recommendation_report.pdf"

    generate_report(
        filename,
        payload["movie"],
        payload["review_sentiment"],
        payload["recommendations"]
    )

    return FileResponse(
        filename,
        media_type="application/pdf",
        filename=filename
    )