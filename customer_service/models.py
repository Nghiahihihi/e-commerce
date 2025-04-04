from django.db import models

# Địa chỉ của khách hàng
class Address(models.Model):
    nation = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=20, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.house_number} {self.street}, {self.city}, {self.nation}"


# Khách hàng
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
