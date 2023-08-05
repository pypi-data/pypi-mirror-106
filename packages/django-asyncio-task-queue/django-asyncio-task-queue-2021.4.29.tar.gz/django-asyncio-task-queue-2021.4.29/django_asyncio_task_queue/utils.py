import django

from .models import AbstractTask


def get_models():
    return list(filter(
        lambda m:issubclass(m,AbstractTask) and not m._meta.abstract,
        django.apps.apps.get_models()
    ))


async def put_tasks(q,count):
    for model in get_models():
        model = task_class.model
        db_table = model._meta.db_table
        enqueued_count = await sync_to_async(model.objects.filter(
            is_enqueued=True).count)()
        enqueued_limit = 10
        if model._meta.db_table in configs:
            config = configs[db_table]
            if config.is_disabled:
                continue
            enqueued_limit = config.enqueued_limit or 10
        count = enqueued_limit - enqueued_count
        if count <= 0:
            continue
