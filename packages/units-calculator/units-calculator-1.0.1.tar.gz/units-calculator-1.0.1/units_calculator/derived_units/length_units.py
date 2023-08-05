"""A module containing distance units definitions"""

from units_calculator.engine.engine import DerivedUnit
from units_calculator.si_units.si_units import Meters


class Decimeters(DerivedUnit):
    """Decimeters"""

    __symbol__ = "dm"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 1e-1


class Centimeters(DerivedUnit):
    """Centimeters"""

    __symbol__ = "cm"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 1e-2


class Millimeters(DerivedUnit):
    """Millimeters"""

    __symbol__ = "mm"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 1e-3


class Micrometers(DerivedUnit):
    """Micrometers"""

    __symbol__ = "um"
    __base_units__ = [(Millimeters, 1)]
    __multiplier__ = 1e-3


class Nanometers(DerivedUnit):
    """Nanometers"""

    __symbol__ = "nm"
    __base_units__ = [(Micrometers, 1)]
    __multiplier__ = 1e-3


class Angstroms(DerivedUnit):
    """Angstroms"""

    __symbol__ = "Å"
    __base_units__ = [(Nanometers, 1)]
    __multiplier__ = 1e-10


class Picometers(DerivedUnit):
    """Picometers"""

    __symbol__ = "pm"
    __base_units__ = [(Nanometers, 1)]
    __multiplier__ = 1e-3


class Kilometers(DerivedUnit):
    """Kilometers"""

    __symbol__ = "km"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 1e3


class Inches(DerivedUnit):
    """Inches"""

    __symbol__ = "in"
    __base_units__ = [(Millimeters, 1)]
    __multiplier__ = 25.4


class Feet(DerivedUnit):
    """Feet"""

    __symbol__ = "ft"
    __base_units__ = [(Inches, 1)]
    __multiplier__ = 12


class Yards(DerivedUnit):
    """Yards"""

    __symbol__ = "yd"
    __base_units__ = [(Feet, 1)]
    __multiplier__ = 3


class Miles(DerivedUnit):
    """Terrestrial miles"""

    __symbol__ = "mi"
    __base_units__ = [(Yards, 1)]
    __multiplier__ = 1760


class NauticalMiles(DerivedUnit):
    """Nautical miles"""

    __symbol__ = "nmi"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 1852


class EarthRadii(DerivedUnit):
    """Earth radii"""

    __symbol__ = "R⊕"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 6.3781e6


class LunarDistances(DerivedUnit):
    """Lunar distances"""

    __symbol__ = "LD"
    __base_units__ = [(Kilometers, 1)]
    __multiplier__ = 384402


class AstronomicalUnits(DerivedUnit):
    """Astronomical units"""

    __symbol__ = "au"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 1.495978707e11


class LightYears(DerivedUnit):
    """Light years"""

    __symbol__ = "ly"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 9.4607e15


class Parsec(DerivedUnit):
    """Parsecs"""

    __symbol__ = "pc"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 3.0857e16
