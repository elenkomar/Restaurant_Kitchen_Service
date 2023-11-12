from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishListView,
    CookListView,
    DishDetailView,
    CookDetailView,
    CookCreateView,
    CookDeleteView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView, toggle_assign_to_dish,
)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path(
        "dish-types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create"
    ),
    path(
        "dish-types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update"
    ),
    path(
        "dish-types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete"
    ),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dishes-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dishes-create"),
    path("dishes/<int:pk>/update/",
         DishUpdateView.as_view(),
         name="dishes-update"
         ),
    path(
        "dishes/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dishes-delete"
    ),
    path(
        "cooks/<int:pk>/toggle-assign/",
        toggle_assign_to_dish,
        name="toggle-dish-assign"
    ),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cooks-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cooks-create"),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cooks-delete"
    ),
]

app_name = "kitchen"
