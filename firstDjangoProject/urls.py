
from django.urls import path,include

urlpatterns = [
    path('',include('firstDjangoApp.urls')),
    # path('admin/', admin.site.urls),
]
