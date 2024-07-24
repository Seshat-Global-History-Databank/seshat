function updateSliderOutput() {
    if (slider.value < 0) {
        output.innerHTML = Math.abs(slider.value) + ' BCE';
    } else {
        output.innerHTML = slider.value + ' CE';
    }
}

function adjustSliderUp() {
    increment = Number(document.getElementById('increment').value)
    slider.value = Number(slider.value) + increment;
    enterYearInput.value = slider.value; // Sync enterYear input with dateSlide value
    updateSliderOutput(); // Update the displayed year
    plotPolities(); // This function is defined differently in the world_map and polity_map templates
}

function adjustSliderDown() {
    increment = Number(document.getElementById('increment').value)
    slider.value = Number(slider.value) - increment;
    enterYearInput.value = slider.value; // Sync enterYear input with dateSlide value
    updateSliderOutput(); // Update the displayed year
    plotPolities(); // This function is defined differently in the world_map and polity_map templates
}

function adjustSliderStartYear() {
    slider.value = slider.min;
    enterYearInput.value = slider.value; // Sync enterYear input with dateSlide value
    updateSliderOutput(); // Update the displayed year
    plotPolities(); // This function is defined differently in the world_map and polity_map templates
}

function adjustSliderEndYear() {
    slider.value = slider.max;
    enterYearInput.value = slider.value; // Sync enterYear input with dateSlide value
    updateSliderOutput(); // Update the displayed year
    plotPolities(); // This function is defined differently in the world_map and polity_map templates
}

function playRateValue() {
    var increment = Number(document.getElementById('increment').value);
    var playRate = document.getElementById('playRate')
    playRate.textContent = increment + ' y/s';
    plotPolities();
}

function setSliderTicks (tickYears) {
    var datalist = document.getElementById('yearTickmarks');
    var tickmarkValuesDiv = document.getElementById('yearTickmarkValues');

    // If the data list already has options, remove them
    while (datalist.firstChild) {
        datalist.removeChild(datalist.firstChild);
    };
    // If the tickmark values div already has spans, remove them
    while (tickmarkValuesDiv.firstChild) {
        tickmarkValuesDiv.removeChild(tickmarkValuesDiv.firstChild);
    };

    // Loop to add tickmarks
    i = 0;
    for (const tickValue of tickYears) {
        var option = document.createElement('option');
        option.value = tickValue;
        datalist.appendChild(option);

        // Create and add corresponding span for tickmark labels
        var span = document.createElement('span');
        span.textContent = tickValue;
        span.style.position = 'absolute';
        span.style.textAlign = 'center';

        // Use transform to center the span over the tickmark, with special handling for the first and last span
        var leftPercentage = (i / (tickYears.length - 1) * 100);
        span.style.left = `${leftPercentage}%`;
        if (i === 0) {
            span.style.transform = 'translateX(0%)'; // No translation for the first span
            span.style.textAlign = 'left'; // Align text to the left for the first span
       } else if (i === (tickYears.length - 1)) {
            span.style.transform = 'translateX(-100%)'; // Adjust the last span to prevent overflow
        } else {
            span.style.transform = 'translateX(-50%)'; // Center all other spans
        }
        tickmarkValuesDiv.appendChild(span);
        i++;
    }
};

function startPlay() {
    stopPlay(); // Clear existing interval before starting a new one
    var increment = Number(document.getElementById('increment').value);

    var milliseconds = 1 / (increment / 1000);

    playInterval = setInterval(function () {
        // Increment the slider value by 1
        slider.value = Number(slider.value) + 1;
        enterYearInput.value = slider.value; // Sync enterYear input with dateSlide value
        updateSliderOutput(); // Update the displayed year
        plotPolities(); // This function is defined differently in the world_map and polity_map templates

        // Stop playing when the slider reaches its maximum value
        if (slider.value >= parseInt(slider.max)) {
            stopPlay();
        }
    }, milliseconds); // Interval based on user input
}

function stopPlay() {
    clearInterval(playInterval);
}

function storeYear() {
    var year = document.getElementById('enterYear').value;
    history.pushState(null, '', '/core/world_map/?year=' + year);
    if (!allPolitiesLoaded) {
        document.getElementById('loadingIndicator').style.display = 'block';
    }
}

