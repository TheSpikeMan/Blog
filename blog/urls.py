
from django.urls import path
from . import views
# zaimportowanie wszystkich widoków
urlpatterns = [
    # przyporządzkowanie widoku view o nazwie post_list do strony głównej
    # nazwa post_list jest nazwą url, która będzie używana do zidentyfikowania widoku
    # nazwa moze byc taka sama jak nazwa widoku lub kompletnie inna
    path('', views.post_list, name='post_list')

]
