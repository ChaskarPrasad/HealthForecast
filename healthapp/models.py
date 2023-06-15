from django.db import models

# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name
    
class DiseaseInfo(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=500,blank=True,null=True)
    info = models.TextField()

    def __str__(self) -> str:
        return str(self.disease)+" Info"