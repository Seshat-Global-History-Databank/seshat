from django.core.management.base import BaseCommand
from django.db import connection
from django.apps import apps

from seshat.apps.core.models import Polity, ScpThroughCtn, Reference, Citation, Seshat_Expert, SeshatCommentPart, SeshatComment, SeshatPrivateComment


from seshat.apps.general.models import Polity_expert, Polity_original_name, Polity_alternative_name

from seshat.apps.crisisdb.models import Instability_event, Instability_type, Instability_ref

#from seshat.apps.crisisdb.instability_events_dic_list import ultimate_dics_list
#from seshat.apps.crisisdb.instability_events_dic_list_2 import ultimate_dics_list
from seshat.apps.crisisdb.instability_events_dic_list_batch_3 import ultimate_dics_list

from django.db import transaction

EVENTS_DATA = [
    {
        'event': 'Revolt of Datames',
        'year_from': -382,
        'year_to': -362,
        'llm_description': 'Datames, satrap of Cappadocia, rebelled against Artaxerxes II, seeking autonomy. He was assassinated in 362 BCE after a decade of resistance.',
        'all_types': ['Assassination', 'Separatist Rebellion'],
        'all_refs': ['Cornelius Nepos, <b>Lives of Eminent Commanders</b> 14 (Datames)',
                     'Diodorus Siculus, <b>Library of History</b> 15.91.'],
        'is_real': True,
        'polity': 'ir_achaemenid_emp',
        'extent': 6,
        'intensity': 6,
        'class_cot': 'Okay, let\'s tackle this for Intensity.',
        'sorokin': 'Extent 6 as the revolt was led by a satrap (provincial governor) in Cappadocia, indicating provincial-level involvement. Intensity 4 due to likely military engagements over a decade, though exact casualty figures are unspecified but consistent with regional rebellion scale.',
        'general_cot': 'Okay, references are academic sources.'
    }
]

class Command(BaseCommand):
    help = "Populate the Instability_event model with sample data"

    @transaction.atomic  # Ensures atomic DB transactions
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Starting data import..."))
        
        #for event_data in EVENTS_DATA:
        for event_data in ultimate_dics_list:
            # Create or get Instability_type records
            instability_types = []
            inst_type_str_list = []
            for type_name in event_data['all_types']:
                if type_name in ['Execution (contextually framed as a consequence of rebellion)','Execution (linked to military failure/revolt)',]:
                    type_name= 'Execution'
                elif type_name in ['Political disturbance (non-violent)',]:
                    type_name= 'Political Disturbance'
                elif type_name in ['Coup d’état (de facto political takeover)',]:
                    type_name= 'Coup d’état'
                inst_type, created = Instability_type.objects.get_or_create(name=type_name)
                inst_type_str_list.append(type_name)
                instability_types.append(inst_type)
            isntabilty_types_str = '; '.join(inst_type_str_list)

            # Create or get Instability_ref records
            instability_refs = []
            for ref_name in event_data['all_refs']:
                inst_ref, created = Instability_ref.objects.get_or_create(name=ref_name, is_real=False)
                instability_refs.append(inst_ref)

            # Polity
            try:
                my_pol = Polity.objects.get(new_name=event_data['polity'])
                my_pc = SeshatPrivateComment.objects.create()
            except:
                #print('Bad Pol')
                continue
            #print(my_pol)
            # Create Instability_event
            real_check = 'Real' if event_data['is_real'] else 'Uncertain'

            if event_data['macro_event']:
                llm_new_name = event_data['event'] + f" (Macro Event: {event_data['macro_event']})"
            else:
                llm_new_name = event_data['event']


            event = Instability_event.objects.create(
                name=event_data['event'],
                llm_name=llm_new_name,
                year_from=event_data['year_from'],
                year_to=event_data['year_to'],
                llm_year_from=event_data['year_from'],
                llm_year_to=event_data['year_to'],
                llm_description=event_data['llm_description'],
                inst_extent=event_data['extent'],
                inst_intensity=event_data['intensity'],
                llm_inst_extent=event_data['extent'],
                llm_inst_intensity=event_data['intensity'],
                classification_cot=event_data['class_cot'],
                sorokin_rationale=event_data['sorokin'],
                general_cot=event_data['general_cot'],
                real_event_check=real_check,
                llm_real_event_check=real_check,
                llm_inst_type=isntabilty_types_str,
                polity_id=my_pol.id,
                private_comment_id=my_pc.id,
            )

            # Add ManyToMany relations
            event.inst_type.set(instability_types)
            event.inst_llm_ref.set(instability_refs)

            self.stdout.write(self.style.SUCCESS(f"Added event: {event.name}"))

        self.stdout.write(self.style.SUCCESS("Data import completed successfully!"))