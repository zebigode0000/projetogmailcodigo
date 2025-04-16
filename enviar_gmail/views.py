import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import VerificationCode
from .forms import CodeVerificationForm

# Email do gestor de PMO
GESTOR_EMAIL = 'gestor.pmo@gmail.com'

def gerar_codigo():
    return f'{random.randint(100000, 999999)}'

def excluir_pedido(request):
    if request.method == 'POST' and 'excluir' in request.POST:
        code = gerar_codigo()
        VerificationCode.objects.create(code=code)

        send_mail(
            'Código de verificação para exclusão',
            f'Seu código de verificação é: {code}',
            'seuemail@gmail.com',  # Email do remetente (configurado no settings)
            [GESTOR_EMAIL],
            fail_silently=False,
        )
        return redirect('verificar_codigo')
    
    return render(request, 'enviar_gmail/excluir.html')


def verificar_codigo(request):
    if request.method == 'POST':
        form = CodeVerificationForm(request.POST)
        if form.is_valid():
            code_input = form.cleaned_data['code']
            try:
                code_obj = VerificationCode.objects.get(code=code_input, verified=False)
                code_obj.verified = True
                code_obj.save()
                return render(request, 'enviar_gmail/verificado.html')
            except VerificationCode.DoesNotExist:
                form.add_error('code', 'Código inválido ou expirado.')
    else:
        form = CodeVerificationForm()

    return render(request, 'enviar_gmail/verificar.html', {'form': form})
