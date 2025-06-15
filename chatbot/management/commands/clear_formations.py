from django.core.management.base import BaseCommand
from chatbot.models import Formation

class Command(BaseCommand):
    help = 'Supprime toutes les formations existantes dans la base de données'

    def handle(self, *args, **kwargs):
        count = Formation.objects.count()
        Formation.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"{count} formations supprimées."))
