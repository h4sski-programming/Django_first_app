from django import forms


class AddVehicleForm(forms.Form):
    CHOICES = [
        ('bike', 'bike'),
        ('scooter', 'scooter'),
        ]
    type = forms.ChoiceField(choices=CHOICES)
    name = forms.CharField(max_length=100, label='Name')


class VehicleChoiceForm(forms.Form):
    CHOICES = [
        ('bike', 'bike'),
        ('scooter', 'scooter'),
        ]
    type = forms.ChoiceField(label='', choices=CHOICES)
