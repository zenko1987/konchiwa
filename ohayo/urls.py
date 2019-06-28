"""ohayo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#ohayo

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('konchiwa.urls')),         
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""

  path('login/', include('konchiwa.urls')),
    path('log_out/', include('konchiwa.urls')),
    
    
    
    path('philosophy/', include('konchiwa.urls')),
    path('history/', include('konchiwa.urls')),
    path('linguistics/', include('konchiwa.urls')),
    path('cul_anthropology/', include('konchiwa.urls')),
    path('pedagogy/', include('konchiwa.urls')),
    path('psychology/', include('konchiwa.urls')),
    path('archeology/', include('konchiwa.urls')),
    path('religion/', include('konchiwa.urls')),
    path('aca_writing/', include('konchiwa.urls'))
    
    """