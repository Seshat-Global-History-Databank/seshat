function createMap() {
    // Use the standard CRS for global maps
    var crs = L.CRS.EPSG3857;

    // Create the map with the defined CRS
    var map = L.map('map', {
        center: [0, 0], // Center at the equator and prime meridian
        zoom: 2, // Initial zoom level to show the entire world
        crs: crs,
        continuousWorld: true,
        worldCopyJump: true, // Enables the seamless panning around the world
        maxBounds: [[-85.06, -180], [85.06, 180]], // Web Mercator bounds
        maxZoom: 18,
        minZoom: 2
    });

    return map;
}

function createGlobe(accessToken) {
    // Ensure Cesium is loaded
    if (typeof Cesium === 'undefined') {
        throw new Error('Cesium library is not loaded.');
    }

    // Set the Cesium Ion default access token
    Cesium.Ion.defaultAccessToken = accessToken;

    // Create the Cesium viewer with the defined container
    var viewer = new Cesium.Viewer('globe', {
        baseLayer: Cesium.ImageryLayer.fromProviderAsync(
            Cesium.TileMapServiceImageryProvider.fromUrl(
                Cesium.buildModuleUrl("Assets/Textures/NaturalEarthII")
            )
        ),
        baseLayerPicker: false, // Disable base layer picker
        geocoder: false, // Disable geocoder
        homeButton: true, // Enable home button
        sceneModePicker: true, // Enable scene mode picker
        timeline: false, // Disable timeline
        animation: false, // Disable animation controls
        fullscreenButton: true, // Enable fullscreen button
        vrButton: false, // Disable VR button
        navigationHelpButton: true, // Enable navigation help button
        infoBox: true, // Enable info box
        selectionIndicator: true, // Enable selection indicator
        scene3DOnly: true // Enable 3D only mode
    });

    // Set the initial view to show the entire globe
    viewer.scene.camera.setView({
        destination: Cesium.Cartesian3.fromDegrees(0, 0, 20000000) // Center at the equator and prime meridian
    });

    return viewer;
}

function createBaseLayers() {
    var baseLayers = {
        "arcgis": L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'),
        "carto": L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}.png'),
        "osm": L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png')
    };
    return baseLayers;
}

