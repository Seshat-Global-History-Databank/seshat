from django_filters import rest_framework as django_filters


class SeshatCommonFilter:

    polity_name_contains = django_filters.CharFilter(
        field_name="polity__name", lookup_expr="icontains"
    )

    @classmethod
    def get_fields(cls):
        fields = cls.Meta.fields

        if "name" not in fields.keys():
            fields["name"] = ["exact", "icontains"]

        fields = dict(
            year_to=["range", "exact", "lte", "gte"],
            year_from=["range", "exact", "lte", "gte"],
            description=["icontains"],
            note=["icontains"],
            finalized=["exact"],
            created_date=["range", "date__exact", "date__lte", "date__gte"],
            modified_date=["range", "date__exact", "date__lte", "date__gte"],
            tag=["exact"],
            is_disputed=["exact"],
            is_uncertain=["exact"],
            expert_reviewed=["exact"],
            drb_reviewed=["exact"],
            polity__name=["icontains"],
            polity__polity_tag=["exact"],
            polity__home_nga__name=["icontains"],
            polity__home_nga__latitude=["range", "exact", "lte", "gte"],
            polity__home_nga__longitude=["range", "exact", "lte", "gte"],
            polity__home_seshat_region__mac_region__name=["exact", "icontains"],
            **fields
        )

        return fields
