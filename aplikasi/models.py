from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(_('email_address'), unique=True)
    phone = models.CharField(_('phone'), null=True, unique=True, max_length=50)
    address = models.CharField(_('address'), null=True, max_length=250)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
    
class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)

    def __str__(self) -> str:
        return f"{self.user.username} Profile"
    
class Posting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    profile_pic = models.CharField(max_length=255, blank=True)
    date_post = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username