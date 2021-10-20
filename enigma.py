from rotor import rotor
from reflector import reflector
def enigma(text, ref, rot1, rot2, rot3):
    res = []
    for s in text.upper():
        if s.isalpha():
            s = rotor(s, rot3)
            s = rotor(s, rot2)
            s = rotor(s, rot1)
            s = reflector(s, ref)
            s = rotor(s, rot1, reverse=True)
            s = rotor(s, rot2, reverse=True)
            s = rotor(s, rot3, reverse=True)
            res.append(s)
    return "".join(res)
