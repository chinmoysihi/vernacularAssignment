from django.urls import re_path,path

from . import views
urlpatterns = [
    #POST API to validate a slot with a finite set of values.
    re_path(r'^finite_set/',views.finite_set,name='finite_set'),
    re_path(r'^numeric_set/',views.numeric_set,name='numeric_set')
]
