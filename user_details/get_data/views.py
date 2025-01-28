from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def get_details(request):
    try:
        user = User.objects.get(id= request.user.id)
        context={'user': user}
        return render(request,'get_details.html', context)
    except User.DoesNotExist:
        return render(request,'404_error.html')