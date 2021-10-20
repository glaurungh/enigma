from shift import shift
from rotor import rotor
from reflector import reflector

def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    res = []
    for s in text.upper():
        if s.isalpha():
            s = shift(s, shift3)
            s = rotor(s, rot3)
            s = shift(s, shift2-shift3)
            s = rotor(s, rot2)
            s = shift(s, shift1 - shift2)
            s = rotor(s, rot1)
            s = shift(s, -shift1)
            s = reflector(s, ref)
            s = shift(s, shift1)
            s = rotor(s, rot1, reverse=True)
            s = shift(s, shift2-shift1)
            s = rotor(s, rot2, reverse=True)
            s = shift(s, shift3-shift2)
            s = rotor(s, rot3, reverse=True)
            s = shift(s, -shift3)
            res.append(s)
    return "".join(res)

