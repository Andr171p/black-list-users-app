from fastapi.templating import Jinja2Templates

from src.config import config


templates = Jinja2Templates(directory=config.web_app.templates)
