from django import template

register = template.Library()

@register.filter
def get_attributes(obj):
    """
    A custom filter to get all attributes of an object in a template.

    Args:
        obj (object): The object to get attributes from.

    Returns:
        dict: A dictionary of the object's attributes.
    """
    return vars(obj)

@register.filter
def zip_lists(a, b):
    """
    A custom filter to zip two lists together in a template.

    Args:
        a (list): The first list to zip.
        b (list): The second list to zip.

    Returns:
        zip: A zip object of the two lists.
    """
    return zip(a, b)

# RA_NOTES
# comments = {
#     "RS": {
#         "21/03/25": {
#             1: {"text": "Reference needs verification.", "writer": "John Doe"},
#             26: {"text": "Check the date of the event.", "writer": "Jane Smith"},
#             2: {"text": "Update required for accuracy.", "writer": "Alice Brown"},
#             5: {"text": "Possible duplicate entry.", "writer": "Bob White"},
#             24: {"text": "Reword for clarity.", "writer": "Charlie Green"},
#             27: {"text": "Missing citation.", "writer": "David Black"},
#             3: {"text": "Connected with the Event: Coup of Darius I against Bardiya, should this be treated separately?", "writer": "RS"}
#         },
#         "23/03/25": {
#             4: {"text": "Data inconsistency detected.", "writer": "Eve Adams"},
#             25: {"text": "Cross-check with other sources.", "writer": "Frank Harris"},
#             8: {"text": "Clarify terminology usage.", "writer": "Grace Lee"},
#             6: {"text": "Update needed to reflect executions of multiple parties following the capture of Babylon.", "writer": "RS"},
#             7: {"text": "Should unsuccessful rebellions be explicitly defined differently?", "writer": "RS"}
#         },
#         "28/03/25": {
#             9: {"text": "Potential conflict in sources.", "writer": "Henry Clark"},
#             12: {"text": "Adjust formatting for readability.", "writer": "Ivy Walker"},
#             13: {"text": "Ensure alignment with the dataset.", "writer": "Jack Hall"}
#         },
#         "30/03/25": {
#             14: {"text": "Reevaluate classification criteria.", "writer": "Karen Lewis"},
#             18: {"text": "Improve explanation of context.", "writer": "Liam Scott"},
#             19: {"text": "Confirm with primary sources.", "writer": "Mia Roberts"},
#             10: {"text": "Brief mention in Olmstead (1948), should alternative spelling of 'Hystaspes' be added?", "writer": "RS"}
#         }
#     },
#     "SH": {
#         "31/03": {
#             210: {"text": "Review structure for coherence.", "writer": "Noah King"},
#             221: {"text": "Clarify ambiguous phrasing.", "writer": "Olivia Turner"},
#             229: {"text": "Sources do not confirm a separatist rebellion, more of an uprising?", "writer": "SH"}
#         }
#     },
#     "General": {
#         "No Date": {
#             214: {"text": "Grammar check required.", "writer": "Paul Martinez"},
#             215: {"text": "Expand on related historical events.", "writer": "Quinn Perez"},
#             217: {"text": "Simplify overly complex sentence.", "writer": "Rachel Stewart"},
#             220: {"text": "Align terminology with standard usage.", "writer": "Samuel Edwards"},
#             149: {"text": "Verify source credibility.", "writer": "Tina Collins"},
#             209: {"text": "Remove redundant information.", "writer": "Umar Foster"},
#             204: {"text": "Update statistical figures.", "writer": "Vera Simmons"},
#             230: {"text": "Ensure logical flow between sections.", "writer": "Walter Hughes"},
#             150: {"text": "Extent may need to be changed to 3 as Miletus was a city with a small castle.", "writer": "General"},
#             206: {"text": "Duplicate: 'Execution of Valentinus' and 'Rebellion of Valentinus' could be separate but relate to the same event.", "writer": "General"},
#             212: {"text": "Mezezius was executed, intensity should be 1 as no other deaths mentioned.", "writer": "General"},
#             216: {"text": "Year should be 706.", "writer": "General"}
#         }
#     }
# }
