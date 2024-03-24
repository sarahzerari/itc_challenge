from django.db import models

class Registration(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    email = models.EmailField()
    number_of_persons = models.IntegerField()
    date = models.DateField()
    duration_type = models.CharField(max_length=10)  # Could be hours, months, years
    time = models.TimeField()
    duration = models.IntegerField(help_text="Duration in selected duration type")

    def __str__(self):
        return f"{self.name} {self.family_name} - {self.email}"