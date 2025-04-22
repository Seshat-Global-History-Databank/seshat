from django import template
import re

from seshat.apps.rt.var_defs import swapped_dict

from seshat.apps.accounts.models import Seshat_Expert  # Update with the correct path to your Seshat_Expert model

register = template.Library()


@register.filter
def zip_lists(a, b):
    return zip(a, b)

@register.filter
def get_columns_with_value(instance, value):
    return instance.get_columns_with_value(value)

@register.filter
def get_columns_with_value_dic(instance, value):
    return instance.get_columns_with_value_dic(value)

@register.filter
def replace_underscore_and_capitalize(value):
    rt_dic = {
        'Theo_sync_dif_rel': 'Theological Syncretism of Different Religions',
        'Sync_rel_pra_ind_beli': 'Syncretism of Religious Practices at the Level of Individual Believers',
        'Gov_vio_freq_rel_grp': 'Frequency of Governmental Violence Against Religious Groups',
        'Gov_res_pub_wor': 'Government Restrictions on Public Worship',
        'Gov_res_pub_pros': 'Government Restrictions on Public Proselytizing',
        'Gov_res_conv': 'Government Restrictions on Conversion',
        'Gov_press_conv': 'Government Pressure to Convert',
        'Gov_res_prop_own_for_rel_grp': 'Government Restrictions on Property Ownership for Adherents of Any Religious Group',
        'Tax_rel_adh_act_ins': 'Taxes Based on Religious Adherence or on Religious Activities and Institutions',
        'Gov_obl_rel_grp_ofc_reco': 'Governmental Obligations for Religious Groups to Apply for Official Recognition',
        'Gov_res_cons_rel_buil': 'Government Restrictions on Construction of Religious Buildings',
        'Gov_res_rel_edu': 'Government Restrictions on Religious Education',
        'Gov_res_cir_rel_lit': 'Government Restrictions on Circulation of Religious Literature',
        'Gov_dis_rel_grp_occ_fun': 'Government Discrimination Against Religious Groups Taking up Certain Occupations or Functions',
        'Soc_vio_freq_rel_grp': 'Frequency of Societal Violence Against Religious Groups',
        'Soc_dis_rel_grp_occ_fun': 'Societal Discrimination Against Religious Groups Taking up Certain Occupations or Functions',
        'Gov_press_conv_for_aga': 'Societal Pressure to Convert or Against Conversion',    }
    if value in rt_dic:
        value = rt_dic[value]
    value = value.replace('_', ' ')
    return value.title()


@register.filter
def replace_underscore_and_capitalize_for_long_vars(value):
    if value in swapped_dict:
        new_value = swapped_dict[value]
        new_value = new_value.replace('_', ' ')
        return new_value.title()
    else:
        value = value.replace('_', ' ')
        return value.title()

@register.filter
def get_item_from_dic(dictionary, key):
    return dictionary.get(key)

@register.filter
def unique_descriptions(values):
    unique_set = set()
    result = []
    
    for value in values:
        if value.description and value.description not in unique_set:
            unique_set.add(value.description)
            result.append(value.description)
    
    return result

@register.filter
def min_max_years(values):
    if not values:
        return ""

    min_year = min(value.year_from for value in values)
    max_year = max(value.year_to for value in values)

    return f"{min_year} - {max_year}"

@register.filter
def beginswith(value, arg):
    return value.startswith(arg)

@register.filter
def username_from_email(email):
    return email.split('@')[0]


# @register.filter
# def make_references_look_nicer(value):
#     value = value.replace("'", "&rsquo;")
#     pattern = r'§REF§(.*?)§REF§'
#     replacement = r"""<sup>
#         <span type="button"  tabindex="0" data-bs-toggle="popover" data-bs-html="true" data-bs-trigger="focus" data-bs-content='<b>Citation: </b>\1'><i class="fa-solid fa-message fa-lg text-teal"></i>
#         </span>
#     </sup>
#     """
#     #replacement = r'XYZ_\1_XYZ'
#     new_string = re.sub(pattern, replacement, value)
#     return new_string



# @register.filter
# def make_references_look_nicer(value):
#     value = value.replace("'", "&rsquo;")
#     pattern = r'§REF§(.*?)§REF§'
#     replacement = r"""<sup>
#         <span type="button" tabindex="0" data-bs-toggle="popover" data-bs-html="true" data-bs-trigger="focus" data-bs-content='<b>Citation:</b> \1'><i class="fa-solid fa-message fa-lg text-teal"></i>
#         </span>
#     </sup>
#     """
#     # replacement = r'XYZ_\1_XYZ'
#     new_string = re.sub(pattern, replacement, value)
    
#     # Collect all the values that go into the <sup> tag
#     references = re.findall(pattern, value)
    
#     # Add the collected references at the end of the string in separate <p> tags with the color red
#     if references:
#         reference_tags = '\n'.join([f'<p style="color: red;">* {reference}</p>' for reference in references])
#         new_string += reference_tags

#     return new_string


