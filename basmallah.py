# Le probleme d'affichage des caracteres arabes est du a lediteur
# Il ne supporte pas langues qui vont de la droite cers la gauche
# LA fonction de recherche doit me servir a rechercher des token par exemple les Ayat ou je retrouve Le Token 'haza' dans le QRN
# J'aimerai avoir un fonctionnalite qui m'aident a attacher des ressources ou des commentaires a un ayatt ou une sourat donne
# pour en faliciter ma meditation et faire du lien plus facilement.
# Idealement je pourrais partager des commentaires ou ressources facilement avec un proche ou recuillier les plus populaires sur la plateforme
# Tips pour decouper un texte en mot  print(re.split(r"\W+", sentence))

# TO DO
# Mettre en place la detection de la basmallah qd on aura aborder louverture de fichier
# Mettre en place la transcription automatique grace a la methode translate et maketranslate
from bidi.algorithm import get_display
import re


def disp(my_surat):
    if (my_surat):
        my_ayat = 'بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ'
        print(get_display(my_ayat))
        return 'بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ'
    else:
        return False


def nbrOfToken(my_ayat):
    if (my_ayat):
        return len(my_ayat.split())
    else:
        return 0


def transcript(my_araf):
    my_alphabet_dico = {"ا": "alif", "ﺍـ": "alif", "ـﺎـ": "alif", "ـﺎ": "alif"}
    # Tester avec le module pyarabic // UnicodeDecodeError: 'charmap'/
    # Prevoir de faire notre propre algo de transcription
    if (my_araf in my_alphabet_dico):
        return my_alphabet_dico[my_araf]
    else:
        return False


def transliterate(my_transcription):
    my_transcription_dico = {
        "â": "ا",
        "A": "اَ", "I": "اِ", "U": "اُ",
        "A-": "اً", "I-": "اٍ", "U-": "اٌ",

        "b": "ب", "t": "ت", "ç": "ث",
        "j": "ج", "h": "ح", "x": "خ",
        "d": "د", "th": "ذ", "r": "ر", "z": "ز",
        "s": "س", "ch": "ش", "f": "ف", "q": "ق",
        "S": "ص", "D": "ض", "T": "ط", "Z": "ظ",
        "ë": "ع", "gh": "غ",
        "k": "ك", "l": "ل", "m": "م", "n": "ن",
        "H": "ه", "w": "و", "y": "ي",
        "ba-": "بً", "bi-": "بٍ", "bu-": "بٌ",
        "a": '\u064e', "i": '\u0650', "u": '\u064f',
		"a-": '\u064b', "i-": '\u064d', "u-": '\u064c'
        # gerer les debut de mots, les fin de mots, et les milieu
    }

    if ((len(my_transcription) > 1) and ( my_transcription not in ['A-', 'U-', 'I-','u-', 'a-', 'i-'])):
	    add_tanwin = '-' if (min(my_transcription) in '-') else ''
	    if (re.match(r"(\w*)[aiu]", my_transcription) is not None):
        	match = re.match(r"(?P<consonne>\w*)(?P<voyelle>[aiu])", my_transcription)
        	return my_transcription_dico[match.group('consonne')] + my_transcription_dico[match.group('voyelle')+add_tanwin]
    elif (my_transcription in my_transcription_dico):
        return my_transcription_dico[my_transcription]
    else:
        return False
