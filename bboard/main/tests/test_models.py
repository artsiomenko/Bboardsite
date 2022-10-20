from django.test import TestCase

from main.models import Bb


class BbTests(TestCase):
    """Тесты для модели Bb"""

    @classmethod
    def setUpTestData(cls):
        cls.bb = Bb.objects.create(
            title='Дом', content='Трехэтажный, кирпич', price=50000000, contacts='7788'
        )

    def test_title(self):
        real_title = getattr(self.bb_field, 'title')
        expected_title = 'Дом'
        self.assertEqual(real_title, expected_title)

    def test_model_verbose_name(self):
        self.assertEqual(Bb._meta.verbose_name, 'Объявление')

    def test_model_verbose_name_plural(self):
        self.assertEqual(Bb._meta.verbose_name_plural, 'Объявления')

    def test_title(self):
        pass

    def test_max_length(self):
        pass

