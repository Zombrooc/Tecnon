from django import forms

class IP(forms.Form):
	Digite_o_número_de_hosts = forms.DecimalField(required=True)