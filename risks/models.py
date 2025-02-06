from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class risk(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class control(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    risk = models.ForeignKey(risk, on_delete=models.CASCADE)

    def __str__(self):
        return self.name