from django import forms

class GraphSaveForm(forms.Form):
    user = forms.CharField(max_length=(32), widget=forms.HiddenInput())
    name = forms.CharField(label="Graph Name", max_length=(32), required=True)
    state = forms.JSONField(widget=forms.HiddenInput())