from django.db import models

DEN_CHOICES = (
        ('Bobcat', 'Bobcat'),
        ('Tiger', 'Tiger'),
        ('Wolf', 'Wolf'),
        ('Bear', 'Bear'),
        ('Weblos I', 'Weblos I'),
        ('Weblos II', 'Weblos II')
        )

# Create your models here.

class Scout(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    den_of_scout =  models.CharField(max_length=256, choices=DEN_CHOICES, default='Bobcat')
    pack_number = models.IntegerField()
    def __unicode__(self):
        return self.last_name


class Den(models.Model):

    leader = models.CharField(max_length=30)
    pack_number = models.IntegerField()
    den_type = models.CharField(max_length=256, choices=DEN_CHOICES, default='Bobcat') 
    meeting_time = models.DateTimeField('Date and time of the meeting')
    meeting_location = models.CharField(max_length=60)
    activities = models.CharField(max_length=256)
    def __unicode__(self):
        return self.den_type

class Pack(models.Model):

    pack_number = models.IntegerField() 
    location = models.CharField(max_length=256)
    leaders = models.CharField(max_length=256)
    def __unicode__(self):
        return self.pack_number

