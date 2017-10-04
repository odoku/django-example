# -*- coding: utf-8 -*-

import random
import string

from django.contrib.auth.hashers import make_password
import factory
from factory.fuzzy import BaseFuzzyAttribute

from .models import Administrator


def generate_random_string(min_length, max_length=None, chars=string.ascii_letters):
    if not max_length:
        max_length = min_length

    chars = tuple(chars)
    return ''.join([
        random.choice(chars)
        for x in range(random.randint(min_length, max_length))
    ])


class FuzzyEmail(BaseFuzzyAttribute):
    def __init__(self, domain=None):
        self.domain = domain or 'samples.com'

    def fuzz(self):
        return '{}@{}'.format(
            generate_random_string(3, 22),
            self.domain,
        )


class AdministratorFactory(factory.django.DjangoModelFactory):
    email = FuzzyEmail()

    class Meta:
        model = Administrator
        django_get_or_create = ('email',)

    @factory.lazy_attribute
    def password(self):
        return make_password('hogehoge')
