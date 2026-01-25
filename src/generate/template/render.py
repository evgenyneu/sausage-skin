from pathlib import Path

from .escape import escape_attribute, escape_text


def read_template(*, template_path: Path) -> str:
    return template_path.read_text(encoding="utf-8")


def replace_attribute_tag(*, template_html: str, tag: str, value: str, escape: bool) -> str:
    placeholder = f"{{{{ {tag} }}}}"

    if escape:
        escaped_value = escape_attribute(value)
    else:
        escaped_value = value

    return template_html.replace(placeholder, escaped_value)


def replace_text_tag(*, template_html: str, tag: str, value: str, escape: bool) -> str:
    placeholder = f"{{{{ {tag} }}}}"

    if escape:
        escaped_value = escape_text(value)
    else:
        escaped_value = value

    return template_html.replace(placeholder, escaped_value)
