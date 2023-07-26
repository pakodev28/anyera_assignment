from django_filters import rest_framework as filters

from pets.models import Pet


class PetSpeciesFilter(filters.FilterSet):
    """Filter for the Pet model based on the species field."""

    species = filters.CharFilter(field_name="species")

    class Meta:
        model = Pet
        fields = ["species"]
