from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

def upload_to(instance, filename):
    return 'files/curriculum/{filename}'.format(filename=filename)

class Partner(models.Model):
    
    cv_file = models.FileField(blank=False, null=False, upload_to = upload_to) 
    message = models.TextField()
    name = models.TextField()
    phone = models.CharField(max_length=255, blank=False, null=False, default='')
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, blank = True, null = True)
    
