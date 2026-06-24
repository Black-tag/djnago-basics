from django.db import models
import uuid
from django.utils import timezone

# Create your models here.





class Company(models.Model):
    class CompanyType(models.TextChoices):
        TECH = "TECH", "Technology"
        FIN = "FIN", "Finance"
        BIO = "BIO", "Biotechnology"

    id = models.UUIDField(
        'uuid_of_comany',
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )
    name = models.CharField(
        'name_of_company',
        max_length=255,
        unique=True
    )
    company_type = models.CharField(
        max_length=10,
        choices=CompanyType,
        
    )
    created_at = models.DateTimeField(
        'created_time_of_comapny',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'latest_updated_time',
        default=timezone.now
    )

    def __str__(self):
        return f"{self.name} | {self.company_type} | {self.created_at:%Y-%m-%d}"

