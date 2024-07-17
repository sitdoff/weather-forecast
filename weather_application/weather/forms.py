from django import forms


class City(forms.Form):
    city = forms.CharField(label="City", max_length=100, required=True)
