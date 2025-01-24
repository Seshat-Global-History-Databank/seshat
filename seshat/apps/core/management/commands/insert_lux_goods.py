from django.core.management.base import BaseCommand
from django.db import connection
from django.apps import apps

from seshat.apps.core.models import Polity, ScpThroughCtn, Reference, Citation, Seshat_Expert, SeshatCommentPart, SeshatComment


from seshat.apps.general.models import Polity_expert, Polity_original_name, Polity_alternative_name
from seshat.apps.ec.models import Lux_precious_metal, Luxury_fabrics, Luxury_manufactured_goods, Luxury_spices_incense_and_dyes, Luxury_drink_alcohol, Luxury_glass_goods, Lux_fine_ceramic_wares, Lux_precious_stone, Lux_statuary, Luxury_food, Other_luxury_personal_items

from seshat.apps.ec.final_dic_insert import my_final_dic_with_citations_stripped



class Command(BaseCommand):
    help = "Update curators table with coded records based on polity experts for all general app models"

    def handle(self, *args, **kwargs):
        self.stdout.write("Fetching polities and experts...")  

        unique_polity_new_ids = Polity.objects.values_list('new_name', flat=True).distinct()

        # Convert the queryset to a list (if needed)
        unique_polity_new_ids_list = list(unique_polity_new_ids)

        for pol_var_tuple, coded_cols in my_final_dic_with_citations_stripped.items():
            polity_new_id, var_name = pol_var_tuple
            print(polity_new_id)
            pol_maps = {
            'af_ghurid_principality' : 'af_ghur_principality',
            'bd_bengal_sul' : 'bd_bengal_sultanate',
            'bd_nawabs_bengal': 'bd_nawabs_of_bengal',
            'eg_ayyubid_sul': 'eg_ayyubid_sultanate',
            'eg_mamluk_sul_3': 'eg_mamluk_sultanate_3',
            'id_mataram_sul': 'id_mataram_k',
            'in_delhi_sul': 'in_delhi_sultanate',
            'in_pandya_emp_222': 'in_pandya_emp_3',
            'in_sena_dyn': 'bd_sena_dyn',
            'in_vanga_dyn': 'in_vanga_k',
            'ma_saadi_sul': 'ma_saadi_sultanate',
            'no_norway_k': 'no_norway_k_2',
            # Problematic
            'rw_rwanda_k_1': 'Early Niynginya',
            'rw_rwanda_k_2': 'Early Niynginya',
            'sl_jaffna_k': 'sl_jaffa_k',
            'sl_polonnaruva_k': 'sl_polonnaruva',
            'so_adal_sul': 'so_adal_sultanate',
            'so_ajuran_sul': 'so_ajuran_sultanate',
            'so_geledi_sul': 'so_geledi_sultanate',
            'so_isaaq_sul': 'so_isaaq_sultanate',
            'so_majeerteen_sul': 'so_majeerteen_sultanate',
            'so_tunni_sul': 'so_tunni_sultanate',
            'tz_buhaya_k': 'tz_buhayo_k',
            'us_hawaii_kamehameha_k': 'us_kamehameha_k',
            # other polity
            'cn_later_jin_dyn': 'cn_later_great_jin',
            'th_ayutthaia': 'th_ayutthaya',
            'om_busaidid_imamate': 'om_busaidi_imamate_1',
            'eg_fatimid_cal': 'tn_fatimid_cal',
            'cn_eastern_jin': 'cn_eastern_jin_dyn',
            'in_satahavana_emp': 'in_satavahana_emp',
            'tr_roman_principate': 'tr_roman_dominate',
            'tr_ottoman_emp_5': 'tr_ottoman_emp_4_copy',
            'eg_mamluk_sul_2': 'eg_mamluk_sultanate_2',
            'tr_ottoman_em_p_2': 'tr_ottoman_emp_2',
            'es_habsburg_emp': 'es_spanish_emp_1',
            'es_habsburg_emp_1': 'es_spanish_emp_2',
            'ko_joseon_dyn': 'kr_joseon',
            'cn_qing_2': 'cn_qing_dyn_2',
            'nl_dutch_empt_1': 'nl_dutch_emp_1',
            'eg_mamluk_sul_1': 'eg_mamluk_sultanate_1',
            'es_habsb_emp_1': 'es_spanish_emp_1',
            'it_venetian_republic_4': 'it_venetian_rep_4',
            'Us_hawaii_3': 'us_hawaii_3',
            'gb_east_india_co': 'in_east_india_co',
            }

            var_to_model = {
            'precious metal': Lux_precious_metal,
            'luxury fabrics': Luxury_fabrics,
            'luxury manufactured goods': Luxury_manufactured_goods,
            'luxury spices incense and dyes': Luxury_spices_incense_and_dyes,
            'Luxury spices incense and dyes': Luxury_spices_incense_and_dyes,
            'luxury drink/alcohol': Luxury_drink_alcohol,
            'luxury glass goods': Luxury_glass_goods,
            'fine ceramic wares': Lux_fine_ceramic_wares,
            'precious stone': Lux_precious_stone,
            'statuary': Lux_statuary,
            'luxury food': Luxury_food,
            'other luxury personal items': Other_luxury_personal_items,
            }
            try:
                my_polity = Polity.objects.get(new_name=polity_new_id)
            except:
                my_polity = Polity.objects.get(new_name=pol_maps[polity_new_id])

            big_father = SeshatComment.objects.create(text='')
            #my_polity = Polity.objects.get(new_name=polity_new_id)
            my_polity_id = my_polity.id

            #big_father = SeshatComment.objects.get(id=com_id)
            com_id = big_father.pk

            # break place_of_prov 
            all_places_str =[]
            all_places_pol = []
            if coded_cols['place_str']:
                all_places = coded_cols['place_str'].split(";")
            else:
                all_places = ''

            for a_p in all_places:
                if a_p == 'domestic':
                    if polity_new_id in unique_polity_new_ids_list:
                        all_places_pol.append(polity_new_id)
                    elif polity_new_id in pol_maps:
                        all_places_pol.append(pol_maps[polity_new_id])
                    else:
                        print("Baaaaaaaaaaaaaaaaaaaaaaaad: ", polity_new_id)
                elif a_p in unique_polity_new_ids_list and a_p not in all_places_pol:
                    all_places_pol.append(a_p)
                elif a_p in pol_maps and a_p not in all_places_pol:
                    all_places_pol.append(pol_maps[a_p])
                else:
                    all_places_str.append(a_p)

            # Str Locations Done
            if all_places_str:
                all_places_str_str = '; '.join(all_places_str)
            else:
                all_places_str_str = None



            #model_class = apps.get_model(app_label='ec', model_name=Lux_precious_metal)

            model_instance = var_to_model[var_name].objects.create(
                coded_value=coded_cols['coded_value'], 
                tag=coded_cols['tag'], 
                ruler_consumption=coded_cols['ruler'], 
                ruler_consumption_tag=coded_cols['ruler_tag'], 
                elite_consumption=coded_cols['elite'], 
                elite_consumption_tag=coded_cols['elite_tag'], 
                common_people_consumption=coded_cols['cp'], 
                common_people_consumption_tag=coded_cols['cp_tag'], 
                place_of_provenance_str=all_places_str_str, 
                polity_id=my_polity_id
                )
            # create model_instance
            model_instance.comment = big_father

            model_instance.save()


            # attach location pols.
            for pol_pol in all_places_pol:
                polity_to_be_added = Polity.objects.get(new_name=pol_pol)
                model_instance.place_of_provenance_pol.add(polity_to_be_added)

            seshat_expert_instance = Seshat_Expert.objects.get(id=2)


            for subcom_details in coded_cols['broken_comments']:
                comment_part = SeshatCommentPart.objects.create(
                                comment=big_father,
                                comment_part_text=subcom_details['sub_text'],
                                comment_order=subcom_details['sub_order'],
                                comment_curator=seshat_expert_instance # Could be werong
                            )
                comment_part.save()
                to_be_added = []

                my_zotero = subcom_details['my_ref']
                if my_zotero:
                    my_reference = Reference.objects.get(zotero_link=my_zotero)
                    if not subcom_details['my_pages']:
                        citation, created = Citation.objects.get_or_create(
                            ref=my_reference,
                            page_from=None,
                            page_to=None
                        )
                        to_be_added.append((citation, ''))

                    else:
                        for page_details in subcom_details['my_pages']:
                            # add citations
                            if page_details == (0, 0):
                                citation, created = Citation.objects.get_or_create(
                                ref=my_reference,
                                page_from=None,
                                page_to=None
                            )
                            else:
                                page_from = page_details[0]
                                page_to = page_details[1]
                                citation, created = Citation.objects.get_or_create(
                                ref=my_reference,
                                page_from=int(page_from),
                                page_to=int(page_to)
                            )

                            parent_pars_inserted = ''

                            to_be_added.append((citation, parent_pars_inserted))

                        
                    for item in to_be_added:
                        # Query for an existing row based on citation and SeshatCommentPart
                        scp_through_ctn, created = ScpThroughCtn.objects.get_or_create(
                            seshatcommentpart=comment_part,
                            citation=item[0],
                            defaults={'parent_paragraphs': item[1]}  # Set defaults including parent_paragraphs
                        )

                # If the row already exists, update its parent_paragraphs
                #if not created:
                #    scp_through_ctn.parent_paragraphs = item[1]
                #    scp_through_ctn.save()

        self.stdout.write("Fetching polities and experts...")

                
    
