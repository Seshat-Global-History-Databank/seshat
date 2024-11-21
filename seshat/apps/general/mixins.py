# mixins.py

class PolityIdMixin:
    """
    Mixin to add the get_initial method to a view that sets the initial value of the polity field.
    """
    def get_initial(self):
        """
        Get the initial value of the polity field from the query string.

        Returns:
            dict: The initial value of the polity field.
        """
        initial = super().get_initial()
        polity_id_x = self.request.GET.get('polity_id_x')
        other_polity_id_x = self.request.GET.get('other_polity_id_x')
        if polity_id_x:
            initial['polity'] = polity_id_x
        if other_polity_id_x:
            initial['other_polity'] = other_polity_id_x
        return initial

    