from django.urls import path
from . import views


urlpatterns=[
    path('base/',views.base,name='base'),
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('',views.user_login,name='user_login'),
    path('ownership/',views.ownership,name="ownership"),
    path('service/',views.service,name="service"),
    path('sign/',views.sign_lo,name='sign_lo'),
    path('logout/',views.logout_us,name='logout_us')
]