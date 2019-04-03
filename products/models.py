from django.db import models
from django.utils import timezone

class Product(models.Model):
    
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class BugTicket(models.Model):

    STATUS_CHOICES = (('todo', 'ToDo'), ('doing', 'Doing'), ('done', 'Done'))

    bug_issue_type = models.CharField(max_length=7, default='Bug',
                                      editable=False)
    bug_name = models.CharField(max_length=30, default='')
    bug_description = models.TextField()
    bug_status = models.CharField(max_length=5, choices=STATUS_CHOICES,
                              default="ToDo")
    bug_urgent = models.BooleanField()
    bug_published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    bug_views = models.IntegerField(default=0)

    def __str__(self):
        return self.issue_name


class FeatureTicket(models.Model):

    STATUS_CHOICES = (('todo', 'ToDo'), ('doing', 'Doing'), ('done', 'Done'))

    feature_type = models.CharField(max_length=7, default='Feature',
                                      editable=False)
    feature_name = models.CharField(max_length=30, default='')
    feature_description = models.TextField()
    feature_status = models.CharField(max_length=5, choices=STATUS_CHOICES,
                              default="ToDo")
    feature_urgent = models.BooleanField()
    feature_published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    feature_views = models.IntegerField(default=0)

    def __str__(self):
        return self.issue_name
