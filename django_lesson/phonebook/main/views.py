from django.shortcuts import render, redirect
from .models import Main, Nam, Street, Fam, Otchestvo
from .forms import namForm, famForm, otchForm, streetForm, MainForm, MainFilterForm
from django.db import connection, IntegrityError


def name(request):
    message = ''
    name_data = Nam.objects.raw("SELECT * FROM main_nam")
    if request.method == "POST":
        form = namForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            existing_names = Nam.objects.filter(name=new_name)
            if existing_names.exists():
                message = 'Поле name должно быть уникальным'
            else:
                form.save()
                return redirect('name')
        else:
            message = 'Неккоректные значения'
    form = namForm()
    data = {
        'form': form,
        'message': message,
        'name_data': name_data
    }

    return render(request, 'main/name.html', data)

def delete_name(request, id_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM main_nam WHERE id_name = {id_name}")
        return redirect('name')
    except IntegrityError:
        return render(request, 'main/name.html',{'message': "Этот объект нельзя удалить, потому что на него все еще есть ссылки в других объектах. Вам может потребоваться обновить или удалить эти ссылки сначала."})



def update_name(request, id_name):
    message = ''
    try:
        item = Nam.objects.get(pk=id_name)
        if request.method == "POST":
            form = namForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('name')
            else:
                message = 'Некорректные значения'
        else:
            form = namForm(instance=item)
    except Nam.DoesNotExist:
        message = 'Запись не найдена'
        form = namForm()

    name_data = Nam.objects.raw("SELECT * FROM main_nam")
    data = {
        'form': form,
        'message': message,
        'name_data': name_data
    }
    return render(request, 'main/name.html', data)

def fam(request):
    message = ''
    fam_data = Fam.objects.raw("SELECT * FROM main_fam")
    if request.method == "POST":
        form = famForm(request.POST)
        if form.is_valid():
            fam = form.save(commit=False)
            fam.save()
            if Fam.objects.filter(fam=fam.fam).exists():
                message = 'Запись с такой фамилией уже существует'
            else:
                fam.save()
                return redirect('fam')
        else:
            message = 'Неккоректные значения'
    form = famForm()
    data = {
        'form': form,
        'message': message,
        'fam_data': fam_data
    }

    return render(request, 'main/surname.html', data)

def delete_fam(request, id_fam):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM main_fam WHERE id_fam = {id_fam}")
        return redirect('fam')
    except IntegrityError:
        return render(request, 'main/surname.html', {'message': "Этот объект нельзя удалить, потому что на него все еще есть ссылки в других объектах. Вам может потребоваться обновить или удалить эти ссылки сначала."})

def update_fam(request, id_fam):
    message = ''
    try:
        item = Fam.objects.get(pk=id_fam)
        if request.method == "POST":
            form = famForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('fam')
            else:
                message = 'Некорректные значения'
        else:
            form = famForm(instance=item)
    except Fam.DoesNotExist:
        message = 'Запись не найдена'
        form = famForm()

    fam_data = Fam.objects.raw("SELECT * FROM main_fam")
    data = {
        'form': form,
        'message': message,
        'fam_data': fam_data
    }

    return render(request, 'main/surname.html', data)


def otch(request):
    message = ''
    otch_data = Otchestvo.objects.raw("SELECT * FROM main_otchestvo")
    if request.method == "POST":
        form = otchForm(request.POST)
        if form.is_valid():
            otch_value = form.cleaned_data['otch']
            if Otchestvo.objects.filter(otch=otch_value).exists():
                message = 'Значение поля otch уже существует'
            else:
                form.save()
                return redirect('otch')
        else:
            message = 'Некорректные значения'
    else:
        form = otchForm()

    data = {
        'form': form,
        'message': message,
        'otch_data': otch_data
    }

    return render(request, 'main/otch.html', data)

def delete_otch(request, id_otch):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM main_otchestvo WHERE id_otch = {id_otch}")
        return redirect('otch')
    except IntegrityError:
        return render(request, 'main/otch.html', {'message': "Этот объект нельзя удалить, потому что на него все еще есть ссылки в других объектах. Вам может потребоваться обновить или удалить эти ссылки сначала."})


def update_otch(request, id_otch):
    message = ''
    try:
        item = Otchestvo.objects.get(pk=id_otch)
        if request.method == "POST":
            form = otchForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('otch')
            else:
                message = 'Некорректные значения'
        else:
            form = otchForm(instance=item)
    except Otchestvo.DoesNotExist:
        message = 'Запись не найдена'
        form = otchForm()

    otch_data = Otchestvo.objects.raw("SELECT * FROM main_otchestvo")
    data = {
        'form': form,
        'error': message,
        'otch_data': otch_data
    }

    return render(request, 'main/otch.html', data)

def streets(request):
    message = ''
    street_data = Street.objects.raw("SELECT * FROM main_street")

    if request.method == "POST":
        form = streetForm(request.POST)
        if form.is_valid():
            street = form.cleaned_data['street']
            if Street.objects.filter(street=street).exists():
                message = 'Значение поля street уже существует'
            else:
                form.save()
                return redirect('street')
        else:
            message = 'Неккоректные значения'

    form = streetForm()
    data = {
        'form': form,
        'message': message,
        'street_data': street_data
    }

    return render(request, 'main/street.html', data)

def delete_street(request, id_street):
    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM main_street WHERE id_street = {id_street}")
    return redirect('street')

def update_street(request, id_street):
    message = ''
    try:
        item = Street.objects.get(pk=id_street)
        if request.method == "POST":
            form = streetForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('street')
            else:
                message = 'Некорректные значения'
        else:
            form = streetForm(instance=item)
    except Street.DoesNotExist:
        message = 'Запись не найдена'
        form = streetForm()

    street_data = Street.objects.raw("SELECT * FROM main_street")
    data = {
        'form': form,
        'message': message,
        'street_data': street_data
    }

    return render(request, 'main/street.html', data)


def add_main(request):
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_table')
    else:
        form = MainForm()

    return render(request, 'main/main_add.html', {'form': form})

def delete_main(request, id):
    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM main_main WHERE id = {id}")
    return redirect('main_table')

def update_main(request, id):
    message = ''
    try:
        item = Main.objects.get(pk=id)
        if request.method == "POST":
            form = MainForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('main_table')
            else:
                message = 'Некорректные значения'
        else:
            form = MainForm(instance=item)
    except Main.DoesNotExist:
        message = 'Запись не найдена'
        form = MainForm()

    main_data = Main.objects.raw("SELECT * FROM main_main")
    data = {
        'form': form,
        'error': message,
        'main_data': main_data
    }

    return render(request, 'main/main_update.html', data)


def main_table(request):
    form = MainFilterForm(request.GET)
    queryset = Main.objects.all()

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