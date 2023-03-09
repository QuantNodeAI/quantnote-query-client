import os

import plotly.graph_objects as go
import plotly.io as pio
from PIL import Image

absolute_path = os.path.dirname(__file__)
relative_path = "quantnote.png"
logo_path = os.path.join(absolute_path, relative_path)
pyLogo = Image.open(logo_path)

pio.templates["quantnote"] = go.layout.Template(
    # LAYOUT
    layout={
        # Fonts
        # Note - 'family' must be a single string, NOT a list or dict!
        'title':
            {'font': {'family': 'HelveticaNeue-CondensedBold, Helvetica, Sans-serif',
                      'size': 30,
                      'color': '#333'}
             },
        'font': {'family': 'Helvetica Neue, Helvetica, Sans-serif',
                 'size': 16,
                 'color': '#333'},
        # Colorways
        'colorway': ['#ec7424', '#a4abab'],
        # Keep adding others as needed below
        'hovermode': 'x unified',

        # for transparent background
        # 'paper_bgcolor': 'rgba(0,0,0,0)',
        # 'plot_bgcolor': 'rgba(0,0,0,0)',
    },
    # DATA
    data={
        # Each graph object must be in a tuple or list for each trace
        'bar': [go.Bar(texttemplate='%{value:$.2s}',
                       textposition='outside',
                       textfont={'family': 'Helvetica Neue, Helvetica, Sans-serif',
                                 'size': 20,
                                 'color': '#FFFFFF'
                                 })]
    },
    # LOGO
    layout_images=[
        dict(
            name="imageName",
            source=pyLogo,
            xref="paper", yref="paper",
            x=0.1, y=1.0,
            sizex=0.2, sizey=0.2,
            xanchor="center", yanchor="bottom"
        )
    ]
)
