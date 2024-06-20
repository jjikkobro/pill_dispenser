from django.core.management.base import BaseCommand
from notes.models import Note

class Command(BaseCommand):
    help = 'Reset finished field to 0 for all notes'

    def handle(self, *args, **kwargs):
        Note.objects.all().update(finished=0)
        self.stdout.write(self.style.SUCCESS('Successfully reset finished field for all notes'))
