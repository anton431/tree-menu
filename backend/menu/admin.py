from .models import Menu
from django.contrib import admin


class MenuInline(admin.TabularInline):
    model = Menu
    fields = ('title', 'slug', )
    prepopulated_fields = {'slug': ('title', )}
    extra = 1


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'slug', )
    prepopulated_fields = {'slug': ('title', )}
    inlines = (MenuInline, )