import random
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Projeto
from .forms import ProjetoForm, CodigoConfirmacaoForm

# Código temporário guardado na sessão
def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'enviar_gmail/criar_projeto.html', {'form': form})

def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'enviar_gmail/listar_projetos.html', {'projetos': projetos})

def solicitar_exclusao(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    codigo = ''.join(random.choices('0123456789', k=6))
    request.session['codigo_exclusao'] = codigo
    request.session['projeto_exclusao_id'] = projeto.id

    send_mail(
        'Código de Exclusão de Projeto',
        f'Seu código de exclusão é: {codigo}',
        'teixeiraqugusto@gmail.com',  # <-- mesmo email do settings
        ['teixeiraqugusto@gmail.com'],
        fail_silently=False,
    )

    return redirect('confirmar_exclusao')

def confirmar_exclusao(request):
    if request.method == 'POST':
        form = CodigoConfirmacaoForm(request.POST)
        if form.is_valid():
            codigo_informado = form.cleaned_data['codigo']
            codigo_real = request.session.get('codigo_exclusao')
            projeto_id = request.session.get('projeto_exclusao_id')

            if codigo_informado == codigo_real:
                projeto = get_object_or_404(Projeto, id=projeto_id)
                projeto.delete()
                return redirect('listar_projetos')
            else:
                form.add_error('codigo', 'Código incorreto. Tente novamente.')
    else:
        form = CodigoConfirmacaoForm()
    return render(request, 'enviar_gmail/confirmar_exclusao.html', {'form': form})

