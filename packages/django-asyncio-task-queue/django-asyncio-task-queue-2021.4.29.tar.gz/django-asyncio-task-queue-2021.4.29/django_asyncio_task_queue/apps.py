from django.apps import AppConfig
from django.db.utils import ImproperlyConfigured, OperationalError, ProgrammingError


class Config(AppConfig):
    name = 'django_asyncio_task_queue'
    verbose_name = 'asyncio-task-queue'

    def ready(self):
        from .models import Debug, Error

        try:
            error_count = Error.objects.all().count()
            Debug._meta.verbose_name_plural = 'Debug (%s)' % Debug.objects.all().count()
            Error._meta.verbose_name_plural = 'Error (%s)%s' % (error_count,' ERRORS!!!11111111' if error_count else '')
        except (ImproperlyConfigured,OperationalError, ProgrammingError):
            pass

