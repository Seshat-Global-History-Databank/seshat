from django.core.management.base import BaseCommand
from django.db import connection
from django.apps import apps

from seshat.apps.core.models import Polity, ScpThroughCtn, Reference, Citation, Seshat_Expert, SeshatCommentPart, SeshatComment, SeshatPrivateComment, SeshatPrivateCommentPart


from seshat.apps.general.models import Polity_expert, Polity_original_name, Polity_alternative_name

from seshat.apps.crisisdb.models import Instability_event, Instability_type, Instability_ref, Check_choice

import datetime

#from seshat.apps.crisisdb.instability_events_notes_dic_list import ultimate_notes_dics_list

from django.db import transaction

NOTES_DATA = [{'Zotero Link': None,
  'issues': ['Good'],
  'Polity': 'tr_east_roman_emp',
  'Event': 'Execution of Rufinus',
  'Year': 395,
  'RA Notes': "SH 25/03: Extent given as 6 because the execution happen at a capital but in terms of the event itself it wasn't widespread. The source tells us that he marched to Constantinople and was immeditely killed by soldiers there without a battle.\n\nJZ 25/03: but thats correct as Peter defined it ? One or two provinces, or only the capital   . So 6 if its only the capital https://docs.google.com/spreadsheets/d/1FB8mgwtwxO4plDRYMhV11SPUSJvLLJr_/edit?gid=1888345229#gid=1888345229&range=48:48\n\nSH: Ok that makes sense, I just wanted to make sure it wasn't, for example, an entire capital involved in a riot v one person being executed at the capital. Which to me is a different type of 'Extent'. But if we are using Extent to refer to a location as well then yes 6 makes sense.\n\nKeeping the conversation here for reference and a check with Peter."},
 {'Zotero Link': 'CVNKALKH',
  'issues': ['Page'],
  'Polity': 'tr_east_roman_emp',
  'Event': "Riots over John Chrysostom's Exile",
  'Year': 404,
  'RA Notes': 'SH 25/03: Reference is fine and the exile and riots are discussed in pages 401-403, however there is no specific mention of the year. However there are several other sources that specifiy the year as 404 so added one into Zotero and linked here. '},
 {'Zotero Link': 'YHPM9LTJ; 5VZYXQAD',
  'issues': ['Year', 'Page'],
  'Polity': 'tr_east_roman_emp',
  'Event': 'Execution of Armatus',
  'Year': 477,
  'RA Notes': "SH 25/03: Bury 1923 says Basiliscus was executed 476, and then goes on to say that Armatus was also later executed but doesn't specify the date (Bury 1923: 393). Cambridge Ancient History source also mentions Armatus' execution but again doesn't mention the date (Mirza 2000: 308) However Evagrius Scholasticus, Ecclesiastical History (AD431-594), translated by E. Walford (1846) states the execution happened in 477 which is what wikipedia has referenced. Added the two referenced sources to Zotero"},
 {'Zotero Link': 'CFEULT5B',
  'issues': ['Good', 'Page'],
  'Polity': 'tr_east_roman_emp',
  'Event': 'Nika Riots',
  'Year': 532,
  'RA Notes': 'SH 25/03: Good entry all around! Only thing missing is page numbers for the reference e.g., Treadgold 1997: 181-182'},
 {'Zotero Link': None,
  'issues': ['Bad Row'],
  'Polity': 'tr_east_roman_emp',
  'Event': 'Execution of Green Faction Conspirators',
  'Year': 562,
  'RA Notes': "SH 26/03: I'm not sure about this one, I can't find reference to this specific event, and the AI may have conflated two things from the look of the CoT. I THINK this reference should be The Cambridge Companion to the Age of Justinian, 2006, Chapter 3, Brian Croke 'Justinian's Constantinople' pp60-86. But there is no mention of this assasination plot and Green Faction executions in that source. I can see that there was an attempt to assasinate Justinian I by an assasin called Ablabius, which is refered to in the Theophanes and Malalas contemporary sources. But his fate after he was arrested for the attempted assasination is apparently not recorded (https://en.wikipedia.org/wiki/Ablabius_(assassin) / Martindale et al. 1992) He MAY have been linked to the Green faction but there doesn't seem to be a definitive answer."},
 {'Zotero Link': 'CFEULT5B; 3GBJI3X8',
  'issues': ['Good', 'Reference'],
  'Polity': 'tr_east_roman_emp',
  'Event': 'Rebellion of Narses',
  'Year': 603,
  'RA Notes': "SH 26/03: The source provided doesn't mention the date of rebellion or his execution, but it does discuss the general rebellion. However I have found reference to both in Treadgold (1997: 238) and in Carr (2015: 101) Added Zotero links here."},
 {'Zotero Link': 'FNP45QKF',
  'issues': ['Good'],
  'Polity': 'tr_east_roman_emp',
  'Event': 'Heraclian Revolt',
  'Year': 608,
  'RA Notes': 'SH: 27/03: Might need to consider if these two need to be recorded as different events or whether the riots are just part of the wider civil war. Though they are both correct. Reference is Kaegi 2003: 48-50, 56.'},
 {'Zotero Link': 'FNP45QKF',
  'issues': ['Good'],
  'Polity': 'tr_east_roman_emp',
  'Event': 'Urban Riots in Constantinople (608–610)',
  'Year': 608,
  'RA Notes': 'SH: 27/03: Might need to consider if these two need to be recorded as different events or whether the riots are just part of the wider civil war. Though they are both correct. Reference is Kaegi 2003: 48-50, 56.'},
 {'Zotero Link': 'CFEULT5B',
  'issues': ['Bad Row'],
  'Polity': 'tr_byzantine_emp_1',
  'Event': 'Assassination of Constantine III',
  'Year': 641,
  'RA Notes': 'SH 27/03: Treadgold 1997: 309, says that Constantine III died of tuberculosis, and that the rumour of poisoning by Martina was a lie spread by partisans. Ostrogorsky (1956: 112-113) says the same.  So I think the AI has taken the mention of the rumour to be the truth but it seems that historians haven\'t come to that conclusion.\n\nCoT says "Constantine III died shortly after, possibly poisoned. That could be an assassination." So it\'s made the decision again.'},
 {'Zotero Link': 'BFS78DVY',
  'issues': ['Year', 'Page'],
  'Polity': 'tr_byzantine_emp_1',
  'Event': 'Rebellion of Olympius in Italy',
  'Year': 649,
  'RA Notes': "SH 27/03: The source states that Olympius tried to start a revolt in 651 (Brown 1984: 108, 151) so I'm not sure where the 649-651 date range came from, but I think that may be the time that he was the Exarch."},
 {'Zotero Link': 'KFVZ8IWP',
  'issues': ['Good', 'Page'],
  'Polity': 'tr_byzantine_emp_1',
  'Event': "Justinian II's overthrow and mutilation",
  'Year': 695,
  'RA Notes': 'SH 27/03: Good entry. Page is 333-334. '},
 {'Zotero Link': 'CFEULT5B',
  'issues': ['Good'],
  'Polity': 'tr_byzantine_emp_1',
  'Event': 'Sicilian Rebellion of Basil Onomagoulos',
  'Year': 717,
  'RA Notes': 'SH 27/03: Good entry. Assumption of Intensity 1 made by the AI but as there were troops dispatched to stop the opposition that is likely? Also pleased that it has providede a page number on this one!'},
 {'Zotero Link': 'CFEULT5B',
  'issues': ['Description', 'Type', 'Page'],
  'Polity': 'tr_byzantine_emp_1',
  'Event': 'Execution of Artabasdos and Sons',
  'Year': 743,
  'RA Notes': 'SH 27/03: Artabasdos (Artavasdus in the source referenced) and his sons were not executed but they were blinded (Treadgold 1997: 357-358)'},
 {'Zotero Link': 'Q8GNFGSL',
  'issues': ['Good'],
  'Polity': 'tr_byzantine_emp_1',
  'Event': 'Rebellion of Bardanes Tourkos',
  'Year': 803,
  'RA Notes': "SH 27/03: Good entry. But I can't see in the sources it has quoted that he was blinded. Brubaker 2015: 357) says he entered a monastary."},
 {'Zotero Link': None,
  'issues': ['Good'],
  'Polity': 'tr_byzantine_emp_1',
  'Event': 'Paulician Rebellion',
  'Year': 843,
  'RA Notes': 'SH 27/03: Good entry.'},
 {'Zotero Link': 'CFEULT5B',
  'issues': ['Reference'],
  'Polity': 'tr_byzantine_emp_2',
  'Event': 'Coup attempt of Constantine Doukas',
  'Year': 913,
  'RA Notes': "SH 27/03: Reference and page is not correct, the people are mentioned in teh book but the coup is not detailed here. Also to note that Constantine VII was the one being usurped. Treadgold 1997: 473, details this well and does mention that Ducas and his son were killed while his partisans were massacred, but there is no number specified. So perhaps Intensity could be 2 (tens killed) but we don't know for sure."},
 {'Zotero Link': 'C9K9R5PC; add Kuhrt ',
  'issues': ['Bad Row'],
  'Polity': 'ir_achaemenid_emp',
  'Event': 'Coup of Darius I against Bardiya',
  'Year': -522,
  'RA Notes': "Event and Description: the latter doesn't match the former accurately; event should be 'against Gaumata/Bardiya' or something along these lines, since he is named in sources using one or other or both names. Major missing event from what I can gather from my research and reading: Achaemenid Civil War (522-520 BC), a large-scale civil war that broke out as a result of the 'mysterious circumstances' surrounding the death of Gaumata/Bardiya and the ascension to the throne by Darius I. The aforementioned 'Behistun Inscription' details the military actions of this civil war. References: Briant (2002) and Kuhrt (2007) relevant and correct. RS 21/03/25."},
 {'Zotero Link': 'C9K9R5PC',
  'issues': ['Bad Row'],
  'Polity': 'ir_achaemenid_emp',
  'Event': 'Babylonian Revolt under Nebuchadnezzar III',
  'Year': -522,
  'RA Notes': 'Event and Description: just a thought: should unsuccessful (vs. successful) separatist rebellions, etc, not be defined in these exact terms in the event/description fields, to differentiate these points of instability? Also, the description notes that Nebuchadnezzar III was executed; the extent 6 suggests that many were killed during this unsuccessful rebellion, but does not provide exact details. References: unknown symbol/unclear referencing with regard to the Behistun Inscription. Briant (2002) relevant and correct. RS 21/03/25.'},
 {'Zotero Link': 'C9K9R5PC',
  'issues': ['Bad Row'],
  'Polity': 'ir_achaemenid_emp',
  'Event': 'Execution of Bardiya/Gaumata',
  'Year': -522,
  'RA Notes': "Event and Description: connected with the first event in the list, should this be treated separately?; not sure if Gaumata's death was definitely an 'execution'? References: unknown symbol/unclear referencing with regard to the Behistun Inscription. Briant (2002) relevant and correct. General Notes: uncertain can be changed to real if keeping as separate event from the first one in the list. RS 21/03/25."},
 {'Zotero Link': None,
  'issues': ['Bad Row'],
  'Polity': 'ir_achaemenid_emp',
  'Event': 'Babylonian Revolt under Nebuchadnezzar IV',
  'Year': -521,
  'RA Notes': 'Event and Description: rebellion seems to be part of a broader series of uprisings following the death of Gaumata/Bardiya, suppressed by Darius I. Also, the rebellion seems to have resulted in a siege, that resulted in Nebuchadnezzar IV and his supporters being executed; is a ‘siege’ included in the ‘separatist rebellion’ or other types of instability, or should this be considered a separate type of instability? Just a thought, as above: should unsuccessful (vs. successful) separatist rebellions, etc, not be defined in these exact terms in the event/description fields, to differentiate these points of instability? References: unknown symbol/unclear referencing with regard to the Behistun Inscription. Dandamaev (1989) relevant and correct. RS 23/03/25.'},
 {'Zotero Link': None,
  'issues': ['References'],
  'Polity': 'ir_achaemenid_emp',
  'Event': 'Execution of Nebuchadnezzar III',
  'Year': -521,
  'RA Notes': 'General Note: should the battle that took place between Nebuchadnezzar III and Darius I near Sippar, be mentioned in the description, given it was a result of/after this defeat, that Nebuchadnezzar III was captured and executed? The latter might also suggest that many rather than a single individual were killed as a result of Nebuchadnezzar III seizing power in the northern part of Babylonia and a battle taking place with Darius I thereafter. References: unknown symbol/unclear referencing with regard to the Behistun Inscription. Kuhrt (2007) relevant and correct. RS 23/03/25.'},
 {'Zotero Link': None,
  'issues': ['Bad Row'],
  'Polity': 'ir_achaemenid_emp',
  'Event': 'Execution of Nebuchadnezzar IV',
  'Year': -520,
  'RA Notes': "Date: it seems that Nebuchadnezzar IV and a larger number of his supporters were executed following the capture of Babylon by the Persians sometime after November 521, which would make the year 520 incorrect. Description: this would need to be updated to take into account execution of multiple parties, if above information correct; online sources suggest that 2,497 Babylonian nobles who had supported Nebuchadnezzar IV's revolt, were killed alongside him. The intensity would therefore also have to be amended! References: unknown symbol/unclear referencing with regard to the Behistun Inscription. Dandamaev (1989) relevant and correct. RS 23/03/25."},
 {'Zotero Link': None,
  'issues': ['Description', 'Reference'],
  'Polity': 'ir_achaemenid_emp',
  'Event': 'Ionian Revolt',
  'Year': -499,
  'RA Notes': "Description: again, should unsuccessful (vs. successful) separatist rebellions, etc, not be defined in these exact terms in the event/description fields, to differentiate these points of instability? The Ionian rebels initially achieved some success, but the Persians, under Darius I, crushed the revolt, defeating the rebels at the Battle of Lade in 494. The revolt also led to the first major conflict between Greece and the Persian Empire, initiating the Greco-Persian Wars; the first Persian invasion of Greece occurred in 492. I'm including the above details here, as an example of the LLM not picking-up preceding and subsequent events that build a more concise and comprehensive overview of instability. References: unclear referencing with regard to Eisenbrauns and Herodotus. Briant (2002) relevant and correct. RS 23/03/25. "},
 {'Zotero Link': None,
  'issues': ['Bad Row'],
  'Polity': 'ir_achaemenid_emp',
  'Event': 'Assassination of Xerxes I',
  'Year': -465,
  'RA Notes': "Event and Description: no mention of the assassination of Xerxe's eldest son and other members of his court at the same time; the intensity field would likely also have to be amended, if the above information is correct. References: unclear referencing with regard to Ctesias, Persica. Olmstead (1948) relevant and correct. RS 23/03/25."},
 {'Zotero Link': 'C9K9R5PC',
  'issues': ['Bad Row'],
  'Polity': 'ir_achaemenid_emp',
  'Event': 'Assassination of Artaxerxes III',
  'Year': -338,
  'RA Notes': 'Event and Description: connected with the event below in the list, should this be treated separately? References: unclear referencing with regard to Eisenbrauns, Diodorus Siculus, and Bibliotheca Historica. Briant (2002) relevant and correct. RS 21/03/25.'},
 {'Zotero Link': None,
  'issues': ['Bad Row'],
  'Polity': 'ir_achaemenid_emp',
  'Event': 'Coup of Bagoas',
  'Year': -336,
  'RA Notes': 'Event and Description: series of coups mentioned in the description but not the event, should all of the latter sit under the same event? References: unclear referencing with regard to Diodorus Siculus, Bibliotheca Historica. Briant (2002) relevant and correct. RS 23/03/25.'},
 {'Zotero Link': None,
  'issues': ['Reference'],
  'Polity': 'ir_achaemenid_emp',
  'Event': 'Egyptian Separatist Rebellion under Khababash',
  'Year': -338,
  'RA Notes': 'General Notes: seems to have been known as Khabash primarily, also known as Khababash and Khabbash; dates of the event vary according to several sources, circa 2-3 years, 338-336 or 335. References: Depuydt (2006) seems to be incorrect as a source, possibly an amalgamation of text found by the LLM, but not a complete and correct reference. Also unclear referencing with regard to Diodorus Siculus, Bibliotheca Historica. RS 23/03/25. '},
 {'Zotero Link': 'C9K9R5PC',
  'issues': ['Reference'],
  'Polity': 'ir_achaemenid_emp',
  'Event': 'Execution of Artaxerxes IV Arses',
  'Year': -336,
  'RA Notes': 'References: unclear referencing with regard to Diodorus Siculus, Bibliotheca Historica. Briant (2002) relevant and correct. RS 21/03/25.'},
 {'Zotero Link': 'C9K9R5PC',
  'issues': ['Reference'],
  'Polity': 'ir_achaemenid_emp',
  'Event': 'Execution of Bagoas',
  'Year': -336,
  'RA Notes': 'References: unclear referencing with regard to Diodorus Siculus, Bibliotheca Historica. Briant (2002) relevant and correct. RS 21/03/25.'}]

