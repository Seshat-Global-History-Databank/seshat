from django.core.management.base import BaseCommand
from django.db import connection
from django.apps import apps

from seshat.apps.core.models import Polity, ScpThroughCtn, Reference, Citation, Seshat_Expert, SeshatCommentPart, SeshatComment, SeshatPrivateComment


from seshat.apps.general.models import Polity_expert, Polity_original_name, Polity_alternative_name

from seshat.apps.crisisdb.models import Instability_event, Instability_type, Instability_ref

#from seshat.apps.crisisdb.instability_events_dic_list import ultimate_dics_list
from seshat.apps.crisisdb.instability_events_dic_list_3 import ultimate_dics_list

from django.db import transaction

EVENTS_DATA = [
{'event': 'Tribal Rebellion Against Osman',
 'year_from': 1420,
 'year_to': None,
 'llm_description': "Turkmen tribes under Ak Koyunlu rule rebelled against Qara Yülük Osman's centralizing policies, leading to a localized rural uprising. The rebellion was suppressed, reinforcing Osman's authority.",
 'all_types': ['Rural Uprising'],
 'all_refs': ['Faruk Sümer, <b>Akkoyunlular</b> p. 1777712'],
 'is_real': True,
 'polity': 'ir_ak_koyunlu',
 'extent': 2,
 'intensity': 1,
 'class_cot': 'Okay, lellion, so REAL.<br><br>Rationale: Extent is 2 because it\'s a localized rural district. Intensity 1 because the suppression likely resulted in a few deaths, even if not explicitly stated. The rationale should mention the description\'s terms and the reasoning for the chosen codes.',
 'sorokin': 'Extent 2 chosen as the rebellion was described as a localized rural uprising, fitting a small town or rural district. Intensity 1 selected because while the rebellion was suppressed, the description implies some casualties (one or few killed) but not reaching tens. The event is documented as a historical rebellion.',
 'general_cot': 'Okay, so I neper the format.'}
]

class Command(BaseCommand):
    help = "Update instability refs in Instability_event model"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Starting instability refs update..."))
        
        #for event_data in EVENTS_DATA:
        for event_data in ultimate_dics_list:
            try:
                # Find the existing event by name (or use another unique field if needed)
                event = Instability_event.objects.get(llm_name=event_data['event'], llm_year_from=event_data['year_from'],  classification_cot=event_data['class_cot'],
 )
            except Instability_event.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Event not found: {event_data['event']}"))
                continue

            # Prepare Instability_ref records
            instability_refs = []
            for ref_name in event_data['all_refs']:
                inst_ref, created = Instability_ref.objects.get_or_create(name=ref_name, is_real=False)
                instability_refs.append(inst_ref)

            # Update ManyToMany field
            event.inst_llm_ref.set(instability_refs)

            self.stdout.write(self.style.SUCCESS(f"Updated refs for event: {event.name}"))

        self.stdout.write(self.style.SUCCESS("Instability refs update completed successfully!"))


# class Command(BaseCommand):
#     help = "Populate the Instability_event model with sample data"

#     @transaction.atomic  # Ensures atomic DB transactions
#     def handle(self, *args, **kwargs):
#         self.stdout.write(self.style.SUCCESS("Starting data import..."))
        
#         #for event_data in EVENTS_DATA:
#         for event_data in ultimate_dics_list:
#             # Create or get Instability_type records
#             instability_types = []
#             inst_type_str_list = []
#             for type_name in event_data['all_types']:
#                 if type_name in ['Execution (contextually framed as a consequence of rebellion)','Execution (linked to military failure/revolt)',]:
#                     type_name= 'Execution'
#                 elif type_name in ['Political disturbance (non-violent)',]:
#                     type_name= 'Political Disturbance'
#                 elif type_name in ['Coup d’état (de facto political takeover)',]:
#                     type_name= 'Coup d’état'
#                 inst_type, created = Instability_type.objects.get_or_create(name=type_name)
#                 inst_type_str_list.append(type_name)
#                 instability_types.append(inst_type)
#             isntabilty_types_str = '; '.join(inst_type_str_list)

#             # Create or get Instability_ref records
#             instability_refs = []
#             for ref_name in event_data['all_refs']:
#                 inst_ref, created = Instability_ref.objects.get_or_create(name=ref_name, is_real=False)
#                 instability_refs.append(inst_ref)

#             # Polity
#             try:
#                 my_pol = Polity.objects.get(new_name=event_data['polity'])
#                 my_pc = SeshatPrivateComment.objects.create()
#             except:
#                 #print('Bad Pol')
#                 continue
#             #print(my_pol)
#             # Create Instability_event
#             real_check = 'Real' if event_data['is_real'] else 'Uncertain'

#             event = Instability_event.objects.create(
#                 name=event_data['event'],
#                 llm_name=event_data['event'],
#                 year_from=event_data['year_from'],
#                 year_to=event_data['year_to'],
#                 llm_year_from=event_data['year_from'],
#                 llm_year_to=event_data['year_to'],
#                 llm_description=event_data['llm_description'],
#                 inst_extent=event_data['extent'],
#                 inst_intensity=event_data['intensity'],
#                 llm_inst_extent=event_data['extent'],
#                 llm_inst_intensity=event_data['intensity'],
#                 classification_cot=event_data['class_cot'],
#                 sorokin_rationale=event_data['sorokin'],
#                 general_cot=event_data['general_cot'],
#                 real_event_check=real_check,
#                 llm_real_event_check=real_check,
#                 llm_inst_type=isntabilty_types_str,
#                 polity_id=my_pol.id,
#                 private_comment_id=my_pc.id,
#             )

#             # Add ManyToMany relations
#             event.inst_type.set(instability_types)
#             event.inst_llm_ref.set(instability_refs)

#             self.stdout.write(self.style.SUCCESS(f"Added event: {event.name}"))

#         self.stdout.write(self.style.SUCCESS("Data import completed successfully!"))