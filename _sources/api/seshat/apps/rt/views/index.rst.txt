seshat.apps.rt.views
====================

.. py:module:: seshat.apps.rt.views


Functions
---------

.. autoapisummary::

   seshat.apps.rt.views.confirm_delete_view
   seshat.apps.rt.views.delete_object_view
   seshat.apps.rt.views.download_csv_all_rt
   seshat.apps.rt.views.download_csv_government_restrictions
   seshat.apps.rt.views.download_csv_religious_landscape
   seshat.apps.rt.views.download_csv_societal_restrictions
   seshat.apps.rt.views.dynamic_create_view
   seshat.apps.rt.views.dynamic_detail_view
   seshat.apps.rt.views.dynamic_update_view
   seshat.apps.rt.views.generic_download
   seshat.apps.rt.views.generic_list_view
   seshat.apps.rt.views.generic_metadata_download
   seshat.apps.rt.views.get_ref_options
   seshat.apps.rt.views.has_add_capital_permission
   seshat.apps.rt.views.rtvars
   seshat.apps.rt.views.show_problematic_rt_data_table


Module Contents
---------------

.. py:function:: confirm_delete_view(request, model_class, pk, var_name)

   View function to confirm the deletion of an object.

   .. note::

      This function is a generic view function that can be used for any model.
      The access to this view is restricted to users with the 'core.add_capital' permission.

   :param request: The request object used to generate this page.
   :type request: HttpRequest
   :param model_class: The model class of the object.
   :type model_class: Model
   :param pk: The primary key of the object.
   :type pk: int
   :param var_name: The variable name.
   :type var_name: str

   :returns: The response object that contains the rendered confirmation page.
   :rtype: HttpResponse


.. py:function:: delete_object_view(request, model_class, pk, var_name)

   View function to delete an object.

   .. note::

      This function is a generic view function that can be used for any model.
      The access to this view is restricted to users with the 'core.add_capital' permission.

   :param request: The request object used to generate this page.
   :type request: HttpRequest
   :param model_class: The model class of the object.
   :type model_class: Model
   :param pk: The primary key of the object.
   :type pk: int
   :param var_name: The variable name.
   :type var_name: str

   :returns: The response object that contains the rendered confirmation page.
   :rtype: HttpResponse


.. py:function:: download_csv_all_rt(request)

   Download all data for all models in the RT app.

   .. note:: The access to this view is restricted to users with the 'core.view_capital' permission.

   :param request: The request object used to generate this page.
   :type request: HttpRequest

   :returns: The response object that contains the CSV file.
   :rtype: HttpResponse


.. py:function:: download_csv_government_restrictions(request)

   Download all data for the Government Restrictions model in the RT app.

   .. note:: The access to this view is restricted to users with the 'core.view_capital' permission.

   :param request: The request object used to generate this page.
   :type request: HttpRequest

   :returns: The response object that contains the CSV file.
   :rtype: HttpResponse


.. py:function:: download_csv_religious_landscape(request)

   Download all data for the Religious Landscape model in the RT app.

   .. note:: The access to this view is restricted to users with the 'core.view_capital' permission.

   :param request: The request object used to generate this page.
   :type request: HttpRequest

   :returns: The response object that contains the CSV file.
   :rtype: HttpResponse


.. py:function:: download_csv_societal_restrictions(request)

   Download all data for the Societal Restrictions model in the RT app.

   .. note:: The access to this view is restricted to users with the 'core.view_capital' permission.

   :param request: The request object used to generate this page.
   :type request: HttpRequest

   :returns: The response object that contains the CSV file.
   :rtype: HttpResponse


.. py:function:: dynamic_create_view(request, form_class, x_name, myvar, my_exp, var_section, var_subsection)

   View function for the create page of a model.

   .. note::

      This function is a generic view function that can be used for any model.
      The access to this view is restricted to users with the 'core.add_capital' permission.

   :param request: The request object used to generate this page.
   :type request: HttpRequest
   :param form_class: The form class used to create the object.
   :type form_class: Form
   :param x_name: The variable name.
   :type x_name: str
   :param myvar: The variable name.
   :type myvar: str
   :param my_exp: The variable explanation.
   :type my_exp: str
   :param var_section: The section name.
   :type var_section: str
   :param var_subsection: The subsection name.
   :type var_subsection: str

   :returns: The response object that contains the rendered create page.
   :rtype: HttpResponse


