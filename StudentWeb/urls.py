#the root url make sure you understand this
from django.contrib import admin
from django.urls  import path, include
from django.conf import settings
from django.conf.urls.static import static


# This is the place where we put the links on where we shhould go after clicking
#the function will be detonated after we click links or change url.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
