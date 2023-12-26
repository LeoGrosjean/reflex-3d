from typing import List

import reflex as rx
from reflex.components.graphing.recharts import YAxis

from reflex3d.templates import template

data = [
    {"vuelta": "0", "valor": 32, "J": 0, "C": 0, "mean": 33.333},
    {"vuelta": "1", "valor": 33, "J": 33.456, "C": 33.800, "mean": 33.333},
    {"vuelta": "3", "valor": 34, "J": 32.090, "C": 32.459, "mean": 33.333},
    {"vuelta": "4", "valor": 35, "J": 33.000, "C": 30.920, "mean": 33.333},
    {"vuelta": "5", "valor": 36, "J": 32.546, "C": 36.909, "mean": 33.333},
    {"vuelta": "6", "valor": 37, "J": 32.890, "C": 34.000, "mean": 33.333},
    {"vuelta": "7", "valor": 38, "J": 34.900, "C": 34.010, "mean": 33.333}
]


class YAxis(YAxis):
    domain: rx.Var[List]


y_axis = YAxis.create


@template(route="/chart", title="Chart")
def plot():
    return rx.recharts.line_chart(
    rx.recharts.line(
        datakey="C",
        type="monotone",
        stroke="#8884d8",
    ),
    rx.recharts.line(
        datakey="J",
        type="monotone",
        stroke="#82ca9d",
    ),
    rx.recharts.line(
        datakey="mean",
        type="monotone",
        stroke="#FF1493",
    ),
    rx.recharts.x_axis(data_key="vuelta"),
    y_axis(domain=[30, 40]),
    rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
    rx.recharts.graphing_tooltip(),
    rx.recharts.legend(),
    height=500,
    width=1000,
    data=data
)