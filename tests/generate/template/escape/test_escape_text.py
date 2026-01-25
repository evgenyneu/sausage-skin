from src.generate.template.escape import escape_text


def test_escape_text_escapes_html_entities() -> None:
    result = escape_text("Hello & World")
    assert result == "Hello &amp; World"


def test_escape_text_escapes_less_than() -> None:
    result = escape_text("Hello < World")
    assert result == "Hello &lt; World"


def test_escape_text_escapes_greater_than() -> None:
    result = escape_text("Hello > World")
    assert result == "Hello &gt; World"


def test_escape_text_does_not_escape_quotes() -> None:
    result = escape_text('Hello "World"')
    assert result == 'Hello "World"'


def test_escape_text_handles_empty_string() -> None:
    result = escape_text("")
    assert result == ""


def test_escape_text_handles_plain_text() -> None:
    result = escape_text("Hello World")
    assert result == "Hello World"
