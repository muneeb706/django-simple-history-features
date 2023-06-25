from django.db import models
from simple_history.models import HistoricalRecords

# Docs: https://django-simple-history.readthedocs.io/en/latest/historical_model.html?highlight=inherit#allow-tracking-to-be-inherited

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(inherit=True)
  
class ChildModel(BaseModel):
    title = models.CharField(max_length=255, blank=False, null=False)

