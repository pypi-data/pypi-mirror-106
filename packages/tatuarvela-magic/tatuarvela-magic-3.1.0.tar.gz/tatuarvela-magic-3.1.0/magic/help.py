from importlib import metadata

from click import Context, Group

from magic.shared.display import EMOJI_SPARKLE, Color, in_color

name = "Magic"
version = metadata.version("tatuarvela-magic")
year = 2021
author = "Tatu Arvela"

version_text = (
    f"{EMOJI_SPARKLE} {in_color(name, Color.BLUE)} v{version} © {year} {author}"
)


def get_help(self, ctx: Context):
    click_help = Group.get_help(self, ctx)
    description = "A tool for simplifying repeated command line tasks"

    return f"{version_text}\n" f"{description}\n" f"\n" f"{click_help}"
