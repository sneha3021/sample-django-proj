from django.conf.urls import url,include
import MyApp.views

urlpatterns = [ url(r'^$',MyApp.views.home,name = 'home'),
                url(r'archive/',MyApp.views.archive, name = 'archive'),
                url(r'create/',MyApp.views.create_blogpost),
              ]

