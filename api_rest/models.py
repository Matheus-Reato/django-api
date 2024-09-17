from django.db import models

class Car(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=80, default='')
    model = models.CharField(max_length=80, default='')
    year = models.CharField(max_length=4, default='')

    def __str__(self):
        return f'ID: {self.id} | Brand: {self.brand} | Model: {self.model}'
    
    class Meta:
        db_table = 'car'
