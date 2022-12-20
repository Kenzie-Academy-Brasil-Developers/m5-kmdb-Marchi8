from users.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create admin"

    def add_arguments(self, parser):
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
        if kwargs["username"]:
            username = kwargs["username"]
        else:
            username = "admin"

        if kwargs["email"]:
            email = kwargs["email"]
        else:
            email = "admin@example.com"

        if kwargs["password"]:
            password = kwargs["password"]
        else:
            password = "admin1234"

        try:
            find_user = User.objects.get(email=email)
            if username == find_user.username:
                raise CommandError("Username `%s` already taken." % username)
            if find_user:
                raise CommandError("Email `%s` already taken." % email)
        except User.DoesNotExist:
            User.objects.create_superuser(
                username=username,
                password=password,
                email=email,
            )

            self.stdout.write(
                self.style.SUCCESS("Admin `%s` successfully created!" % username)
            )
