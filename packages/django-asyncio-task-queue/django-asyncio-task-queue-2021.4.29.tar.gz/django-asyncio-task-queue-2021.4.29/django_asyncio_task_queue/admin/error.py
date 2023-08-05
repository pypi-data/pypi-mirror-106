from django.contrib import admin
from django.utils.timesince import timesince

from django_asyncio_task_queue.models import Error

class ErrorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Error._meta.get_fields()]+['timesince']
    list_filter = ['db_table','exc_type']

    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request, obj=None):
        return False

    def timesince(self, stat):
        if stat.created_at:
            return timesince(stat.created_at).split(',')[0]+' ago'
    timesince.short_description = ''

admin.site.register(Error, ErrorAdmin)

