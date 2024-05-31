from django.contrib import admin
from django.urls import path
from aplikasi.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:user_id>', profile_view, name='profile'),
    path('posting/', posting_view, name='posting'),
    path('register/', register_view, name='register'),
    # path('profile/image/', add_image_profile, name='profile_image'),
    path('profile/image/edit/<int:user_id>', add_image_profile, name='profile_image'),
    path('profile/edit/<int:user_id>', edit_profile_view, name='edit_profile'),
    path('posting/delete/<int:post_id>', delete_posting_view, name='delete_posting'),
    path('user/ban/<int:user_id>', ban_user_view, name='ban_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
