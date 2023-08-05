from django.contrib import admin
from django_asyncio_task_queue.models import Debug

class DebugAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
       return False

admin.site.register(Debug, DebugAdmin)


