from django.contrib import admin
from django.urls import path
#from rest_framework.urlpatterns import format_suffix_pformat_suffix_patterns
from sports.views import sport, sportbyid, landingpage

urlpatterns = [
    path('',landingpage.as_view()),
    path('admin/', admin.site.urls),
    path('sports/', sport.as_view()),
    path('sports/<int:id>/', sportbyid.as_view()),
]