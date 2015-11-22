# Get this figure: fig = py.get_figure("https://plot.ly/~AnnaG/2/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~AnnaG/2/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="Barometer: Children's Safety",
# fileopt="extend"))
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~AnnaG/2/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *

py.sign_in('rafeh01', '1iglsyzwiy' )
trace1 = Bar(
    x=[0.29, 0.17, 0.21, 0.07, 0.11, 0.07, 0.12, 0.3, 0.04, 0.09, 0.04, 0.1, 0.05, 0.04, 0.03, 0.02],
    y=['Sri Lanka', 'Italy', 'South Africa', 'France', 'England', 'Ireland', 'Portugal', 'Brazil', 'Australia',
       'Israel', 'Denmark', 'Sweden', 'Germany', 'Norway', 'Japan', 'Finland'],
    marker=Marker(
        color='rgb(131, 186, 106)'
    ),
    name='',
    orientation='h',
    uid='e58139'
)
trace2 = Bar(
    x=[0.52, 0.28, 0.32, 0.17, 0.25, 0.18, 0.21, 0.3, 0.16, 0.24, 0.13, 0.18, 0.13, 0.09, 0.13, 0.12],
    y=['Sri Lanka', 'Italy', 'South Africa', 'France', 'England', 'Ireland', 'Portugal', 'Brazil', 'Australia',
       'Israel', 'Denmark', 'Sweden', 'Germany', 'Norway', 'Japan', 'Finland'],
    marker=Marker(
        color='rgb(168, 209, 152)'
    ),
    name='',
    orientation='h',
    uid='04bff1'
)
trace3 = Bar(
    x=[0.05, 0.33, 0.16, 0.3, 0.25, 0.19, 0.3, 0.2, 0.21, 0.08, 0.21, 0.13, 0.11, 0.19, 0.37, 0.13],
    y=['Sri Lanka', 'Italy', 'South Africa', 'France', 'England', 'Ireland', 'Portugal', 'Brazil', 'Australia',
       'Israel', 'Denmark', 'Sweden', 'Germany', 'Norway', 'Japan', 'Finland'],
    marker=Marker(
        color='rgb(209, 230, 201)'
    ),
    name='',
    orientation='h',
    uid='44c3e5'
)
trace4 = Bar(
    x=[0.06, 0.15, 0.18, 0.3, 0.28, 0.36, 0.23, 0.14, 0.38, 0.33, 0.42, 0.15, 0.3, 0.39, 0.38, 0.44],
    y=['Sri Lanka', 'Italy', 'South Africa', 'France', 'England', 'Ireland', 'Portugal', 'Brazil', 'Australia',
       'Israel', 'Denmark', 'Sweden', 'Germany', 'Norway', 'Japan', 'Finland'],
    marker=Marker(
        color='rgb(182, 206, 210)'
    ),
    name='',
    orientation='h',
    uid='0ce36f'
)
trace5 = Bar(
    x=[0.07999999999999985, 0.06999999999999995, 0.1299999999999999, 0.15999999999999992, 0.10999999999999999,
       0.19999999999999996, 0.14000000000000012, 0.05999999999999994, 0.20999999999999996, 0.26, 0.19999999999999996,
       0.43999999999999995, 0.41000000000000003, 0.29000000000000004, 0.08999999999999997, 0.29000000000000004],
    y=['Sri Lanka', 'Italy', 'South Africa', 'France', 'England', 'Ireland', 'Portugal', 'Brazil', 'Australia',
       'Israel', 'Denmark', 'Sweden', 'Germany', 'Norway', 'Japan', 'Finland'],
    marker=Marker(
        color='rgb(150, 182, 199)'
    ),
    name='',
    orientation='h',
    uid='60cb54'
)
data = Data([trace1, trace2, trace3, trace4, trace5])
layout = Layout(
    annotations=Annotations([
        Annotation(
            x=0.1,
            y=4.3,
            align='center',
            arrowcolor='rgba(0, 0, 0, 0)',
            arrowhead=1,
            arrowsize=1,
            arrowwidth=0,
            ax=-6,
            ay=-209,
            bgcolor='rgba(0,0,0,0)',
            bordercolor='',
            borderpad=1,
            borderwidth=1,
            font=Font(
                color='rgb(131, 186, 106)',
                family='',
                size=16
            ),
            opacity=1,
            ref='plot',
            showarrow=True,
            text='<b>Agree strongly</b>',
            xanchor='auto',
            xref='x',
            yanchor='auto',
            yref='y'
        ),
        Annotation(
            x=0.1,
            y=4.3,
            align='center',
            arrowcolor='rgba(0, 0, 0, 0)',
            arrowhead=1,
            arrowsize=1,
            arrowwidth=0,
            ax=508,
            ay=-208,
            bgcolor='rgba(0,0,0,0)',
            bordercolor='',
            borderpad=1,
            borderwidth=1,
            font=Font(
                color='rgb(150, 182, 199)',
                family='',
                size=16
            ),
            opacity=1,
            ref='plot',
            showarrow=True,
            text='<b>Disagree strongly</b>',
            xanchor='auto',
            xref='x',
            yanchor='auto',
            yref='y'
        )
    ]),
    autosize=False,
    bargap=0.2,
    bargroupgap=0,
    barmode='stack',
    boxgap=0.3,
    boxgroupgap=0.3,
    boxmode='overlay',
    dragmode='zoom',
    font=Font(
        color='#000',
        family='"PT Sans Narrow", sans-serif',
        size=12
    ),
    height=473,
    hidesources=False,
    hovermode='x',
    legend=Legend(
        x=0.98,
        y=0.98,
        bgcolor='#fff',
        bordercolor='#000',
        borderwidth=1,
        font=Font(
            color='',
            family='',
            size=0
        ),
        traceorder='normal'
    ),
    margin=Margin(
        r=80,
        t=80,
        autoexpand=True,
        b=80,
        l=100,
        pad=0
    ),
    paper_bgcolor='rgb(255, 255, 255)',
    plot_bgcolor='#fff',
    separators='.,',
    showlegend=False,
    smith=False,
    title='Agreement with: <i>"Some young people and adults in the area make you afraid to let your '
          'children play outdoors."</i>',
    titlefont=dict(
        color='',
        family='"PT Sans Narrow", sans-serif',
        size=0
    ),
    width=800,
    xaxis=XAxis(
        anchor='y',
        autorange=False,
        autotick=False,
        domain=[0, 1],
        dtick=0.5,
        exponentformat='e',
        gridcolor='#ddd',
        gridwidth=1,
        linecolor='#000',
        linewidth=1.5,
        mirror=False,
        nticks=0,
        overlaying=False,
        position=0,
        range=[0, 1],
        rangemode='normal',
        showexponent='all',
        showgrid=False,
        showline=False,
        showticklabels=True,
        tick0=0,
        tickangle=0,
        tickcolor='rgb(57, 57, 57)',
        tickfont=dict(
            color='',
            family='',
            size=14
        ),
        ticklen=5,
        ticks='outside',
        tickwidth=1.5,
        title='Proportion of parent respondents',
        titlefont=dict(
            color='',
            family='',
            size=16
        ),
        type='linear',
        zeroline=False,
        zerolinecolor='#000',
        zerolinewidth=1
    ),
    yaxis=YAxis(
        anchor='x',
        autorange=False,
        autotick=True,
        domain=[0, 1],
        dtick=1,
        exponentformat='e',
        gridcolor='#ddd',
        gridwidth=1,
        linecolor='#000',
        linewidth=1.5,
        mirror=False,
        nticks=0,
        overlaying=False,
        position=0,
        range=[-1.1, 16.96800548444918],
        rangemode='normal',
        showexponent='all',
        showgrid=False,
        showline=True,
        showticklabels=True,
        tick0=0,
        tickangle=0,
        tickcolor='rgba(217, 217, 217, 0)',
        tickfont=dict(
            color='',
            family='',
            size=14
        ),
        ticklen=5,
        ticks='outside',
        tickwidth=1.5,
        title='',
        titlefont=dict(
            color='',
            family='',
            size=16
        ),
        type='category',
        zeroline=False,
        zerolinecolor='#000',
        zerolinewidth=1
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)

# save as png
py.image.save_as(fig, 'the_plotly.pdf')
