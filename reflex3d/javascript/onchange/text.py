
import reflex as rx


class HelloTest(rx.Component):
    tag = "HelloTest"

    def _get_custom_code(self) -> str | None:
        return f"""
function helloTest({{url}}) {{
    console.log("boom")
}}"""

    def render(self):
        return "helloTest"
