from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

def generate_report(
    filename,
    movie,
    sentiment,
    recommendations
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Movie Recommendation Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"Selected Movie: {movie}",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Review Sentiment: {sentiment['label']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Confidence: {sentiment['score']:.2f}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "Recommendations",
            styles["Heading2"]
        )
    )

    for item in recommendations:

        content.append(
            Paragraph(
                f"{item['title']} "
                f"(Adjusted Score: "
                f"{item['adjusted_score']})",
                styles["Normal"]
            )
        )

    doc.build(content)

    return filename