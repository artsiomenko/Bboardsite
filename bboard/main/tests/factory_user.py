from factory.django import DjangoModelFactory
import factory

from bboard.models import Bb, Rubric


class RubricFactory(DjangoModelFactory):
    class Meta:
        model = Rubric

    name = 'Транспорт'


class BbFactory(DjangoModelFactory):
    class Meta:
        model = Bb

    title = 'Автомобиль'
    content = 'Renault Megan tDi 1.5 2013'
    price = 30000
    rubric = factory.SubFactory(RubricFactory)