#     for subcom_details in coded_cols['broken_comments']:
        
#         zot_id = data.get('zot_id')
#         pages_tuples = data.get('pages_tuples', [])

#         if not zot_id:
#             print(f"Skipping entry due to missing zot_id or pages_tuples: {data}")
#             continue

#         try:
#             # Fetch the reference by zot_id
#             reference = Reference.objects.get(zotero_link=zot_id)
#         except Reference.DoesNotExist:
#             print(f"Reference with zotero_link={zot_id} not found. Skipping entry.")
#             continue

#         for page_from, page_to in pages_tuples:
#             # Check if a citation already exists
#             citation, created = Citation.objects.get_or_create(
#                 ref=reference,
#                 page_from=page_from,
#                 page_to=page_to
#             )

#             if created:
#                 print(f"Created new Citation: {citation}")
#             else:
#                 print(f"Found existing Citation: {citation}")

#             # Assign the citation to SubComment
#             #subcomment_instance = SeshatCommentPart.objects.create(comment_part_text='A subdescription text placeholder (to be edited)', comment=comment_instance, comment_curator= seshat_expert_instance,comment_order=1)

#             # comment_part = SeshatCommentPart.objects.create(
#             #             comment=comment_instance,
#             #             comment_part_text=comment_text,
#             #             comment_order=comment_order,
#             #             comment_curator=seshat_expert_instance 
#             #         )
#             #     comment_part = SeshatCommentPart.objects.get(id=pk)
#             # parent_comment_id = comment_part.comment.id
#             # subcomment_order = comment_part.comment_order
#             # parent_comment_part = SeshatComment.objects.get(id=parent_comment_id)
#             #########SeshatCommentPart.objects.filter(pk=instance.pk).update(comment_order=instance.comment_order)
#             ###########            
#             # 
#             comment_part = SeshatCommentPart.objects.create(
#                 comment=comment_instance,
#                 comment_part_text=comment_text,
#                 comment_order=comment_order,
#                 comment_curator=seshat_expert_instance 
#             )
#             comment_part.comment_citations.add(citation)
#             comment_part = SeshatCommentPart.objects.filter(comment_citations=None).first()  # Adjust filter as needed
#             if comment_part:
#                 # Add the citation to the comment_citations ManyToMany field
#                 comment_part.comment_citations.add(citation)
#                 comment_part.save()
#                 print(f"Assigned Citation {citation.id} to SeshatCommentPart {comment_part.id}")
#             else:
#                 print(f"No SeshatCommentPart available to assign Citation {citation.id}")

