from django.urls import path, reverse_lazy
from.views import servico_views, usuario_views
from django.contrib.auth import views as auth_views

urlpatterns =[
path('servicos/cadastrar',servico_views.cadastrar_servico,name='cadastrar_servico'),
path('servicos/listar',servico_views.listar_servicos,name='listar_servicos'),
path('servicos/editar/<int:id>',servico_views.editar_servico,name='editar_servico'),
path('usuarios/cadastrar',usuario_views.cadastrar_usuario,name='cadastrar_usuario'),
path('usuarios/listar',usuario_views.listar_usuarios,name='listar_usuarios'),
path('usuarios/editar/<int:id>',usuario_views.editar_usuario,name='editar_usuario'),
path('autenticacao/login',auth_views.LoginView.as_view(),name='logar_usuario'),
path('autenticacao/logout',auth_views.LogoutView.as_view(),name='deslogar_usuario'),
path('autenticacao/alterar_senha',auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('listar_servicos')),name='alterar_senha'),
]