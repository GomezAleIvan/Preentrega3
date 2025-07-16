from django.http import HttpResponse
from django.template import Template, Context
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login



def saludar(request):
    return HttpResponse("Buenas")



def mayor_edad(request, edad):
   if edad >= 18:
    return  HttpResponse("es mayor de edad")
   else:
      return HttpResponse("es menor de edad")
   
def probando_template(request):
    
    mi_html = open("C:/Users/gomez/OneDrive/Escritorio/Ale/Coder/Python/Visual python/sistemaslatinos/sistemaslatinos/plantillas/template.html")

    plantilla = Template(mi_html.read())

    mi_html.close()

    mi_contexto = Context({"nombre":"Alejandro"})

    document = plantilla.render(mi_contexto)

    return HttpResponse(document)


def login_request(request):
   if request.method == "POST":
      form = AuthenticationForm(request, data=request.POST)
      if form.is_valid():
         usuario = form.cleaned_data.get("username")
         contra = form.cleane_data.get("password")

         usuario = authenticate(username=usuario, password=contra)

         if user is not None:
            login(request, user)
            return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
         else:
            return render(request, "inicio.html", {"mensaje":f"usuario no encontrado {usuario}"})

   form = AuthenticationForm()

   return render(request, "login.html", {"form":form})

def register(request):
   if request.metod == "POST":
      
      form = UserCreationForm(request.POST)

      if form.is_valid():
         form.save()
         return HttpResponse("Usuario Creado")
   else:
      form = UserCreationForm()
      return render(request, "registro.html", {"form":form})


