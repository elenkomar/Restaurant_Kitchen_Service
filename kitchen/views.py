from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.models import Dish, DishType, Cook
from kitchen.forms import (
    CookForm,
    DishForm,
    DishSearchForm,
    CookSearchForm,
    DishTypeSearchForm
)


@login_required
def index(request):
    num_dishes = Dish.objects.count()
    num_cooks = get_user_model().objects.count()
    num_dish_types = DishType.objects.count()
    num_visits = request.session.get("visit_count", 1)
    request.session["visit_count"] = num_visits + 1

    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits,
    }

    return render(request, "kitchen/index.html", context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    template_name = "kitchen/dish_types_list.html"
    model = DishType
    paginate_by = 5
    context_object_name = "dish_type_list"
    queryset = DishType.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form_dish_types"] = DishTypeSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")

        if name:
            self.queryset = self.queryset.filter(
                name__icontains=name
            )
        return self.queryset


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.all().select_related("dish_type")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form_dishes"] = DishSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")

        if name:
            self.queryset = self.queryset.filter(
                name__icontains=name
            )
        return self.queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_types_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_types_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "kitchen/dish_types_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = DishForm
    model = Dish
    success_url = reverse_lazy("kitchen:dishes-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = DishForm
    model = Dish
    success_url = reverse_lazy("kitchen:dishes-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dishes-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5
    queryset = get_user_model().objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form_cooks"] = CookSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        username = self.request.GET.get("username")

        if username:
            self.queryset = self.queryset.filter(
                username__icontains=username
            )
        return self.queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = get_user_model().objects.prefetch_related("dishes__dish_type")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookForm


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cooks-list")


@login_required
def toggle_assign_to_dish(request, pk):
    user = get_user_model().objects.get(id=request.user.id)
    dish = Dish.objects.get(pk=pk)

    if user in dish.cooks.all():
        dish.cooks.remove(user)
    else:
        dish.cooks.add(user)
    return HttpResponseRedirect(reverse_lazy(
        "kitchen:dishes-detail",
        args=[pk])
    )
