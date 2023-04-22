from django.db import models


class signin(models.Model):
    email_address=models.CharField(max_length=50)
    password=models.CharField(max_length=25)


    def __str__(self):
        return self.email_address



class signup(models.Model):
    email_address=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    password=models.CharField(max_length=25)
    confirm_password=models.CharField(max_length=25)
    country=models.CharField(max_length=25)
    address=models.CharField(max_length=25)



    def __str__(self):
        return self.email_address