function updateSliderOutput() {
    if (slider.value < 0) {
        sliderDate.innerHTML = Math.abs(slider.value) + ' BCE';
        if (sliderDate2) { // Exists in world_map.html but not in polity_map.html
            sliderDate2.innerHTML = Math.abs(slider.value) + ' BCE';
        }
    } else {
        sliderDate.innerHTML = slider.value + ' CE';
        if (sliderDate2) { // Exists in world_map.html but not in polity_map.html
            sliderDate2.innerHTML = slider.value + ' CE';
        }
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

function playBack() {

    var increment = Number(document.getElementById('increment').value);
    var milliseconds = 1 / (increment / 1000);
    var symbol = document.getElementById('playButton').innerHTML;
    if (symbol === '▶️') {
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
        document.getElementById('playButton').innerHTML = '⏸';
    } else {
        stopPlay();
    }

}

function stopPlay() {
    clearInterval(playInterval);
    document.getElementById('playButton').innerHTML = '▶️';
};

function storeYear() {
    var year = document.getElementById('enterYear').value;
    history.pushState(null, '', '/core/world_map/?year=' + year);
    if (!allPolitiesLoaded) {
        document.getElementById('loadingIndicator').style.display = 'block';
    }
}

function storeYearMobile() {
    document.getElementById('enterYear').value = document.getElementById('enterYearMobile').value;
    if(document.getElementById('enterYearMobile').value >= 0) {
        document.getElementById('switchToBCE').innerHTML = 'To BCE';
    };
}

function switchToBCE() {
    if (document.getElementById('enterYearMobile').value < 0) {
        document.getElementById('switchToBCE').innerHTML = 'To BCE';
    } else {
        document.getElementById('switchToBCE').innerHTML = 'To CE';
    }
    document.getElementById('enterYearMobile').value = 0 - document.getElementById('enterYearMobile').value;
}

function switchBaseMap() {
    var selectedMap = document.querySelector('input[name="baseMap"]:checked').value;
    var base = document.getElementById("baseMapGADM").value

    if (selectedMap === 'cesium') {
        // Disable the play button when switching to the globe view
        document.getElementById('playButton').disabled = true;
    } else {
        // Enable the play button when switching to the map view
        document.getElementById('playButton').disabled = false;
    }

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
    } else if (selectedMap === 'carto') {
        currentLayer = baseLayers.carto.addTo(map);
    } else if (selectedMap === 'arcgis') {
        currentLayer = baseLayers.arcgis.addTo(map);
    } else if (selectedMap === 'gadm') {
        currentLayer = baseLayers.carto.addTo(map);
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
    plotPolities();
}

function updateLegend() {
    var variable = document.getElementById('chooseVariable').value;
    var legendDiv = document.getElementById('variableLegend');
    var selectedYearInteger = parseInt(document.getElementById('dateSlide').value);
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
                if ((parseInt(shape.start_year) <= selectedYearInteger && parseInt(shape.end_year) >= selectedYearInteger)
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

        // Add a legend for highlighted polities
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

    if (variable == 'polity') {
        if (addedPolities.length > 0) {
            // Add clear selection button
            var clearSelectionButton = document.createElement('button');
            clearSelectionButton.textContent = 'Clear selection';
            clearSelectionButton.onclick = clearSelection;
            legendDiv.appendChild(clearSelectionButton);

            // Make the polityContainer scrollable if there are more than 7 polities
            if (addedPolities.length > 7) {
                polityContainer.style.maxHeight = '420px';
                polityContainer.style.overflowY = 'scroll';
            } else {
                // Reset to default if fewer than 7 polities to ensure it behaves correctly on subsequent updates
                polityContainer.style.maxHeight = '';
                polityContainer.style.overflowY = '';
            }
        }
    }
}

function updateComponentLegend() {

    var legendDiv = document.getElementById('componentLegend');
    var legendDiv2 = document.getElementById('componentLegend2');
    var displayComponent = document.getElementById('switchPolitiesComponents').value;
    var selectedYearInteger = parseInt(document.getElementById('dateSlide').value);
    // Create a container for polity items
    var polityContainer = document.createElement('div');

    // Clear current legend and ensure it is displayed
    legendDiv.innerHTML = '';
    legendDiv2.innerHTML = '';
    legendDiv.style.display = 'block';
    legendDiv2.style.display = 'block';

    var addedPolities = [];
    var addedPolityNames = [];
    polityMapShapesData.forEach(function (shape) {
        shape_name_col_dict = {};
        shape_name_col_dict['polity'] = shape.name;
        shape_name_col_dict['colour'] = shape.colour;
        if (!addedPolityNames.includes(shape_name_col_dict['polity'])) {
            if ((parseInt(shape.start_year) <= selectedYearInteger && parseInt(shape.end_year) >= selectedYearInteger)
                && shouldDisplayComponent(displayComponent, shape)
            ) {
                addedPolities.push(shape_name_col_dict);
                addedPolityNames.push(shape_name_col_dict['polity']);
            };
        };
    });

    // Sort the polities by name
    addedPolities.sort(function (a, b) {
        return a.polity.localeCompare(b.polity);
    });

    // Add a legend for polity components if the displayComponent is set to 'components' and there is more than one
    if (addedPolities.length > 0 && displayComponent == 'components') {
        var legendTitle = document.createElement('h3');
        legendTitle.textContent = 'Components';
        legendDiv.appendChild(legendTitle);
        legendDiv2.appendChild(legendTitle.cloneNode(true));
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
        polityContainer2 = polityContainer.cloneNode(true);
        legendDiv2.appendChild(polityContainer2);

        // Make the polityContainer scrollable if there are more than 7 polities
        if (addedPolities.length > 7) {
            polityContainer.style.maxHeight = '300px';
            polityContainer.style.overflowY = 'scroll';
            polityContainer2.style.maxHeight = '300px';
            polityContainer2.style.overflowY = 'scroll';
        } else {
            // Reset to default if fewer than 7 polities to ensure it behaves correctly on subsequent updates
            polityContainer.style.maxHeight = '';
            polityContainer.style.overflowY = '';
            polityContainer2.style.maxHeight = '';
            polityContainer2.style.overflowY = '';
        }
    } else {
        // Hide the component legend if there are no components to display
        legendDiv.style.display = 'none';
        legendDiv2.style.display = 'none';
    }
}

function clearSelection() {
    var popup = document.getElementById('popup');
    popup.innerHTML = '';
    popup.style.display = 'none';
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

function toggleTips() {
    var dropdown = document.getElementById("tips");
    if (dropdown.style.display === "none" || dropdown.style.display === "") {
        dropdown.style.display = "block";
    } else {
        dropdown.style.display = "none";
    }
}