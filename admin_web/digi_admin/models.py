from django.db import models
import uuid
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.





class Companies(models.Model):
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
    verified = models.BooleanField(
        'verified_compnay',
        default=False
    )
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ["name"]

        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["verified"]),
            models.Index(fields=["company_type"]),
        ]

    def __str__(self):
        return f"{self.name} | {self.company_type} | {self.created_at:%Y-%m-%d}"

class Departments(models.Model):

    id = models.UUIDField(
        'department_id',
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        'department_name',
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )
    company = models.ForeignKey(
        Companies,
        on_delete=models.CASCADE
    )
    description = models.TextField(
        verbose_name='description of departments',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False
    )
    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ["company","name"]

        indexes = [
            models.Index(fields=["name"])
        ]

    def __str__(self):
        return self.name

class Employees(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        verbose_name='name of employee',
        unique=True,
        blank=False,
        null=False,
        editable=True,
        max_length=255
    )
    department = models.ForeignKey(
        Departments,
        on_delete=models.CASCADE
    )
    salary = models.PositiveIntegerField()
    joined_date = models.DateField(
        verbose_name='joining date of employee',
        
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    manager = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0.00,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    # rating2 = models.DecimalField(
    #     max_digits=3,
    #     decimal_places=2,
    #     default=0.00,
    #     validators=[
    #         MinValueValidator(0),
    #         MaxValueValidator(5)
    #     ]
    # )
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ["name"]

        indexes = [
            models.Index(fields=["name"])
        ]

    def __str__(self):
        if self.manager:
            return f"{self.name} (Manager: {self.manager.name})"
        return self.name

class Users(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False
    )
    employee = models.ForeignKey(
        Employees,
        on_delete=models.CASCADE
    )
    email = models.EmailField(
        null=False,
        blank=False,
        unique=True
    )
    ip_address = models.GenericIPAddressField(
        protocol="both"
    )
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class EmployeeProject(models.Model):

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False
        )
    duration = models.DurationField(
        blank=False,
        null=False
        )
    employees = models.ManyToManyField(
        Employees,
        related_name="projects"
    )
    website = models.URLField()
    metadata = models.JSONField(default=dict)
    logo = models.ImageField(
        upload_to="logos/",
        null=True,
        blank=True,
        )
    document = models.FileField(
        upload_to="documents/",
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.title
    


    






