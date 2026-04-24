from django.core.management.base import BaseCommand
from faker import Faker
from products.models import Product, Category
import random
import decimal


class Command(BaseCommand):
    help = 'Générer des fausses données avec Faker'

    def handle(self, *args, **kwargs):
        fake = Faker('fr_FR')

        categories_names = ['Épices', 'Légumes', 'Fruits', 'Viandes', 'Poissons', 'Laitiers']
        categories = []
        for name in categories_names:
            cat, created = Category.objects.get_or_create(
                name=name,
                defaults={'description': fake.text(max_nb_chars=100)}
            )
            categories.append(cat)
            if created:
                self.stdout.write(f'  Catégorie créée : {name}')

        for i in range(30):
            Product.objects.create(
                name=fake.word().capitalize() + ' ' + fake.word(),
                description=fake.text(max_nb_chars=200),
                price=decimal.Decimal(str(round(random.uniform(1.99, 49.99), 2))),
                stock=random.randint(5, 100),
                category=random.choice(categories),
            )

        self.stdout.write(self.style.SUCCESS('✓ 30 produits et 6 catégories générés avec succès !'))
