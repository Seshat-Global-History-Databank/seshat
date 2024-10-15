seshat.utils.utils
==================

.. py:module:: seshat.utils.utils


Attributes
----------

.. autoapisummary::

   seshat.utils.utils.vars_dic_for_utils


Functions
---------

.. autoapisummary::

   seshat.utils.utils.adder
   seshat.utils.utils.dic_of_all_vars
   seshat.utils.utils.dic_of_all_vars_in_sections
   seshat.utils.utils.dic_of_all_vars_with_varhier
   seshat.utils.utils.get_all_crisis_cases_data_for_a_polity
   seshat.utils.utils.get_all_data_for_a_polity
   seshat.utils.utils.get_all_general_data_for_a_polity
   seshat.utils.utils.get_all_general_data_for_a_polity_old
   seshat.utils.utils.get_all_power_transitions_data_for_a_polity
   seshat.utils.utils.get_all_rt_data_for_a_polity
   seshat.utils.utils.get_all_sc_data_for_a_polity
   seshat.utils.utils.get_all_wf_data_for_a_polity
   seshat.utils.utils.get_all_wf_data_for_a_polity_old
   seshat.utils.utils.give_polity_app_data
   seshat.utils.utils.list_of_all_Polities
   seshat.utils.utils.polity_detail_data_collector
   seshat.utils.utils.qing_vars_links_creator
   seshat.utils.utils.section_dic_extractor
   seshat.utils.utils.subsection_dic_extractor
   seshat.utils.utils.test_for_varhier_dic


Module Contents
---------------

.. py:function:: adder(a, b)

   Adds two numbers together.

   :param a: The first number to be added.
   :type a: int
   :param b: The second number to be added.
   :type b: int

   :returns: The sum of the two numbers.
   :rtype: int


.. py:function:: dic_of_all_vars()

   Returns a dictionary of all variables in the database.

   :returns: A dictionary of all variables.
   :rtype: dict


.. py:function:: dic_of_all_vars_in_sections()

   Returns a dictionary of all variables in the database. This dictionary is
   structured in a way that it can be used to generate a hierarchical
   representation of the variables.

   .. note::

      This function does not seem to be used in the current version of the
      application.

   :returns: A dictionary of all variables.
   :rtype: dict


.. py:function:: dic_of_all_vars_with_varhier()

   Returns a dictionary of all variables in the database. This dictionary is
   structured in a way that it can be used to generate a hierarchical
   representation of the variables.

   :returns: A dictionary of all variables.
   :rtype: dict


.. py:function:: get_all_crisis_cases_data_for_a_polity(polity_id)

   Gets all data for a given polity ID from the "crisisdb" app.

   :param polity_id: The ID of the polity.
   :type polity_id: int

   :returns: A dictionary of all data for the polity.
   :rtype: dict


.. py:function:: get_all_data_for_a_polity(polity_id, db_name)

   Gets all data for a given polity ID.

   :param polity_id: The ID of the polity.
   :type polity_id: int
   :param db_name: The name of the database.
   :type db_name: str

   :returns: A dictionary of all data for the polity.
   :rtype: dict


.. py:function:: get_all_general_data_for_a_polity(polity_id)

   Gets all data for a given polity ID from the "general" app.

   :param polity_id: The ID of the polity.
   :type polity_id: int

   :returns: A tuple containing a dictionary of all data for the polity and a boolean value indicating whether the polity has any data.
   :rtype: tuple


.. py:function:: get_all_general_data_for_a_polity_old(polity_id)

   Gets all general data for a given polity ID.

   :private:

   .. note:: This function is not used in the current version of the application.

   :param polity_id: The ID of the polity.
   :type polity_id: int

   :returns: A dictionary of all general data for the polity.
   :rtype: dict


.. py:function:: get_all_power_transitions_data_for_a_polity(polity_id)

   Gets all data for a given polity ID from the "rt" app.

   :param polity_id: The ID of the polity.
   :type polity_id: int

   :returns: A dictionary of all data for the polity.
   :rtype: dict


