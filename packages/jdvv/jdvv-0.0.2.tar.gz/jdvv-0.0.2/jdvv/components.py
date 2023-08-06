import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
from dash_vtk.utils import to_mesh_state, preset_as_options
from .import utils

def grid_controls(vtkobj):
    """controls specific to each vtk object"""
    field_name_options = []
    color_by_disabled = True
    cell_data = vtkobj.GetCellData() 
    point_data = vtkobj.GetPointData()   
    cell_data_names = [cell_data.GetArrayName(i) for i in range(cell_data.GetNumberOfArrays())]
    point_data_names = [point_data.GetArrayName(i) for i in range(point_data.GetNumberOfArrays())]
    data_names = cell_data_names+point_data_names

    if len(data_names) != 0:
        field_name_options = [
            {"label": name, "value": name} for name in data_names
        ]
        color_by_disabled = False
    text_id = utils.random_string()
    layout =  dbc.Card(
        [
            dbc.CardHeader(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    html.I(className="fas fa-plus"),
                                    color="light",
                                    size="sm",
                                    id={"type": "accordian-btn", "name": vtkobj.name},
                                    
                                ),
                                width=1,
                            ),
                            
                            dbc.Col([html.B(vtkobj.name, id=text_id, className="mb-1", ),
                            dbc.Tooltip(vtkobj.name,  target=text_id)],
                            width=8, style={"height":"1.5rem","text-overflow":"ellipsis","overflow":"hidden","whitespace":"nowrap"}
                            ),
                            dbc.Col(
                                dbc.Checklist(
                                    options=[{"label": "", "value": True}],
                                    value=[True],
                                    id={"type": "bool-visibility", "name": vtkobj.name},
                                    switch=True,
                                ),
                                width=2,
                            ),
                        ]
                    ),
                ],
                # style={"height": "3rem"},
            ),
            dbc.Collapse(
                id={"type": "accordian", "name": vtkobj.name},
                children=dbc.CardBody(
                    [
                        dbc.FormGroup(
                            [
                                dbc.Label(
                                    "Display Property",
                                    html_for={
                                        "type": "dropdown-colorby",
                                        "name": vtkobj.name,
                                    },
                                ),
                                dcc.Dropdown(
                                    id={
                                        "type": "dropdown-colorby",
                                        "name": vtkobj.name,
                                    },
                                    options=field_name_options,
                                    value="",
                                    disabled=color_by_disabled,
                                ),
                            ]
                        ),
                        color_widget(vtkobj),
                        daq.ColorPicker(
                            id={"type": "color-picker", "name": vtkobj.name},
                            value=dict(rgb=dict(r=255, g=255, b=255, a=1)),
                            style={"display": "none"},
                        ),
                        type_specific_properties(vtkobj),
                    ],
                ),
            ),
        ]
    )
    return layout


def color_widget(vtkobj):
    """color map and opacity selector"""
    layout= dbc.Col(
        id={"type": "colormap-properties-div", "name": vtkobj.name},
        children=[
            dbc.Row(
                dbc.Col(
                    dbc.FormGroup(
                        [
                            dbc.Label(
                                "colormap",
                                html_for={
                                    "type": "colormap-select",
                                    "name": vtkobj.name,
                                },
                            ),
                            dcc.Dropdown(
                                id={"type": "colormap-select", "name": vtkobj.name},
                                options=preset_as_options,
                                value="erdc_rainbow_bright",
                            ),
                        ]
                    )
                )
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.FormGroup(
                            [
                                dbc.Label(
                                    "cmin",
                                    html_for={
                                        "type": "input-cmin",
                                        "name": vtkobj.name,
                                    },
                                ),
                                dbc.Input(
                                    id={
                                        "type": "input-cmin",
                                        "name": vtkobj.name,
                                    },
                                    type="number",
                                ),
                            ]
                        ),
                        width=6,
                    ),
                    dbc.Col(
                        dbc.FormGroup(
                            [
                                dbc.Label(
                                    "cmax",
                                    html_for={
                                        "type": "input-cmax",
                                        "name": vtkobj.name,
                                    },
                                ),
                                dbc.Input(
                                    id={
                                        "type": "input-cmax",
                                        "name": vtkobj.name,
                                    },
                                    type="number",
                                ),
                            ]
                        ),
                        width=6,
                    ),
                ]
            ),
            dbc.Row(
                dbc.Col(
                    dbc.FormGroup(
                        [
                            dbc.Label(
                                "Opacity",
                                html_for={
                                    "type": "slider-opacity",
                                    "name": vtkobj.name,
                                },
                            ),
                            dcc.Slider(
                                id={
                                    "type": "slider-opacity",
                                    "name": vtkobj.name,
                                },
                                min=0,
                                max=1,
                                value=1,
                                step=0.05,
                                marks={0: "O%", 1: "100%"},
                            ),
                        ]
                    )
                )
            ),
        ],
        style={"display": "none"},
    )
    return layout


def type_specific_properties(vtkobj):
    """dash controls specific to vtk object type"""
    pt_size = dbc.FormGroup(
        [
            dbc.Label(
                "Point Size", html_for={"type": "input-size", "name": vtkobj.name}
            ),
            dbc.Input(
                id={"type": "input-size", "name": vtkobj.name},
                value=3,
                type="number",
            ),
        ]
    )
    edge_viz = dbc.FormGroup(
        [
            dbc.Label(
                "Surface Representation",
                html_for={"type": "surface-representation", "name": vtkobj.name},
            ),
            dcc.Dropdown(
                options=[
                    {"label": "Surface", "value": 2},
                    {"label": "Wireframe", "value": 1},
                    {"label": "Points", "value": 0},
                ],
                value=2,
                id={"type": "surface-representation", "name": vtkobj.name},
            ),
        ]
    )
    return dbc.Col([pt_size, edge_viz])


def view_controls():
    """dash controls for entire viewer"""
    return dbc.Card(
        [
            dbc.CardHeader("Scene Controls"),
            dbc.CardBody(
                [
                    dbc.Button(
                        "Background Color",
                        id="background-color-btn",
                        color="light",
                        size="sm",
                        className="m-2",
                    ),
                    dbc.Popover(
                        [
                            dbc.PopoverBody(
                                dbc.FormGroup(
                                    [
                                        dbc.Label(
                                            "Background Color",
                                            html_for="background-color-picker",
                                        ),
                                        daq.ColorPicker(
                                            id="background-color-picker",
                                            value=dict(rgb=dict(r=55, g=55, b=55, a=1)),
                                        ),
                                    ]
                                )
                            )
                        ],
                        id="background-color-popover",
                        is_open=False,
                        target="background-color-btn",
                        hide_arrow=True,
                        container="vtk-view",
                        trigger="legacy",
                    ),
                    dbc.Button(
                        "Reset Camera",
                        id="camera-reset-btn",
                        color="light",
                        size="sm",
                        className="m-2",
                    ),
                ]
            ),
        ]
    )