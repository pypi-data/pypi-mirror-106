from magic.shared.display import EMOJI_TRASH, Color
from magic.shared.prompt import create_prompt
from magic.shared.spellbook import delete
from magic.shared.validate import is_y_or_n
from magic.show import show_spell

color = Color.YELLOW
prompt = create_prompt(color)


def delete_spell(magic_word):
    show_spell(magic_word, spell_args=[], skip_arguments_provided=True)
    confirm = prompt(
        f"{EMOJI_TRASH} Do you want to delete this spell, y or n?",
        validate=is_y_or_n,
        default="n",
    )

    if confirm == "y":
        delete(magic_word)
