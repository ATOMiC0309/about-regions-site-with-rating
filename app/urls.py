from django.urls import path
from .views import index, region_detail, user_login, user_logout, user_register, about_us, rate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('selected-info/<int:pk>/', region_detail, name="region_detail"),
    path('about/', about_us, name="about"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('register/', user_register, name="register"),
    path('rate/<int:post_id>/<int:rating>/', rate),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
