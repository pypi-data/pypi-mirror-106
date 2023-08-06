from django.db import models
from django.urls import reverse
# from django_rq import get_queue
from rq import cancel_job

from dcim.models import Device, DeviceRole, Platform, Site
from ipam.fields import IPAddressField, IPNetworkField
from np_autodisc.np_transitions.models import ChangeLoggedModel

from np_autodisc.constants import *

# from np_autodisc.worker import discovery_job


class DiscoveryResult(models.Model):
    discovery_request = models.ForeignKey(
        to = DiscoveryRequest,
        related_name = 'results',
        on_delete = models.CASCADE
    )
    device = models.ForeignKey(
        to = Device,
        related_name = '+',
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
    )
    address = IPAddressField()
    status = models.PositiveSmallIntegerField(
        choices = RESULT_STATUS_CHOICES,
        default = RESULT_STATUS_TRYING
    )

    def __str__(self):
        return f'{self.address} {self.status}'

    def get_absolute_url(self):
        return reverse('np_autodisc:discoveryresult', args = [self.pk])

    def get_status_class(self):
        return RESULT_STATUS_CLASSES[self.status]
