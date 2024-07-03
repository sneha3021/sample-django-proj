from django.conf.urls import url,include
import factapp.views

urlpatterns = [url(r'factarchive/',factapp.views.fact_archive, name = 'fact_archive'),
               url(r'^$',factapp.views.index,name = 'index'),
               url(r'factpost/',factapp.views.fact_post,name = 'fact_post'),
              ]
