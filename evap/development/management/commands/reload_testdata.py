from django.core.management import call_command
from django.core.management.base import BaseCommand

from evap.evaluation.management.commands.tools import confirm_harmful_operation


class Command(BaseCommand):
    args = ""
    help = "Drops the database, recreates it and then loads the testdata."

    def handle(self, *args, **options):
        self.stdout.write("")
        self.stdout.write("WARNING! This will drop the database and cause IRREPARABLE DATA LOSS.")
        if not confirm_harmful_operation(self.stdout):
            return

        self.stdout.write('Executing "python manage.py reset_db"')
        call_command("reset_db", interactive=False)

        self.stdout.write('Executing "python manage.py migrate"')
        call_command("migrate")

        # clear any data the migrations created.
        # their pks might differ from the ones in the dump, which results in errors on loaddata
        self.stdout.write('Executing "python manage.py flush"')
        call_command("flush", interactive=False)

        self.stdout.write('Executing "python manage.py loaddata test_data"')
        call_command("loaddata", "test_data")

        self.stdout.write('Executing "python manage.py clear_cache --all -v=1"')
        call_command("clear_cache", "--all", "-v=1")

        self.stdout.write('Executing "python manage.py refresh_results_cache"')
        call_command("refresh_results_cache")

        self.stdout.write("Done.")
