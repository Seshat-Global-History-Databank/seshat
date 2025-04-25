swapped_dict = {
    'Widespread_religion': 'Widespread religion',}


general_var_defs = {
    #'Polity capital':"The capital of a polity is connection point between an existing Polity instance and an existing Capital instance. Optionally, year range associations can be specified. If not provided, it implies that the capital remains constant throughout the entire duration of the polity's existence.",
    'polity_utm_zone': 'Usually where the capital city is locate. List only one per polity.',
    'polity_original_name': 'Original name of the polity.',
    'polity_alternative_name': 'Used in the historical literature; also supply the most common name used by the natives.',
    'polity_peak_years': 'The period when the polity was at its peak, whether militarily, in terms of the size of territory controlled, or the degree of cultural development. This variable has a subjective element, but typically historians agree when the peak was.',
    'polity_duration': 'The starting and ending dates of the polity. For example, the starting date could be the establishment of a long-ruling dynasty, while the ending date may be the year when the polity was conquered by an aggressive neighbor. In cases when starting and/or ending dates are fuzzy, as explained above, use the earliest possible starting date and the latest possible ending date. This approach will result in a temporal overlap, so that some NGAs for some periods will be coded as belonging to two polities simultaneously (e.g., to a disintegrating overarching polity and to the rising regional subpolity). Such overlap is acceptable, and will be dealt with at the analysis stage.',
    'polity_degree_of_centralization': """unknown/ quasi-polity/ nominal/ loose/ confederated state /unitary state

'quasi-polity' = or 'none'. Use if, for example, the NGA is inhabited by many politically independent groups. There are four types of quasi-polity: archaeological, temporal, complex and dominant. Quasi-Polities: further information.
'nominal' = regional rulers pay only nominal allegiance to the overall ruler and maintain independence on all important aspects of governing, including taxation and warfare. (example: Japan during the Sengoku period)
'loose' = the central government exercises a certain degree of control, especially over military matters and international relations. Otherwise the regional rulers are left alone (example: European 'feudalism' after the collapse of the Carolingian empire)
'confederated state' = regions enjoy a large degree of autonomy in internal (regional) government. In particular, the regional governors are either hereditary rulers, or are elected by regional elites or by the population of the region; and regional governments can levy and dispose of regional taxes. Use this category for the more centralized 'feudal states'.
'unitary state' = regional governors are appointed and removed by the central authorities, taxes are imposed by, and transmitted to the center""",
    'polity_suprapolity_relations': """unknown/ none/ alliance/ nominal allegiance/ personal union/ vassalage/

'alliance' = belongs to a long-term military-political alliance of independent polities ('long-term' refers to more or less permanent relationship between polities extending over multiple years)
'nominal allegiance' = same as 'nominal' under the variable "Degree of centralization" but now reflecting the position of the focal polity within the overarching political authority
'personal union' = the focal polity is united with another, or others, as a result of a dynastic marriage
'vassalage' = corresponding to 'loose' category in the Degree of centralization""",
    'polity_capital': 'The city where the ruler spends most of its time. If there were more than one capital supply all names and enclose in curly braces. For example, {Susa; Pasargadae; Persepolis; Ecbatana; Babylon}. Note that the capital may be different from the largest city (see below). Capital may be difficult to code for archaeologically known societies. If there is reasonable basis to believe that the largest known settlement was the seat of the ruler code it as capital (and indicate uncertainty in the narrative paragraph). Archaeologists are able to recognize special architectural structures, such as a ceremonial centres and some kind of citadels or palaces. These features could be recognized with certainty after a careful study of the whole region and the settlement network. If such an inference cannot be made, code as "unknown" (again, the largest settlement is coded elsewhere).',
    'polity_language': 'The language(s) used polity-wide for administration, religion, and military affairs.',
    'polity_linguistic_family': 'Linguistic family of the Polity.',
    'polity_language_genus': 'Language genus of the Polity.',
    'polity_religion_genus': 'Religion genus of the Polity.',
    'polity_religion_family': 'Religion family of the Polity.',
    'polity_religion': 'Religion of the Polity.',
    'polity_relationship_to_preceding_entity': 'Possible codes: continuity (gradual change), cultural assimilation (by another quasi-polity in the absence of substantial population replacement), elite migration (the preceding elites replaced by new elites coming from elsewhere), population migration (evidence for substantial population replacement), secession (from another polity). In the narrative paragraph explain the evidential basis for the code: what are the proxies for change? Examples include DNA data, isotope data, material (other than subsistence) culture, subsistence mode, symbolic culture (incl. burial practices), settlement patterns.',
    'polity_preceding_entity': "This code is based on the core region of the current polity (not the NGA region). E.g. Achaemenid Empire's core region was Persia, where they were preceded by the Median Empire.",
    'polity_succeeding_entity': "This code is based on the core region of the current polity (not the NGA region). E.g. Achaemenid Empire's core region was Persia, where they were preceded by the Median Empire.",
    'polity_supracultural_entity': "Our quasi-polity are often embedded within larger-scale cultural groupings of polities or quasi-polities. These are sometimes referred to as 'civilizations'. For example, medieval European kingdoms were part of Latin Christendom. During the periods of disunity in China, warring states there, nevertheless, belonged to the same Chinese cultural sphere. Archaeologists often use 'archaeological traditions' to denote such large-scale cultural entities (for example, Peregrine's Atlas of Cultural Evolution). Note, 'supracultural entity' refers to cultural interdependence, and is distinct from a political confederation or alliance, which should be coded under 'supra-polity relations.'",
    'polity_scale_of_supracultural_interaction': 'km squared. An estimate of the area encompassed by the supracultural entity',
    'polity_alternate_religion_genus': 'Alternate Religion genus of the Polity.',
    'polity_alternate_religion_family': 'Alternate Religion family of the Polity.',
    'polity_alternate_religion': 'Alternate Religion of the Polity.',
    'polity_religious_tradition': 'Religious tradition  of the Polity.',

}

