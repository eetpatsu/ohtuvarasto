import unittest
from varasto import Varasto
# kommentti

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_huomaa_virheellisen_tilavuuden(self):
        self.varasto = Varasto(-1.0)
        self.assertEqual(self.varasto.tilavuus, 0.0)

    def test_konstruktori_huomaa_virheellisen_saldon(self):
        self.varasto = Varasto(0, -1.0)
        self.assertEqual(self.varasto.saldo, 0.0)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_varastoon_liian_pieni(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertEqual(self.varasto.saldo, 0)

    def test_lisays_varastoon_liian_suuri(self):
        self.varasto.lisaa_varastoon(11)

        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ottaminen_varastosta_liian_pieni(self):
        saatu_maara = self.varasto.ota_varastosta(-1)

        self.assertEqual(saatu_maara, 0.0)

    def test_ottaminen_varastosta_liian_suuri(self):
        self.varasto.lisaa_varastoon(10)
        saatu_maara = self.varasto.ota_varastosta(11)

        self.assertEqual(saatu_maara, 10)

    def test_varasto_tulostuu_oikein(self):
        vastaus = str(self.varasto)

        self.assertEqual(vastaus, "saldo = 0, vielä tilaa 10")

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
