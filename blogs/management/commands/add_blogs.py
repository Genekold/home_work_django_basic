from django.core.management.base import BaseCommand
from django.core.management import call_command
from blogs.models import Blog


class Command(BaseCommand):
    help = 'Добавление тестовых продуктов в базу данных из фикстуры'

    def handle(self, *args, **kwargs):

        Blog.objects.all().delete()

        call_command('loaddata', 'blogs_fixture.json')
        self.stdout.write(self.style.SUCCESS('Данные загружены'))
