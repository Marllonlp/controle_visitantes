from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from apps.dashboard.views import index
from apps.visitantes.views import finalizar_visita, informacoes_visitante, registrar_visitante

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path("", index, name='index'),
    path("registrar-visitante/", registrar_visitante, name='registrar_visitante'),
    path("visitante/<int:id>/", informacoes_visitante, name ='informacoes_visitante'),
    path("visitante/<int:id>/finalizar-visita", finalizar_visita, name='finalizar_visita')
]
