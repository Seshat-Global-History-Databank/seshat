crisisdb_var_defs = {
    'power_transition': '''
    We are interested in cataloguing the relative stability of past societies as proxied by the transition of power from one ruler to the next. In particular, we identify each transition of power (from named predecessor to named successor) and record whether it took place through normal succession mechanisms (whether legal/institutionalized means or customary/de facto procedures) or as the result of a conflict. We are seeking to record this information across the Seshat sample of polities, subject to availability of evidence. We are particularly interested in documenting the ebb and flow of stability in particular regions over time.<br><br>

            <div class="accordion accordion-flush pb-4" id="accordionpt_id">
                <div class="accordion-item" style="background-color:#fffdf2;">
                  <h2 class="accordion-header" id="headingOneCont">
                    <button class="accordion-button collapsed px-0" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOnept_id" aria-expanded="false" aria-controls="collapseOnept_id" style="background-color:#fffdf2; padding-top: 0.25rem !important; padding-bottom: 0.25rem !important;">
                      <span><i class="fa-solid fa-arrow-down-short-wide"></i> &nbsp; Coding Instructions:</span> 
                    </button>
                  </h2>
                  <div id="collapseOnept_id" class="accordion-collapse collapse" aria-labelledby="headingOneCont">
                    <div class="accordion-body table-responsive p-0">
                        <div class="pt_id">
    <b>Predecessor:</b> If a ruler came to power after a period during which the polity had no ruler (e.g. an interregnum), enter “None” in the predecessor field.<br>
<b>Successor:</b> If a ruler’s reign was followed by a period during which there was no ruler, enter “None” in the successor field.<br>
<b>Contested:</b> Was the transition from predecessor to successor contested in any way? Code present if there was a contest at any time from the end of the predecessor’s reign to the end of the first 365 days of the successor’s reign. This is a general variable covering many possibilities, disambiguated in other variables. It should also be coded present if the transition was contested in a way not covered by any of the other variables, e.g. the judiciary challenges the result of a presidential election.If there was a contest, code for the following types of contest (note: multiple types of contest can be present).<br>
<b>Overturn:</b> Was the predecessor forcibly removed from power, e.g. through assassination, forced abdication, external invasion forcing them into exile? Note: There will often be succession crises when there is no “normal line of succession,” so that there will be a “contested transition” with no overturn. Examples: 1. The dynasty ends with no heir (typical cause of a succession crisis); 2. The previous ruler has died and divided the kingdom between his sons (who then decide to fight for it all); 3. There is no formal succession procedure and every power transitions is a fight (e.g., Mamluk Sultanate). These cases should not qualify as a successful overturn as nobody is being overturned, but still count as a contested transition.<br>
<b>Predecessor assassination:</b> Was the predecessor assassinated? This does not have to be carried out by the ultimate successor or their allies, but applies to any killing. Judicially sanctioned executions (e.g. of Charles I of England) also count.<br>
<b>Intra-elite coup:</b> Code present if either 1. the predecessor was removed from power by an intra-elite coup; or 2. the successor was unsuccessfully challenged by rival elites during their first year.<br>
<b>Military revolt:</b> Code as for intra-elite coup, but for rebellions that have military leadership. “Military” refers to professional soldiers and officers, not to nobles who have armed retinues (these are counted as elites).<br>
<b>Popular uprising:</b> For rebellions in which the majority of participants are non-elites.<br>
<b>Separatist rebellion:</b> Part of the polity attempts to secede, whether successfully or unsuccessfully.<br>
<b>External invasion: </b> An external polity invades. An invasion does not have to aim specifically at removing the ruler in order to code this variable present. However, small border skirmishes do not justify a “present” code and can be ignored. <br>
<b>External interference: </b> Code this variable present when an external force helps internal rebels, e.g. by providing financial support or arms. Both external invasion and external interference may be present, e.g. when one polity sends military aid for a time, and then turns to an invasion.
                          </div>
                      </div>
                    </div>
                  </div>
                </div>

    ''',
}


