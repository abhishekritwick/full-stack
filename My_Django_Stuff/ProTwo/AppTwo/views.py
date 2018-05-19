from django.shortcuts import render
# from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import UserForm

# Create your views here.
def index(request):
    return render(request,'AppTwo/index.html')

# def help(request):
#     my_dict = {'new_text':"HELP PAGE"}
#     return render(request,'AppTwo/help.html',context=my_dict)

def users(request):
    usersList = User.objects.order_by('first_name')
    user_dict = {'user_data':usersList}
    return render(request,'AppTwo/users.html',context=user_dict)

def user_form(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR, FORM INVALID')

    return render(request,'AppTwo/user_form.html', {'user_form':form})
