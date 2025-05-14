from django.core.management.base import BaseCommand
from django.urls import reverse, resolve
from django.conf import settings
from seshat.apps.core.models import Variablehierarchy, Section
from django.utils.text import slugify
import inflect
import requests

p = inflect.engine()


class Command(BaseCommand):
    help = "Check if all Variablehierarchy names can be used to generate valid API endpoints."

    def handle(self, *args, **kwargs):
        base_url = getattr(settings, 'BASE_URL', 'http://127.0.0.1:8000')
        failed = []
        failed_dic = {}
        passed_dic = {}

        for vh in Variablehierarchy.objects.all():
            section: Section = vh.section
            if not section or not section.db_table_name:
                self.stdout.write(self.style.WARNING(f"Skipping variable '{vh.name}' (no section)."))
                continue

            slug_name = slugify(vh.name)
            majid_name = vh.name.lower().replace(' ', '-')
            plural_slug = p.plural(slug_name)
            majid_plural = majid_name + "s"

            endpoint = f"/api/{section.db_table_name}/{plural_slug}/"
            full_url = f"{base_url}{endpoint}"

            endpoint2 = f"/api/{section.db_table_name}/{majid_plural}/"
            full_url2 = f"{base_url}{endpoint2}"
            #print(full_url2)

            endpoint3 = f"/api/{section.db_table_name}/{majid_name}/"
            full_url3 = f"{base_url}{endpoint3}"
            #print(full_url2)

            mapped_names = {
                'Leather Cloth': '/api/wf/leathers/',
                'Small Vessels Canoes Etc': '/api/wf/small-vessel-canoe-etc/',
                'Merchant Ships Pressed Into Service': '/api/wf/merchant-ship-pressed-into-service/',
                'Settlements In A Defensive Position': '/api/wf/settlement-in-defensive-positions/',
                'Drinking Water Supply System': '/api/sc/drinking-water-supplies/',
                'Government Restrictions On Property Ownership For Adherents Of Any Religious Group': '/api/rt/government-restrictions-on-property-ownership-for-adherents-of-any-religious-groups/',
                'Polity Utm Zone': '/api/general/polity-utm-timezones/',
                'Fine Ceramic Wares': '/api/ec/lux-fine-ceramic-wares/',
                'Polity Suprapolity Relations': '/api/general/polity-suprapolities/',
                #'Polity Relationship To Preceding Entity': '/api/general/polity relationships-to-preceding entity/',
                'Precious Metal': '/api/ec/lux-precious-metal/',
                'Luxury Drink/Alcohol': '/api/ec/luxury-drink-alcohol/',
                'Precious Stone': '/api/ec/lux-precious-stone/',
                'Statuary': '/api/ec/lux-statuary/',
                'Human Sacrifice': '/api/rt/human-sacrifices/',
            }

            if vh.name in mapped_names:
                endpoint = f"{mapped_names[vh.name]}"
                full_url = f"{base_url}{endpoint}"


            try:
                response = requests.get(full_url)
                response2 = requests.get(full_url2)
                response3 = requests.get(full_url3)
                if response.status_code == 200:
                    self.stdout.write(self.style.SUCCESS(f"✓ {full_url} exists"))
                    passed_dic[vh.name] = endpoint
                elif response2.status_code == 200:
                    self.stdout.write(self.style.SUCCESS(f"✓✓ {full_url2} exists"))
                    passed_dic[vh.name] = endpoint2
                elif response3.status_code == 200:
                    self.stdout.write(self.style.SUCCESS(f"✓✓✓ {full_url3} exists"))
                    passed_dic[vh.name] = endpoint3
                else:
                    self.stdout.write(self.style.ERROR(f"✗ {full_url} returned {response.status_code}"))
                    failed.append((vh.id, vh.name, full_url))
                    failed_dic[vh.name] = endpoint
            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.ERROR(f"✗ Failed to access {full_url}: {e}"))
                failed.append((vh.id, vh.name, full_url))

        self.stdout.write("\nSummary:")
        if failed:
            self.stdout.write(self.style.ERROR(f"{len(failed)} endpoints failed:"))
            for fid, fname, furl in failed:
                self.stdout.write(f"  [{fid}] {fname} → {furl}")
        else:
            self.stdout.write(self.style.SUCCESS("All endpoints are valid."))

        print('####### PASSED ####')
        print(passed_dic)
        print('###################')
        print('####### Failed ####')
        print(failed_dic)
        print('###################')

