from django.core.management.base import BaseCommand
from django.db import connection
from django.apps import apps

from seshat.apps.core.models import Polity, ScpThroughCtn, Reference, Citation, Seshat_Expert, SeshatCommentPart, SeshatComment


from seshat.apps.general.models import Polity_expert, Polity_original_name, Polity_alternative_name


from seshat.apps.rt.models import Moralizing_supernatural_punishment_and_reward, Moralizing_supernatural_concern_is_primary, Moralizing_enforcement_is_certain, Moralizing_enforcement_is_broad, Moralizing_enforcement_is_targeted, Moralizing_enforcement_of_rulers, Moralizing_religion_adopted_by_elites, Moralizing_religion_adopted_by_commoners, Moralizing_enforcement_in_afterlife, Moralizing_enforcement_in_this_life, Moralizing_enforcement_is_agentic

from seshat.apps.rt.final_dic_insert_msp_3 import my_final_dic_extra_with_citations_stripped



class Command(BaseCommand):
    help = "Update sc descriptions"

    def handle(self, *args, **kwargs):
        self.stdout.write("Fetching polities and experts...")  

        unique_polity_new_ids = Polity.objects.values_list('new_name', flat=True).distinct()
        var_to_model = {
            'Moralizing Enforcement is Broad': Moralizing_enforcement_is_broad,
            'Moralizing Supernatural Concern is Primary': Moralizing_supernatural_concern_is_primary,
            'Moralizing Enforcement is Agentic': Moralizing_enforcement_is_agentic,
            'Moralizing Enforcement in This Life': Moralizing_enforcement_in_this_life,
            'Moralizing Punishment and Reward': Moralizing_supernatural_punishment_and_reward,
            'Moralizing Religion Adopted by Commoners': Moralizing_religion_adopted_by_commoners,
            'Moralizing Enforcement is Targeted': Moralizing_enforcement_is_targeted,
            'Moralizing Enforcement in Afterlife': Moralizing_enforcement_in_afterlife,
            'Moralizing Religion Adopted by Elites': Moralizing_religion_adopted_by_elites,
            'Moralizing Enforcement of Rulers': Moralizing_enforcement_of_rulers,
            'Moralizing Enforcement is Certain': Moralizing_enforcement_is_certain,
            }

        var_to_coded_var = {'coded_value': 'coded_value'}
        xyzp = {('et_ethiopian_k_3', 'Moralizing Enforcement is Broad'): {'age': 'new', 'coded_value': 'present', 'tag': 'TRS', 'content': [{'sub_text': "The idea of loving one's neighbour implies a broad range of moral activity. “We have said that deification means ‘following the commandments’; and these commandments were briefly described by Christ as love of God and love of neighbour. The two forms of love are inseparable. A man can love his neighbour as himself only if he loves God above all; and a man cannot love God if he does not love his fellow men (1 John iv, 20).”", 'sub_order': 1, 'citations': [{'my_ref': 'N4A4ZTEH', 'my_pages': (0, 0)}]}]}, ('tr_byzantine_emp_1', 'Moralizing Enforcement is Broad'): {'age': 'new', 'coded_value': 'present', 'tag': 'TRS', 'content': [{'sub_text': "The idea of loving one's neighbour implies a broad range of moral activity. “We have said that deification means ‘following the commandments’; and these commandments were briefly described by Christ as love of God and love of neighbour. The two forms of love are inseparable. A man can love his neighbour as himself only if he loves God above all; and a man cannot love God if he does not love his fellow men (1 John iv, 20).”", 'sub_order': 1, 'citations': [{'my_ref': 'N4A4ZTEH', 'my_pages': (0, 0)}]}]}, ('tr_byzantine_emp_3', 'Moralizing Enforcement is Broad'): {'age': 'new', 'coded_value': 'present', 'tag': 'TRS', 'content': [{'sub_text': "The idea of loving one's neighbour implies a broad range of moral activity. “We have said that deification means ‘following the commandments’; and these commandments were briefly described by Christ as love of God and love of neighbour. The two forms of love are inseparable. A man can love his neighbour as himself only if he loves God above all; and a man cannot love God if he does not love his fellow men (1 John iv, 20).”", 'sub_order': 1, 'citations': [{'my_ref': 'N4A4ZTEH', 'my_pages': (0, 0)}]}]}, ('ru_romanov_dyn_2', 'Moralizing Enforcement is Broad'): {'age': 'new', 'coded_value': 'present', 'tag': 'TRS', 'content': [{'sub_text': "The idea of loving one's neighbour implies a broad range of moral activity. “We have said that deification means ‘following the commandments’; and these commandments were briefly described by Christ as love of God and love of neighbour. The two forms of love are inseparable. A man can love his neighbour as himself only if he loves God above all; and a man cannot love God if he does not love his fellow men (1 John iv, 20).”", 'sub_order': 1, 'citations': [{'my_ref': 'N4A4ZTEH', 'my_pages': (0, 0)}]}]}, ('tr_byzantine_emp_2', 'Moralizing Enforcement is Broad'): {'age': 'new', 'coded_value': 'present', 'tag': 'TRS', 'content': [{'sub_text': "The idea of loving one's neighbour implies a broad range of moral activity. “We have said that deification means ‘following the commandments’; and these commandments were briefly described by Christ as love of God and love of neighbour. The two forms of love are inseparable. A man can love his neighbour as himself only if he loves God above all; and a man cannot love God if he does not love his fellow men (1 John iv, 20).”", 'sub_order': 1, 'citations': [{'my_ref': 'N4A4ZTEH', 'my_pages': (0, 0)}]}]}, ('ru_moskva_rurik_dyn', 'Moralizing Enforcement is Broad'): {'age': 'new', 'coded_value': 'present', 'tag': 'TRS', 'content': [{'sub_text': "The idea of loving one's neighbour implies a broad range of moral activity. “We have said that deification means ‘following the commandments’; and these commandments were briefly described by Christ as love of God and love of neighbour. The two forms of love are inseparable. A man can love his neighbour as himself only if he loves God above all; and a man cannot love God if he does not love his fellow men (1 John iv, 20).”", 'sub_order': 1, 'citations': [{'my_ref': 'N4A4ZTEH', 'my_pages': (0, 0)}]}]}, ('et_ethiopian_k', 'Moralizing Enforcement is Broad'): {'age': 'new', 'coded_value': 'present', 'tag': 'TRS', 'content': [{'sub_text': "The idea of loving one's neighbour implies a broad range of moral activity. “We have said that deification means ‘following the commandments’; and these commandments were briefly described by Christ as love of God and love of neighbour. The two forms of love are inseparable. A man can love his neighbour as himself only if he loves God above all; and a man cannot love God if he does not love his fellow men (1 John iv, 20).”", 'sub_order': 1, 'citations': [{'my_ref': 'N4A4ZTEH', 'my_pages': (0, 0)}]}]}, ('et_ethiopian_k_2', 'Moralizing Enforcement is Broad'): {'age': 'new', 'coded_value': 'present', 'tag': 'TRS', 'content': [{'sub_text': "The idea of loving one's neighbour implies a broad range of moral activity. “We have said that deification means ‘following the commandments’; and these commandments were briefly described by Christ as love of God and love of neighbour. The two forms of love are inseparable. A man can love his neighbour as himself only if he loves God above all; and a man cannot love God if he does not love his fellow men (1 John iv, 20).”", 'sub_order': 1, 'citations': [{'my_ref': 'N4A4ZTEH', 'my_pages': (0, 0)}]}]}, ('ru_romanov_dyn_1', 'Moralizing Enforcement is Broad'): {'age': 'new', 'coded_value': 'present', 'tag': 'TRS', 'content': [{'sub_text': "The idea of loving one's neighbour implies a broad range of moral activity. “We have said that deification means ‘following the commandments’; and these commandments were briefly described by Christ as love of God and love of neighbour. The two forms of love are inseparable. A man can love his neighbour as himself only if he loves God above all; and a man cannot love God if he does not love his fellow men (1 John iv, 20).”", 'sub_order': 1, 'citations': [{'my_ref': 'N4A4ZTEH', 'my_pages': (0, 0)}]}]}, ('tr_east_roman_emp', 'Moralizing Enforcement is Broad'): {'age': 'new', 'coded_value': 'present', 'tag': 'TRS', 'content': [{'sub_text': "The idea of loving one's neighbour implies a broad range of moral activity. “We have said that deification means ‘following the commandments’; and these commandments were briefly described by Christ as love of God and love of neighbour. The two forms of love are inseparable. A man can love his neighbour as himself only if he loves God above all; and a man cannot love God if he does not love his fellow men (1 John iv, 20).”", 'sub_order': 1, 'citations': [{'my_ref': 'N4A4ZTEH', 'my_pages': (0, 0)}]}]}}

        # my_final_dic_extra_with_citations_stripped
        bad_zots = []
        bad_pols = []
        #for pol_var_tuple, age_content in my_final_dic_extra_with_citations_stripped.items():
        for pol_var_tuple, age_content in xyzp.items():
            polity_old_id, var_name = pol_var_tuple

            try:
                my_polity = Polity.objects.get(new_name=polity_old_id)
            except:
                print(f'Bad pol: {polity_old_id}.', )

            my_polity_id = my_polity.id
            #print(my_polity_id)

            if age_content['age'] == 'new':
                # there might be model instances (check)
                model_instances = var_to_model[var_name].objects.filter(
                    polity_id=my_polity_id
                )  #
                # create model_instance
                if not model_instances:
                    model_instances = []
                    new_model_instance = var_to_model[var_name].objects.create(
                        polity_id=my_polity_id,
                        coded_value=age_content['coded_value'],
                        tag=age_content['tag'],
                    )
                    new_model_instance.save()


                    model_instances.append(new_model_instance)
                else:
                    print(f'Fooooooooor {var_name} there is coded value in {polity_old_id}...')

                # Now we are sure we have model_instances!
                # Modifications to the model instance
                for model_instance in model_instances:
                    if model_instance.comment and model_instance.comment.id != 1:
                        #print('Existing NEW Description:', pol_var_tuple, model_instance.comment.id)
                        big_father = SeshatComment.objects.get(id=model_instance.comment.id)

                    else:
                    #model_instance_existing_comment = model_instance.comment.id
                        big_father = SeshatComment.objects.create(text='')

                    model_instance.comment = big_father
                    model_instance.save()

                seshat_expert_instance = Seshat_Expert.objects.get(id=2)

                # Modifications to the new comment of the instance (if it exists)

                if age_content['coded_value'] == 'unknown':
                    continue
                for subcom_details in age_content['content']:
                    comment_part = SeshatCommentPart.objects.create(
                                    comment=big_father,
                                    comment_part_text=subcom_details['sub_text'],
                                    comment_order=subcom_details['sub_order'],
                                    comment_curator=seshat_expert_instance # Could be werong
                                )
                    comment_part.save()
                    to_be_added = []
                    # EXCEPTION: 
                    # a_citation might be {'my_ref': None, 'my_pages': None, 'ref_original': None}
                    for a_citation in subcom_details['citations']:
                        my_zotero = a_citation['my_ref']
                            
                        if my_zotero:
                            #print(my_zotero)
                            try:
                                my_reference = Reference.objects.get(zotero_link=my_zotero)
                            except:
                                bad_zots.append(my_zotero)
                                my_reference = Reference.objects.get(zotero_link='Z4ACHZRD')
                            if not a_citation['my_pages']:
                                citation, created = Citation.objects.get_or_create(
                                    ref=my_reference,
                                    page_from=None,
                                    page_to=None
                                )
                                to_be_added.append((citation, ''))

                            else:
                                page_range = a_citation['my_pages']
                                # add citations
                                if page_range == (0, 0) or page_range == (None, None):
                                    citation, created = Citation.objects.get_or_create(
                                    ref=my_reference,
                                    page_from=None,
                                    page_to=None
                                )
                                else:
                                    page_from = page_range[0]
                                    page_to = page_range[1]
                                    citation, created = Citation.objects.get_or_create(
                                    ref=my_reference,
                                    page_from=int(page_from),
                                    page_to=int(page_to)
                                )

                                parent_pars_inserted = ''

                                to_be_added.append((citation, parent_pars_inserted))

                                
                            for item in to_be_added:
                                #print('Inside SCPPPPPPPPPPPPP')
                                #print(to_be_added)
                                # Query for an existing row based on citation and SeshatCommentPart
                                scp_through_ctn, created = ScpThroughCtn.objects.get_or_create(
                                    seshatcommentpart=comment_part,
                                    citation=item[0],
                                    defaults={'parent_paragraphs': item[1]}  # Set defaults including parent_paragraphs
                                )
                        #else: # No REf (Only Texty subdescription)
                    

                # If the row already exists, update its parent_paragraphs
                #if not created:
                #    scp_through_ctn.parent_paragraphs = item[1]
                #    scp_through_ctn.save()

            elif age_content['age'] == 'old':
                print('Bad age')
        print('BAD ZOTS')
        print(set(bad_zots))
        print('BAD POLLLLLLLLLLS')
        print(set(bad_pols))

        self.stdout.write("Done.")

