from src.generate.template.render import replace_attribute_tag


def test_replace_attribute_tag_replaces_placeholder() -> None:
    template = '<img alt="{{ alt_text }}" />'
    result = replace_attribute_tag(
        template_html=template, tag="alt_text", value="Hello", escape=True
    )
    assert result == '<img alt="Hello" />'


def test_replace_attribute_tag_escapes_value_when_escape_true() -> None:
    template = '<img alt="{{ alt_text }}" />'
    result = replace_attribute_tag(
        template_html=template, tag="alt_text", value='Hello "World"', escape=True
    )
    assert result == '<img alt="Hello &quot;World&quot;" />'


def test_replace_attribute_tag_does_not_escape_when_escape_false() -> None:
    template = '<img alt="{{ alt_text }}" />'
    result = replace_attribute_tag(
        template_html=template, tag="alt_text", value='Hello "World"', escape=False
    )
    assert result == '<img alt="Hello "World"" />'


def test_replace_attribute_tag_handles_multiple_placeholders() -> None:
    template = '<a href="{{ url }}" title="{{ title }}">Link</a>'
    result = replace_attribute_tag(template_html=template, tag="url", value="/test", escape=True)
    result = replace_attribute_tag(template_html=result, tag="title", value="Test", escape=True)
    assert result == '<a href="/test" title="Test">Link</a>'


def test_replace_attribute_tag_handles_empty_value() -> None:
    template = '<img alt="{{ alt_text }}" />'
    result = replace_attribute_tag(template_html=template, tag="alt_text", value="", escape=True)
    assert result == '<img alt="" />'
