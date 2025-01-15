from app import app
from dash.html import H1
from dash.dcc import Graph, RadioItems


def test_header_exists():
    assert type(app.layout[0]) == H1

def test_region_picker_exists():
    assert type(app.layout[1]) == RadioItems

def test_visualization_exists():
    assert type(app.layout[2]) == Graph
