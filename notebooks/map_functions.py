import geopandas as gpd
import json
import folium
import ipywidgets as widgets
from IPython.display import display, clear_output


def convert_name(gdf, i):
    """
        Convert the polity name of a shape in the Cliopatria dataset to what we want to display on the Seshat world map.
        Where gdf is the geodataframe, i is the index of the row/shape of interest.
        Returns the name to display on the map.
        Returns None if we don't want to display the shape (see comments below for details).
    """
    polity_name = gdf.loc[i, 'Name'].replace('(', '').replace(')', '')  # Remove spaces and brackets from name
    # If a shape has components (is a composite) we'll load the components instead
    # ... unless the components have their own components, then load the top level shape
    # ... or the shape is in a personal union, then load the personal union shape instead
    try:
        if gdf.loc[i, 'Components']:  # If the shape has components
            if ';' not in gdf.loc[i, 'SeshatID']:  # If the shape is not a personal union
                if len(gdf.loc[i, 'Components']) > 0 and '(' not in gdf.loc[i, 'Components']:  # If the components don't have components
                    polity_name = None
    except KeyError:  # If the shape has no components, don't modify the name
        pass
    return polity_name


def cliopatria_gdf(cliopatria_geojson_path, cliopatria_json_path):
    """
        Load the Cliopatria shape dataset with GeoPandas and add the EndYear column to the geodataframe.
    """
    # Load the geojson and json files
    gdf = gpd.read_file(cliopatria_geojson_path)
    with open(cliopatria_json_path, 'r') as f:
        name_years = json.load(f)

    # Create new columns in the geodataframe
    gdf['EndYear'] = None
    gdf['DisplayName'] = None

    # Loop through the geodataframe
    for i in range(len(gdf)):

        # Get the raw name of the current row and the name to display
        polity_name_raw = gdf.loc[i, 'Name']
        polity_name = convert_name(gdf, i)

        # convert_name has returned None if we don't want to display the shape
        if polity_name:
            if gdf.loc[i, 'Type'] != 'POLITY':  # Add the type to the name if it's not a polity
                polity_name = gdf.loc[i, 'Type'] + ': ' + polity_name

            # Get the start year of the current row
            start_year = gdf.loc[i, 'Year']

            # Get a sorted list of the years for that name from the geodataframe
            this_polity_years = sorted(gdf[gdf['Name'] == polity_name_raw]['Year'].unique())

            # Get the end year for a shape    
            # Most of the time, the shape end year is the year of the next shape
            # Some polities have a gap in their active years
            # For a shape year at the start of a gap, set the end year to be the shape year, so it doesn't cover the inactive period
            start_end_years = name_years[polity_name_raw]
            end_years = [x[1] for x in start_end_years]

            polity_start_year = start_end_years[0][0]
            polity_end_year = end_years[-1]

            # Raise an error if the shape year is not the start year of the polity
            if this_polity_years[0] != polity_start_year:
                raise ValueError(f'First shape year for {polity_name} is not the start year of the polity')

            # Find the closest higher value from end_years to the shape year
            next_end_year = min(end_years, key=lambda x: x if x >= start_year else float('inf'))

            if start_year in end_years:
                # If the shape year is in the list of polity end years, the start year is the end year
                end_year = start_year
            else:
                this_year_index = this_polity_years.index(start_year)  
                try:
                    # Try to use the next shape year minus one as the end year if possible,
                    # unless it's higher than the next_end_year
                    next_shape_year_minus_one = this_polity_years[this_year_index + 1] - 1
                    end_year = next_shape_year_minus_one if next_shape_year_minus_one < next_end_year else next_end_year
                except IndexError:
                    # Otherwise assume the end year of the shape is the end year of the
                    # polity
                    end_year = polity_end_year

            # Set the EndYear column to the end year
            gdf.loc[i, 'EndYear'] = end_year

            # Set the DisplayName column to the name to display
            gdf.loc[i, 'DisplayName'] = polity_name

    return gdf


def create_map(selected_year, gdf, map_output):
    global m
    m = folium.Map(location=[0, 0], zoom_start=2, tiles='https://a.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}.png', attr='CartoDB')

    # Filter the gdf for shapes that overlap with the selected_year
    filtered_gdf = gdf[(gdf['Year'] <= selected_year) & (gdf['EndYear'] >= selected_year)]

    # Remove '0x' and add '#' to the start of the color strings
    filtered_gdf['Color'] = '#' + filtered_gdf['Color'].str.replace('0x', '')

    # Transform the CRS of the GeoDataFrame to WGS84 (EPSG:4326)
    filtered_gdf = filtered_gdf.to_crs(epsg=4326)

    # Define a function for the style_function parameter
    def style_function(feature, color):
        return {
            'fillColor': color,
            'color': color,
            'weight': 2,
            'fillOpacity': 0.5
        }

    # Add the polygons to the map
    for _, row in filtered_gdf.iterrows():
        # Convert the geometry to GeoJSON
        geojson = folium.GeoJson(
            row.geometry,
            style_function=lambda feature, color=row['Color']: style_function(feature, color)
        )

        # Add a popup to the GeoJSON
        folium.Popup(row['DisplayName']).add_to(geojson)

        # Add the GeoJSON to the map
        geojson.add_to(m)

    # Display the map
    with map_output:
        clear_output(wait=True)
        display(m)


def display_map(gdf, display_year):

    # Create a text box for input
    year_input = widgets.IntText(
        value=display_year,
        description='Year:',
    )

    # Define a function to be called when the value of the text box changes
    def on_value_change(change):
        create_map(change['new'], gdf, map_output)

    # Create a slider for input
    year_slider = widgets.IntSlider(
        value=display_year,
        min=gdf['Year'].min(),
        max=gdf['EndYear'].max(),
        description='Year:',
    )

    # Link the text box and the slider
    widgets.jslink((year_input, 'value'), (year_slider, 'value'))

    # Create an output widget
    map_output = widgets.Output()

    # Attach the function to the text box
    year_input.observe(on_value_change, names='value')

    # Display the widgets
    display(year_input, year_slider, map_output)

    # Call create_map initially to display the map
    create_map(display_year, gdf, map_output)