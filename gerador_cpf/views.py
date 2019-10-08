from django.shortcuts import render
from django.http import HttpResponse
from random import randrange
# Create your views here.
def gerador_cpf(request):
    def calculo_1(cpf):
        i = 0
        modulo = 0
        j = 10
        soma = 0
        cpf2 = str(cpf)[1::3]
        tam = len(cpf)
        for num in range(tam):
            x = int(cpf2[num])*j
            soma = soma + x
            j-=1
        if soma%11 <= 2:
            cpf.append(0)
        else:
            modulo = 11-(soma%11)
            cpf.append(modulo)
        calculo_2(cpf)


    def calculo_2(cpf):
        i = 0
        modulo = 0
        j = 11
        soma = 0
        cpf2 = str(cpf)[1::3]
        tam = len(cpf)
        for num in range(tam):
            x = int(cpf2[num])*j
            soma = soma + x
            j-=1
        if soma%11 <= 2:
            cpf.append(0)
        else:
            modulo = 11-(soma%11)
            cpf.append(modulo)


    if request.method == 'POST':
        cpf = []
        i=1
        while i<10:
            n = randrange(10)
            cpf.append(n)
            i+=1
        calculo_1(cpf)
        traco = 0
        ponto1 = 0
        ponto2 = 0
        resultado = ""
        for el in cpf:
            resultado = resultado + str(el)
            ponto1 += 1
            if traco != 8:
                if ponto1 == 3:
                    resultado = resultado + '.'
                    ponto1 = 0
            traco+=1
            if traco == 9:
                resultado= resultado + '-'

    else:
        resultado = ""
    return render(request, 'gerador.html', {'resultado': resultado})