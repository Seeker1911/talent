from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.timezone import datetime

# musicians can only have one manager and one producer
class Musicians(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    phone = models.CharField(max_length=15, null=True, default=None)
    social = models.CharField(max_length=200, blank=True, null=True, default=None)
    genre = models.CharField(max_length=200, blank=True ,null=True, default=None)
    company = models.CharField(max_length=200, blank=True, null=True, default=None)
    engineering = models.BooleanField(default=False)
    artistDevelopment = models.BooleanField(default=False)
    bio = models.TextField(max_length=500, blank=True ,null=True, default=None)
    location = models.CharField(max_length=30, blank=True, null=True, default=None)
    image = models.CharField(max_length=300, blank=True, null=True, default=None)

    def __str__(self):
        return self.user.last_name

    class Meta:
        ordering = ('user',)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Musicians.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.musicians.save()


# Events can have many musicians and musicians can have many events.
class Events(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField('email')
    phone = PhoneNumberField(max_length=15, null=True, default=None)
    social = models.CharField(max_length=200, blank=True, null=True, default=None)
    genre = models.CharField(max_length=200, blank=True, null=True, default=None)
    location = models.CharField(max_length=200, blank=True, null=True, default=None)
    musician = models.ManyToManyField(Musicians, related_name='events')
    # date = models.DateField(auto_now=False, auto_now_add=False)
    date = models.CharField(max_length=200, blank=True, null=True, default=None)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

# Musicians can have many songs.
class Song(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    artist = models.ForeignKey(Musicians, related_name='songs')
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, default=0)
    length = models.CharField(max_length=8, default=0)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
