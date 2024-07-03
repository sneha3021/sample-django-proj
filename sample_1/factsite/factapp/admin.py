from django.contrib import admin

from factapp import models

admin.site.register(models.FactModel)

#class BlogPostAdmin(admin.ModelAdmin):
#    list_display = ('title', 'timestamp','body')

#admin.site.register(models.BlogPost,BlogPostAdmin)

