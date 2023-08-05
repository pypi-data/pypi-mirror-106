import click

from magic.add import add_spell
from magic.cast import cast_spell
from magic.delete import delete_spell
from magic.edit import edit_spellbook
from magic.help import get_help
from magic.shared.display import Color, in_color
from magic.shared.spellbook import get_spells
from magic.show import show_spell

CONTEXT_SETTINGS = dict(allow_extra_args=True, help_option_names=["-h", "--help"])


class MagicGroup(click.Group):
    def get_help(self, ctx):
        return get_help(self, ctx)


@click.group(cls=MagicGroup, context_settings=CONTEXT_SETTINGS)
def main():
    pass  # no-op


@main.command(name="add")
def __add():
    """Add spell to spellbook"""
    return add_spell()


@main.command(name="edit")
def __edit():
    """Open spellbook in editor"""
    return edit_spellbook()


def spell_to_command(magic_word, spell):
    def create_command(magic_word):
        @click.pass_context
        @click.option("-d", "--delete", is_flag=True, help="Delete this spell.")
        @click.option("-s", "--show", is_flag=True, help="Show details of this spell.")
        def command(ctx, delete, show):
            if delete:
                return delete_spell(magic_word)
            if show:
                return show_spell(magic_word=magic_word, spell_args=ctx.args)
            return cast_spell(magic_word=magic_word, arguments=ctx.args)

        return command

    main.command(
        name=magic_word,
        help=in_color(spell.get("description"), Color.CYAN),
        context_settings=dict(allow_extra_args=True, ignore_unknown_options=True),
    )(create_command(magic_word))


for magic_word, spell in get_spells().items():
    spell_to_command(magic_word, spell)
