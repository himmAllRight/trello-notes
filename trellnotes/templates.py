"""Controls and managed templates in Trellnotes."""

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("trellnotes", "templates"),
    autoescape=select_autoescape(["html", "xml"]),
)
