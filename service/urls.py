from django.urls import path
from service import views
from django.contrib.auth import views as ad
urlpatterns=[
       path('',views.home,name="home"),
       path('a/',views.about,name="ab"),
       path('c/',views.contact,name="cn"),
       path('log/',ad.LoginView.as_view(template_name="services/login.html"),name="lg"),
       path('reg/',views.registration,name="reg"),
       path('ser/',views.Service,name="ser"),
       path('logout/',ad.LogoutView.as_view(template_name="services/logout.html"),name="lgo"),
       path('profile/',views.profile,name='pro'),
       path('e/<int:si>/',views.userupdate,name="ue"),
       path('delt/<int:st>/',views.deletedata,name="delete"),
       path('showdata/',views.showinfo,name="show"),
       path('infodelete/<int:et>',views.infodelete,name='infodelete'),

      
]