.. py:function:: get_all_rt_data_for_a_polity(polity_id)

   Gets all data for a given polity ID from the "rt" app.

   :param polity_id: The ID of the polity.
   :type polity_id: int

   :returns: A tuple containing a dictionary of all data for the polity and a boolean value indicating whether the polity has any data.
   :rtype: tuple


.. py:function:: get_all_sc_data_for_a_polity(polity_id)

   Gets all data for a given polity ID from the "sc" app.

   :param polity_id: The ID of the polity.
   :type polity_id: int

   :returns: A tuple containing a dictionary of all data for the polity and a boolean value indicating whether the polity has any data.
   :rtype: tuple


.. py:function:: get_all_wf_data_for_a_polity(polity_id)

   Gets all data for a given polity ID from the "wf" app.

   :param polity_id: The ID of the polity.
   :type polity_id: int

   :returns: A tuple containing a dictionary of all data for the polity and a boolean value indicating whether the polity has any data.
   :rtype: tuple


.. py:function:: get_all_wf_data_for_a_polity_old(polity_id)

   Gets all data for a given polity ID from the "wf" app.

   :private:

   .. note:: This function is not used in the current version of the application.

   :param polity_id: The ID of the polity.
   :type polity_id: int

   :returns: A dictionary of all data for the polity.
   :rtype: dict


.. py:function:: give_polity_app_data()

.. py:function:: list_of_all_Polities()

   Returns a list of all polities in the database.

   :returns: A list of all polity names.
   :rtype: list


.. py:function:: polity_detail_data_collector(polity_id)

.. py:function:: qing_vars_links_creator(vars_dic_for_here)

   Creates a dictionary of all variables in the database. This dictionary is
   structured in a way that it can be used to generate a hierarchical
   representation of the variables.

   :param vars_dic_for_here: A dictionary of all variables.
   :type vars_dic_for_here: dict

   :returns: A dictionary of all variables.
   :rtype: dict


.. py:function:: section_dic_extractor()

   Extracts a dictionary of all sections in the database.

   :returns: A dictionary of all sections.
   :rtype: dict


.. py:function:: subsection_dic_extractor()

   Extracts a dictionary of all subsections in the database.

   :returns: A dictionary of all subsections.
   :rtype: dict


.. py:function:: test_for_varhier_dic()

   Extracts a dictionary of all variables in the database. This dictionary is
   structured in a way that it can be used to generate a hierarchical
   representation of the variables.

   :returns: A dictionary of all variables.
   :rtype: dict


.. py:data:: vars_dic_for_utils

   vars_dic_for_utils is a dictionary that contains the definitions of all the variables in the database. It is used to generate the models and views for the variables. It is a dictionary of dictionaries, where the key is the name of the variable and the value is a dictionary that contains the following keys:
   - notes: A description of the variable.
   - main_desc: The main description of the variable.
   - main_desc_source: The source of the main description.
   - cols: The number of columns in the variable.
   - section: The section of the variable.
   - subsection: The subsection of the variable.
   - null_meaning: The meaning of a null value in the variable.
   - col1: A dictionary that contains the definition of the first column of the variable. It contains the following keys:
       - dtype: The data type of the column.
       - varname: The name of the column.
       - var_exp: The explanation of the column.
       - var_exp_source: The source of the explanation.
       - units: The units of the column.
       - min: The minimum value of the column.
       - max: The maximum value of the column.
       - scale: The scale of the column.
       - decimal_places: The number of decimal places in the column.
       - max_digits: The maximum number of digits in the column.
   - col2: A dictionary that contains the definition of the second column of the variable. It contains the same keys as col1.
   - col3: A dictionary that contains the definition of the third column of the variable. It contains the same keys as col1.
   - col4: A dictionary that contains the definition of the fourth column of the variable. It contains the same keys as col1.
   - col5: A dictionary that contains the definition of the fifth column of the variable. It contains the same keys as col1.
   - col6: A dictionary that contains the definition of the sixth column of the variable. It contains the same keys as col1.

