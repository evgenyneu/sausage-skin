from src.generate.pages.home import render_index_html


def test_render_index_html_replaces_placeholder() -> None:
    layout_html = "<html><body>{{ body }}</body></html>"

    result = render_index_html(layout_html=layout_html, body_html="<div>Hello World</div>")

    assert result == "<html><body><div>Hello World</div></body></html>"
