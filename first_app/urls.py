from django.conf.urls import url
from first_app import views
from django.urls import path



app_name = 'first_app'



urlpatterns = [
path('',views.SchoolListView.as_view(),name='list'),
path('<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),

]
