from django.shortcuts import render
#from django.http import HttpResponse
#from second_app.models import User
from second_app.forms import NewUserForm
def index(request):
    return render(request,'second_app/index.html')

def users(request):
    form=NewUserForm()
    if request.method=="POST":
        form=NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR,Form Invalid")

    return render(request,'second_app/users.html',{'forms':form})

# Create your views here.
