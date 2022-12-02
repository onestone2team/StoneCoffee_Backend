from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/',include("user.urls")),
    path('/',include("director.urls")),
    path('product/',include("product.urls")),
    path('/',include("comment.urls")),
    path('/',include("mypage.urls")),
    path('/',include("survey.urls")),
    path('/',include("order.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)