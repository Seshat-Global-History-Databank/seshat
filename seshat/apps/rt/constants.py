__all__ = [
    "APP_NAME",
    "FREQUENCY_CHOICES",
    "ORDER_CHOICES",
    "PREVALENCE_CHOICES",
    "SWAPPED_DICT",
    "VARIABLE_DEFINITIONS",
]

APP_NAME = "rt"

FREQUENCY_CHOICES = (
    ("never", "never (absent)"),
    ("vr", "very rarely"),
    ("mftvr", "more frequently than very rarely"),
    ("unknown", "unknown"),
)

ORDER_CHOICES = (
    ("1", "1. Most widespread"),
    ("2", "2. Second most widespread"),
    ("3", "3. Third most widespread"),
    ("4", "4. Fourth most widespread"),
    ("9", "Other"),
)

PREVALENCE_CHOICES = (
    ("v_m", "Vast majority"),
    ("o_h_p", "Over half of the population"),
    ("sz_m", "Sizeable minority"),
    ("a_m", "Minority"),
    ("sm_m", "Small minority"),
    ("vs_m", "Very small minority"),
    ("unk", "unknown"),  # suspected goes into the tag
    ("unc", "uncoded"),
    ("n_d", "no_data"),  # none
)

SWAPPED_DICT = {
    "Widespread_religion": "Widespread religion",
    "Official_religion": "Official religion",
    "Elites_religion": "Elites religion",
    "Theo_sync_dif_rel": "Theological syncretism of different religions",
    "Sync_rel_pra_ind_beli": "Syncretism of religious practices at the level of individual believers",
    "Religious_fragmentation": "Religious fragmentation",
    "Gov_vio_freq_rel_grp": "Frequency of governmental violence against religious groups",
    "Gov_res_pub_wor": "Government restrictions on public worship",
    "Gov_res_pub_pros": "Government restrictions on public proselytizing",
    "Gov_res_conv": "Government restrictions on conversion",
    "Gov_press_conv": "Government pressure to convert",
    "Gov_res_prop_own_for_rel_grp": "Government restrictions on property ownership for adherents of any religious group",
    "Tax_rel_adh_act_ins": "Taxes based on religious adherence or on religious activities and institutions",
    "Gov_obl_rel_grp_ofc_reco": "Governmental obligations for religious groups to apply for official recognition",
    "Gov_res_cons_rel_buil": "Government restrictions on construction of religious buildings",
    "Gov_res_rel_edu": "Government restrictions on religious education",
    "Gov_res_cir_rel_lit": "Government restrictions on circulation of religious literature",
    "Gov_dis_rel_grp_occ_fun": "Government discrimination against religious groups taking up certain occupations or functions",
    "Soc_vio_freq_rel_grp": "Frequency of societal violence against religious groups",
    "Soc_dis_rel_grp_occ_fun": "Societal discrimination against religious groups taking up certain occupations or functions",
    "Gov_press_conv_for_aga": "Societal pressure to convert or against conversion",
}

