from reflex.components import NumberInput
import reflex as rx


class NumberInputImproved(NumberInput):
    step: rx.Var[float]

numberinputimproved = NumberInputImproved.create