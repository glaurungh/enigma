from shift import shift
from rotor import rotor
from reflector import reflector
from pairs import check_pairs, get_pair

ROTORS_SHIFT = {
    1: [17],
    2: [5],
    3: [22],
    4: [10],
    5: [0],
    6: [0, 13],
    7: [0, 13],
    8: [0, 13]
}

def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs = ""):
    if not check_pairs(pairs):
        return "Извините, невозможно произвести коммутацию"
     
    res = []
    for s in text.upper():
        if s.isalpha():
            
            # Shift all the rotors
            shift3 = (shift3 + 1) % 26
            if shift2+1 in ROTORS_SHIFT[rot2]:
                shift2 = (shift2 + 1) % 26            
                for sh in ROTORS_SHIFT[rot2]:
                    if shift2 == sh:
                        shift1 = (shift1 + 1) % 26
            for sh in ROTORS_SHIFT[rot3]:
                if shift3 == sh:
                    shift2 = (shift2 + 1) % 26
            # End of rotors shiting
            s = get_pair(s, pairs)
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
            s = get_pair(s, pairs)
            res.append(s)
    return "".join(res)
