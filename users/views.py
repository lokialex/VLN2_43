from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from users.models import Profile
from users.forms.update_profile_form import EditProfileForm, EditUserForm
from users.forms.register_form import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    context = {"users": "active"}
    return render(request, "users/index.html", context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            #new_profile = Profile(user_id='')
            form.save()
            return redirect('/users/login')
        else:
            return render(request, 'users/register.html', {
                'form': form
            })
    return render(request, 'users/register.html', {
        'form': RegisterForm()
    })


@login_required
def profile(request):
    info_key_dict = {'username': '', 'email': '', 'first_name': '', 'last_name': '', 'address_1': '',
                     'address_2': '', 'city': '', 'postcode': '', 'country': '', 'profile_image': ''}
    label_dict = {'username': 'Username', 'email': 'Email', 'first_name': 'First name', 'last_name': 'Last name',
                  'address_1': 'Address 1',
                  'address_2': 'Address 2', 'city': 'City', 'postcode': 'Postcode', 'country': 'Country',
                  'profile_image': 'Profile image'}
    print()
    user = User.objects.filter(username=request.user.username).first()
    current_profile = Profile.objects.filter(user=request.user).first()
    if current_profile == None:
        current_profile = Profile(user_id=user.id)
        current_profile.save()
    profile_dict = current_profile.__dict__
    user_dict = user.__dict__

    for key in info_key_dict:
        if key in profile_dict:
            info_key_dict[key] = profile_dict[key]
        elif key in user_dict:
            info_key_dict[key] = user_dict[key]

    complete_info_dict = dict((label_dict[key], value) for (key, value) in info_key_dict.items())

    return render(request, 'users/profile.html', {
        'info_dict': complete_info_dict
    })


@login_required
def update_profile(request):
    current_profile = Profile.objects.filter(user=request.user).first()

    # user portion does not update!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    if request.method == 'POST':
        profile_form = EditProfileForm(instance=current_profile, data=request.POST)
        user_form = EditUserForm(instance=current_profile.user, data=request.POST)

        if profile_form.is_valid() and user_form.is_valid():
            user_save_form = user_form.save(commit=False)
            custom_form = profile_form.save(commit=False)
            custom_form.user = user_save_form
            custom_form.save()
            return redirect('profile')

    return render(request, 'users/update_profile.html', {
        'profile_form': EditProfileForm(instance=current_profile),
        'user_form': EditUserForm(instance=current_profile.user)
    })