# ### Usage

# ```python
# # Example data
# data_dicts = [
#     {
#         'zot_id': 'SFWWGFG3',
#         'p_range': '390',
#         'step': '2',
#         'full': '...',
#         'pages_tuples': [(390, 390)],
#         'invalid_pages': None
#     },
#     {
#         'zot_id': 'INVALID_ZOT_ID',
#         'p_range': '391-393',
#         'step': '1',
#         'full': '...',
#         'pages_tuples': [(391, 393)],
#         'invalid_pages': None
#     }
# ]

# # Call the function
# process_references_and_citations(data_dicts)


# class Command(BaseCommand):
#     help = "Update curators table with coded records based on polity experts for all general app models"

#     def handle(self, *args, **kwargs):
#         self.stdout.write("Fetching polities and experts...")
        
#         # Fetch polity_id and expert mapping
#         polity_experts = Polity_expert.objects.all().values_list('polity_id', 'expert_id')
#         print("Polity Experts Mapping: ", polity_experts)

#         # Get all models in the 'general' app
#         general_models = apps.get_app_config('general').get_models()

#         for model in general_models:
#             if hasattr(model, 'curator') and hasattr(model, 'polity_id'):  # Ensure the model has required fields
#                 self.stdout.write(f"Processing model: {model.__name__}")

