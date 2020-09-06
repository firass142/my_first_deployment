from . import views
from django.conf.urls import url
urlpatterns =[
    url(r'^',views.Index.as_view,name='index'),
    url(r'formpage/',views.form_page_view,name='form_view')
 ]