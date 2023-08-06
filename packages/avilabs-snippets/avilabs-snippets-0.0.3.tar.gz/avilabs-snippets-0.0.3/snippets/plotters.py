import plotly.graph_objects as go


def _get_bounds(self, x1=None, x2=None, y1=None, y2=None):
    layout = self.to_dict()["layout"]

    if "xaxis" in layout and "range" in layout["xaxis"]:
        x_lower, x_upper = self.to_dict()["layout"]["xaxis"]["range"]
    else:
        x_lower, x_upper = None, None

    if "yaxis" in layout and "range" in layout["yaxis"]:
        y_lower, y_upper = self.to_dict()["layout"]["yaxis"]["range"]
    else:
        y_lower, y_upper = None, None

    if x_lower is not None and y_lower is None:
        y_lower, y_upper = x_lower, x_upper
    elif x_lower is None and y_lower is not None:
        x_lower, x_upper = y_lower, y_upper
    elif x_lower is None and y_lower is None:
        x_lower, x_upper = x1, x2
        y_lower, y_upper = y1, y2

    return x_lower, x_upper, y_lower, y_upper


def _plot_line(self, x_lower, x_upper, y_lower, y_upper, x1, x2, y1, y2, name):
    if x1 == x2:
        xs = (x1, x1)
        ys = (y_lower, y_upper)
    elif y1 == y2:
        xs = (x_lower, x_upper)
        ys = (y1, y1)
    else:
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m * x1
        y = lambda x: m * x + c
        xs = (x_lower, x_upper)
        ys = (y(x_lower), y(x_upper))

    self.add_scatter(x=xs, y=ys, name=name)


def plot_line_with_coeffs(self, a, b, c, name=""):
    """Plots a line ax + by + c = 0"""
    m = -a / b
    c = -c / b
    y = lambda x: m * x + c
    x_lower, x_upper, _, _ = self._get_bounds()
    self.add_scatter(x=(x_lower, x_upper), y=(y(x_lower), y(x_upper)), name=name)


def plot_line_segment(self, p1, p2, name=""):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x_lower, x_upper = x1, x2
    y_lower, y_upper = y1, y2
    self._plot_line(x_lower, x_upper, y_lower, y_upper, x1, x2, y1, y2, name)


def plot_line_with_points(self, p1, p2, name=""):
    """Plots a line connecting p1 and p2"""
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x_lower, x_upper, y_lower, y_upper = self._get_bounds(x1, x2, y1, y2)
    self._plot_line(x_lower, x_upper, y_lower, y_upper, x1, x2, y1, y2, name)


def plot_point(self, x, y, name=""):
    self.add_scatter(x=(x,), y=(y,), name=name)


go.Figure._get_bounds = _get_bounds
go.Figure._plot_line = _plot_line
go.Figure.plot_line_with_coeffs = plot_line_with_coeffs
go.Figure.plot_line_segment = plot_line_segment
go.Figure.plot_line_with_points = plot_line_with_points
go.Figure.plot_point = plot_point
