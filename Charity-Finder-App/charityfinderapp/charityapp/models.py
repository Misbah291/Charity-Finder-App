from django.db import models

# Create your models here.
class Charity(models.Model):
    charity_id = models.CharField(max_length=100)
    charity_name = models.CharField(max_length=150)
    street_name = models.CharField(max_length=150)
    post_code = models.CharField(max_length=50)
    district_name = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=15)
    extra_info = models.CharField(max_length=200)

    class Meta:
        db_table ="charity"