#                 for item in polity_experts:
#                     try:
#                         # Filter by polity_id
#                         main_objects = model.objects.filter(polity_id=item[0])

#                     except model.DoesNotExist:
#                         self.stdout.write(f"No matching object found in {model.__name__} for polity_id {item[0]}")
#                         continue

#                     # Get the expert
#                     try:
#                         new_curator = Seshat_Expert.objects.get(id=item[1])
#                     except Seshat_Expert.DoesNotExist:
#                         self.stdout.write(f"No expert found with ID {item[1]}")
#                         continue
#                     # Add the new curator to the ManyToManyField for all cases

#                     for main_object in main_objects:
#                         main_object.curator.add(new_curator)

#                         # Save the main object (optional since ManyToManyField updates are saved immediately)
#                         main_object.save()
#                         print("Yes")
#                     self.stdout.write(f"Added curator {new_curator} to {model.__name__} with polity_id {item[0]}")

#         self.stdout.write("Update completed.")



# #############################
# def seshatcomment_create_view(request):
#     """
#     View to create a SeshatComment instance.

#     Note:
#         This view can handle POST and GET requests.

#     Args:
#         request: The request object.

#     Returns:
#         HttpResponse: The HTTP response.
#     """
#     if request.method == 'POST':
#         form = SeshatCommentForm2(request.POST)
#         if form.is_valid():
#             user_logged_in = request.user

#             comment_instance = SeshatComment.objects.create(text='')

#             try:
#                 seshat_expert_instance = Seshat_Expert.objects.get(user=user_logged_in)
#             except Seshat_Expert.DoesNotExist:
#                 seshat_expert_instance = None

#             # Create the SeshatCommentPart instance
#             comment_instance = SeshatComment.objects.create(text='')
#         a = """
#         ALi yaret <ref> grgfg </ref> hasan be hamreahet <ref>gfgfg </ref>
#         """
        
#         comment_broken_part = {
#             ''
#         }

#         for ref_raw in 

#             data_dicts = [{
#                 'zot_id': 'SFWWGFG3',
#                 'p_range': '390',
#                 'step': '2',
#                 'full': '...',
#                 'pages_tuples': [(390, 390)],
#                 'invalid_pages': None
#                 }]


#             # get the text
#             subcomment_text = data_dicts['subcomment_text']
#             subcomment_order = my_index
#             user_logged_in = request.user

#             # Create the SeshatCommentPart instance
#             subcomment_part = SeshatCommentPart.objects.create(
#                 comment=comment_instance,
#                 subcomment_part_text=subcomment_text,
#                 subcomment_order=subcomment_order,
#                 comment_curator=seshat_expert_instance 
#             )

#             # Process the citations

