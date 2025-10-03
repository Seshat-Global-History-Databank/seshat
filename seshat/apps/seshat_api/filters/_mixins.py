from django_filters import rest_framework as django_filters


class SeshatCommonFilter:
    # <> polity
    # <>+ curator
    # <> comment
    # <> private_comment

    # TODO: can we remove fields that are not intended for public view?

    polity_name_contains = django_filters.CharFilter(
        field_name="polity__name", lookup_expr="icontains"
    )

    @classmethod
    def get_fields(cls):
        fields = cls.Meta.fields

        #if "name" not in fields.keys():
        #    fields["name"] = ["exact", "icontains"]

        fields = dict(
            **fields,
            year_from=["range",],
            year_to=["range",],
            #description=["icontains"],
            #note=["icontains"],
            #finalized=["exact"],
            #created_date=["range", "date__exact", "date__lte", "date__gte"],
            #modified_date=["range", "date__exact", "date__lte", "date__gte"],
            tag=["exact"],
            is_disputed=["exact"],
            is_uncertain=["exact"],
            #expert_reviewed=["exact"],
            #drb_reviewed=["exact"],
            polity__new_name=["icontains"],
            polity__name=["exact"],
            polity__long_name=["icontains"],
            #polity__polity_tag=["exact"],
            #polity__home_nga__name=["icontains"],
            #polity__home_nga__latitude=["range", "exact", "lte", "gte"],
            #polity__home_nga__longitude=["range", "exact", "lte", "gte"],
            #polity__home_seshat_region__mac_region__name=["exact", "icontains"],
        )

        return fields
