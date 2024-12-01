from fastapi import APIRouter
from fastapi import Request, Form
from fastapi.responses import RedirectResponse

from src.app.web.templates import templates


form_router = APIRouter(
    prefix="/api/form"
)


@form_router.get(path="/")
async def get_form(request: Request) -> ...:
    return templates.TemplateResponse(
        "form.html",
        {
            "request": request
        }
    )
