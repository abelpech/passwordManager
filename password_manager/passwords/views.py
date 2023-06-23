from django.shortcuts import render, redirect
from .models import Password, PasswordGroup, Category


def password_list(request):
    passwords = Password.objects.filter(user=request.user)
    return render(request, 'passwords/password_list.html', {'passwords': passwords})


def add_password(request):
    if request.method == 'POST':
        website = request.POST.get('website')
        username = request.POST.get('username')
        password = request.POST.get('password')
        category_id = request.POST.get('category')
        group_id = request.POST.get('group')

        category = Category.objects.get(id=category_id)
        encrypted_password = request.user.profile.encrypted_key.encrypt(password.encode())

        password_obj = Password(
            category=category,
            website=website,
            username=username,
            encrypted_password=encrypted_password,
            user=request.user,
            group_id=group_id
        )
        password_obj.save()

        return redirect('password_list')

    categories = Category.objects.all()
    groups = PasswordGroup.objects.filter(users=request.user)
    return render(request, 'passwords/add_password.html', {'categories': categories, 'groups': groups})