function switchBaseMap() {
    var selectedMap = document.querySelector('input[name="baseMap"]:checked').value;
    var base = document.getElementById("baseMapGADM").value

    if (base == 'province') {
        var baseShapeData = provinceShapeData;
    } else if (base == 'country') {
        var baseShapeData = countryShapeData;
    }

    // Only show "Current borders" select for GADM
    var baseMapGADMFieldset = document.getElementById("baseMapGADMFieldset");
    if (selectedMap == 'gadm') {
        baseMapGADMFieldset.style.display = "block"
    } else {
        baseMapGADMFieldset.style.display = "none"
    }

    // Remove all province layers
    provinceLayers.forEach(function (layer) {
        map.removeLayer(layer);
    });

    // Clear the provinceLayers array
    provinceLayers = [];

    map.removeLayer(currentLayer);

    if (selectedMap === 'osm') {
        currentLayer = baseLayers.osm.addTo(map);
    } else {
        currentLayer = baseLayers.carto.addTo(map);
    }

    if (selectedMap === 'gadm') {
        // Add countries or provinces to the base map
        baseShapeData.forEach(function (shape) {
            // Ensure the geometry is not empty
            if (shape.geometry && shape.geometry.type) {
                gadmFillColour = "#fffdf2";  // Default fill colour
                if (shape.country.toLowerCase().includes('sea')) {
                    gadmFillColour = 'lightblue';
                }
                // Loop through each polygon and add it to the map
                for (var i = 0; i < shape.geometry.coordinates.length; i++) {
                    var coordinates = shape.geometry.coordinates[i][0];
                    // Swap latitude and longitude for each coordinate
                    coordinates = coordinates.map(function (coord) {
                        return [coord[1], coord[0]];
                    });
                    var polygon = L.polygon(coordinates).addTo(map);
                    if (!shape.country.toLowerCase().includes('sea')) {
                        if (base == 'province') {
                            var popupContent = `
                                <table>
                                    <tr>
                                        <th>${shape.province}</th>
                                        <th></th>
                                    </tr>
                                    <tr>
                                        <td>Type</td>
                                        <td>${shape.provinceType}</td>
                                    </tr>
                                    <tr>
                                        <td>Country</td>
                                        <td>Modern ${shape.country}</td>
                                    </tr>
                                </table>
                            `;
                        } else if (base == 'country') {
                            var popupContent = `
                                <table>
                                    <tr>
                                        <th>Modern ${shape.country}</td>
                                    </tr>
                                </table>
                            `;
                        }
                        polygon.bindPopup(popupContent);
                    };               
                    // Set the style using the style method
                    polygon.setStyle({
                        fillColor: gadmFillColour,   // Set the fill color based on the "colour" field
                        color: 'black',       // Set the border color
                        weight: 1,            // Set the border weight
                        fillOpacity: 0.5        // Set the fill opacity
                    });
                    polygon.bringToBack(); // Move the province layers to back so they are always behind polity shapes
                    provinceLayers.push(polygon); // Add the layer to the array
                }
            }
        });
    }
}

