from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
import uuid

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user