####### PASSED ####
# {'Calendar': '/api/sc/calendars/',
# 'Sacred Text': '/api/sc/sacred-texts/',
# 'Religious Literature': '/api/sc/religious-literatures/',
# 'Practical Literature': '/api/sc/practical-literatures/',
# 'History': '/api/sc/histories/',
# 'Philosophy': '/api/sc/philosophies/',
# 'Scientific Literature': '/api/sc/scientific-literatures/',
# 'Fiction': '/api/sc/fictions/',
# 'Article': '/api/sc/articles/',
# 'Token': '/api/sc/tokens/',
# 'Precious Metal': '/api/sc/precious-metals/',
# 'Foreign Coin': '/api/sc/foreign-coins/',
# 'Indigenous Coin': '/api/sc/indigenous-coins/',
# 'Paper Currency': '/api/sc/paper-currencies/',
# 'Courier': '/api/sc/couriers/',
# 'Postal Station': '/api/sc/postal-stations/',
# 'General Postal Service': '/api/sc/general-postal-services/',
# 'Fastest Individual Communication': '/api/sc/fastest-individual-communications/',
# 'communal building': '/api/sc/communal-buildings/',
# 'Utilitarian Public Building': '/api/sc/utilitarian-public-buildings/',
# 'Symbolic Building': '/api/sc/symbolic-buildings/',
# 'Entertainment Building': '/api/sc/entertainment-buildings/',
# 'Knowledge Or Information Building': '/api/sc/knowledge-or-information-buildings/',
# 'Other Utilitarian Public Building': '/api/sc/other-utilitarian-public-buildings/',
# 'Special Purpose Site': '/api/sc/special-purpose-sites/',
# 'Ceremonial Site': '/api/sc/ceremonial-sites/',
# 'Burial Site': '/api/sc/burial-sites/',
# 'Trading Emporia': '/api/sc/trading-emporia/',
# 'Enclosure': '/api/sc/enclosures/',
# 'Length Measurement System': '/api/sc/length-measurement-systems/',
# 'Area Measurement System': '/api/sc/area-measurement-systems/',
# 'Volume Measurement System': '/api/sc/volume-measurement-systems/',
# 'Weight Measurement System': '/api/sc/weight-measurement-systems/',
# 'Long Wall': '/api/wf/long-walls/',
# 'Copper': '/api/wf/coppers/',
# 'Bronze': '/api/wf/bronzes/',
# 'Iron': '/api/wf/irons/',
# 'Steel': '/api/wf/steels/',
# 'Javelin': '/api/wf/javelins/',
# 'Atlatl': '/api/wf/atlatls/',
# 'Sling': '/api/wf/slings/',
# 'Self Bow': '/api/wf/self-bows/',
# 'Composite Bow': '/api/wf/composite-bows/',
# 'Crossbow': '/api/wf/crossbows/',
# 'Tension Siege Engine': '/api/wf/tension-siege-engines/',
# 'Sling Siege Engine': '/api/wf/sling-siege-engines/',
# 'Gunpowder Siege Artillery': '/api/wf/gunpowder-siege-artilleries/',
# 'Handheld Firearm': '/api/wf/handheld-firearms/',
# 'War Club': '/api/wf/war-clubs/',
# 'Battle Axe': '/api/wf/battle-axes/',
# 'Dagger': '/api/wf/daggers/',
# 'Sword': '/api/wf/swords/',
# 'Spear': '/api/wf/spears/',
# 'Polearm': '/api/wf/polearms/',
# 'Dog': '/api/wf/dogs/',
# 'Donkey': '/api/wf/donkeys/',
# 'Horse': '/api/wf/horses/',
# 'Camel': '/api/wf/camels/',
# 'Elephant': '/api/wf/elephants/',
# 'Wood Bark Etc': '/api/wf/wood-bark-etc/',
# 'Shield': '/api/wf/shields/',
# 'Helmet': '/api/wf/helmets/',
# 'Breastplate': '/api/wf/breastplates/',
# 'Limb Protection': '/api/wf/limb-protections/',
# 'Scaled Armor': '/api/wf/scaled-armors/',
# 'Laminar Armor': '/api/wf/laminar-armors/',
# 'Plate Armor': '/api/wf/plate-armors/',
# 'Specialized Military Vessel': '/api/wf/specialized-military-vessels/',
# 'Wooden Palisade': '/api/wf/wooden-palisades/',
# 'Earth Rampart': '/api/wf/earth-ramparts/',
# 'Ditch': '/api/wf/ditches/',
# 'Moat': '/api/wf/moats/',
# 'Stone Walls Non Mortared': '/api/wf/stone-walls-non-mortared/',
# 'Stone Walls Mortared': '/api/wf/stone-walls-mortared/',
# 'Fortified Camp': '/api/wf/fortified-camps/',
# 'Complex Fortification': '/api/wf/complex-fortifications/',
# 'Modern Fortification': '/api/wf/modern-fortifications/',
# 'Chainmail': '/api/wf/chainmails/',
# 'Polity Territory': '/api/sc/polity-territories/',
# 'Polity Population': '/api/sc/polity-populations/',
# 'Population Of The Largest Settlement': '/api/sc/population-of-the-largest-settlements/',
# 'Settlement Hierarchy': '/api/sc/settlement-hierarchies/',
# 'Administrative Level': '/api/sc/administrative-levels/',
# 'Religious Level': '/api/sc/religious-levels/',
# 'Phonetic Alphabetic Writing': '/api/sc/phonetic-alphabetic-writings/',
# 'Lists Tables And Classification': '/api/sc/lists-tables-and-classifications/',
# 'Military Level': '/api/sc/military-levels/',
# 'Professional Military Officer': '/api/sc/professional-military-officers/',
# 'Professional Soldier': '/api/sc/professional-soldiers/',
# 'Professional Priesthood': '/api/sc/professional-priesthoods/',
# 'Full Time Bureaucrat': '/api/sc/full-time-bureaucrats/',
# 'Examination System': '/api/sc/examination-systems/',
# 'Merit Promotion': '/api/sc/merit-promotions/',
# 'Specialized Government Building': '/api/sc/specialized-government-buildings/',
# 'Formal Legal Code': '/api/sc/formal-legal-codes/',
# 'Judge': '/api/sc/judges/',
# 'Court': '/api/sc/courts/',
# 'Professional Lawyer': '/api/sc/professional-lawyers/',
# 'Irrigation System': '/api/sc/irrigation-systems/',
# 'Market': '/api/sc/markets/',
# 'Food Storage Site': '/api/sc/food-storage-sites/',
# 'Road': '/api/sc/roads/',
# 'Bridge': '/api/sc/bridges/',
# 'Canal': '/api/sc/canals/',
# 'Port': '/api/sc/ports/',
# 'Mines Or Quarry': '/api/sc/mines-or-quarries/',
# 'Mnemonic Device': '/api/sc/mnemonic-devices/',
# 'Nonwritten Record': '/api/sc/nonwritten-records/',
# 'Written Record': '/api/sc/written-records/',
# 'Script': '/api/sc/scripts/',
# 'Non Phonetic Writing': '/api/sc/non-phonetic-writings/',
# 'Time Measurement System': '/api/sc/time-measurement-systems/',
# 'Geometrical Measurement System': '/api/sc/geometrical-measurement-systems/',
# 'Other Measurement System': '/api/sc/other-measurement-systems/',
# 'Debt And Credit Structure': '/api/sc/debt-and-credit-structures/',
# 'Store Of Wealth': '/api/sc/stores-of-wealth/',
# 'Source Of Support': '/api/sc/sources-of-support/',
# 'Occupational Complexity': '/api/sc/occupational-complexities/',
# 'Special Purpose House': '/api/sc/special-purpose-houses/',
# 'Other Special Purpose Site': '/api/sc/other-special-purpose-sites/',
# 'Largest Communication Distance': '/api/sc/largest-communication-distances/',
# 'Official Religion': '/api/rt/official-religions/',
# 'Elites Religion': '/api/rt/elites-religions/',
# 'Theological Syncretism Of Different Religions': '/api/rt/theological-syncretism-of-different-religions/',
# 'Syncretism Of Religious Practices At The Level Of Individual Believers': '/api/rt/syncretism-of-religious-practices-at-the-level-of-individual-believers/',
# 'Religious Fragmentation': '/api/rt/religious-fragmentations/',
# 'Frequency Of Governmental Violence Against Religious Groups': '/api/rt/frequency-of-governmental-violence-against-religious-groups/',
# 'Government Restrictions On Public Worship': '/api/rt/government-restrictions-on-public-worships/',
# 'Government Restrictions On Public Proselytizing': '/api/rt/government-restrictions-on-public-proselytizings/',
# 'Government Restrictions On Conversion': '/api/rt/government-restrictions-on-conversions/',
# 'Government Pressure To Convert': '/api/rt/government-pressure-to-converts/',
# 'Taxes Based On Religious Adherence Or On Religious Activities And Institutions': '/api/rt/taxes-based-on-religious-adherence-or-on-religious-activities-and-institutions/',
# 'Governmental Obligations For Religious Groups To Apply For Official Recognition': '/api/rt/governmental-obligations-for-religious-groups-to-apply-for-official-recognitions/',
# 'Government Restrictions On Construction Of Religious Buildings': '/api/rt/government-restrictions-on-construction-of-religious-buildings/',
# 'Government Restrictions On Religious Education': '/api/rt/government-restrictions-on-religious-educations/',
# 'Government Restrictions On Circulation Of Religious Literature': '/api/rt/government-restrictions-on-circulation-of-religious-literatures/',
# 'Government Discrimination Against Religious Groups Taking Up Certain Occupations Or Functions': '/api/rt/government-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions/',
# 'Frequency Of Societal Violence Against Religious Groups': '/api/rt/frequency-of-societal-violence-against-religious-groups/',
# 'Societal Discrimination Against Religious Groups Taking Up Certain Occupations Or Functions': '/api/rt/societal-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions/',
# 'Societal Pressure To Convert Or Against Conversion': '/api/rt/societal-pressure-to-convert-or-against-conversions/',
# 'Moralizing Supernatural Concern Is Primary': '/api/rt/moralizing-supernatural-concern-is-primary/',
# 'Moralizing Enforcement Is Certain': '/api/rt/moralizing-enforcement-is-certain/',
# 'Moralizing Enforcement Is Broad': '/api/rt/moralizing-enforcement-is-broad/',
# 'Moralizing Enforcement Is Targeted': '/api/rt/moralizing-enforcement-is-targeted/',
# 'Moralizing Enforcement Of Rulers': '/api/rt/moralizing-enforcement-of-rulers/',
# 'Moralizing Religion Adopted By Elites': '/api/rt/moralizing-religion-adopted-by-elites/',
# 'Moralizing Religion Adopted By Commoners': '/api/rt/moralizing-religion-adopted-by-commoners/',
# 'Moralizing Enforcement In Afterlife': '/api/rt/moralizing-enforcement-in-afterlife/',
# 'Moralizing Enforcement In This Life': '/api/rt/moralizing-enforcement-in-this-life/',
# 'Moralizing Enforcement Is Agentic': '/api/rt/moralizing-enforcement-is-agentic/',
# 'Polity Original Name': '/api/general/polity-original-names/',
# 'Polity Alternative Name': '/api/general/polity-alternative-names/',
# 'Polity Peak Years': '/api/general/polity-peak-years/',
# 'Polity Duration': '/api/general/polity-durations/',
# 'Polity Degree Of Centralization': '/api/general/polity-degree-of-centralizations/',
# 'Polity Capital': '/api/general/polity-capitals/',
# 'Polity Language': '/api/general/polity-languages/',
# 'Polity Linguistic Family': '/api/general/polity-linguistic-families/',
# 'Polity Language Genus': '/api/general/polity-language-genuses/',
# 'Polity Religion Genus': '/api/general/polity-religion-genuses/',
# 'Polity Religion Family': '/api/general/polity-religion-families/',
# 'Polity Religion': '/api/general/polity-religions/',
# 'Polity Preceding Entity': '/api/general/polity-preceding-entities/',
# 'Polity Succeeding Entity': '/api/general/polity-succeeding-entities/',
# 'Polity Supracultural Entity': '/api/general/polity-supracultural-entities/',
# 'Polity Scale Of Supracultural Interaction': '/api/general/polity-scale-of-supracultural-interactions/',
# 'Polity Alternate Religion Genus': '/api/general/polity-alternate-religion-genuses/',
# 'Polity Alternate Religion Family': '/api/general/polity-alternate-religion-families/',
# 'Polity Alternate Religion': '/api/general/polity-alternate-religions/',
# 'Polity Religious Tradition': '/api/general/polity-religious-traditions/',
# 'Luxury Fabrics': '/api/ec/luxury-fabrics/',
# 'Luxury Manufactured Goods': '/api/ec/luxury-manufactured-goods/',
# 'Luxury Spices Incense And Dyes': '/api/ec/luxury-spices-incense-and-dyes/',
# 'Luxury Glass Goods': '/api/ec/luxury-glass-goods/',
# 'Luxury Food': '/api/ec/luxury-food/',
# 'Other Luxury Personal Items': '/api/ec/other-luxury-personal-items/',
# 'Crisis Consequence': '/api/crisisdb/crisis-consequences/',


