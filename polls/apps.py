from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # sets default type of auto-incrementing primary keys to BigAutoField
    name = 'polls'
