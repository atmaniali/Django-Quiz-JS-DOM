
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls', namespace='quiz')),
    path('__debug__/', include('debug_toolbar.urls')),
]

admin.site.index_title = "Quiz App" # header
admin.site.site_header = "Quiz App Admin" 
admin.site.site_title = "Administration" # hedaer

