from django import forms
from MyAPP.models import PLAYER

class PLAYERFORM(forms.ModelForm):
    class Meta:
        model = PLAYER
        fields = '__all__'
        