class Command(BaseCommand):
    help = "Populate the Instability_event model with sample data"

    @transaction.atomic  # Ensures atomic DB transactions
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Starting data import..."))
        
        for event_data in NOTES_DATA:
        #for event_data in ultimate_notes_dics_list:
            # Create or get Instability_type records
            instability_checks = []
            for issue_name in event_data['issues']:
                if issue_name in ['References',]:
                    issue_name= 'Reference'
                inst_check, created = Check_choice.objects.get_or_create(name=issue_name)
                instability_checks.append(inst_check)

            # Polity
            #try:
            seshat_expert_instance = Seshat_Expert.objects.get(id=17)
            my_pol = Polity.objects.get(new_name=event_data['Polity'])
            event = Instability_event.objects.get(
                        name=event_data['Event'],
                        year_from=event_data['Year'],
                        polity_id=my_pol.id,
                    )
            my_pc = SeshatPrivateComment.objects.get(id=event.private_comment_id)
            if event_data['Zotero Link']:
                full_comment= event_data['RA Notes'] + f"(Suggested Zotero Link: {event_data['Zotero Link']})"
            else:
                full_comment= event_data['RA Notes']
            my_pc_part =  SeshatPrivateCommentPart.objects.create(
                private_comment_part_text=full_comment,
                private_comment=my_pc,
                private_comment_owner=seshat_expert_instance,
                created_date=datetime.datetime.now()
            )
            # except:
            #     print('Bad Pol')
            #     continue
            #print(my_pol)
            # Create Instability_event
      

            event.ra_check.set(instability_checks)
            

            self.stdout.write(self.style.SUCCESS(f"Added notes: {event.name}"))

        self.stdout.write(self.style.SUCCESS("Data import completed successfully!"))