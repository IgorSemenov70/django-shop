from django.core.management.commands.createcachetable import BaseCommand
from shops.models import Offer, Promotion


class Command(BaseCommand):
    help = 'Добавление акций и предложений'

    def handle(self, *args, **options):
        for i in range(100, 1100):
            Promotion.objects.create(name=f'Акция {i}', description=f'Описание акции {i}')
            Offer.objects.create(name=f'Предложение {i}', description=f'Описание предложения {i}')

        self.stdout.write('Акции и предложения успешно загружены')