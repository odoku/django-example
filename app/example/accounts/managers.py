# -*- coding: utf-8 -*-

from django.contrib.auth.models import UserManager as BaseUserManager


class AdministratorManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        from example.accounts.models import Administrator
        instance = Administrator(email=email)
        instance.set_password(password)
        instance.save(self._db)
        return instance

    def create_superuser(self, email, password, **extra_fields):
        from example.accounts.models import Administrator
        instance = Administrator(email=email, is_superuser=True)
        instance.set_password(password)
        instance.save(self._db)
        return instance
