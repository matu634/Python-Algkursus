"""Wizards."""


class MismatchError(Exception):
    """
    Class MismatchError inherits its properties from Exception class.

    Should have user-defined message.
    """

    def __init__(self, message):
        """
        Class constructor.

        :param message: user message
        """
        self.message = message


class Wand:
    """Class for Wand object."""

    def __init__(self, wood_type, core):
        """Define wand attributes."""
        self.wood_type = wood_type
        self.core = core

    def set_wood_type(self, wood_type):
        """Give wand a new wood type."""
        self.wood_type = wood_type

    def set_core(self, core):
        """Give wand a new core."""
        self.core = core

    @staticmethod
    def check_wand(wand):
        """Make sure object is Wand class and has both required arguments."""
        if isinstance(wand, Wand) is False:
            raise MismatchError("The wand like that does not exist!")
        elif wand.wood_type is None:
            raise MismatchError("The wand like that does not exist!")
        elif wand.core is None:
            raise MismatchError("The wand like that does not exist!")

    def __str__(self):
        """Object returns in a string format."""
        return self.wood_type + ", " + self.core


class Wizard:
    """Class for Wizard object."""

    def __init__(self, name, wand=None):
        """Define wizaed's name and wand if it's formatted correctly."""
        if wand is not None:
            Wand.check_wand(wand)
        self.name = name
        self.wand = wand

    def set_wand(self, wand):
        """Give wizard a new wand if wand is correctly formatted."""
        Wand.check_wand(wand)
        self.wand = wand

    def get_wand(self):
        """Return wand."""
        return self.wand

    def __str__(self):
        """Return wizard's name if object is called."""
        return self.name


class School:
    """Class for school object."""

    schools = [
        "Hogwarts School of Witchcraft and Wizardry", "Durmstrang Institute",
        "Ilvermorny School of Witchcraft and Wizardry", "Castelobruxo",
        "Beauxbatons Academy of Magic"
    ]

    def __init__(self, name: str):
        """Define school name and make sure it exists in the schools list."""
        if name not in School.schools:
            raise MismatchError("There is no such school!")

        self.name = name
        self.students = []

    def add_wizard(self, wizard):
        """Add a new wizard to the school.

        wizard must have a name and a correct wand.
        wizard must be of Wizard class
        """
        if isinstance(wizard, Wizard) is False:  # Isn't Wizard class instance
            raise MismatchError("It's a filthy muggle!")
        elif type(wizard.name) is not str:
            raise MismatchError("It's a filthy muggle!")
        elif wizard.get_wand() is None:  # No wand defined
            raise MismatchError("It's a filthy muggle!")
        elif wizard in self.students:
            return f"{wizard.name} is already studying in this school!"
        else:
            self.students.append(wizard)
            return f"{wizard.name} started studying in {self.name}."

    def remove_wizard(self, wizard):
        """Remove a wizard from the school."""
        if wizard in self.students:
            self.students.remove(wizard)

    def get_wizards(self):
        """Return a list of students in school."""
        return self.students

    def get_wizard_by_wand(self, wand):
        """Search for a wizard, based on wand."""
        Wand.check_wand(wand)
        for student in self.students:
            if student.get_wand() == wand:
                return student
        return None

    def __str__(self):
        """When School object is called, return it's name."""
        return self.name
wand1 = Wand("Oak","Kek")
wiz1 = Wizard("KEK",wand1)
print(wiz1)