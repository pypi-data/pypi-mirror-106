"""Converts MEI files to volpiano strings.

Takes in one or more MEI files and outputs their volpiano representation.
See README for flags and usage.
"""

import xml.etree.ElementTree as ET

# namespace for MEI tags
NAMESPACE = "{http://www.music-encoding.org/ns/mei}"


class MEItoVolpiano:
    """
    Class: MEItoVolpiano

    Methods:

        [Main]:
            get_mei_elements(file) -> list[MEI elements]
            sylb_volpiano_map(list[elements]) -> dict[str, str]
            get_syl_key(element, integer) -> str
            get_volpiano(str, str) -> str
            export_volpiano(dict[str, str]) -> str
            convert_mei_volpiano(file) -> str

            ^ convert_mei_volpiano handles all methods in main.

        [Western]:
            Wsylb_volpiano_map(list[elements]) -> dict[str, str]
            Wconvert_mei_volpiano(file) -> str

            ^ Wconvert_mei_volpiano calls methods in Main to give
            the volpiano string for MEI files written in Western notation.

        [Debugging]:
            find_clefs(list[elements]) -> list[str]
            find_notes(list[elements]) -> list[str]
            find_syls(list[elements]) -> list[str]
            sylb_note_map(list[elements]) -> dict[str, str]

            ^ useful for MEI parsing and testing outputs.

    """

    def get_mei_elements(self, filename: str) -> list:
        """Returns a list of all elements in the MEI file.

        Args:
            filename (str): An open MEI file.

        Returns:
            elements (list): List of all elements found.
        """
        tree = ET.parse(filename)
        root = tree.getroot()
        mei_element_objects = root.findall(".//")

        return [mei_element for mei_element in mei_element_objects]

    def find_clefs(self, elements: list) -> list:
        """Finds all clefs in a given elements list

        Args:
            elements (list): List of elements

        Returns:
            clefs (list): char list of all clefs found, in order.
        """
        clefs = []
        for element in elements:
            if element.tag == f"{NAMESPACE}staffDef":
                clefs.append(element.attrib["clef.shape"])
            elif element.tag == f"{NAMESPACE}clef":
                clefs.append(element.attrib["shape"])
        return clefs

    def find_notes(self, elements: list) -> list:
        """Finds all notes in a given elements list

        Args:
            elements (list): List of elements

        Returns:
            notes (list): char list of all notes found, in order.
        """
        notes = []
        for element in elements:
            if element.tag == f"{NAMESPACE}nc":
                notes.append(element.attrib["pname"])

        return notes

    def find_syls(self, elements: list) -> list:
        """Finds all syllables in a given elements list

        Args:
            elements (list): List of elements

        Returns:
            syls (list): string list of all syllables found, in order.
        """
        syls = []
        for element in elements:
            if element.tag == f"{NAMESPACE}syl":
                if element.text:
                    syls.append(element.text)
        return syls

    def sylb_note_map(self, elements: list) -> dict:
        """Creates a dictionary map of syllables and their notes (with octaves).

        Args:
            elements (list): List of elements

        Returns:
            syl_dict (dict): Dictionary {identifier: notes} of syllables and
            their unique data base numbers as keys and notes (with octaves) as values.
        """

        syl_dict = {"dummy": ""}
        dbase_bias = 0
        last = "dummy"

        for element in elements:

            if element.tag == f"{NAMESPACE}syl":
                key = self.get_syl_key(element, dbase_bias)
                syl_dict[key] = syl_dict[last]
                dbase_bias += 1
                syl_dict["dummy"] = ""
                last = key

            if element.tag == f"{NAMESPACE}nc":
                note = element.attrib["pname"]
                ocv = element.attrib["oct"]
                finNote = f"{note}{ocv}"
                syl_dict[last] = f"{syl_dict[last]}{finNote}"

            if element.tag == f"{NAMESPACE}neume":
                if syl_dict[last] != "":
                    syl_dict[last] = f'{syl_dict[last]}{"-"}'

            if element.tag == f"{NAMESPACE}syllable":
                last = "dummy"

        del syl_dict["dummy"]
        return syl_dict

    def sylb_volpiano_map(self, elements: list) -> dict:
        """Creates a dictionary of syllables and their volpiano values.

        Args:
            elements (list): List of elements

        Returns:
            syl_note (dict): Dictionary {identifier: volpiano notes} of
            syllables and their unique data base numbers as keys and volpiano
            notes with correct octaves as values.
        """
        syl_note = {"dummy": ""}
        dbase_bias = 0
        last = "dummy"
        for element in elements:

            if element.tag == f"{NAMESPACE}syl":
                key = self.get_syl_key(element, dbase_bias)
                syl_note[key] = syl_note[last]
                dbase_bias += 1
                syl_note["dummy"] = ""
                last = key

            if element.tag == f"{NAMESPACE}nc":
                note = element.attrib["pname"]
                ocv = element.attrib["oct"]
                volpiano = self.get_volpiano(note, ocv)
                syl_note[last] = f"{syl_note[last]}{volpiano}"

            if element.tag == f"{NAMESPACE}neume":
                if syl_note[last] != "":
                    syl_note[last] = f'{syl_note[last]}{"-"}'

            if element.tag == f"{NAMESPACE}sb":
                if syl_note[last] != "":
                    syl_note[last] = f'{syl_note[last]}{"7"}'

            if element.tag == f"{NAMESPACE}syllable":
                if syl_note[last] != "":
                    syl_note[last] = f'{syl_note[last]}{"---"}'
                last = "dummy"

        return syl_note

    def Wsylb_volpiano_map(self, elements: list) -> dict:
        """Western notation - Creates a dictionary of syllables and their volpiano values.

        Args:
            elements (list): List of elements

        Returns:
            syl_note (dict): Dictionary {identifier: volpiano notes} of
            syllables and their unique data base numbers as keys and volpiano
            notes with correct octaves as values.
        """
        syl_note = {"dummy": ""}
        dbase_bias = 0
        octave_converter_weight = 2 #C4 in CWMN is octave 2 in volpiano
        last = "dummy"
        num = True
        for element in elements:
            if element.tag == f"{NAMESPACE}syl":
                key = self.get_syl_key(element, dbase_bias)
                if num:
                    syl_note[key] = f"{syl_note[last]}"
                    num = False
                else:
                    syl_note[key] = f'{"--"}{syl_note[last]}'
                dbase_bias += 1
                syl_note["dummy"] = ""
                last = "dummy"
            if element.tag == f"{NAMESPACE}note":
                note = element.attrib["pname"]
                ocv = element.attrib["oct"]
                ocv = int(ocv) - octave_converter_weight
                ocv = f"{ocv}"
                volpiano = self.get_volpiano(note, ocv)
                syl_note[last] = f"{syl_note[last]}{volpiano}"
        return syl_note

    def get_syl_key(self, element: object, bias: int) -> str:
        """Finds the dictionary key of a syllable from their 'syl' and database
        identifier.

        Args:
            element (element): A single element representing a syllable (syl)
            bias (int): The database identifier.

        Returns:
            key (str): The dictionary key for the given syllable.
        """
        key = -1
        if element.text:
            key = "".join(f"{bias}_")
            key = f"{key}{element.text}"
        else:
            key = "".join(f"{bias}")
        return key

    def get_volpiano(self, note: str, ocv: str) -> str:
        """Finds the volpiano representation of a note given its value and octave.

        Args:
            note (str): Note value taken from an element ('c', 'd', 'e' etc.)
            ocv (str): Octave of a given note ('1', '2', '3', or '4')

        Returns:
            oct{x}[note] (str): Volpiano character corresponding to
            input note and octave

            or

            error (str): Error if octave is out of range or note not in
            octave.

        """
        octs = {
            "1": {"g": "9", "a": "a", "b": "b"},
            "2": {"c": "c", "d": "d", "e": "e", "f": "f", "g": "g", "a": "h", "b": "j"},
            "3": {"c": "k", "d": "l", "e": "m", "f": "n", "g": "o", "a": "p", "b": "q"},
            "4": {"c": "r", "d": "s"},
        }

        oct_error = "OCTAVE_RANGE_ERROR"
        note_error = "NOTE_NOT_IN_OCTAVE"

        for key in octs:
            if key == ocv:
                if note in octs[key]:
                    return octs[key][note]
                else:
                    return note_error

        return oct_error

    def export_volpiano(self, mapping_dictionary: dict) -> str:
        """Creates volpiano string with clef attached.

        Args:
            mapping_dictionary (dict): Dictionary of syllables and their
            corresponding volpiano notes.

        Returns:
            (str): Final, valid volpiano with the clef attached in a single line.
        """
        values = list(mapping_dictionary.values())[1::]
        clef = "1---"
        vol_string = "".join(values)
        floating_notes = mapping_dictionary["dummy"]
        if len(floating_notes) == 1:
            notes = f"We found one syllable-independent note at the end of the MEI file: {floating_notes}"
            return f"{clef}{vol_string} \n\n{notes}"
        elif len(floating_notes) > 1:
            notes = f"We found numerous syllable-independent notes at the end of the MEI file: {floating_notes}"
            return f"{clef}{vol_string} \n\n{notes}"
        else:
            return f"{clef}{vol_string}"

    def convert_mei_volpiano(self, filename: str) -> str:
        """All-in-one method for converting MEI file to valid volpiano string.

        Args:
            filename (file): Open MEI file you want the volpiano of.

        Returns:
            volpiano (str): Valid volpiano string representation of the input.
        """
        elements = self.get_mei_elements(filename)
        mapped_values = self.sylb_volpiano_map(elements)
        volpiano = self.export_volpiano(mapped_values)
        return volpiano

    def Wconvert_mei_volpiano(self, filename: str) -> str:
        """All-in-one method for converting MEI in Western notation to volpiano.

        Args:
            filename (file): Open MEI file you want the volpiano of.

        Returns:
            volpiano (str): Valid volpiano string representation of the input.
        """

        elements = self.get_mei_elements(filename)
        mapped_values = self.Wsylb_volpiano_map(elements)
        volpiano = self.export_volpiano(mapped_values)
        return volpiano
