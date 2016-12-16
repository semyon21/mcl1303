from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
import smtplib
from main.models import Student
from django.contrib.auth.decorators import login_required
from email.mime.text import MIMEText
from email.header import Header


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))

def register(request):
    """Регистрирует нового пользователя"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username = new_user.username, password = request.POST['password1'])
            
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('main:index'))
    context = {'form': form}
    return render(request, 'teacher/register.html', context)

def send_message(request):
    students = Student.objects.all()
    if request.method != 'POST':
        pass


    else:
        to_smn = request.POST['mails[]']
        sub = request.POST['subject']
        cont = request.POST['text']
        print(to_smn)
        if cont and to_smn and sub:
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.starttls()
            mail.login('bmxtrialler@gmail.com', 'myman113S')
            msg = MIMEText(cont, 'plain', 'utf-8')
            msg['Subject'] = Header(sub, 'utf-8')
            mail.sendmail('bmxtrialler@gmail.com', ['bmxtrialler@gmail.com', 'semyon21@inbox.ru'], msg.as_string)
            mail.quit()
            return HttpResponseRedirect(reverse('main:index'))
    return render(request, 'teacher/send_message.html', {'students': students})
