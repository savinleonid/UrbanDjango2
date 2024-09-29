from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game


# Create your views here.


def main_page(request):
    return render(request, 'fourth_task/main_page.html')


def shop_page(request):
    return render(request, 'fourth_task/shop_page.html', {'games': Game.objects.all()})


def cart_page(request):
    return render(request, 'fourth_task/cart_page.html')


def sign_up_by_django(request):
    info = {}
    users = Buyer.objects.all()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверка условий
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in [user.name for user in users]:
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, balance=300, age=age)
                return render(request, 'fourth_task/registration_page.html',
                              {'message': f'Приветствуем, {username}!', 'form': UserRegister()})
        else:
            info['form'] = form
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fourth_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    users = Buyer.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        # Проверка условий
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in [user.name for user in users]:
            info['error'] = 'Пользователь уже существует'
        else:
            Buyer.objects.create(name=username, balance=300, age=age)
            return render(request, 'fourth_task/registration_page.html',
                          {'message': f'Приветствуем, {username}!'})
    return render(request, 'fourth_task/registration_page.html', info)
