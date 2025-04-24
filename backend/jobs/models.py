from django.db import models
from django.utils import timezone
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField(blank=True, null=True)
    posted_date = models.DateTimeField(default=timezone.now)
    apply_link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} at {self.company_name}"

    class Meta:
         ordering = ['-posted_date']