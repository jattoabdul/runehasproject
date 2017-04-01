from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from runehas.models import *
from django.db import models


# Create your admin model classes here
class BlockAdmin(admin.ModelAdmin):
    search_fields = ['name', 'hall']
    list_display = ['blockid', 'name', 'hall']
    ordering = ['blockid', 'name', 'hall']


class RoomAdmin(admin.ModelAdmin):
    search_fields = ['name', 'block']
    list_display = ['rid', 'name', 'block']
    ordering = ['rid', 'name', 'block']


class BedAdmin(admin.ModelAdmin):
    search_fields = ['bname', 'room']
    list_display = ['bid', 'bname', 'room', 'allocation_status']
    ordering = ['bid', 'bname', 'room']


class BookingAdmin(admin.ModelAdmin):
    search_fields = ['brefid', 'student', 'block', 'room', 'bed']
    list_display = ['brefid', 'student', 'block', 'room', 'bed', 'booking_status', 'booked_on']
    ordering = ['booked_on']


# Register your models here.
admin.site.register(Block, BlockAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Bed, BedAdmin)
admin.site.register(Booking, BookingAdmin)
# admin.site.register(Student, StudentAdmin)


# class StudentAdmin(admin.ModelAdmin):
#     search_fields = ['sname', 'fname', 'faculty', 'department', 'level']
#     list_display = ['sname', 'fname', 'faculty', 'department', 'level', 'gender']
#     ordering = ['sname', '-level', 'faculty', 'department']
