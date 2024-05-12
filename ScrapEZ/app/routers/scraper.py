from fastapi import APIRouter, Response
from app.models import ScrapeRequest
from app.services.scraper_service import scrape_website

router = APIRouter(
    prefix="/scrape",
    tags=["scraper"],
)


@router.post("/")
async def scrape(request: ScrapeRequest, response: Response):
    url = request.url
    format = request.format
    data = scrape_website(url)
    if format == "csv":
        response.headers["Content-Disposition"] = "attachment; filename=data.csv"
        return Response(data.to_csv(), media_type="text/csv")
    elif format == "json":
        response.headers["Content-Disposition"] = "attachment; filename=data.json"
        return Response(data.to_json(), media_type="application/json")
    else:
        return {"error": "Invalid format. Please choose 'csv' or 'json'."}