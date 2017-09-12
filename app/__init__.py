from app.customTemplateFlask import CustomTemplateFlask

app = CustomTemplateFlask(__name__)
from app import views
