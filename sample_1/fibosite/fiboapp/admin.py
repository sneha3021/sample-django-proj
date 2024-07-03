from django.contrib import admin

# Register your models here.

from fiboapp import models

admin.site.register(models.FiboModel)

#class BlogPostAdmin(admin.ModelAdmin):
#    list_display = ('title', 'timestamp','body')

#admin.site.register(models.BlogPost,BlogPostAdmin)
