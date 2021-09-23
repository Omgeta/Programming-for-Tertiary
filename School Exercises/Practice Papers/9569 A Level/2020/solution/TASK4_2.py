# Author: Omgeta
# Description: Task 4.2 Python File
# Date: 23/9/2021
# Version: 1.0
import sqlite3
from datetime import datetime
from string import punctuation


class Person:
    def __init__(self, full_name: str, date_of_birth: str):
        self.full_name = full_name
        self.date_of_birth = date_of_birth

    def is_adult(self) -> bool:
        """
        Checks if a person is an adult by checking their Date of Birth with the current year

        Returns:
            If the person is an adult
        """
        birth_year = int(self.date_of_birth.split('-')[0])
        curr_year = datetime.now().year
        return curr_year - birth_year > 18

    def screen_name(self) -> str:
        """
        Creates screen name identifier for a person.

        Returns:
            Screen name string
        """
        screen_name = ""

        # Removing all spaces and punctuation
        banned_chars = (" ", *punctuation)
        for char in self.full_name:
            if char not in banned_chars:
                screen_name += char

        # Adding month and day
        year, month, day = self.date_of_birth.split("-")
        screen_name = screen_name + month + day

        return screen_name


class Staff(Person):
    def screen_name(self):
        """
        Creates screen name identifier with Staff at the end
        """
        screen_name = super().screen_name()
        return screen_name + "Staff"

    def is_adult(self):
        """
        All staff are adults
        """
        return True


class Student(Person):
    def is_adult(self):
        """
        All students are not adults
        """
        return False


# Databasing


def get_conn():
    conn = sqlite3.connect("school.db")