# 'Leather Cloth': '/api/wf/leathers/',
# 'Small Vessels Canoes Etc': '/api/wf/small-vessel-canoe-etc/',
# 'Merchant Ships Pressed Into Service': '/api/wf/merchant-ship-pressed-into-service/',
# 'Settlements In A Defensive Position': '/api/wf/settlement-in-defensive-positions/',
# 'Drinking Water Supply System': '/api/sc/drinking-water-supplies/',
# 'Government Restrictions On Property Ownership For Adherents Of Any Religious Group': '/api/rt/government-restrictions-on-property-ownership-for-adherents-of-any-religious-groups/',
# 'Polity Utm Zone': '/api/general/polity-utm-timezones/',
# 'Fine Ceramic Wares': '/api/ec/fine-ceramic-wares/',
# 'Polity Suprapolity Relations': '/api/general/polity-suprapolities/',
# #'Polity Relationship To Preceding Entity': '/api/general/polity relationships-to-preceding entity/',
# 'Precious Metal': '/api/ec/lux-precious-metal/',
# 'Luxury Drink/Alcohol': '/api/ec/luxury-drink-alcohol/',
# 'Precious Stone': '/api/ec/lux-precious-stone/',
# 'Statuary': '/api/ec/lux-statuary/',
# 'Human Sacrifice': '/api/rt/human-sacrifices/',

# }
# ###################
# ####### Failed ####

# ###################
