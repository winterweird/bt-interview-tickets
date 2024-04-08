from django.db import models
from django.contrib.auth.models import User
from .infrastructure import Infrastructure


class Ticket(models.Model):
    status_choices = (
        ("open", "Open"),
        ("in_progress", "In progress"),
        ("closed", "Closed"),
        ("pending", "Pending"),
    )
    priority_choices = (
        (1, "P1"),
        (2, "P2"),
        (3, "P3"),
    )
    resolution_choices = (
        ("hardware", "Hardware"),
        ("customer", "Customer"),
        ("thirdparty", "Third party"),
        ("operations", "Operations"),
        ("change", "Change"),
        ("merged", "Merged"),
    )
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="createdby", blank=True, null=True
    )
    last_modified = models.DateTimeField(auto_now=True)
    assignee = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="assignee", blank=True, null=True
    )
    status = models.CharField(max_length=255, choices=status_choices, default="open")
    priority = models.IntegerField(choices=priority_choices, default=2)
    infrastructure = models.ForeignKey(
        Infrastructure, on_delete=models.CASCADE, blank=True, null=True
    )
    resolution = models.CharField(
        max_length=255, choices=resolution_choices, blank=True, null=True
    )
    response_eta = models.DateTimeField(blank=True, null=True)
    eta = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
