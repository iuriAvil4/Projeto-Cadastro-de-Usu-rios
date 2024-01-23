from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def home(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = UsuarioForm()

    return render(request, 'usuarios/home.html', {'form': form})

def usuarios(request):
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)

def usuarios_sem_entrada(request):
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)
