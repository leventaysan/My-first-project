from django.contrib import admin

# Register your models here.
from blog.models import post



class postAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}

admin.site.register(post,postAdmin)
