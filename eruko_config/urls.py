from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# THIS IS THE MISSING IMPORT FIX:
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # For login/logout
    path('', include('core.urls')),      # Homepage & Forms
    path('members/', include('members.urls')), # Dashboard & Profiles
]

# This line uses the 'static' function we just imported
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)