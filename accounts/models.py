from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile


# Create your models here.
class MyProfile(UserenaBaseProfile):
    Mr = 'mr'
    Miss = 'mi'
    Mrs = 'ms'
    TITLE_CHOICES = (
        (Mr, _('Mr')),
        (Miss, _('Miss')),
        (Mrs, _('Mrs')),
    )

    MALE = 'ML'
    FEMALE = 'FL'
    GENDER_CHOICES = (
        (MALE, _('MALE')),
        (FEMALE, _('FEMALE')),
    )

    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('User'),
                                related_name='my_profile')
    title = models.CharField(max_length=2, verbose_name=_('Title(Mr/Miss/Mrs)'), choices=TITLE_CHOICES, blank=True)
    mat_no = models.CharField(max_length=250, verbose_name=_('Student\'s Matric No'), help_text='Student\'s matric number e.g. RUN/CMP/13/5219', blank=True, null=True)
    email = models.EmailField(max_length=254, verbose_name=_('Email'), null=True)
    mobileNo = models.PositiveIntegerField(verbose_name=_('Phone No'), null=True)
    homeAddress = models.TextField(max_length=250, verbose_name=_('Permanent Home Address'), blank=True)
    dob = models.DateField(verbose_name=_('Date of Birth'), blank=True, null=True)
    lga = models.CharField(max_length=250, verbose_name=_('Local Government Area'), blank=True, null=True)
    state_of_origin = models.CharField(max_length=250, verbose_name=_('State of Origin'), blank=True, null=True)
    faculty = models.CharField(max_length=250, verbose_name=_('Faculty'), blank=True, null=True)
    department = models.CharField(max_length=250, verbose_name=_('Department'), blank=True, null=True)
    level = models.IntegerField(verbose_name=_('Level(Year of Study)'), blank=True, null=True)
    gender = models.CharField(max_length=2, verbose_name=_('Gender'), choices=GENDER_CHOICES, null=True)

    def __str__(self):
        return "{fullname}".format(fullname=self.user.last_name + ' ' + self.user.first_name)
