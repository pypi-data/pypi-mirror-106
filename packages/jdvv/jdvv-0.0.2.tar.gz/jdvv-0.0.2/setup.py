import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="jdvv",
    author="Eric Daniels",
    description="Jupyter Dash Viewer for VTK",
    packages=["jdvv"],
    version="0.0.2",
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/ericbdaniels/jupyter-dash-vtk-viewer",
    install_requires=[
        "dash-vtk",
        "vtk",
        "plotly",
        "dash",
        "dash-daq",
        "dash-bootstrap-components",
        "jupyter-dash"   
    ],
    python_requires=">=3.6",
)