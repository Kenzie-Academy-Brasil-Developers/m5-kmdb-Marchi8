from users.models import User
from django.core.management.base import BaseCommand, CommandError
import ipdb


class Command(BaseCommand):
    help = "Create admin"

    def add_arguments(self, parser):
        # Optional argument
        parser.add_argument(
            "--email",
            type=str,
            help="Defina o email do admin",
        )
        parser.add_argument(
            "--username",
            type=str,
            help="Defina o username do admin",
        )
        parser.add_argument(
            "--password",
            type=str,
            help="Defina a senha do admin",
        )

    def handle(self, *args, **kwargs):
        # username = kwargs["username"]
        # ipdb.set_trace()
        username = "admin"
        password = "admin1234"
        email = "admin@example.com"

        find_email = User.objects.get(email=email)
        find_username = User.objects.get(username=username)
        """
        Verificar pq que cai nos dois erros juntos...
        """
        if find_username:
            raise CommandError("Username `%s` already taken." % username)
        elif find_email:
            # ipdb.set_trace()
            raise CommandError("Email `%s` already taken." % email)

        User.objects.create_superuser(
            username=username,
            password=password,
            email=email,
        )
        self.stdout.write(
            self.style.SUCCESS("Admin `%s` successfully created!" % username)
        )
