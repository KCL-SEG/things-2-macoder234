"""Forms of the project."""
from django import forms

# Create your forms here.
class ThingForm(forms.Form):
    name = forms.CharField(max_length=35)
    description = forms.CharField(max_length = 120, widget = forms.Textarea()) #TextArea
    quantity = forms.IntegerField(min_value = 0, max_value = 50, widget = forms.NumberInput()) #NumberInput