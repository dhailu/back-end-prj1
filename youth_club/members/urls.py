from django.urls import path
from . import views


## First version URL
# urlpatterns = [
#     path('members/', views.members, name='members'),
# ]

## Note about detail URL
# Now we need to make sure that the /details/ url points to the correct view, with id as a parameter.

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]