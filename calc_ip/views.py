from django.shortcuts import render
from .forms import IP

def calc_ip(request):
	form = IP()
	mascara_sub_rede = 0
	numero_de_sub_redes = 0
	numero_de_ip_p_rede = 0
	numero_ip_valido = 0
	if request.method == 'POST':
		def calculo(p):
		    i = 0
		    while True:
		        if ((2**i)-2) >= p:
		            subrede = 256-2**i
		            return subrede
		            break
		        else:
		            i+=1


		def numsubrede(p):
		    bin = dec_to_bin(p)
		    bit1 = 0
		    for n in bin:
		        if n == '1':
		            bit1 += 1
		    numero_de_subs = 2**bit1
		    return numero_de_subs
		            
		            
		def numip(p):
		    bin = dec_to_bin(p)
		    bit0 = 0
		    for n in bin:
		        if n == '0':
		            bit0 += 1
		    num_ip = 2**bit0
		    return num_ip
		     
		               
		def dec_to_bin(p):
		    p = calculo(p)
		    binario = ""
		    while p >= 1:
		        binario = (binario + str(int(p % 2)))
		        p = p//2
		    binario = binario[::-1]
		    return binario


		form = IP(request.POST)
		if form.is_valid():
			p = form.cleaned_data['Digite_o_número_de_hosts']
			if p >126 and p<=254:
				mascara_sub_rede = 0
				numero_de_sub_redes = 1
				numero_de_ip_p_rede = 256
				numero_ip_valido = 254
			else:
				mascara_sub_rede = calculo(p)
				numero_de_sub_redes = numsubrede(p)
				numero_de_ip_p_rede = numip(p)
				numero_ip_valido = numero_de_ip_p_rede-2
	context = {
		'form': form,
		'mascara_sub_rede': mascara_sub_rede,
		'numero_de_sub_redes': numero_de_sub_redes,
		'numero_de_ip_p_rede': numero_de_ip_p_rede,
		'numero_ip_valido': numero_ip_valido,
	}
	return render(request, 'calc_ip.html', context)