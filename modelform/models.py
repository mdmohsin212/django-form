from django.db import models

# Create your models here.

class ModelForm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    email = models.EmailField()
    about = models.TextField()
    # binary_field = models.BinaryField()
    date = models.DateField()
    date_time = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()
    float_value = models.FloatField()
    ip = models.GenericIPAddressField()
    time = models.TimeField()
    url = models.URLField()
    image = models.ImageField(upload_to='file/')
    file = models.FileField(upload_to='files/')
    agree = models.BooleanField()
