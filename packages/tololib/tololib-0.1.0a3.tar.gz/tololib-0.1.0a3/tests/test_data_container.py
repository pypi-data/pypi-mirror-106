
from unittest import TestCase

from tololib.const import LampMode
from tololib.data_container import BooleanContainer, EnumContainer


class BooleanContainerTest(TestCase):
    def test_init(self) -> None:
        self.assertEqual(BooleanContainer().normalize(False), False)
        self.assertEqual(BooleanContainer().normalize(True), True)
        self.assertEqual(BooleanContainer().normalize('off'), False)
        self.assertEqual(BooleanContainer().normalize('on'), True)
        self.assertEqual(BooleanContainer().normalize('off'), False)
        self.assertEqual(BooleanContainer().normalize('on'), True)


class EnumContainerTest(TestCase):
    def test_init(self) -> None:
        self.assertEqual(EnumContainer[LampMode](LampMode).normalize(LampMode.MANUAL), LampMode.MANUAL)
        self.assertEqual(EnumContainer[LampMode](LampMode).normalize(LampMode.AUTOMATIC), LampMode.AUTOMATIC)
        self.assertEqual(EnumContainer[LampMode](LampMode).normalize('manual'), LampMode.MANUAL)
        self.assertEqual(EnumContainer[LampMode](LampMode).normalize('automatic'), LampMode.AUTOMATIC)
        self.assertEqual(EnumContainer[LampMode](LampMode).normalize(0), LampMode.MANUAL)
        self.assertEqual(EnumContainer[LampMode](LampMode).normalize(1), LampMode.AUTOMATIC)
