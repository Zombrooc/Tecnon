from django import forms

OPCAO = (('bin', 'Binário'), ('dec', 'Decimal'), ('hex', 'Hexadecimal'),
	('oct', 'Octal'))

class ConversorForm(forms.Form):
	selecione_uma_opcão = forms.ChoiceField(widget=forms.Select, choices=OPCAO, required=True)
	selecione_a_segunda_opcão = forms.ChoiceField(widget=forms.Select, choices=OPCAO, required=True)
	Número_CPF = forms.CharField(required=True)