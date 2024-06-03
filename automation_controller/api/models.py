from django.db import models

# Create your models here.
class User(models.Model):
    mac_addr = models.CharField(max_length=17, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    orange_hrm_username = models.CharField(max_length=30)
    orange_hrm_password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email