# @register.filter
# def make_references_look_nicer(value):
#     value = value.replace("'", "&rsquo;")
#     pattern = r'§REF§(.*?)§REF§'
#     replacement = r"""<sup class="fs-6 text-secondary">[{ref_num}]
#     </sup>
#     """
#     new_string = value
#     references = re.findall(pattern, value)
    
#     # Dictionary to store unique reference numbers for each reference
#     reference_numbers = {}
    
#     # Assign a unique reference number to each reference in the order they appear
#     for index, reference in enumerate(references):
#         if reference not in reference_numbers:
#             reference_numbers[reference] = len(reference_numbers) + 1
            
#         ref_num = reference_numbers[reference]
#         sup_tag = replacement.format(ref_num=ref_num)
#         new_string = new_string.replace(f'§REF§{reference}§REF§', sup_tag, 1)
    
#     # Add the collected references at the end of the string in separate <p> tags with the color red

#     if reference_numbers:
#         new_string += "<h6 class='pt-3 pb-0'># Reference(s): </h6>"
#         reference_tags = '\n'.join([f'<p class="p-0 m-0 fs-6 text-secondary">[{ref_num}]: {reference}</p>' for reference, ref_num in reference_numbers.items()])
#         new_string += reference_tags

#     return new_string


# @register.filter
# def make_references_look_nicer(value):
#     value = value.replace("'", "&rsquo;")
#     pattern = r'§REF§(.*?)§REF§'
#     replacement = r"""<sup>
#         <a href="#{ref_id}">{ref_num}</a>
#         <span type="button" tabindex="0" data-bs-toggle="popover" data-bs-html="true" data-bs-trigger="focus" data-bs-content='<b>Citation:</b> \1'><i class="fa-solid fa-message fa-lg text-teal"></i>
#         </span>
#     </sup>
#     """
#     new_string = value
#     references = re.findall(pattern, value)
    
#     # Dictionary to store unique reference numbers and their corresponding unique identifiers
#     reference_data = {}
    
#     # Assign a unique reference number and identifier to each reference in the order they appear
#     for index, reference in enumerate(references):
#         if reference not in reference_data:
#             reference_data[reference] = {
#                 'ref_num': len(reference_data) + 1,
#                 'ref_id': f'ref_{len(reference_data) + 1}'
#             }
        
#         data = reference_data[reference]
#         sup_tag = replacement.format(ref_num=data['ref_num'], ref_id=data['ref_id'])
#         new_string = new_string.replace(f'§REF§{reference}§REF§', sup_tag, 1)
    
#     # Add the collected references at the end of the string in separate <p> tags with the color red
#     if reference_data:
#         reference_tags = '\n'.join([f'<p id="{data["ref_id"]}" style="color: red;">[{data["ref_num"]}] {reference}</p>' for reference, data in reference_data.items()])
#         new_string += reference_tags

#     return new_string


import uuid

@register.filter
def make_references_look_nicer(value):
    value = value.replace("'", "&rsquo;").replace("\n", "MJD_BNM_NEWLINE_TAG_XYZ")
    pattern = r'§REF§(.*?)§REF§'
    replacement = r"""<sup class="fw-bold" id="sup_{ref_id}">
        <a href="#{ref_id}">[{ref_num}]</a>
    </sup>
    """
    new_string = value
    references = re.findall(pattern, value)
    
    # Dictionary to store unique reference numbers and their corresponding unique identifiers
    reference_data = {}
    
    # Assign a unique reference number and identifier to each reference in the order they appear
    for index, reference in enumerate(references):
        if reference not in reference_data:
            ref_num = len(reference_data) + 1
            ref_id = f"ref_{ref_num}_{str(uuid.uuid4())[:8]}"
            reference_data[reference] = {
                'ref_num': ref_num,
                'ref_id': ref_id
            }
        
        data = reference_data[reference]
        sup_tag = replacement.format(ref_num=data['ref_num'], ref_id=data['ref_id'])
        new_string = new_string.replace(f'§REF§{reference}§REF§', sup_tag, 1)
    
    # Add the collected references at the end of the string in separate <p> tags with the color red
    if reference_data:
        #new_string += "<h6 class='pt-1 pb-0 text-secondary'><i class='fa-solid fa-bookmark fa-xs '></i> Reference(s): </h6>"
        reference_tags = '\n'.join([f'<p id="{data["ref_id"]}" class="px-0 pt-1 pb-0  m-0 text-secondary"><span class="fw-bold">  <a href="#sup_{data["ref_id"]}">[{data["ref_num"]}]</a></span>: <span>{reference.replace("MJD_BNM_NEWLINE_TAG_XYZ", " ")}</span> </p>' for reference, data in reference_data.items()])
        new_string += reference_tags

    paargraphed_new_str = new_string.replace("MJD_BNM_NEWLINE_TAG_XYZ", "<br>")
    return paargraphed_new_str


