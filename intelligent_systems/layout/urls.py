from django.urls import path, include

from . import views
from AST import views as ast_views
from FL import views as fl_views

urlpatterns=[
    path('', views.homeLayout, name='index'),
    path('AST/', ast_views.migration_AST_View, name='migration_AST'),
    path('FL/', fl_views.migration_FL_View, name='migration_FL'),
]