.. py:function:: dynamic_detail_view(request, pk, model_class, myvar, var_name_display)

   View function for the detail page of a model.

   .. note::

      This function is a generic view function that can be used for any model.
      The access to this view is restricted to users with the 'core.add_capital' permission.

   :param request: The request object used to generate this page.
   :type request: HttpRequest
   :param pk: The primary key of the object.
   :type pk: int
   :param model_class: The model class of the object.
   :type model_class: Model
   :param myvar: The variable name.
   :type myvar: str
   :param var_name_display: The variable name to display.
   :type var_name_display: str

   :returns: The response object that contains the rendered detail page.
   :rtype: HttpResponse


.. py:function:: dynamic_update_view(request, object_id, form_class, model_class, x_name, myvar, my_exp, var_section, var_subsection, delete_url_name)

   View function for the update page of a model.

   .. note::

      This function is a generic view function that can be used for any model.
      The access to this view is restricted to users with the 'core.add_capital' permission.

   :param request: The request object used to generate this page.
   :type request: HttpRequest
   :param object_id: The primary key of the object.
   :type object_id: int
   :param form_class: The form class used to update the object.
   :type form_class: Form
   :param model_class: The model class of the object.
   :type model_class: Model
   :param x_name: The variable name.
   :type x_name: str
   :param myvar: The variable name.
   :type myvar: str
   :param my_exp: The variable explanation.
   :type my_exp: str
   :param var_section: The section name.
   :type var_section: str
   :param var_subsection: The subsection name.
   :type var_subsection: str
   :param delete_url_name: The URL name for deleting the object.
   :type delete_url_name: str

   :returns: The response object that contains the rendered update page.
   :rtype: HttpResponse


.. py:function:: generic_download(request, model_class, var_name)

   Download all data for a given model.

   .. note::

      This function is a generic view function that can be used for any model.
      The access to this view is restricted to users with the 'core.add_capital' permission.

   :param request: The request object used to generate this page.
   :type request: HttpRequest
   :param model_class: The model class of the object.
   :type model_class: Model
   :param var_name: The variable name.
   :type var_name: str

   :returns: The response object that contains the CSV file.
   :rtype: HttpResponse


.. py:function:: generic_list_view(request, model_class, var_name, var_name_display, var_section, var_subsection, var_main_desc)

   View function for the list page of a model.

   .. note::

      This function is a generic view function that can be used for any model.
      The access to this view is restricted to users with the 'core.add_capital' permission.

   :param request: The request object used to generate this page.
   :type request: HttpRequest
   :param model_class: The model class of the object.
   :type model_class: Model
   :param var_name: The variable name.
   :type var_name: str
   :param var_name_display: The variable name to display.
   :type var_name_display: str
   :param var_section: The section name.
   :type var_section: str
   :param var_subsection: The subsection name.
   :type var_subsection: str
   :param var_main_desc: The main description.
   :type var_main_desc: str

   :returns: The response object that contains the rendered list page.
   :rtype: HttpResponse


.. py:function:: generic_metadata_download(request, var_name, var_name_display, var_section, var_subsection, var_main_desc)

   Download metadata for a given model.

   .. note::

      This function is a generic view function that can be used for any model.
      This view is only accessible to users with the 'add_capital' permission.

   :param request: The request object used to generate this page.
   :type request: HttpRequest
   :param var_name: The variable name.
   :type var_name: str
   :param var_name_display: The variable name to display.
   :type var_name_display: str
   :param var_section: The section name.
   :type var_section: str
   :param var_subsection: The subsection name.
   :type var_subsection: str
   :param var_main_desc: The main description.
   :type var_main_desc: str

   :returns: The response object that contains the CSV file.
   :rtype: HttpResponse


.. py:function:: get_ref_options(request)

.. py:function:: has_add_capital_permission(user)

   Check if the user has the 'core.add_capital' permission.

   .. note:: TODO This is built-in functionality in Django. You can use the built-in permission_required decorator instead.

   :param user: The user object.
   :type user: User

   :returns: True if the user has the 'core.add_capital' permission, False otherwise.
   :rtype: bool


.. py:function:: rtvars(request)

   View function for the RT variables page.

   :param request: The request object used to generate this page.
   :type request: HttpRequest

   :returns: The response object that contains the rendered RT variables page.
   :rtype: HttpResponse


.. py:function:: show_problematic_rt_data_table(request)

   View that shows a table of problematic data in the RT app.

   .. note:: The access to this view is restricted to users with the 'core.view_capital' permission.

   :param request: The request object used to generate this page.
   :type request: HttpRequest

   :returns: The response object that contains the rendered problematic data table.
   :rtype: HttpResponse


