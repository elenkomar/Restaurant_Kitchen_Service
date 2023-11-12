from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish


class DishTypeTest(TestCase):

    def test_str_method(self) -> None:
        dish_type = DishType.objects.create(name="test_name")
        self.assertEqual(f"{dish_type}", "test_name")


class CookTest(TestCase):

    def setUp(self) -> None:
        self.cook = get_user_model().objects.create_user(
            username="test_cook",
            password="test_password",
            years_of_experience=2,
            first_name="fist_name",
            last_name="last_name"
        )

    def test_str_method(self) -> None:

        self.assertEqual(
            f"{self.cook}", "test_cook (fist_name last_name)"
        )

    def test_years_of_experience_present(self) -> None:
        self.assertEqual(self.cook.years_of_experience, 2)


class DishTest(TestCase):

    def test_str_method(self) -> None:
        dish_type = DishType.objects.create(name="test_name")
        dish = Dish.objects.create(
            name="test_name",
            description="test_description",
            price=10.50,
            dish_type=dish_type,
        )
        self.assertEqual(f"{dish}", "test_name: 10.5$")
