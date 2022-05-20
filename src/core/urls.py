from django.contrib import admin
from django.urls import path


admin.site.site_header = 'Отдел кадров компании «Нефтегазик»'
admin.site.site_title = 'Отдел кадров'

urlpatterns = [
    path('', admin.site.urls),
]
