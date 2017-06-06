from django.db import models


class Hostels(models.Model):
    Hostel_name = models.CharField(max_length=200)
    Area = models.CharField(max_length=50)
    Category = models.CharField(max_length=200)
    Price = models.IntegerField()

    def __str__(self):
        return self.Hostel_name + ' - ' + self.Area


class Owner(models.Model):
    Name = models.ForeignKey(Hostels, on_delete=models.CASCADE)
    Owner_name = models.CharField(max_length=200)
    Contacts = models.IntegerField()
    Email = models.EmailField(max_length=200)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.Owner_name
