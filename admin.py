from django.contrib import admin
from django.forms.widgets import ClearableFileInput
from juss.widgets import JFileInputWidget

from .models import *


class JBoxAdmin(admin.ModelAdmin):
    list_display = ('id', 'show_html', 'name', 'created')
    list_display_links = ('id', 'show_html')
    list_filter = ('created', )
    list_per_page = 12
    search_fields = ('name',)
    formfield_overrides = {
        models.ImageField: {'widget':JFileInputWidget}
    }
    #readonly_fields = ('archive',)

admin.site.register(JBox, JBoxAdmin)
