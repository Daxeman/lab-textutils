import pytest
from textutils.slugify import slugify, truncate_slug


class TestSlugify:
    def test_enkelt_ord(self):
        assert slugify("hello") == "hello"

    def test_gemener(self):
        assert slugify("HELLO") == "hello"

    def test_mellanslag_blir_bindestreck(self):
        assert slugify("hello world") == "hello-world"

    def test_flera_mellanslag_ger_ett_bindestreck(self):
        assert slugify("hello   world") == "hello-world"

    def test_specialtecken_tas_bort(self):
        assert slugify("hello!world") == "hello-world"

    def test_siffror_bevaras(self):
        assert slugify("topp 10 listan") == "topp-10-listan"

    def test_inledande_mellanslag_ignoreras(self):
        assert slugify("  hello") == "hello"

    def test_avslutande_mellanslag_ignoreras(self):
        assert slugify("hello  ") == "hello"

    def test_tomt_strang_ger_valuerror(self):
        with pytest.raises(ValueError):
            slugify("")

    def test_bara_mellanslag_ger_valuerror(self):
        with pytest.raises(ValueError):
            slugify("   ")

    def test_fel_typ_ger_typeerror(self):
        with pytest.raises(TypeError):
            slugify(123)

    def test_none_ger_typeerror(self):
        with pytest.raises(TypeError):
            slugify(None)

    def test_bindestreck_i_borjan_tas_bort(self):
        assert not slugify("!hello").startswith("-")

    def test_bindestreck_i_slutet_tas_bort(self):
        assert not slugify("hello!").endswith("-")


class TestTruncateSlug:
    def test_kort_slug_andras_inte(self):
        assert truncate_slug("hello", max_length=50) == "hello"

    def test_lang_slug_kapas(self):
        slug = "detta-ar-en-valdigt-lang-slug-som-maste-kortas-ned"
        result = truncate_slug(slug, max_length=20)
        assert len(result) <= 20

    def test_kapning_sker_vid_ordgrans(self):
        result = truncate_slug("ett-tva-tre-fyra", max_length=10)
        assert not result.endswith("-")

    def test_exakt_langd_andras_inte(self):
        slug = "hello-world"
        assert truncate_slug(slug, max_length=11) == "hello-world"

    def test_max_length_noll_ger_valuerror(self):
        with pytest.raises(ValueError):
            truncate_slug("hello", max_length=0)

    def test_negativ_max_length_ger_valuerror(self):
        with pytest.raises(ValueError):
            truncate_slug("hello", max_length=-5)
