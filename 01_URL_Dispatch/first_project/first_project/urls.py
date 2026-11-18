from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('okaimonohelp/', include('okaimonohelp.urls')),
    path('accounts/', include('accounts.urls')),
]