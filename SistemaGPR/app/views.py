
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')


def registro(request):
    
    if request.method == 'GET':
          return render(request, 'registro.html', {
        'form': UserCreationForm 
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #registro de usuarion
            try:
                user = User.objects.create_user(username=request.POST['username'], 
                                     password=request.POST['password1'])
                user.save()
                return HttpResponse('Usuario creado correctamente')
            except:
                return HttpResponse('El usuario ya existe')
        return HttpResponse('Las contraseñas no coinciden' )