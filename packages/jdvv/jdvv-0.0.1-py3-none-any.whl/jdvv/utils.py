import random
import string 
from collections import Counter
import dash_vtk
from dash_vtk.utils import to_mesh_state
from typing import Optional


def random_string(n=10):
    """Create random string - can be useful to creat unique id for dash component

    Args:
        n (int, optional): length of random string. Defaults to 10.

    Returns:
        str: random string
    """    
    return ''.join([random.choice(string.ascii_lowercase) for i in range(10)])

def set_names(vtkobjs):
    """Set the name attribute of vtk objects if not already established
    """    
    names = []
    for vtkobj in vtkobjs:
        if not hasattr(vtkobj, "name"):
            vtkobj.name = vtkobj.__repr__()
        if vtkobj.name in names:
            names.append(vtkobj.name)
            n = dict(Counter(names))[vtkobj.name]
            vtkobj.name = f"{vtkobj.name}: {n-1}"

def geom_representation(vtkobj, **kwargs):
    """Create dash geometry representation of vtk object

    Args:
        vtkobj (vtk object)

    Returns:
        dash_vtk.GeometryRepresentation
    """    
    return dash_vtk.GeometryRepresentation(
        id={"type": "geom-rep", "name": vtkobj.name},
        colorMapPreset="erdc_rainbow_bright",
        children=dash_vtk.Mesh(
            id={"type": "mesh", "name": vtkobj.name}, state=create_mesh_state(vtkobj)
        ),
        **kwargs,
    )

def create_mesh_state(vtkobj, scalar_name:Optional[str]=None):
    """Create mesh state from vtk object and optional array of data

    Args:
        vtkobj (vtk object): 
        scalar_name (str, optional): [description]. Defaults to None.

    Returns:
        [type]: [description]
    """    
    if scalar_name:
        return to_mesh_state(vtkobj, field_to_keep=scalar_name)
    else:
        return to_mesh_state(vtkobj)