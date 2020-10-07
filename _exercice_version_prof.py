#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys
sys.path.insert(1, 'PUT_YOUR_PATHHERE')
from c04_ch6_exercices.exercice import frequence



def compute_volume_and_mass(a=2, b=4, c=6, masse_vol=10):
    volume = math.pi * a * b * c * 4 / 3
    masse = volume * masse_vol

    return volume, masse


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(compute_volume_and_mass())
    print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("bbbig bbbig test"))

    pass
