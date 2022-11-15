from my_calendar import vaiGaraisGads, dienuSkaits, ievaddatuParbaude


""" Garais gads - testi """

def test_vaiGG_2018():
    assert vaiGaraisGads(2018) is False

def test_vaiGG_2002():
    assert vaiGaraisGads(2002) is False

def test_vaiGG_1900():
    assert vaiGaraisGads(1900) is False

def test_vaiGG_1988():
    assert vaiGaraisGads(1988) is True

def test_vaiGG_2000():
    assert vaiGaraisGads(2000) is True

def test_vaiGG_2400():
    assert vaiGaraisGads(2400) is True
    

""" Dienu skaits - testi """

def test_dienuSkaits_feb28():
    assert dienuSkaits(2, False) == 28

def test_dienuSkaits_feb29():
    assert dienuSkaits(2, True) == 29

def test_dienuSkaits_30():
    assert dienuSkaits(4) == 30  # aprīlis
    assert dienuSkaits(6) == 30  # jūnijs
    assert dienuSkaits(9) == 30  # septembris
    assert dienuSkaits(11) == 30  # novembris

def test_dienuSkaits_31():
    assert dienuSkaits(1) == 31  # janvāris
    assert dienuSkaits(3) == 31  # marts
    assert dienuSkaits(5) == 31  # maijs
    assert dienuSkaits(7) == 31  # jūlijs
    assert dienuSkaits(8) == 31  # augusts
    assert dienuSkaits(10) == 31  # oktobris
    assert dienuSkaits(12) == 31  # decembris


""" Ievaddatu pārbaude - testi """

def test_ievaddatuParbaude_pareizi():
    assert ievaddatuParbaude("11/2005") is True
    assert ievaddatuParbaude("09/1878") is True
    assert ievaddatuParbaude("01/2020") is True

def test_ievaddatuParbaude_kludaini():
    assert ievaddatuParbaude("1/1999") is False
    assert ievaddatuParbaude("10.1999") is False
    assert ievaddatuParbaude("04/800") is False
    assert ievaddatuParbaude("12\1996") is False
    assert ievaddatuParbaude("janvaris\1996") is False