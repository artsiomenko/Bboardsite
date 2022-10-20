import datetime

from factory.django import DjangoModelFactory
import factory

from main.models import Bb, Rubric, AdvUser


class RubricFactory(DjangoModelFactory):
    class Meta:
        model = Rubric

    name = 'Недвижимость'


class UserFactory(DjangoModelFactory):
    class Meta:
        model = AdvUser

    username = 'Angelika'


class BbFactory(DjangoModelFactory):
    class Meta:
        model = Bb

    title = 'Дом'
    content = 'Трехэтажный, кирпич'
    price = 50000000
    contacts = '7788'
    author = factory.SubFactory(UserFactory)
    rubric = factory.SubFactory(RubricFactory)


