import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH, ALL
from dash.exceptions import PreventUpdate
import dash_vtk
from jupyter_dash import JupyterDash
from . import utils

import random
from . import components

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"


class DashVtkViewer:
    """Jupyter Dash App for viewing vtk objects
    """    
    def __init__(self, *vtkobjs):
        """Intantiate jupyter dash vtk viewer

        Args:
            vtkobjs(vtk object): vtk objects(s) to display

        """        
        self.app = JupyterDash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP, FONT_AWESOME],
        )
        utils.set_names(vtkobjs)
        self.vtkobjs_dict = {vtkobj.name: vtkobj for vtkobj in vtkobjs}

        self.app.layout = dbc.Container(
            fluid=True,
            style={"margin-top": "15px", "height": "35rem"},
            children=[
                dbc.Row(
                    [
                        dbc.Col(
                            width=3,
                            style={"height": "100%", "overflow-y": "scroll"},
                            children=dbc.Card(
                                [
                                    dbc.CardHeader(html.B("Controls")),
                                    dbc.CardBody(
                                        [components.grid_controls(vtkobj) for vtkobj in vtkobjs]
                                        + [components.view_controls()],
                                        style={"padding": "0.75rem"},
                                    ),
                                ]
                            ),
                        ),
                        dbc.Col(
                            width=9,
                            children=[
                                html.Div(
                                    dash_vtk.View(background=[55, 55, 55], id="vtk-view", children=
                                        [
                                            utils.geom_representation(vtkobj)
                                            for vtkobj in vtkobjs
                                        ],
                                    ),
                                    style={"height": "100%", "width": "100%"},
                                )
                            ],
                        ),
                    ],
                    style={"height": "100%"},
                ),
            ],
        )

        @self.app.callback(
            [
                Output({"type": "mesh", "name": MATCH}, "state"),
                Output({"type": "color-picker", "name": MATCH}, "style"),
                Output({"type": "colormap-properties-div", "name": MATCH}, "style"),
                Output({"type": "input-cmin", "name": MATCH}, "value"),
                Output({"type": "input-cmax", "name": MATCH}, "value"),
            ],
            [
                Input({"type": "dropdown-colorby", "name": MATCH}, "value"),
            ],
            State({"type": "dropdown-colorby", "name": MATCH}, "id"),
        )
        def color_select_type(arr_name, colorby_id):
            name = colorby_id["name"]
            vtkobj = self.vtkobjs_dict[name]
            if arr_name:
                mesh_state = utils.create_mesh_state(vtkobj, arr_name)
                data_range = mesh_state["field"]["dataRange"]
                return mesh_state, {"display": "none"}, {}, data_range[0], data_range[1]

            else:
                mesh_state = utils.create_mesh_state(vtkobj)
                return mesh_state, {}, {"display": "none"}, None, None

        @self.app.callback(
            Output("vtk-view", "triggerRender"),
            [
                Input({"type": "dropdown-colorby", "name": ALL}, "value"),
                Input({"type": "color-picker", "name": ALL}, "value"),
                Input({"type": "colormap-select", "name": ALL}, "value"),
                Input({"type": "input-size", "name": ALL}, "value"),
                Input({"type": "slider-opacity", "name": ALL}, "value"),
                Input({"type": "input-cmin", "name": ALL}, "value"),
                Input({"type": "input-cmax", "name": ALL}, "value"),
                Input({"type": "bool-visibility", "name": ALL}, "value"),
                Input({"type": "surface-representation", "name": ALL}, "value"),
                Input("background-color-picker", "value"),
            ],
        )
        def update_view(*args):
            return random.random()

        @self.app.callback(
            Output("vtk-view", "triggerResetCamera"),
            Input("camera-reset-btn", "n_clicks"),
        )
        def reset_camera(
            n_clicks,
        ):
            if n_clicks:
                return random.random()
            else:
                raise PreventUpdate

        @self.app.callback(
            [
                Output({"type": "geom-rep", "name": MATCH}, "colorMapPreset"),
                Output({"type": "geom-rep", "name": MATCH}, "colorDataRange"),
                Output({"type": "geom-rep", "name": MATCH}, "property"),
            ],
            [
                Input({"type": "dropdown-colorby", "name": MATCH}, "value"),
                Input({"type": "color-picker", "name": MATCH}, "value"),
                Input({"type": "colormap-select", "name": MATCH}, "value"),
                Input({"type": "input-size", "name": MATCH}, "value"),
                Input({"type": "slider-opacity", "name": MATCH}, "value"),
                Input({"type": "input-cmin", "name": MATCH}, "value"),
                Input({"type": "input-cmax", "name": MATCH}, "value"),
                Input({"type": "surface-representation", "name": MATCH}, "value"),
            ],
            State({"type": "dropdown-colorby", "name": MATCH}, "id"),
        )
        def property_select(
            color_by,
            color,
            colormap,
            size,
            opacity,
            cmin,
            cmax,
            surface_rep,
            dropdown_id,
        ):

            vtkobj = self.vtkobjs_dict[dropdown_id["name"]]
            if color_by:
                return (
                    colormap,
                    (cmin, cmax),
                    {
                        "pointSize": size,
                        "Opacity": opacity,
                        "representation": surface_rep,
                    },
                )
            else:
                rgb_color = (
                    float(color["rgb"]["r"]) / 255,
                    float(color["rgb"]["g"]) / 255,
                    float(color["rgb"]["b"]) / 255,
                )
                return (
                    None,
                    (None, None),
                    {
                        "pointSize": size,
                        "Opacity": color["rgb"]["a"],
                        "Color": rgb_color,
                        "representation": surface_rep,
                    },
                )

        @self.app.callback(
            Output({"type": "geom-rep", "name": MATCH}, "actor"),
            Input({"type": "bool-visibility", "name": MATCH}, "value"),
        )
        def toggle_visibility(value):
            try:
                return {"visibility": value[0]}
            except:
                return {"visibility": False}

        @self.app.callback(
            Output("vtk-view", "background"), Input("background-color-picker", "value")
        )
        def set_scene(color):
            rgb_color = (
                float(color["rgb"]["r"]) / 255,
                float(color["rgb"]["g"]) / 255,
                float(color["rgb"]["b"]) / 255,
            )
            return rgb_color

        @self.app.callback(
            [
                Output({"type": "accordian", "name": MATCH}, "is_open"),
                Output({"type": "accordian-btn", "name": MATCH}, "children"),
            ],
            Input({"type": "accordian-btn", "name": MATCH}, "n_clicks"),
        )
        def collapse(
            n_clicks,
        ):
            if n_clicks is None:
                return False, html.I(className="fas fa-plus")
            elif n_clicks % 2 == 0:
                return False, html.I(className="fas fa-plus")
            else:
                return True, html.I(className="fas fa-minus")

        @self.app.callback(
            Output("background-color-popover", "is_open"),
            Input("background-color-btn", "n_clicks"),
            State("background-color-popover", "is_open"),
        )
        def toggle_popover(n_clicks, is_open):
            if n_clicks:
                return True

    def show(self, mode="inline", port=8051):
        """Display the viewer

        Args:
            mode (str, optional): display mode]. Defaults to "inline".
            port (int, optional): port to run app. Defaults to 8051.
        """        
        return self.app.run_server(mode="inline", debug=True, port=port)

def inline(*vtkobjs, port=8051):
    """Display jupyter dash vtk viewer inline

    Args:
        vtkobjs(vtk polydata): vtk polydata object(s)
        port (int, optional): port used to run app. 
            Defaults to 8051 to avoid conflict with any other dash instance on 8050
    """    
    return DashVtkViewer(*vtkobjs).show(mode="inline", port=port)

def tab(*vtkobjs, port=8051):
    """Display jupyter dash vtk viewer in a new jupyter lab tab

    Args:
        vtkobjs(vtk polydata): vtk polydata object(s)
        port (int, optional): port used to run app. 
            Defaults to 8051 to avoid conflict with any other dash instance on 8050
    """  
    return DashVtkViewer(*vtkobjs).show(mode="jupyterlab", port=port)

def external(*vtkobjs, port=8051):
    """Display jupyter dash vtk viewer externally (separate browser tab)

    Args:
        vtkobjs(vtk polydata): vtk polydata object(s)
        port (int, optional): port used to run app. 
            Defaults to 8051 to avoid conflict with any other dash instance on 8050
    """  
    return DashVtkViewer(*vtkobjs).show(mode="external", port=port)