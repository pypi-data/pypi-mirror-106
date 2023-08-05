from magic.shared.display import Color, clear_last_line, in_color
from magic.shared.spellbook import get_spells


def is_not_empty(line):
    return line != ""


def is_a_number(line):
    return line.isnumeric()


def is_y_or_n(line):
    return line.lower() == "y" or line.lower() == "n"


def is_not_empty_list(_list):
    return "" not in _list


def list_has_no_duplicates(_list):
    return len(_list) == len(set(_list))


reserved_words = ["add", "edit"]


def magic_word_validator():
    spells = get_spells()

    def validate(line):
        words = [word.strip(" ") for word in line.split(",")]

        if is_not_empty_list(words) is not True:
            return False
        if list_has_no_duplicates(words) is not True:
            return False

        clash = False
        for word in words:
            if word in reserved_words:
                clear_last_line()
                print(in_color(f"'{word}' is a reserved word\n", Color.YELLOW))
                clash = True
            if spells.get(word):
                clear_last_line()
                print(in_color(f"'{word}' is already used in a spell\n", Color.YELLOW))
                clash = True

        return not clash

    return validate
