import pytest
from textutils.stats import word_count, sentence_count, average_word_length, summarize


class TestWordCount:
    def test_enkelt(self):
        assert word_count("hej varlden") == 2

    def test_ett_ord(self):
        assert word_count("hej") == 1

    def test_tom_strang(self):
        assert word_count("") == 0

    def test_bara_mellanslag(self):
        assert word_count("   ") == 0

    def test_flera_mellanslag_mellan_ord(self):
        assert word_count("hej   varlden") == 2

    def test_radbrytning_raknas_som_separator(self):
        assert word_count("hej\nvarlden") == 2

    def test_fel_typ_ger_typeerror(self):
        with pytest.raises(TypeError):
            word_count(42)


class TestSentenceCount:
    def test_en_mening(self):
        assert sentence_count("Hej varlden.") == 1

    def test_tva_meningar(self):
        assert sentence_count("Hej. Hur mar du?") == 2

    def test_utropstecken(self):
        assert sentence_count("Hej! Vad kul!") == 2

    def test_blandade_avslut(self):
        assert sentence_count("Hej. Hur mar du? Bra!") == 3

    def test_tom_strang(self):
        assert sentence_count("") == 0

    def test_bara_mellanslag(self):
        assert sentence_count("   ") == 0

    def test_tre_punkter_raknas_som_ett_avslut(self):
        assert sentence_count("Hmm... Det var intressant.") == 2

    def test_fel_typ_ger_typeerror(self):
        with pytest.raises(TypeError):
            sentence_count(None)


class TestAverageWordLength:
    def test_enkelt(self):
        assert average_word_length("hej du") == 2.5

    def test_ett_ord(self):
        assert average_word_length("hej") == 3.0

    def test_tom_strang(self):
        assert average_word_length("") == 0.0

    def test_avrundat_till_tva_decimaler(self):
        result = average_word_length("ett tva tre")
        assert result == round(result, 2)

    def test_fel_typ_ger_typeerror(self):
        with pytest.raises(TypeError):
            average_word_length(["hej", "varlden"])


class TestSummarize:
    def test_returnerar_ordbok(self):
        result = summarize("Hej varlden. Hur mar du?")
        assert isinstance(result, dict)

    def test_korrekt_ordrakning(self):
        result = summarize("ett tva tre")
        assert result["ord"] == 3

    def test_korrekt_meningsrakning(self):
        result = summarize("Hej. Hur mar du?")
        assert result["meningar"] == 2

    def test_korrekt_teckenrakning(self):
        text = "abc"
        result = summarize(text)
        assert result["tecken"] == 3

    def test_alla_nycklar_finns(self):
        result = summarize("test")
        assert "ord" in result
        assert "meningar" in result
        assert "tecken" in result
        assert "genomsnittlig_ordlangd" in result

    def test_tom_strang(self):
        result = summarize("")
        assert result["ord"] == 0
        assert result["meningar"] == 0
        assert result["tecken"] == 0
        assert result["genomsnittlig_ordlangd"] == 0.0

    def test_fel_typ_ger_typeerror(self):
        with pytest.raises(TypeError):
            summarize(42)
