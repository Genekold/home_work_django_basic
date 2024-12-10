from django.core.management.base import BaseCommand
from django.core.management import call_command
from users.models import User


class Command(BaseCommand):
    help = 'Добавление тестовых продуктов в базу данных из фикстуры'

    def handle(self, *args, **kwargs):

        User.objects.all().delete()

        call_command('loaddata', 'groups.json')
        self.stdout.write(self.style.SUCCESS('Данные загружены'))
