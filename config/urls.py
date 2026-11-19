"""
URL configuration for config project.

This file maps web addresses (URLs) to the code that handles them.
Think of it like a phone book: when someone visits a URL, Django looks it up
here to find which view function or class should handle the request.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin        # Django's built-in admin site
from django.urls import path            # Function to define a URL route
from django.urls import path            # (duplicate import, harmless)
from config.views import HealthCheckView   # Our custom health check page

# urlpatterns is a list of URL routes. Each route tells Django:
# "when someone visits this web address, run this view code".
# Order matters: Django checks them from top to bottom and uses the first match.
urlpatterns = [
    # /admin/ -> Django's built-in admin site for managing data
    path('admin/', admin.site.urls),
    # /health/ -> our HealthCheckView (returns "healthy" status)
    # as_view() turns the class into something Django can call as a view.
    # name="health-check" gives this route a nickname we can use elsewhere.
    path(
        "health/",
        HealthCheckView.as_view(),
        name="health-check"
    ),
]
