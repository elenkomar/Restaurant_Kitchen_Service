from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType, Dish

HOME_URL = reverse("kitchen:index")
DISH_TYPE_LIST_URL = reverse("kitchen:dish-type-list")
DISH_LIST_URL = reverse("kitchen:dishes-list")
COOK_LIST_URL = reverse("kitchen:cooks-list")
URLS = [
    HOME_URL,
    DISH_TYPE_LIST_URL,
    DISH_LIST_URL,
    COOK_LIST_URL,
    reverse("kitchen:dishes-create"),
    reverse("kitchen:dishes-delete", kwargs={"pk": 1}),
    reverse("kitchen:dishes-detail", kwargs={"pk": 1}),
    reverse("kitchen:dishes-update", kwargs={"pk": 1}),
    reverse("kitchen:cooks-create"),
    reverse("kitchen:cooks-delete", kwargs={"pk": 1}),
    reverse("kitchen:cooks-detail", kwargs={"pk": 1}),
    reverse("kitchen:dish-type-list"),
    reverse("kitchen:dish-type-delete", kwargs={"pk": 1}),
    reverse("kitchen:dish-type-update", kwargs={"pk": 1}),
]


class PublicTest(TestCase):

    def test_login_required_to_all_pages(self) -> None:
        for url in URLS:
            with self.subTest(url):
                response = self.client.get(url)

                self.assertNotEqual(response.status_code, 200)


class PrivateTest(TestCase):

    def test_access_with_login(self) -> None:
        user = get_user_model().objects.create(
            username="test",
            years_of_experience=2,
            password="test_password",
        )
        self.client.force_login(user)
        dish_type = DishType.objects.create(name="test")
        Dish.objects.create(
            name="test",
            description="test_description",
            price=10.5,
            dish_type=dish_type,
        )
        for url in URLS:
            with self.subTest(url):
                response = self.client.get(url)

                self.assertEqual(response.status_code, 200)


class HomeTest(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="test",
            years_of_experience=2,
            password="test_password",
        )
        self.client.force_login(self.user)

    def test_correct_info_on_page(self) -> None:
        dish_type = None
        for dish_types_count in range(1, 5):
            dish_type = DishType.objects.create(
                name=f"test_{dish_types_count}"
            )
            response = self.client.get(HOME_URL)
            self.assertEqual(
                response.context["num_dish_types"],
                dish_types_count
            )

        for dishes_count in range(1, 4):
            Dish.objects.create(
                name="test",
                description="test_description",
                price=10.5,
                dish_type=dish_type,
            )
            response = self.client.get(HOME_URL)
            self.assertEqual(
                response.context["num_dishes"],
                dishes_count
            )
        response = self.client.get(HOME_URL)
        self.assertEqual(response.context["num_cooks"], 1)


class DishListTest(TestCase):

    def test_search_filter_working(self) -> None:
        user = get_user_model().objects.create(
            username="test",
            years_of_experience=2,
            password="test_password",
        )
        self.client.force_login(user)
        dish_type = DishType.objects.create(name="test")

        for dish_index in range(1, 12):
            Dish.objects.create(
                name=f"test dish №{dish_index}",
                description="test_description",
                price=10.5,
                dish_type=dish_type,
            )

        response = self.client.get(DISH_LIST_URL + "?name=1")
        # dishes №1, 10, 11
        self.assertEqual(response.context["dish_list"].count(), 3)


class DishTypeListTest(TestCase):

    def test_search_filter_working(self) -> None:
        user = get_user_model().objects.create(
            username="test",
            years_of_experience=2,
            password="test_password",
        )
        self.client.force_login(user)

        for dish_type_index in range(1, 12):
            DishType.objects.create(
                name=f"test dish_type №{dish_type_index}",
            )

        response = self.client.get(DISH_TYPE_LIST_URL + "?name=1")
        # dish_types №1, 10, 11
        self.assertEqual(response.context["dish_type_list"].count(), 3)


class CookListTest(TestCase):

    def test_search_filter_working(self) -> None:
        user = get_user_model().objects.create(
            username="test",
            years_of_experience=2,
            password="test_password",
        )
        self.client.force_login(user)

        for cook_index in range(1, 12):
            get_user_model().objects.create(
                username=f"test cook №{cook_index}",
                years_of_experience=2,
                password="test_password",
            )

        response = self.client.get(COOK_LIST_URL + "?username=1")
        # cooks №1, 10, 11
        self.assertEqual(response.context["cook_list"].count(), 3)
