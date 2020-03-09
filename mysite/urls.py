from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('main.urls','main'), namespace='main')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('accounts/', include(('accounts.urls', 'accounts') ,namespace='accounts')),
    path('teacher/', include(('teacher.urls','teacher'), namespace='teacher')),
    path('student/', include(('student.urls', 'student'), namespace='student')),


]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)