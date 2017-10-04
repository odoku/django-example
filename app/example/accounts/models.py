# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from model_utils.fields import AutoCreatedField, AutoLastModifiedField

from .managers import AdministratorManager


class Administrator(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    is_staff = True

    email = models.EmailField('メールアドレス', unique=True)
    is_active = models.BooleanField('有効', default=True)
    created_at = AutoCreatedField('作成日時')
    modified_at = AutoLastModifiedField('更新日時')

    objects = AdministratorManager()

    class Meta:
        verbose_name = "管理者"
        verbose_name_plural = "管理者"

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.__unicode__()

    def get_short_name(self):
        return self.__unicode__()

    def save(self, *args, **kwargs):
        self.is_superuser = True
        return super(Administrator, self).save(*args, **kwargs)
