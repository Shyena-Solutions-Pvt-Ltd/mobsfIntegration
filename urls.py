# Create this file if it doesn't exist
# mobsf/urls.py
from django.urls import path, include

urlpatterns = [
    path('owasp/', include('owasp_integration.urls')),
] 