# TODO: The last two values in this dictionary are doubled up. Verify with the team which one should be present here.
VARIABLE_DEFINITIONS = {
    "Official religion": "This variable is coded to capture the official religion within \
        the polity. It reflects the specific religious faith officially endorsed and \
        supported by the polity as the polity religion, if any.",
    "Elites religion": "Coded to capture the religion associated with or favored by the \
        political or societal elites within the polity, this variable reflects the \
        specific religious belief system prevalent among the elite class, if identifiable.",
    "Widespread religion": "This variable captures the prevalence of widespread religions \
        within the polity. It includes the most widespread religion, the second most \
        widespread religion, and up to the fourth most widespread religion if available. \
        The coding indicates the degree of prevalence of the corresponding religions in \
        the polity, providing insights into the distribution of religious beliefs across \
        the population.",
    "Theological syncretism of different religions": "This variable is coded to indicate \
        the presence or absence of theological syncretism among different religions within \
        the polity. It reflects whether diverse religious beliefs coexist and influence \
        each other's theological doctrines.",
    "Syncretism of religious practices at the level of individual believers": "Coded to \
        reflect the presence or absence of syncretism of religious practices at the \
        individual level, this variable signifies whether believers combine or adopt \
        practices from multiple religious traditions within the polity.",
    "Religious fragmentation": "Coded to assess the level of diversity and division among \
        religious groups within the polity, this variable indicates whether various \
        distinct religious factions or denominations exist, reflecting the degree of \
        religious diversity.",
    "Frequency of governmental violence against religious groups": "This variable is coded \
        to indicate the presence or absence of governmental violence against religious \
        groups within the polity. It provides insights into the relationship between the \
        state and religious communities, particularly in terms of conflict.",
    "Government restrictions on public worship": "Coded to reflect the presence or absence \
        of government control over public worship, this variable indicates whether \
        authorities regulate and limit religious gatherings and ceremonies within the \
        polity.",
    "Government restrictions on public proselytizing": "Coded to indicate the presence or \
        absence of government restrictions on public proselytizing, this variable reflects \
        the limitations imposed on the act of promoting or spreading religious beliefs to \
        others within the public domain of the polity.",
    "Government restrictions on conversion": "Coded to reflect the presence or absence of \
        government constraints on religious conversion, this variable indicates the degree \
        to which authorities regulate or restrict individuals' ability to change their \
        religious affiliation within the polity.",
    "Government pressure to convert": "Coded to indicate the presence or absence of \
        government-induced pressure for religious conversion, this variable reflects the \
        extent to which authorities influence or coerce individuals to adopt a specific \
        religious faith within the polity.",
    "Government restrictions on property ownership for adherents of any religious group": "Coded to indicate the presence or absence of government restrictions on property \
        ownership for religious adherents, this variable reflects limitations imposed on \
        individuals' rights to own property based on their religious affiliation within \
        the polity.",
    "Taxes based on religious adherence or on religious activities and institutions": "This variable is coded to indicate the presence or absence of taxes based on \
        religious adherence or on religious activities and institutions. It reflects the \
        financial burdens placed on religious individuals and institutions within the \
        polity.",
    "Governmental obligations for religious groups to apply for official recognition": "Coded to indicate the presence or absence of governmental obligations for \
        religious groups to seek official recognition, this variable reflects the extent \
        to which religious communities are required to obtain formal approval or \
        acknowledgment from authorities within the polity.",
    "Government restrictions on construction of religious buildings": "Coded to indicate \
        the presence or absence of government limitations on the construction of religious \
        buildings, this variable reflects the extent to which authorities regulate the \
        establishment of places of worship within the polity.",
    "Government restrictions on religious education": "Coded to indicate the presence or \
        absence of government restrictions on religious education, this variable reflects \
        limitations imposed on the teaching and dissemination of religious knowledge \
        within educational institutions in the polity.",
    "Government restrictions on circulation of religious literature": "Coded to indicate \
        the presence or absence of government restrictions on the circulation of religious \
        literature, this variable reflects limitations on the production, distribution, \
        and accessibility of religious texts within the polity.",
    "Government discrimination against religious groups taking up certain occupations or functions": "Coded to indicate the presence or absence of government discrimination against \
        religious groups in terms of access to specific occupations or functions, this \
        variable reflects the degree to which authorities limit certain roles based on \
        religious affiliation within the polity.",
    "Frequency of societal violence against religious groups": "This variable is coded to indicate the presence or absence of societal violence \
        against religious groups within the polity. It reflects the extent to which \
        non-governmental entities engage in violent actions against religious communities.",
    "Societal discrimination against religious groups taking up certain occupations or functions": "Coded to indicate the presence or absence of societal discrimination against \
        religious groups in occupational or functional contexts, this variable reflects \
        the degree to which individuals face discrimination based on their religious \
        affiliation within the polity.",
    "Societal pressure to convert or against conversion": "Coded to indicate the presence \
        or absence of societal pressure for religious conversion or against conversion, \
        this variable reflects the influence of social norms and expectations on \
        individuals' decisions to adopt or abandon specific religious beliefs within the \
        polity.",
    # "Frequency of governmental violence against religious groups": "This variable is \
    #   coded to measure the frequency of governmental violence against religious groups \
    #   within the polity. It indicates how often the government engages in violent \
    #   actions directed towards religious communities, providing insights into the \
    #   recurring nature of such incidents.",
    # "Frequency of societal violence against religious groups": "This variable is coded \
    #   to measure the frequency of societal violence against religious groups within the \
    #   polity. It reflects how often non-governmental entities, such as societal groups \
    #   or individuals, engage in violent actions against religious communities. The \
    #   variable provides insights into the recurring nature of violence originating from \
    #   societal sources against religious groups.",
}
