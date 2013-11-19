from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def index(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			email = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=email, password=password)
			if user is not None and user.is_active:
				login(request, user)
				return redirect('/privada')
			else:
				return HttpResponse('Algo salio mal')
		else:
			return HttpResponse('El formulario no es valido')
	else:
		form = AuthenticationForm()
	ctx = {'form':form}
	return render(request, 'index.html', ctx)

def privada(request):
	if request.user.is_authenticated():
		return HttpResponse('Bienvenido!<br>DNI: %s<br>Email:%s' % (request.user.dni, request.user.email))
	else:
		return redirect('/')