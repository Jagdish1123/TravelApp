from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()

# Create your models here.
class Trip(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=2)  # ISO country code (e.g., "US", "IN")
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city}, {self.country}"


class Notes(models.Model):
    NOTE_TYPES = [
        ("event", "Event"),
        ("dining", "Dining"),
        ("experience", "Experience"),
        ("general", "General"),
    ]

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="notes")
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=NOTE_TYPES)
    img = models.ImageField(upload_to="note/", blank=True, null=True)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True
    )

    def __str__(self):
        return f"{self.name} in ({self.trip.city})"
