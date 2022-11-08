from django import forms


class AddVechicleForm(forms.Form):
    choices = [
        ('bike', 'bike'),
        ('scooter', 'scooter'),
        ]
    type = forms.ChoiceField(choices=choices)
    name = forms.CharField(max_length=100, label='Name')
