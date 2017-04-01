from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
from guardian.shortcuts import get_perms_for_model, get_perms
from django.utils.translation import ugettext as _
from django.conf import settings


# Create your models here.
class Block(models.Model):
    KINGS = 'KG'
    QUEENS = 'QN'
    HOSTEL_CHOICES = (
        (KINGS, _('KINGS')),
        (QUEENS, _('QUEENS')),
    )
    blockid = models.AutoField(verbose_name=_('Block ID'), primary_key=True)
    name = models.CharField(max_length=250, verbose_name=_('Hostel Block Name'), blank=True)
    hall = models.CharField(max_length=2, verbose_name=_('hostel'), choices=HOSTEL_CHOICES)

    def __str__(self):
        return "{id} - {name}".format(id=self.blockid, name=self.name)


class Room(models.Model):
    rid = models.AutoField(verbose_name=_('Room ID'), primary_key=True)
    name = models.CharField(max_length=15, verbose_name=_('Room Name'), blank=True)
    block = models.ForeignKey(Block, related_name='block', verbose_name=_('Room\'s Block'), on_delete=models.CASCADE)

    def __str__(self):
        return "{id} - {hostel} - {room}".format(id=self.rid, hostel=self.block.name, room=self.name)


class Bed(models.Model):
    BEDA = 'BA'
    BEDB = 'BB'

    BED_CHOICES = (
        (BEDA, _('Bed A')),
        (BEDB, _('Bed B')),
    )

    bid = models.AutoField(verbose_name=_('BED UNIQUE ID'), primary_key=True)
    bname = models.CharField(max_length=2, verbose_name=_('Bed Name'), choices=BED_CHOICES, null=True)
    room = models.ForeignKey(Room, related_name='room', verbose_name=_('Room Name'), on_delete=models.CASCADE)
    allocation_status = models.BooleanField(_('Allocated Status'), help_text=_("not allocated by default but when value is true i.e.(checked), bed is allocated"), default=False)

    def __str__(self):
        return "{id} - {room} - {bed}".format(id=self.bid, room=self.room.name, bed=self.bname)


class Booking(models.Model):
    brefid = models.AutoField(verbose_name=_('BED UNIQUE ID'), primary_key=True)
    student = models.OneToOneField(User, verbose_name=_('Student'), related_name='room_of', on_delete=models.CASCADE)
    block = models.CharField(max_length=250, verbose_name=_('Block of Room Allotted'), blank=True)
    room = models.CharField(max_length=250, verbose_name=_('Room Allotted'), blank=True)
    bed = models.CharField(max_length=15, verbose_name=_('Bed Allotted'), blank=True)
    booking_status = models.BooleanField(verbose_name=_('Booking Status'), default=False)
    booked_on = models.DateTimeField(verbose_name=_('Date of Booking'), db_index=True, auto_now_add=True)

    def __str__(self):
        return "{bookingref} - {student} - {bed}".format(bookingref=self.brefid, student=self.student, bed=self.bed)
