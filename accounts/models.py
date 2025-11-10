from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
import uuid

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_email_verified = models.BooleanField(default=False)
    email_token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
