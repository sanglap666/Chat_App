from django import forms
class ThreadForm(forms.Form):

    message = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control"}
                )
            )