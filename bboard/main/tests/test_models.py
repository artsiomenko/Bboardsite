from django.test import TestCase
from main.models import Bb, AdvUser, Rubric
from main.tests.model_factories import BbFactory, RubricFactory


class BbTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.bb = BbFactory()

    def test_title(self):
        real_title = getattr(self.bb, 'title')
        expected_title = 'Дом'
        self.assertEqual(real_title, expected_title)

    def test_content(self):
        real_title = getattr(self.bb, 'content')
        expected_title = 'Трехэтажный, кирпич'
        self.assertEqual(real_title, expected_title)

    def test_user(self):
        real_title = getattr(self.bb.author, 'username')
        expected_title = 'Angelika'
        self.assertEqual(real_title, expected_title)

    def test_model_verbose_name(self):
        self.assertEqual(Bb._meta.verbose_name, 'Объявление')

    def test_model_plural_verbose_name(self):
        self.assertEqual(Bb._meta.verbose_name_plural, 'Объявления')


class RubricTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.rubric = RubricFactory()

    def test_title(self):
        real_title = getattr(self.rubric, 'name')
        expected_title = 'Недвижимость'
        self.assertEqual(real_title, expected_title)

    def test_model_verbose_name(self):
        self.assertEqual(Rubric._meta.verbose_name, 'Рубрика')

    def test_model_plural_verbose_name(self):
        self.assertEqual(Rubric._meta.verbose_name_plural, 'Рубрики')
