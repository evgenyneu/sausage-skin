from html import escape


def escape_text(text: str) -> str:
    return escape(text, quote=False)


def escape_attribute(text: str) -> str:
    return escape(text, quote=True)