#             for k, v in data_dicts.items():
#                 reference = reference = Reference.objects.get(zotero_link=v['zot_id'])
#                 for page_from, page_to in v['pages_tuples']:
#                     citation, created = Citation.objects.get_or_create(
#                         ref=reference,
#                         page_from=int(page_from),
#                         page_to=int(page_to)
#                     )
#                     # Associate the Citation with the SeshatCommentPart
#                     subcomment_part.comment_citations.add(citation)




# def xx_yy_zz(request, app_name, model_name, instance_id):
#     big_father = SeshatComment.objects.create(text='')
#     #big_father = SeshatComment.objects.get(id=com_id)
#     com_id = big_father.pk
#     model_class = apps.get_model(app_label=app_name, model_name= model_name)

#     model_instance = get_object_or_404(model_class, id=instance_id)
#     # create model_instance
#     model_instance.comment = big_father

#     model_instance.save()

#     # Attach Comment PArts to the Comment
#     if True:
#         subcomment_text = form.cleaned_data['sub_comment_text']
#         subcomment_order = form.cleaned_data['comment_order']

#         seshat_comment_part = SeshatCommentPart(comment_part_text=comment_text, comment_order=1, comment_curator=2, comment= big_father)

#         seshat_comment_part.save()

#         # Process the formset
#         reference_formset = ReferenceFormSet2(request.POST, prefix='refs')
#         if reference_formset.is_valid():
#             #print("ALOOOOOOOOOOOOOOOOOOO: ", len(reference_formset))
#             to_be_added = []
#             to_be_deleted_later = []
#             for reference_form in reference_formset:
#                 if reference_form.is_valid():
#                     try:
#                         reference = reference_form.cleaned_data['ref']
#                         page_from = reference_form.cleaned_data['page_from']
#                         page_to = reference_form.cleaned_data['page_to']
#                         to_be_deleted = reference_form.cleaned_data['DELETE']
#                         parent_pars_inserted = reference_form.cleaned_data['parent_pars']


#                         # Get or create the Citation instance
#                         if page_from and page_to:
#                             citation, created = Citation.objects.get_or_create(
#                                 ref=reference,
#                                 page_from=int(page_from),
#                                 page_to=int(page_to)
#                             )
#                         elif page_from:
#                             citation, created = Citation.objects.get_or_create(
#                                 ref=reference,
#                                 page_from=int(page_from),
#                                 page_to=int(page_from)
#                             )
#                         elif page_to:
#                             citation, created = Citation.objects.get_or_create(
#                                 ref=reference,
#                                 page_from=int(page_to),
#                                 page_to=int(page_to)
#                             )
#                             #print(page_from, "AAAAAAAAAAAAAAAAAAAAND ", page_to)
#                         else:
#                             citation, created = Citation.objects.get_or_create(
#                                 ref=reference,
#                                 page_from=None,
#                                 page_to=None
#                             )

#                         # Associate the Citation with the SeshatCommentPart
#                         if to_be_deleted:
#                             #comment_part.comment_citations.remove(citation)
#                             to_be_deleted_later.append((citation, parent_pars_inserted))
#                         else:
#                             #comment_part.comment_citations.add((citation, parent_pars_inserted))
#                             to_be_added.append((citation, parent_pars_inserted))
#                     except:
#                         pass  # Handle the exception as per your requirement
#             # seshat_comment_part.comment_citations.clear()
#             # seshat_comment_part.comment_citations.add(*to_be_added)
#             seshat_comment_part.comment_citations_plus.clear()
#             #seshat_comment_part.comment_citations_plus.add(*to_be_added)

#             for item in to_be_added:
#                 # Query for an existing row based on citation and SeshatCommentPart
#                 scp_through_ctn, created = ScpThroughCtn.objects.get_or_create(
#                     seshatcommentpart=seshat_comment_part,
#                     citation=item[0],
#                     defaults={'parent_paragraphs': item[1]}  # Set defaults including parent_paragraphs
#                 )

#                 # If the row already exists, update its parent_paragraphs
#                 if not created:
#                     scp_through_ctn.parent_paragraphs = item[1]
#                     scp_through_ctn.save()
