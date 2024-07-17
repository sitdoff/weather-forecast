from django import forms


class CityForm(forms.Form):
    """
    Форма запроса города.
    """

    city = forms.CharField(label="City", max_length=100, required=True)
