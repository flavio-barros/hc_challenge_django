from django.db import models

# Create your models here.
class Report(models.Model):
    message = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    supervisors = models.ManyToManyField('auth.User', related_name="reports")

class ReportResponse(models.Model):
    message = models.TextField()
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)