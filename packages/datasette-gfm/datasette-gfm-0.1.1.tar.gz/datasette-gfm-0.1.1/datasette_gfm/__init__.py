import json

from datasette import hookimpl
from datasette.utils.asgi import Response


def render_gfm(rows,columns):
    output = "|"
    for column in columns:
        output += str(column) + "|"
    output += "\n"
    for column in columns:
        output += "|---"
    output += "|\n"

    for row in rows:
        for field in row:
            output += str(field) + "|"
        output += "\n"
    return Response.text(output)


@hookimpl
def register_output_renderer():
    return {"extension": "md", "render": render_gfm}

