import unittest
import basmallah


class TestBsmllh(unittest.TestCase):
    def test_do_nothing(self):
        self.assertEqual(basmallah.disp(''), False)

    def test_firstLineOfSouratShouldBeBasmallah(self):
        my_surat_file = 'fatiha.txt'
        self.assertEqual(basmallah.disp(my_surat_file),
                         'بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ')

    def test_shouldReturn4IfAyatIsBasmallah(self):
        self.assertEqual(basmallah.nbrOfToken(
            'بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ'), 4)

    def test_shouldReturn_Alif(self):
        self.assertEqual(basmallah.transcript('ا'), 'alif')

    def test_shouldReturn_AlifenDebut2mot(self):
        self.assertEqual(basmallah.transcript('ﺍـ'), 'alif')

    def test_shouldReturn_Alif_milieu(self):
        self.assertEqual(basmallah.transcript('ـﺎـ'), 'alif')

    def test_shouldReturn_Alif_fin(self):
        self.assertEqual(basmallah.transcript('ـﺎ'), 'alif')

    def test_shouldReturn_Alif_if_alif(self):
        self.assertEqual(basmallah.transliterate('â'), 'ا')

    def test_shouldReturn_AlifAndFata_if_a(self):
        self.assertEqual(basmallah.transliterate('A'), 'اَ')

    def test_shouldReturn_AlifAndKassra_if_i(self):
        self.assertEqual(basmallah.transliterate('I'), 'اِ')

    def test_shouldReturn_AlifAndDamma_if_u(self):
        self.assertEqual(basmallah.transliterate('U'), 'اُ')

    def test_shouldReturn_AlifAndTnwnFata_if_a(self):
        self.assertEqual(basmallah.transliterate('A-'), 'اً')

    def test_shouldReturn_AlifAndTnwnKassra_if_i(self):
        self.assertEqual(basmallah.transliterate('I-'), 'اٍ')

    def test_shouldReturn_AlifAndTnwnDamma_if_u(self):
        self.assertEqual(basmallah.transliterate('U-'), 'اٌ')

    def test_shouldReturn_bAndTnwnDamma_if_bu(self):
        self.assertEqual(basmallah.transliterate('bu-'), 'بٌ')

    def test_shouldReturn_Damma_if_u(self):
        self.assertEqual(basmallah.transliterate('u'), '\u064f')

    def test_shouldReturn_TanwinDamma_ifuAndMinus(self):
        self.assertEqual(basmallah.transliterate('u-'), '\u064c')

    def test_shouldReturn_bAndDamma_if_bu(self):
        self.assertEqual(basmallah.transliterate('bu'), 'بُ')

    def test_shouldReturn_bAndKassra_if_bi(self):
        self.assertEqual(basmallah.transliterate('bi'), 'بِ')

    def test_shouldReturn_bAndFatha_if_ba(self):
        self.assertEqual(basmallah.transliterate('ba'), 'بَ')

    def test_shouldReturn_tAndFatha_if_ta(self):
        self.assertEqual(basmallah.transliterate('ta'), 'تَ')

    def test_shouldReturn_chAndFatha_if_cha(self):
        self.assertEqual(basmallah.transliterate('cha'), 'شَ')

    def test_shouldReturn_thAndKassra_if_thi(self):
        self.assertEqual(basmallah.transliterate('thi'), 'ذِ')
		
    def test_shouldReturn_thAndTanwinKassra_if_thi_and_minus(self):
    	self.assertEqual(basmallah.transliterate('thi-'), 'ذٍ')
    # def test_shoulReturn_i(self):
    #	self.assertEqual(basmallah.transcript('اِ'), 'i')


if __name__ == '__main__':
    unittest.main()