function updateLegend() {
    var variable = document.getElementById('chooseVariable').value;
    var legendDiv = document.getElementById('variableLegend');
    var selectedYear1 = document.getElementById('dateSlide').value;  // Giving it the same name as a var used in the templated JS caused an error
    var selectedYearInt1 = parseInt(selectedYear1);
    var displayComponent = document.getElementById('switchPolitiesComponents').value;

    // Clear the current legend
    legendDiv.innerHTML = '';

    if (variable == 'polity') {
        var addedPolities = [];
        var addedPolityNames = [];
        shapesData.forEach(function (shape) {
            shape_name_col_dict = {};
            shape_name_col_dict['polity'] = shape.name;
            shape_name_col_dict['colour'] = shape.colour;
            if (shape.weight > 0 && !addedPolityNames.includes(shape_name_col_dict['polity'])) {
                // If the shape spans the selected year and should be displayed according to the shouldDisplayComponent() function
                if ((parseInt(shape.start_year) <= selectedYearInt1 && parseInt(shape.end_year) >= selectedYearInt1)
                    && shouldDisplayComponent(displayComponent, shape)
                ) {
                    // Add the polity to the list of added polities
                    addedPolities.push(shape_name_col_dict);
                    addedPolityNames.push(shape_name_col_dict['polity']);
                };
            };
        });

        // Sort the polities by name
        addedPolities.sort(function (a, b) {
            return a.polity.localeCompare(b.polity);
        });

        // After adding polities to the legend
        if (addedPolities.length > 0) {
            var legendTitle = document.createElement('h3');
            legendTitle.textContent = 'Selected Polities';
            legendDiv.appendChild(legendTitle);

            // Create a container for polity items
            var polityContainer = document.createElement('div');

            for (var i = 0; i < addedPolities.length; i++) {
                var legendItem = document.createElement('p');
                var colorBox = document.createElement('span');
                colorBox.style.display = 'inline-block';
                colorBox.style.width = '20px';
                colorBox.style.height = '20px';
                colorBox.style.backgroundColor = addedPolities[i].colour;
                colorBox.style.border = '1px solid black';
                colorBox.style.marginRight = '10px';
                legendItem.appendChild(colorBox);
                legendItem.appendChild(document.createTextNode(addedPolities[i].polity));
                polityContainer.appendChild(legendItem); // Append to the container
            }

            // Append the container to the legendDiv
            legendDiv.appendChild(polityContainer);

            // Make the polityContainer scrollable if there are more than 7 polities
            if (addedPolities.length > 7) {
                polityContainer.style.maxHeight = '420px'; // Adjust based on actual item height
                polityContainer.style.overflowY = 'scroll';
            } else {
                // Reset to default if fewer than 7 polities to ensure it behaves correctly on subsequent updates
                polityContainer.style.maxHeight = '';
                polityContainer.style.overflowY = '';
            }
        }

    } else if (variable in categorical_variables) {
        
        var legendTitle = document.createElement('h3');
        legendTitle.textContent = document.getElementById('chooseCategoricalVariableSelection').value;
        legendDiv.appendChild(legendTitle);

        for (var key in oneLanguageColourMapping) {
            if (key === 'No Seshat page') {  // Skip the "No Seshat page" key as it's the same colour as "Uncoded" (see world_map.html)
                continue;
            }
            var legendItem = document.createElement('p');

            var colorBox = document.createElement('span');
            colorBox.style.display = 'inline-block';
            colorBox.style.width = '20px';
            colorBox.style.height = '20px';
            colorBox.style.backgroundColor = oneLanguageColourMapping[key];
            colorBox.style.marginRight = '10px';
            legendItem.appendChild(colorBox);

            if (key === 'Unknown') {
                colorBox.style.border = '1px solid black';
            }
            if (key === 'Unknown') {
                legendItem.appendChild(document.createTextNode('Coded unknown'));
            } else {
                legendItem.appendChild(document.createTextNode(`${key}`));
            }

            legendDiv.appendChild(legendItem);
        };

    } else {  // Absent-present variables
        var legendTitle = document.createElement('h3');
        legendTitle.textContent = variable;
        legendDiv.appendChild(legendTitle);

        for (var key in variableColourMapping) {
            if (key === 'no seshat page') {  // Skip the "No Seshat page" key as it's the same colour as "Uncoded" (see world_map.html)
                continue;
            }
            var legendItem = document.createElement('p');

            var colorBox = document.createElement('span');
            colorBox.style.display = 'inline-block';
            colorBox.style.width = '20px';
            colorBox.style.height = '20px';
            colorBox.style.backgroundColor = variableColourMapping[key];
            colorBox.style.marginRight = '10px';
            legendItem.appendChild(colorBox);

            if (key === 'unknown') {
                colorBox.style.border = '1px solid black';
            }

            legendItem.appendChild(document.createTextNode(longAbsentPresentVarName(key)));

            legendDiv.appendChild(legendItem);
        }
    }

    if (document.querySelector('input[name="baseMap"]:checked').value == 'gadm') {
        var legendItem = document.createElement('p');

        var colorBox = document.createElement('span');
        colorBox.style.display = 'inline-block';
        colorBox.style.width = '20px';
        colorBox.style.height = '20px';
        colorBox.style.backgroundColor = '#fffdf2';
        colorBox.style.border = '1px solid black';
        colorBox.style.marginRight = '10px';

        legendItem.appendChild(colorBox);
        legendItem.appendChild(document.createTextNode('Base map'));

        legendDiv.appendChild(legendItem);
    }
}

function clearSelection() {
    document.getElementById('popup').innerHTML = '';
    shapesData.forEach(function (shape) {
        shape['weight'] = 0;
    });
    plotPolities();
}

