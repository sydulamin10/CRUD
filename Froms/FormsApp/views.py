from django.shortcuts import render
from .models import profile


def login(r):
    if r.method == 'POST':
        name = r.POST['name']
        email = r.POST['email']
        img = r.FILES['fileupload']
        user = profile.objects.create(name=name, email=email, proPic=img)
        user.save()

    return render(r, 'login.html', locals())


def Prof(r):
    pro = profile.objects.all()
    return render(r, 'newProf.html', locals())


def update(r, id):
    pro = profile.objects.filter(id=id).all()
    if r.method == 'POST':
        name = r.POST['name']
        email = r.POST['email']
        img = r.FILES['fileupload']

        user = pro.update(name=name, email=email, proPic=img)

    return render(r, 'Update.html', locals())


def delete(r):
    return render(r, 'newProf.html', locals())
