from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from form import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.models import User
from models import *
import pdb
# Create your views here.
def temas_view(request):
	if request.user.is_authenticated():
		usuario=request.user
		if  request.method=="POST":
			auxform=formulario_temas(request.POST)
			#datouser=User.objects.get(username=usuario)
			if auxform.is_valid():
				#pdb.set_trace()
				post = auxform.save(commit=False)
		        post.username = usuario
		        post.save()
		        return HttpResponseRedirect("/")
		else:
			auxform=formulario_temas()
		return render_to_response("sistema/temas.html",{"form_tema":auxform},context_instance=RequestContext(request))
	else:
		return HttpResponse("no esta logeado")
def registro_view(request):
	if request.method=="POST":
		auxform=formulario_usuario_registro(request.POST)
		if auxform.is_valid():
			usuario=request.POST['username']
			auxform.save()
			usuariodato=User.objects.get(username=usuario)
			#pdb.set_trace()
			perfil=datos_adicionales_usuario.objects.create(username=usuariodato)
			return HttpResponseRedirect("/")
	else:
		auxform = formulario_usuario_registro()
	return render_to_response("usuario/registro.html",{"form_regi":auxform},context_instance=RequestContext(request))

def login_view(request):
	if request.method=="POST":
		auxform=AuthenticationForm(data=request.POST)
		#pdb.set_trace()
		if request.session['con']>3:
			form_captcha=formulario_capcha(request.POST)
			if form_captcha.is_valid():
				pass
			else:
				datos={"form_login":auxform,"form_chaptcha":form_captcha}
				return render_to_response("usuario/login.html",datos,context_instance=RequestContext(request))		
		if auxform.is_valid():
			usuario=request.POST['username']
			contrasena=request.POST['password']
			acceso=authenticate(username=usuario,password=contrasena)
			#pdb.set_trace()
			if acceso is not None:
				del request.session['con']
				login(request,acceso)
				return HttpResponseRedirect("/")
		else:
			request.session['con']=request.session['con']+1
			auxcon=request.session["con"]
			estado=True
			mensaje="Error en los datos "+str(auxcon)
			if auxcon>3:
				estado=False
				form_captcha=formulario_capcha()
				return render_to_response("usuario/login.html",{"form_login":auxform,"estado":estado,"mensaje":mensaje,"form_chaptcha":form_captcha},context_instance=RequestContext(request))
			else:
				return render_to_response("usuario/login.html",{"form_login":auxform,"estado":estado,"mensaje":mensaje},context_instance=RequestContext(request))
	else:
		request.session['con']=0
		auxform=AuthenticationForm()
	return render_to_response("usuario/login.html",{"form_login":auxform},context_instance=RequestContext(request))
def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")
def actualisar_perfil_view(request):
	if request.user.is_authenticated():
		usuario=request.user
		if request.method=="POST":
			auxform=formulario_de_perfil(data=request.POST)
			datouser=User.objects.get_by_natural_key(username=usuario)
			datosadiuser=datos_adicionales_usuario.objects.get(username=datouser)
			auxform=formulario_de_perfil(request.POST,request.FILES,instance=datosadiuser)
			if auxform.is_valid():
				auxform.save()
				return HttpResponseRedirect("/")
			else:
				return HttpResponse("algo salio mal")
		else:
			auxform=formulario_de_perfil()
		return render_to_response("usuario/actualisar.html",{"form_actua":auxform},context_instance=RequestContext(request))
	else:
		return HttpResponse("no esta logeado")