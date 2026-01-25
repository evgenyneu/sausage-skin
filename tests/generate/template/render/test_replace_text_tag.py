from src.generate.template.render import replace_text_tag


def test_replace_text_tag_replaces_placeholder() -> None:
    template = "<p>{{ description }}</p>"
    result = replace_text_tag(template_html=template, tag="description", value="Hello", escape=True)
    assert result == "<p>Hello</p>"


def test_replace_text_tag_escapes_value_when_escape_true() -> None:
    template = "<p>{{ description }}</p>"
    result = replace_text_tag(
        template_html=template, tag="description", value="Hello < World", escape=True
    )
    assert result == "<p>Hello &lt; World</p>"


def test_replace_text_tag_does_not_escape_when_escape_false() -> None:
    template = "<p>{{ description }}</p>"
    result = replace_text_tag(
        template_html=template, tag="description", value="<strong>Hello</strong>", escape=False
    )
    assert result == "<p><strong>Hello</strong></p>"


def test_replace_text_tag_handles_multiple_placeholders() -> None:
    template = "<div>{{ title }} - {{ subtitle }}</div>"
    result = replace_text_tag(template_html=template, tag="title", value="Hello", escape=True)
    result = replace_text_tag(template_html=result, tag="subtitle", value="World", escape=True)
    assert result == "<div>Hello - World</div>"


def test_replace_text_tag_handles_empty_value() -> None:
    template = "<p>{{ description }}</p>"
    result = replace_text_tag(template_html=template, tag="description", value="", escape=True)
    assert result == "<p></p>"


def test_replace_text_tag_does_not_escape_quotes() -> None:
    template = "<p>{{ description }}</p>"
    result = replace_text_tag(
        template_html=template, tag="description", value='Hello "World"', escape=True
    )
    assert result == '<p>Hello "World"</p>'
