from . import views
from django.urls import path, include
from .views import EmployeeCreate, EmployeeRetrieve, EmployeeDetail, EmployeeUpdate, EmployeeDelete, detail_view, delete_view, update_view, list_view, create_view
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns=[
    path('', views.index, name='index'),
    path('2/', views.form_class, name='form_class'),
    path('3/', views.model_form_class, name='model_form_class'),
    path('4/', EmployeeCreate.as_view(), name = 'EmployeeCreate'),
    path('4/r/', EmployeeRetrieve.as_view(), name = 'EmployeeRetrieve'),
    path('4/r/<int:pk>', EmployeeDetail.as_view(), name='EmployeeDetail'),
    path('4/r/<int:pk>/u/', EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),
    path('4/r/<int:pk>/d/', EmployeeDelete.as_view(), name='EmployeeDelete'),
    path('5/', views.create_view, name='create_view'),
    path('5/r', list_view ),
    path('5/<id>', detail_view ),
    path('5/<id>/u', update_view),
    path('5/<id>/d', delete_view),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
]