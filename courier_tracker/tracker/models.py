from django.db import models
from accounts.models import User
import uuid


class Status(models.Model):
    description = models.CharField(max_length=50, blank=False, null=False)


    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.description


class Package(models.Model):
    tracking_id = models.UUIDField(default=uuid.uuid4)
    weight = models.DecimalField(max_digits=15, decimal_places=2, blank=False, help_text='Kg\'s')
    length = models.DecimalField(max_digits=15, decimal_places=2, blank=False, help_text='Inches')
    width = models.DecimalField(max_digits=15, decimal_places=2, blank=False, help_text='Centimetres')
    height = models.DecimalField(max_digits=15, decimal_places=2, blank=False, help_text='Metres')    
    sender = models.ManyToManyField(User, blank=False, null=False)
    sender_address = models.CharField(max_length=255, blank=False, null=False)
    recepient_name = models.CharField(max_length=100, blank=False, null=False)
    recepient_address = models.CharField(max_length=255, default='', blank=False, null=False)
    estimated_time_arrival = models.IntegerField(max_length=100, default=1, blank=True, help_text='Days')
    description = models.TextField(max_length=1000, blank=True, null=True)
    status_id = models.ManyToManyField(Status, null=False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at', '-updated_at']
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'


    def __str__(self):
        first_sender = self.sender.first()

        if(first_sender):
            return f'{first_sender.get_full_name} package -> {self.recepient_name}'
        else:
            return f'Package -> {self.recepient_name}'


class TrackingEvent(models.Model):
    package_id = models.OneToOneField(Package, null=False, blank=True, on_delete=models.CASCADE)
    status_id = models.ManyToManyField(Status, null=False, blank=True)
    timestamp =  models.DateTimeField(auto_now=True)
    note = models.TextField(max_length=1000, null=True, blank=True)


    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Tracking Event'
        verbose_name_plural = 'Tracking Events'

    def __str__(self):
        sender = self.package_id.sender.first()
        status = self.status_id.first()

        if(sender and status):
            return f'{sender.get_full_name} package -> status({status.description})'
        else:
            return f'Unknown package -> status(Unknown)'
    


