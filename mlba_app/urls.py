from mlba import settings
from django.contrib.staticfiles.urls import static
from django.urls import path
import mlba_app.views

urlpatterns = [
                  # path('',pink_salt_app.views.index,name="index"),
                  path('', mlba_app.views.index, {'pagename': ''}, name='home'),
                  path('<str:pagename>', mlba_app.views.index, name='index'),
                  path('about', mlba_app.views.about, {'pagename': 'about'}, name='about'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
