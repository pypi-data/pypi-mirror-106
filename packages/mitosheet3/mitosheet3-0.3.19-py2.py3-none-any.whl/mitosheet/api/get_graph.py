import io
import base64
import pandas as pd
from mitosheet.sheet_functions.types.utils import get_mito_type
import matplotlib.pyplot as plt
import seaborn as sns
import sys # In order to print in this file use sys.stdout.flush() once after the print statements.

def get_graph(send, event, wsc):
    """
    Creates a graph of the passed parameters, and sends it back as a PNG
    string to the frontend for display.

    Requires params: column_header_x_axis, sheet_index_x_axis. Optionally takes the same
    params for column_header_y_axis and sheet_index_y_axis.

    If only an x axis is given, and if the series is a numeric series,
    will return a histogram. Otherwise, as long as there are less than 
    20 distinct items in the series, will return a bar chart of the 
    value count. Otherwise, will return nothing.
    """
    # We turn off interactive plotting for this function, to avoid graphs 
    # being printed to the console. However we make sure to turn it back on 
    # at the end if it was originally on, to not mess with any users code 
    # in the rest of their notebook
    was_interactive = plt.isinteractive()
    if was_interactive:
        plt.ioff()

    keys = event.keys()

    # If an x axis was not provided, then return an empty string
    if 'column_header_x_axis' not in keys or 'sheet_index_x_axis' not in keys:
        # Send an empty response
        send({
            'event': 'api_response',
            'id': event['id'],
            'data': ''
        })
        # Then return so we only respond with an empty string
        return

    sheet_index_x_axis = event['sheet_index_x_axis']
    column_header_x_axis = event['column_header_x_axis']
    x_series: pd.Series = wsc.dfs[sheet_index_x_axis][column_header_x_axis]

    # Determine if a y axis was provided
    column_header_y_axis, sheet_index_y_axis =  None, None

    if 'column_header_y_axis' in keys:
        column_header_y_axis = event['column_header_y_axis']
    if 'sheet_index_y_axis' in keys:
        sheet_index_y_axis = event['sheet_index_y_axis']

    # See if we should include axes or not, by default we do not
    include_axes = False
    if 'include_axes' in keys:
        include_axes = event['include_axes']
   
    try:
        # When the x and y axis are specified in the API call, create a scatter plot 
        if column_header_y_axis is not None and sheet_index_y_axis is not None:
            # Get the y axis series
            sheet_index_y_axis = event['sheet_index_y_axis']
            y_series: pd.Series = wsc.dfs[sheet_index_y_axis][column_header_y_axis]

            # Create the scatter plot
            ax = sns.scatterplot(x=x_series, y=y_series)

            # Remove the x and y labels as we make them on the frontend
            # so that they are clickable
            if not include_axes:
                ax.set(xLabel=None, yLabel=None) 

            # Set the title of the graph
            ax.set_title(f'{column_header_x_axis} vs {column_header_y_axis}')

            # Remove the top and right border for better frontend display
            sns.despine(bottom=False, left=False) 

        # If only the x axis is specified in the API call, create a histogram or bar graph
        else:
            mito_type = get_mito_type(x_series)

            if mito_type == 'number_series':
                ax = x_series.plot.hist()
            else:
                if x_series.nunique() > 20:
                    # Send an empty response
                    send({
                        'event': 'api_response',
                        'id': event['id'],
                        'data': ''
                    })
                    # Then return so we only respond with an empty string
                    return
                ax = x_series.value_counts().plot.bar()

            ax.set_title(column_header_x_axis + ' frequencies')

        # Send the graph back to the frontend
        # From here: https://stackoverflow.com/questions/38061267/matplotlib-graphic-image-to-base64
        pic_IObytes = io.BytesIO()
        ax.figure.savefig(pic_IObytes, format='png', transparent=True, bbox_inches='tight')
        pic_IObytes.seek(0)
        pic_hash = base64.b64encode(pic_IObytes.read()).decode("utf-8").replace("\n", "")
        # Close all graphs so they don't each other write each
        plt.close('all')
        send({
            'event': 'api_response',
            'id': event['id'],
            'data': pic_hash
        })
    except Exception as e:
        # As not being able to make a graph is a non-critical error that doesn't
        # result from user interaction, we don't want to throw an error if something
        # weird happens, so we just return nothing in this case
        send({
            'event': 'api_response',
            'id': event['id'],
            'data': ''
        })
    
    # Turn interactive plotting back on, if it was on in the first place,
    # so we dont mess with users matplotlib code
    if was_interactive:
        plt.ion()