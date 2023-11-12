from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Cook, Dish


class CookForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name"
        )


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Search by dish name.."}),
    )


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Search by username.."}),
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Search by name.."}),
    )