function updateCategoricalVariableSelection(variable){
    var dropdown = document.getElementById('chooseCategoricalVariableSelection');
    dropdown.innerHTML = '';
    if (localStorage.getItem(variable)) {
        document.getElementById('chooseCategoricalVariableSelection').value = localStorage.getItem(variable);
    }
    if (categorical_variables[variable] && categorical_variables[variable].length > 0) {
        categorical_variables[variable].forEach(function (choice) {
            var option = document.createElement('option');
            option.value = choice;
            option.text = choice;

            // Set some default selections if no selection has been made
            if (localStorage.getItem(variable)) {
                if (localStorage.getItem(variable) === choice) {
                    option.selected = true;
                }
            } else {
                if (choice === 'Greek' || choice === 'Indo-European') {
                    option.selected = true;
                }
            }

            dropdown.appendChild(option);
        });
    }
    var varSelectElement = document.getElementById('chooseVariable');
    var varText = varSelectElement.options[varSelectElement.selectedIndex].text;
    document.querySelector('label[for="chooseCategoricalVariableSelection"]').textContent = varText + ': ';
}

function longAbsentPresentVarName(var_name){
    if (var_name === 'A~P') {
        var_name = 'Absent then Present';
    } else if (var_name === 'P~A') {
        var_name = 'Present then Absent';
    } else if (var_name === 'unknown') {
        var_name = 'Coded Unknown';
    } else if (var_name === 'no seshat page') {
        var_name = 'No Seshat Page';
    } else {
        var_name = `${var_name[0].toUpperCase()}${var_name.slice(1)}`;
    }
    return var_name;
}

function shouldDisplayComponent(displayComponent, shape) {
    if (displayComponent == 'polities'
        && (shape.member_of === null || shape.member_of === '')) {
        return true;
    } else if (displayComponent == 'components'
        && (shape.components === null || shape.components === '')) {
        return true;
    } else {
        return false;
    }
}

function populateVariableDropdown(variables) {
    const chooseVariableDropdown = document.getElementById('chooseVariable');
    chooseVariableDropdown.innerHTML = ''; // Clear existing options

    // Add the static option
    const staticOption = document.createElement('option');
    staticOption.value = 'polity';
    staticOption.textContent = 'Polity';
    chooseVariableDropdown.appendChild(staticOption);

    // Process 'General Variables' first
    if (variables['General Variables']) {
        const optgroup = document.createElement('optgroup');
        optgroup.label = 'General Variables';
        Object.entries(variables['General Variables']).forEach(([variable, details]) => {
            const option = document.createElement('option');
            option.value = details.formatted;
            option.textContent = details.full_name;
            optgroup.appendChild(option);
        });
        chooseVariableDropdown.appendChild(optgroup);
    }

    // Process other categories
    Object.entries(variables).forEach(([category, vars]) => {
        if (category !== 'General Variables') {
            const optgroup = document.createElement('optgroup');
            optgroup.label = category;
            Object.entries(vars).forEach(([variable, details]) => {
                const option = document.createElement('option');
                option.value = details.formatted;
                option.textContent = details.full_name;
                optgroup.appendChild(option);
            });
            chooseVariableDropdown.appendChild(optgroup);
        }
    });
}

function setBlur(layer) {
    var polityYear = layer.feature.properties.polity_start_year;
    var stdDeviationValue;
    if (polityYear < 0) {
        stdDeviationValue = 2;
    } else if (polityYear < 1500) {
        stdDeviationValue = 1;
    } else {
        stdDeviationValue = 0;
    }

    // Generate a unique filter ID based on the stdDeviationValue or another unique property
    var filterId = 'shape-blur-' + stdDeviationValue;

    // Check if the filter already exists, if not, create it
    if (!document.getElementById(filterId)) {
        var svgDefs = document.querySelector('svg defs') || createSvgDefs();
        var filter = document.createElementNS('http://www.w3.org/2000/svg', 'filter');
        filter.setAttribute('id', filterId);
        var feGaussianBlur = document.createElementNS('http://www.w3.org/2000/svg', 'feGaussianBlur');
        feGaussianBlur.setAttribute('stdDeviation', stdDeviationValue);
        filter.appendChild(feGaussianBlur);
        svgDefs.appendChild(filter);
    }

    // Apply the unique filter to this layer's path elements
    layer._path.style.filter = 'url(#' + filterId + ')';
}

// Helper function to create SVG defs if it doesn't exist
function createSvgDefs() {
    var svgElement = document.querySelector('svg');
    var defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
    svgElement.appendChild(defs);
    return defs;
}