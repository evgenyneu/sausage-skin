from src.generate.template.escape import escape_attribute


def test_escape_attribute_escapes_html_entities() -> None:
    result = escape_attribute("Hello & World")
    assert result == "Hello &amp; World"


def test_escape_attribute_escapes_less_than() -> None:
    result = escape_attribute("Hello < World")
    assert result == "Hello &lt; World"


def test_escape_attribute_escapes_greater_than() -> None:
    result = escape_attribute("Hello > World")
    assert result == "Hello &gt; World"


def test_escape_attribute_escapes_double_quotes() -> None:
    result = escape_attribute('Hello "World"')
    assert result == "Hello &quot;World&quot;"


def test_escape_attribute_escapes_single_quotes() -> None:
    result = escape_attribute("Hello 'World'")
    assert result == "Hello &#x27;World&#x27;"


def test_escape_attribute_handles_empty_string() -> None:
    result = escape_attribute("")
    assert result == ""


def test_escape_attribute_handles_plain_text() -> None:
    result = escape_attribute("Hello World")
    assert result == "Hello World"
