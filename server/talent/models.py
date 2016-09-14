from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Talent Manager can have many musicians.
class Talent_management(User):
    # name = models.CharField(max_length=200)
    # email = models.EmailField('email')
    phone = PhoneNumberField()
    social = models.CharField(max_length=200, default=0)
    genre = models.CharField(max_length=200, default=0)
    company = models.CharField(max_length=200, default=0)
    artistDevelopment = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

# Production can have many musicians.
class Production(User):
    # name = models.CharField(max_length=200)
    # email = models.EmailField('email')
    phone = PhoneNumberField()
    social = models.CharField(max_length=200, default=0)
    genre = models.CharField(max_length=200, default=0)
    company = models.CharField(max_length=200, default=0)
    engineering = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

# musicians can only have one manager and one producer
class Musicians(User):
    # name = models.CharField(max_length=200)
    # email = models.EmailField('email')
    phone = PhoneNumberField()
    social = models.CharField(max_length=200, default=0)
    genre = models.CharField(max_length=200, default=0)
    songs = models.CharField(max_length=200, default=0)
    manager = models.ForeignKey(Talent_management, related_name='musicians', on_delete=models.SET_NULL, null=True)
    production = models.ForeignKey(Production, related_name='musicians', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

# Events can have many musicians and musicians can have many events.
class Events(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField('email')
    phone = PhoneNumberField()
    social = models.CharField(max_length=200, default=0)
    genre = models.CharField(max_length=200, default=0)
    location = models.CharField(max_length=200, default=0)
    musician = models.ManyToManyField(Musicians, related_name='events')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

# Musicians can have many songs.
class Songs(models.Model):
    owner = models.ForeignKey(Musicians, related_name='songs')
    name = models.CharField(max_length=200)
    email = models.EmailField('email')
    phone = PhoneNumberField()
    social = models.CharField(max_length=200, default=0)
    genre = models.CharField(max_length=200, default=0)
    location = models.CharField(max_length=200, default=0)
    musician = models.ManyToManyField(Musicians, related_name='events')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
