from django.contrib import admin
from .models import *

# Register your models here.

class ImageAdmin(admin.TabularInline):
    model=Images



class TechnologyAdmin(admin.ModelAdmin):
    inlines=[ImageAdmin]
    prepopulated_fields={'slug':('name',)}

admin.site.register(Technology,TechnologyAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
admin.site.register(Category,CategoryAdmin)


admin.site.register(Characteristics)

admin.site.register(Reviews)