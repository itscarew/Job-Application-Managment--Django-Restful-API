from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class JobCategory(models.Model):
    name = models.CharField(max_length=100)
    published_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1
    )  # Associate with a user

    def __str__(self):
        return f"{self.name}"


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    requirements = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    published_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        JobCategory, on_delete=models.CASCADE, default=1
    )  # Associate with a category
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1
    )  # Associate with a user

    def __str__(self):
        return f"{self.title}"


class Application(models.Model):
    STATUS_CHOICES = [
        ("Submitted", "Submitted"),
        ("Reviewed", "Reviewed"),
        ("Interviewed", "Interviewed"),
        ("Hired", "Hired"),
        ("Rejected", "Rejected"),
    ]
    job_posting = models.ForeignKey(
        Job, on_delete=models.CASCADE, default=1
    )  # Associate with a job
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    resume = models.FileField(upload_to="resumes/")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="Submitted"
    )
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.job_posting} "
