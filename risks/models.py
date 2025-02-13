from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class section(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.code} {self.name}"

class control(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    section = models.ForeignKey(section, on_delete=models.CASCADE)
    description = models.TextField()
    objective = models.TextField()

    def __str__(self):
        return self.name