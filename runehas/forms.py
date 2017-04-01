from django import forms
from runehas.models import *
from accounts.models import *


class SelectPreferenceForm(forms.Form):
    prefered_block = forms.ModelChoiceField(queryset=Block.objects.all())
    prefered_room = forms.ModelChoiceField(queryset=Room.objects.all())
    prefered_bed = forms.ModelChoiceField(queryset=Bed.objects.all().filter(allocation_status=False))

