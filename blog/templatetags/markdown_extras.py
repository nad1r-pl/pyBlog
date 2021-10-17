"""Set up the markdown processor tag."""
import markdown as md
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    """Define the markdown filter."""
    return md.markdown(
        value,
        extensions=[
            "mdx_headdown",
            "pymdownx.extra",
            "pymdownx.highlight",
            "nl2br",
            "markdown_del_ins",
            # "sane_lists",
            # "markdown_blockdiag",
        ],
        extension_configs={
            "pymdownx.highlight": {
                "guess_lang": True,
                "linenums": True,
                "linenums_style": "pymdownx-inline",
            }
        },
    )
