from django.shortcuts import render, redirect
from .models import main, nam, patronymic, street
from .models import surname
from .forms import namForm, surnameForm, patronymicForm, streetForm, MainForm, MainFilterForm
from django.views.generic import UpdateView
from django.db import connection, IntegrityError
from django.http import HttpResponse



def name(request):
    error = ''
    name_data = Nam.objects.raw("SELECT * FROM main_nam")
    if request.method == "POST":
        form = namForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            existing_names = Nam.objects.filter(name=new_name)
            if existing_names.exists():
                error = 'Поле name должно быть уникальным'
            else:
                form.save()
                return redirect('main_table')
        else:
            error = 'Неккоректные значения'
    form = namForm()
    data = {
        'form': form,
        'error': error,
        'name_data': name_data
    }

    return render(request, 'main/name.html', data)

def delete_item(request, id_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM main_nam WHERE id_name = {id_name}")
        return redirect('name')
    except IntegrityError:
        return HttpResponse(
            "This object cannot be deleted because it is still referenced by other objects. You may need to update or remove those references first.")

def update_item(request, id_name):
    error = ''
    try:
        item = nam.objects.get(pk=id_name)
        if request.method == "POST":
            form = namForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('name')
            else:
                error = 'Некорректные значения'
        else:
            form = namForm(instance=item)
    except nam.DoesNotExist:
        error = 'Запись не найдена'
        form = namForm()

    name_data = nam.objects.raw("SELECT * FROM main_nam")
    data = {
        'form': form,
        'error': error,
        'name_data': name_data
    }

    return render(request, 'main/name.html', data)

def surnam(request):
    error = ''
    surname_data = surname.objects.raw("SELECT * FROM main_surname")
    if request.method == "POST":
        form = famForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_table')
        else:
            error = 'Неккоректные значения'
    form = famForm()
    data = {
        'form': form,
        'error': error,
        'surname_data': surname_data
    }

    return render(request, 'main/surname.html', data)
def delete_surname(request, id_fam):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM main_fam WHERE id_fam = {id_fam}")
        return redirect('surname')
    except IntegrityError:
        return HttpResponse(
            "This object cannot be deleted because it is still referenced by other objects. You may need to update or remove those references first.")


def update_surname(request, id_fam):
    error = ''
    try:
        item = surname.objects.get(pk=id_fam)
        if request.method == "POST":
            form = surnameForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('surname')
            else:
                error = 'Некорректные значения'
        else:
            form = surnameForm(instance=item)
    except surname.DoesNotExist:
        error = 'Запись не найдена'
        form = surnameForm()

    surname_data = surname.objects.raw("SELECT * FROM main_fam")
    data = {
        'form': form,
        'error': error,
        'surname_data': surname_data
    }

    return render(request, 'main/surname.html', data)

def patronym(request):
    error = ''
    patronymic_data = patronymic.objects.raw("SELECT * FROM main_otchestvo")
    if request.method == "POST":
        form = patronymicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_table')
        else:
            error = 'Неккоректные значения'
    form = patronymicForm()
    data = {
        'form': form,
        'error': error,
        'patronymic_data': patronymic_data
    }

    return render(request, 'main/otch.html', data)
def delete_patronymic(request, id_otch):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM main_otchestvo WHERE id_otch = {id_otch}")
        return redirect('patronymic')
    except IntegrityError:
        return HttpResponse(
            "This object cannot be deleted because it is still referenced by other objects. You may need to update or remove those references first.")


def update_patronymic(request, id_otch):
    error = ''
    try:
        item = patronymic.objects.get(pk=id_otch)
        if request.method == "POST":
            form = patronymicForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('patronymic')
            else:
                error = 'Некорректные значения'
        else:
            form = patronymicForm(instance=item)
    except surname.DoesNotExist:
        error = 'Запись не найдена'
        form = patronymicForm()

    patronymic_data = patronymic.objects.raw("SELECT * FROM main_otchestvo")
    data = {
        'form': form,
        'error': error,
        'patronymic_data': patronymic_data
    }

    return render(request, 'main/otch.html', data)

def streets(request):
    error = ''
    street_data = street.objects.raw("SELECT * FROM main_street")
    if request.method == "POST":
        form = streetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_table')
        else:
            error = 'Неккоректные значения'
    form = streetForm()
    data = {
        'form': form,
        'error': error,
        'street_data': street_data
    }

    return render(request, 'main/street.html', data)
def delete_street(request, id_street):
    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM main_street WHERE id_street = {id_street}")
    return redirect('street')

def update_street(request, id_street):
    error = ''
    try:
        item = street.objects.get(pk=id_street)
        if request.method == "POST":
            form = streetForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('street')
            else:
                error = 'Некорректные значения'
        else:
            form = streetForm(instance=item)
    except surname.DoesNotExist:
        error = 'Запись не найдена'
        form = streetForm()

    street_data = street.objects.raw("SELECT * FROM main_street")
    data = {
        'form': form,
        'error': error,
        'street_data': street_data
    }

    return render(request, 'main/street.html', data)


def add_main(request):
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_table')  # Перенаправление на страницу успешного сохранения
    else:
        form = MainForm()

    return render(request, 'main/main_add.html', {'main_form': form})

def delete_main(request, id):
    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM main_main WHERE id = {id}")
    return redirect('main_table')

def update_main(request, id):
    error = ''
    try:
        item = main.objects.get(pk=id)
        if request.method == "POST":
            form = MainForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('main_table')
            else:
                error = 'Некорректные значения'
        else:
            form = MainForm(instance=item)
    except main.DoesNotExist:
        error = 'Запись не найдена'
        form = MainForm()

    main_data = main.objects.raw("SELECT * FROM main_main")
    data = {
        'form': form,
        'error': error,
        'main_data': main_data
    }

    return render(request, 'main/main_update.html', data)


def main_table(request):
    form = MainFilterForm(request.GET)
    queryset = main.objects.all()

    if form.is_valid():
        name = form.cleaned_data.get('name')
        fam = form.cleaned_data.get('fam')
        otch = form.cleaned_data.get('otch')
        street = form.cleaned_data.get('street')
        bldn = form.cleaned_data.get('bldn')
        bldn_k = form.cleaned_data.get('bldn_k')
        appr = form.cleaned_data.get('appr')
        tel = form.cleaned_data.get('tel')

        if name:
            queryset = queryset.filter(name=name)
        if fam:
            queryset = queryset.filter(fam=fam)
        if otch:
            queryset = queryset.filter(otch=otch)
        if street:
            queryset = queryset.filter(street=street)
        if bldn:
            #номер дома
            queryset = queryset.filter(bldn=bldn)
        if bldn_k:
            #корпус
            queryset = queryset.filter(bldn_k=bldn_k)
        if appr:
            #квартира
            queryset = queryset.filter(appr=appr)
        if tel:
            queryset = queryset.filter(tel=tel)

    return render(request, 'main/main_table.html', {'queryset': queryset, 'form': form})