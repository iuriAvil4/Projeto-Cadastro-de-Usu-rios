from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #SALVAR OS DADOS DA TELA PARA O BANCO A DADOS
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #EXIBIR TODOS OS USUARIOS EM OUTRA PAGINA
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #RETORNA OS DADOS PRA NOVA PAGINA
    return render(request,'usuarios/usuarios.html', usuarios)

def usuarios_sem_entrada(request):
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # RETORNA OS DADOS PRA NOVA PAGINA
    return render(request, 'usuarios/usuarios.html', usuarios)