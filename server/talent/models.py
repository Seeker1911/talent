from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Talent Manager can have many musicians.

# musicians can only have one manager and one producer
class Musicians(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    phone = PhoneNumberField(blank=True)
    social = models.CharField(max_length=200, default=0)
    genre = models.CharField(max_length=200, default=0)
    company = models.CharField(max_length=200, default=0)
    engineering = models.BooleanField(default=False)
    artistDevelopment = models.BooleanField(default=False)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

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
    phone = PhoneNumberField(blank=True)
    social = models.CharField(max_length=200, default=0)
    genre = models.CharField(max_length=200, default=0)
    location = models.CharField(max_length=200, default=0)
    musician = models.ManyToManyField(Musicians, related_name='events')

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

        # class Talent_management(models.Model):
        #     # name = models.CharField(max_length=200)
        #     # email = models.EmailField('email')
        #     user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
        #     phone = PhoneNumberField(blank=True)
        #     social = models.CharField(max_length=200, default=0)
        #     genre = models.CharField(max_length=200, default=0)
        #     company = models.CharField(max_length=200, default=0)
        #     artistDevelopment = models.BooleanField(default=False)
        #
        #     @receiver(post_save, sender=User)
        #     def create_user_profile(sender, instance, created, **kwargs):
        #         if created:
        #             Talent_management.objects.create(user=instance)
        #
        #     @receiver(post_save, sender=User)
        #     def save_user_profile(sender, instance, **kwargs):
        #         instance.profile.save()
        #
        #     def __str__(self):
        #         return self.last_name
        #
        #     class Meta:
        #         ordering = ('user',)
        #
        # # Production can have many musicians.
        # class Production(models.Model):
        #     # name = models.CharField(max_length=200)
        #     # email = models.EmailField('email')
        #     user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
        #     phone = PhoneNumberField(blank=True)
        #     social = models.CharField(max_length=200, default=0)
        #     genre = models.CharField(max_length=200, default=0)
        #     company = models.CharField(max_length=200, default=0)
        #     engineering = models.BooleanField(default=False)
        #
        #     @receiver(post_save, sender=User)
        #     def create_user_profile(sender, instance, created, **kwargs):
        #         if created:
        #             Production.objects.create(user=instance)
        #
        #     @receiver(post_save, sender=User)
        #     def save_user_profile(sender, instance, **kwargs):
        #         instance.profile.save()
        #
        #     def __str__(self):
        #         return self.user.last_name
        #
        #     class Meta:
        #         ordering = ('user',)
