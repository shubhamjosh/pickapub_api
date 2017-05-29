from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view

from restaurants.views import RestaurantsList

schema_view = get_swagger_view(title='PickaPub API')
urlpatterns = [
    url(r'^$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^restaurants/', RestaurantsList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

urlpatterns = format_suffix_patterns(urlpatterns)
