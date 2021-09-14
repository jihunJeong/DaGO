"""shopping_mall URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from user.views import logout, RegisterView,LoginView
from contact import views as contact_views
from mall.views import SearchFormView
from mall.views import MainView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mall.urls')),
    path('product/', include('product.urls')),
    path('logout/', logout),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('contact/', contact_views.contact_view, name='contact'),
    path('cart/', include('cart.urls')),
    path('search/', SearchFormView.as_view(), name='search'),
]
    
