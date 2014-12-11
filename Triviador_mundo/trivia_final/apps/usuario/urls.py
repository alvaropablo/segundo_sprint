from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import AdminPasswordChangeForm
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trivia_final.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^registro/', registro_view, name="registro"),
    url(r'^login/', login_view, name="login"),
    url(r'^logout/', logout_view, name="logout"),
    url(r'^actualisar/', actualisar_perfil_view, name="actualisar"),
    url(r'^tema/', temas_view, name="tema"),
    url(r'^crear_pregunta/', preguntas_view, name="preguntas"),
    url(r'^crear_respuestas/', respuestas_view, name="respuestas"),
    url(r'^lista_preguntas/', lista_preguntas_view, name="lista_preguntas"),
    url(r'^eliminar/(?P<id>.+?)/$', lista_preguntas_eliminar_view, name="eliminar"),
    url(r'^editar/(?P<id>.+?)/$', lista_preguntas_modificar_pregunta_view, name="editar"),
    url(r'^editar_respuesta/(?P<id>.+?)/$', lista_preguntas_modificar_respuesta_view, name="editarResp"),
    url(r'password_change/$', password_change,name="pass"),
    url(r'crear_sala/$', crear_sal_view,name="sala"),
    url(r'staff/(?P<id>.+?)/$', permisos_view,name="permisos"),
    url(r'quitarstaf/(?P<id>.+?)/$', permisos_quitar_view,name="permisosquitar"),
    url(r'lista_premisos/', permisos_lista_view,name="permisoslista"),
)