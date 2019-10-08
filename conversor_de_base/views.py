from django.shortcuts import render
from .forms import ConversorForm


def Dec_to_Other(dec):
    decimal = dec
    hexadecimal = hex(dec)[2:].upper()
    octal = oct(dec)[2:]
    binario = bin(dec)[2:]
    return decimal, hexadecimal, octal, binario


# Create your views here.
def Conversor_de_Base(request):
    form = ConversorForm()
    resultado = ""
    if request.method == 'POST':
        form = ConversorForm(request.POST)
        if form.is_valid(): 
            numero = form.cleaned_data['Número_a_ser_convertido']
            if form.cleaned_data['selecione_uma_opcão'] == 'dec':
                try:
                    numero = int(numero)
                    decimal = Dec_to_Other(numero)
            
                    if form.cleaned_data['selecione_a_segunda_opcão'] == 'dec': #--------> Decimal para Decimal
                        resultado = decimal[0]
            
                    elif form.cleaned_data['selecione_a_segunda_opcão'] == 'hex': #--------> Decimal para Hexadecimal
                        resultado = decimal[1]
            
                    elif form.cleaned_data['selecione_a_segunda_opcão'] == 'oct': #-------> Decimal para Octal
                        resultado = decimal[2]
            
                    elif form.cleaned_data['selecione_a_segunda_opcão'] == 'bin': #-----> Decimal para Binário
                        resultado = decimal[3]
                except ValueError:
                    resultado = 'Por favor digite apenas número'
    
    #Converter Hexadecimal para as demais bases
            elif form.cleaned_data['selecione_uma_opcão'] == 'hex':
                try:
                    p = numero
                    p = p[::-1]
                    tam = len(p)
                    decimal = 0
                    for algo in range(tam):
                        p = str(p)
                        p = p.upper()
                        if p[algo] == 'A':
                            decimal = decimal + (10*(16**algo))
                        elif p[algo] == 'B':
                            decimal = decimal + (11*(16**algo))
                        elif p[algo] == 'C':
                            decimal = decimal + (12*(16**algo))
                        elif p[algo] == 'D':
                            decimal = decimal + (13*(16**algo))
                        elif p[algo] == 'E':
                            decimal = decimal + (14*(16**algo))
                        elif p[algo] == 'F':
                            decimal = decimal + (15*(16**algo))
                        else:
                            decimal = decimal + int(p[algo]) * (16 ** algo)
                    decimal = Dec_to_Other(decimal)
                    if form.cleaned_data['selecione_a_segunda_opcão'] == 'dec': #--------> Decimal para Decimal
                        resultado = decimal[0]
            
                    elif form.cleaned_data['selecione_a_segunda_opcão'] == 'hex': #--------> Decimal para Hexadecimal
                        resultado = decimal[1]
            
                    elif form.cleaned_data['selecione_a_segunda_opcão'] == 'oct': #-------> Decimal para Octal
                        resultado = decimal[2]
            
                    elif form.cleaned_data['selecione_a_segunda_opcão'] == 'bin': #-----> Decimal para Binário
                        resultado = decimal[3]
                except:
                    resultado = 'Por favor digite apenas digitos Hexadecimais \'0-9 a-F\''
    

    #Converter Octal para as demais bases
            elif form.cleaned_data['selecione_uma_opcão'] == 'oct':
                octal = True
                for num in numero:
                    if int(num) >= 8:
                        octal = False
                if octal == True:
                    p = numero
                    tam = len(p)
                    p = p[::-1]
                    decimal = 0
                    for algo in range(tam):
                        decimal = decimal + int(p[algo]) * (8 ** algo)
                    decimal = Dec_to_Other(decimal)
                    if form.cleaned_data['selecione_a_segunda_opcão'] == 'dec': #--------> Decimal para Decimal
                        resultado = decimal[0]
            
                    elif form.cleaned_data['selecione_a_segunda_opcão'] == 'hex': #--------> Decimal para Hexadecimal
                        resultado = decimal[1]
            
                    elif form.cleaned_data['selecione_a_segunda_opcão'] == 'oct': #-------> Decimal para Octal
                        resultado = decimal[2]
            
                    elif form.cleaned_data['selecione_a_segunda_opcão'] == 'bin': #-----> Decimal para Binário
                        resultado = decimal[3]
                else:
                    resultado = 'Digite apenas caracteres Octais \'0-7\''
    
    
    #Converter Binário para as demais bases
            elif form.cleaned_data['selecione_uma_opcão'] == 'bin':
                numero = numero[::-1]
                tam = len(numero)
                decimal = 0
                binario = True
                for num in range(tam):
                    if numero[num] == '1':
                        decimal = decimal + (2**num)
                    elif numero[num] == '0':
                        ...
                    else:
                        binario = False
                        resultado = 'Não digite números diferentes de 0 e 1'
                        break
                if binario == True:
                    decimal = Dec_to_Other(decimal)
                    if form.cleaned_data['selecione_a_segunda_opcão'] == 'dec': #--------> Decimal para Decimal
                        resultado = decimal[0]
            
                    elif form.cleaned_data['selecione_a_segunda_opcão'] == 'hex': #--------> Decimal para Hexadecimal
                        resultado = decimal[1]
            
                    elif form.cleaned_data['selecione_a_segunda_opcão'] == 'oct': #-------> Decimal para Octal
                        resultado = decimal[2]
            
                    elif form.cleaned_data['selecione_a_segunda_opcão'] == 'bin': #-----> Decimal para Binário
                        resultado = decimal[3]
                
    context = {
        'form': form,
        'resultado': resultado
    }
    return render(request, 'conversor-de-bases.html', context)
