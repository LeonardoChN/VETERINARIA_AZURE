#FUNCIONAMIENTO DEL LOGIN
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt

#FUNCIONAMIENTO DE LA APP
from APPVET.forms import   formFunc,formMasc, formCliente,   formCita,  formRaza,formTipom,formTipoat
from APPVET.models import  funcionarios,mascota,clientes ,   cita



#VISTA PARTE DEL LOGIN
@csrf_exempt
def index(request):
    return render(request, 'APPVET/index.html')
@csrf_exempt
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
    return render(request, 'APPVET/register.html')
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'APPVET/login.html')
@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('/')

#VISTA PARTE DE LA VETERINARIA

##FUNCIONARIOS
@login_required
@csrf_exempt
def listarfuncionario(request):
    fun = funcionarios.objects.all()
    data = {'funcionario': fun}
    return render(request, 'APPVET/vistafun.html', data)
#AGREGAR
@login_required
@csrf_exempt
def agregarfun(request):
    form = formFunc()
    if request.method == 'POST' : 
        form = formFunc(request.POST)
        if form.is_valid(): 
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APPVET/agregarfun.html', data)


## VISTA CITAS
@login_required
@csrf_exempt
def listarcitas(request):
    citas = cita.objects.all()
    data = {'cita': citas}
    return render(request, 'APPVET/vistacitas.html', data)
#AGREGAR
@login_required
@csrf_exempt
def agregarcitas(request):
    form = formCita()
    if request.method == 'POST' : 
        form = formCita(request.POST)
        if form.is_valid(): 
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APPVET/agregarcitas.html', data)


## VISTA CLIENTES
@login_required
@csrf_exempt
def listarcliente(request):
    cliente = clientes.objects.all()
    data = {'clientes': cliente}
    return render(request, 'APPVET/vistaclient.html', data)
#AGREGAR
@login_required
@csrf_exempt
def agregarcliente(request):
    form = formCliente()
    if request.method == 'POST' : 
        form = formCliente(request.POST)
        if form.is_valid(): 
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APPVET/agregarclient.html', data)


## VISTA MASCOTAS
@login_required
@csrf_exempt
def listarmascotas(request):
    masc = mascota.objects.all()
    data = {'mascota': masc}
    return render(request, 'APPVET/vistamasc.html', data)
#AGREGAR
@login_required
@csrf_exempt
def agregarmascota(request):
    form = formMasc()
    if request.method == 'POST' : 
        form = formMasc(request.POST)
        if form.is_valid(): 
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APPVET/agregarmasc.html', data)



#-----------------------------------------------------------
# ------- AGREGAR TIPO ATECION, TIPO MASCOTA Y RAZA --------
#-----------------------------------------------------------

#TIPO ATECION
@login_required
@csrf_exempt
def agregaratencion(request):
    form = formTipoat()
    if request.method == 'POST' : 
        form = formTipoat(request.POST)
        if form.is_valid(): 
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APPVET/agregartipoaten.html', data)


#TIPO MASCOTA
@login_required
@csrf_exempt
def agregartipomascota(request):
    form = formTipom()
    if request.method == 'POST' : 
        form = formTipom(request.POST)
        if form.is_valid(): 
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APPVET/agregartipomasc.html', data)

#TIPO RAZA
@login_required
@csrf_exempt
def agregarraza(request):
    form = formRaza()
    if request.method == 'POST' : 
        form = formRaza(request.POST)
        if form.is_valid(): 
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APPVET/agregarraza.html', data)



#--------------------------------------------
#---------  ELIMINAR Y ACTUALIZAR   ---------
#--------------------------------------------


#CLIENTES
@csrf_exempt
def eliminarcliente(request, id):
    clientex = clientes.objects.get(id= id)
    clientex.delete()
    return redirect('/clientes')

@csrf_exempt
def actualzarcliente (request, id) :
    clientex = clientes.objects.get(id= id)
    form = formCliente (instance=clientex)
    if request.method == 'POST':
        form = formCliente(request.POST, instance=clientex)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APPVET/agregarclient.html', data)


    #FUNCIONARIOS
@csrf_exempt
def eliminarfuncionario(request, id):
    funcionariox = funcionarios.objects.get(id= id)
    funcionariox.delete()
    return redirect('/func')
@csrf_exempt
def actualizarfuncionario (request, id) :
    funcionariox = funcionarios.objects.get(id= id)
    form = formFunc (instance=funcionariox)
    if request.method == 'POST':
        form = formFunc(request.POST, instance=funcionariox)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APPVET/agregarfun.html', data)


    #CITAS
@csrf_exempt
def eliminarcitas(request, id):
    citax = cita.objects.get(id= id)
    citax.delete()
    return redirect('/citas')
@csrf_exempt
def actualizarcitas (request, id) :
    citax = cita.objects.get(id= id)
    form = formCita (instance=citax)
    if request.method == 'POST':
        form = formCita(request.POST, instance=citax)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APPVET/agregarcitas.html', data)