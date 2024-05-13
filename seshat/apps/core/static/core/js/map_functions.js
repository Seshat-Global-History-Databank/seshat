function updateSliderOutput() {
    if (slider.value < 0) {
        output.innerHTML = Math.abs(slider.value) + ' BCE';
    } else {
        output.innerHTML = slider.value + ' CE';
    }
}

function adjustSliderUp() {
    slider.value = Number(slider.value) + 1;
    enterYearInput.value = slider.value; // Sync enterYear input with dateSlide value
    updateSliderOutput(); // Update the displayed year
    plotPolities(); // This function is defined differently in the world_map and polity_map templates
}

function adjustSliderDown() {
    slider.value = Number(slider.value) - 1;
    enterYearInput.value = slider.value; // Sync enterYear input with dateSlide value
    updateSliderOutput(); // Update the displayed year
    plotPolities(); // This function is defined differently in the world_map and polity_map templates
}

function startPlay() {
    stopPlay(); // Clear existing interval before starting a new one

    var animationSpeed = parseFloat(playRateInput.value);
    if (animationSpeed == 1) {
        var yearsPerSecond = 1;
    } else if (animationSpeed == 2) {
        var yearsPerSecond = 5;
    } else if (animationSpeed == 3) {
        var yearsPerSecond = 20;
    } else if (animationSpeed == 4) {
        var yearsPerSecond = 50;
    } else if (animationSpeed == 5) {
        var yearsPerSecond = 100;
    }

    var milliseconds = 1 / (yearsPerSecond / 1000);

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
        // Refresh the page to load all polities
        location.reload();
        var loadingTextElement = document.getElementById('loadingText');
        loadingTextElement.innerHTML = 'Loading polities for <b>' + year + '</b>...';
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
                gadmFillColour = 'none';  // Default fill colour
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
                        fillOpacity: 1        // Set the fill opacity
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

    // Clear the current legend
    legendDiv.innerHTML = '';

    if (variable == 'polity') {
        var addedPolities = [];
        var addedPolityNames = [];
        shapesData.forEach(function (shape) {
            // If the polity shape is part of a personal union or meta-polity active in the selected year, don't add it to the legend
            var ignore = false;
            if (shape.union_name) {
                if ((parseInt(shape.union_start_year) <= selectedYearInt1 && parseInt(shape.union_end_year) >= selectedYearInt1)) {
                    ignore = true;
                };
            };
            if (!ignore) {
                shape_name_col_dict = {};
                shape_name_col_dict['polity'] = shape.polity;
                shape_name_col_dict['colour'] = shape.colour;
                if (shape.weight > 0 && !addedPolityNames.includes(shape_name_col_dict['polity'])) {
                    // If the shape spans the selected year
                    if ((parseInt(shape.start_year) <= selectedYearInt1 && parseInt(shape.end_year) >= selectedYearInt1)) {
                        // Add the polity to the list of added polities
                        addedPolities.push(shape_name_col_dict);
                        addedPolityNames.push(shape_name_col_dict['polity']);
                    };
                };
            };
        });

        // Sort the polities by name
        addedPolities.sort(function (a, b) {
            return a.polity.localeCompare(b.polity);
        });

        // Add a legend for highlighted polities
        if (addedPolities.length > 0) {
            var legendTitle = document.createElement('h3');
            legendTitle.textContent = 'Selected Polities';
            legendDiv.appendChild(legendTitle);
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
                legendDiv.appendChild(legendItem);
            }
        };

    } else if (variable in categorical_variables) {
        
        var legendTitle = document.createElement('h3');
        legendTitle.textContent = document.getElementById('chooseCategoricalVariableSelection').value;
        legendDiv.appendChild(legendTitle);

        for (var key in oneLanguageColourMapping) {
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

            if (key === 'A~P') {
                legendItem.appendChild(document.createTextNode('Absent then present'));
            } else if (key === 'P~A') {
                legendItem.appendChild(document.createTextNode('Present then absent'));
            } else if (key === 'unknown') {
                legendItem.appendChild(document.createTextNode('Coded unknown'));
            } else {
                legendItem.appendChild(document.createTextNode(`${key[0].toUpperCase()}${key.slice(1)}`));
            }

            legendDiv.appendChild(legendItem);
        }
    }

    if (document.querySelector('input[name="baseMap"]:checked').value == 'gadm') {
        var legendItem = document.createElement('p');

        var colorBox = document.createElement('span');
        colorBox.style.display = 'inline-block';
        colorBox.style.width = '20px';
        colorBox.style.height = '20px';
        colorBox.style.backgroundColor = 'white';
        colorBox.style.border = '1px solid black';
        colorBox.style.marginRight = '10px';

        legendItem.appendChild(colorBox);
        legendItem.appendChild(document.createTextNode('Base map'));

        legendDiv.appendChild(legendItem);
    }
}

function updateCategoricalVariableSelection(variable){
    var dropdown = document.getElementById('chooseCategoricalVariableSelection');
    dropdown.innerHTML = '';
    if (localStorage.getItem(variable)) {
        document.getElementById('chooseCategoricalVariableSelection').value = localStorage.getItem(variable);
    }
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
    var varSelectElement = document.getElementById('chooseVariable');
    var varText = varSelectElement.options[varSelectElement.selectedIndex].text;
    document.querySelector('label[for="chooseCategoricalVariableSelection"]').textContent = varText + ': ';
}