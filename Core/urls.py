from django.contrib import admin
from django.urls import include, path
from Apps.base.views import LandingPage

urlpatterns = [
    path('', LandingPage.as_view()),
    path('admin/', admin.site.urls),
    path('users/', include('Apps.users.urls')),
]