@register.filter
def give_me_a_color(value):
    light_colors = [
        '#b86354',  # Darker red tone of #e6b8af
        '#cc6666',  # Darker red tone of #f4cccc
        '#d9a065',  # Darker orange tone of #fce5cd
        '#d6b656',  # Darker yellow tone of #fff2cc
        '#94b373',  # Darker green tone of #d9ead3
        '#6c8488',  # Darker blue-gray tone of #d0e0e3
        '#6a92d1',  # Darker blue tone of #c9daf8
        '#7292a6',  # Darker gray-blue tone of #cfe2f3
        '#8f78c3',  # Darker purple tone of #d9d2e9
        '#c35b7f',  # Darker pink-purple tone of #ead1dc
        '#a93d2b',  # Darker orange-red tone of #dd7e6b
        '#b85454',  # Darker red tone of #ea9999
        '#e09957',  # Darker orange tone of #f9cb9c
        '#d7b942',  # Darker yellow tone of #ffe599
        '#79a659',  # Darker green tone of #b6d7a8
        '#4e7476',  # Darker teal tone of #a2c4c9
        '#4a7bbf',  # Darker blue tone of #a4c2f4
        '#4e92b8',  # Darker blue tone of #9fc5e8
        '#6c5ba3',  # Darker purple tone of #b4a7d6
        '#a35f88',  # Darker pink-purple tone of #d5a6bd
        '#892f15',  # Darker red tone of #cc4125
        '#a73f3f',  # Darker red tone of #e06666
        '#b86b35',  # Darker orange tone of #f6b26b
        '#d6ac34',  # Darker yellow tone of #ffd966
        '#5d8e52',  # Darker green tone of #93c47d
        '#43696d',  # Darker teal tone of #76a5af
        '#3d64b3',  # Darker blue tone of #6d9eeb
        '#4176a5',  # Darker blue tone of #6fa8dc
        '#654da6',  # Darker purple tone of #8e7cc3
        '#8f5477',  # Darker pink tone of #c27ba0
    ]


    # light_colors = [
    # '#e6b8af',
    # '#f4cccc',
    # '#fce5cd',
    # '#fff2cc',
    # '#d9ead3',
    # '#d0e0e3',
    # '#c9daf8',
    # '#cfe2f3',
    # '#d9d2e9',
    # '#ead1dc',
    # '#dd7e6b',
    # '#ea9999',
    # '#f9cb9c',
    # '#ffe599',
    # '#b6d7a8',
    # '#a2c4c9',
    # '#a4c2f4',
    # '#9fc5e8',
    # '#b4a7d6',
    # '#d5a6bd',
    # '#cc4125',
    # '#e06666',
    # '#f6b26b',
    # '#ffd966',
    # '#93c47d',
    # '#76a5af',
    # '#6d9eeb',
    # '#6fa8dc',
    # '#8e7cc3',
    # '#c27ba0',
    # ]

    index = int(value) % 30

    return light_colors[index]


@register.filter
def in_group(user, group_name):
    """
    Checks if a user is in a given group.
    """
    if user.is_authenticated:
        return user.groups.filter(name=group_name).exists()
    return False


@register.filter
def is_user_real(user):
    """
    Check if the username has an underscore and if the part after the underscore
    matches the domain part of the email.

    Args:
        username (str): The username to check.
        email (str): The email to check against.

    Returns:
        bool: True if the username is valid, False otherwise.
    """
    if "_" not in user.username or user.last_login:
        return True  # No underscore in username

    # Split username and email
    username_part_2 = user.username.split("_")[1]
    email_domain = user.email.split("@")[1]  # Get the part after '@' in the email

    # if email_domain.startswith(username_part_2):
    #     return False
    # Compare second part of username to email domain
    return username_part_2 != email_domain.split(".")[0]

@register.filter
def textincludes(value, arg):
    """Check if a string includes a given substring."""
    if isinstance(value, str):
        return arg in value
    return False

@register.filter
def get_seshat_expert(user):
    """
    Custom filter to get the Seshat_Expert object associated with a user.
    """
    try:
        return Seshat_Expert.objects.get(user=user).id
    except Seshat_Expert.DoesNotExist:
        return None
    

@register.simple_tag(takes_context=True)
def track_last(context, current_name):
    """Keeps track of the last clean_name_spaced and appends '_copy' if repeated."""
    if 'last_clean_name' not in context:
        context['last_clean_name'] = None

    if context['last_clean_name'] == current_name:
        result = f'<span style="color: gray;">{current_name}</span>'
    else:
        result = current_name

    context['last_clean_name'] = current_name  # Update the last seen name
    return result


@register.inclusion_tag('core/partials/_progress_row.html')
def render_progress_row(freq_data, key, label, title, color_class="", bg_color="", text_class="text-dark"):
    value = freq_data.get(key, 0)
    total = freq_data.get("pol_count", 1)
    percent = round((value / total) * 100) if total else 0
    return {
        "value": value,
        "total": total,
        "percent": percent,
        "label": label,
        "title": title,
        "color_class": color_class,
        "bg_color": bg_color,
        "text_class": text_class,
    }