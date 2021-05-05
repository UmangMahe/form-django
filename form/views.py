from django.shortcuts import redirect, render
from .models import Form
from django.contrib import messages
from django.http import JsonResponse

def form(request):
    
    if request.method == 'POST' :
        email = request.POST['email']
        password = request.POST['pswd']
        
        if 'submit_post' in request.POST:
            if(email == "" or password == ""):
                messages.warning(request, "Fields cannot be blank")
                return redirect('/')
            elif Form.objects.filter(email=email).exists():
                messages.warning(request, "Email exists")
                return redirect('/')
            else:
                form = Form(email=email, password=password)
                form.save()
                messages.success(request, "Saved Successfully")
                return redirect('/')
        elif request.is_ajax:
            if(email == "" or password == ""):
                return JsonResponse({"errors": "Fields cannot be blank"}, status=400)
            elif(Form.objects.filter(email=email).exists()):
                return JsonResponse({"errors": "Email exists!"}, status=400)
            
            else:
                form = Form(email=email, password=password)
                form.save()
                return JsonResponse({"msg":"AJAX: Saved Successfully"})
    else:    
        return render(request, 'home.html')


# Create your views here.
