import pytest
from textutils.password import (
    check_strength,
    has_common_pattern,
    WEAK,
    MEDIUM,
    STRONG,
    VERY_STRONG,
)


class TestCheckStrength:
    def test_kort_losenord_ar_svagt(self):
        assert check_strength("abc") == WEAK

    def test_bara_gemener_ar_svagt(self):
        assert check_strength("abcdefgh") == WEAK

    def test_gemener_och_siffror_ger_medium(self):
        assert check_strength("abcde123") == MEDIUM

    def test_tre_teckrenklasser_ger_starkt(self):
        assert check_strength("Abcde12345") == STRONG

    def test_alla_teckrenklasser_och_lang_ger_mycket_starkt(self):
        assert check_strength("Abcde12345!@") == VERY_STRONG

    def test_tomt_losenord_ar_svagt(self):
        assert check_strength("") == WEAK

    def test_fel_typ_ger_typeerror(self):
        with pytest.raises(TypeError):
            check_strength(12345)

    def test_none_ger_typeerror(self):
        with pytest.raises(TypeError):
            check_strength(None)

    def test_exakt_12_tecken_med_alla_klasser(self):
        assert check_strength("Abc123!@#def") == VERY_STRONG

    def test_10_tecken_tre_klasser_ger_starkt(self):
        assert check_strength("Abcde12345") == STRONG


class TestHasCommonPattern:
    def test_upprepade_tecken_ger_true(self):
        assert has_common_pattern("aaabbb") is True

    def test_siffersekvens_ger_true(self):
        assert has_common_pattern("abc123456xyz") is True

    def test_qwerty_ger_true(self):
        assert has_common_pattern("myqwertypass") is True

    def test_slumpmassigt_losenord_ger_false(self):
        assert has_common_pattern("xK9!mP2#vL5") is False

    def test_tomt_losenord_ger_false(self):
        assert has_common_pattern("") is False

    def test_fel_typ_ger_typeerror(self):
        with pytest.raises(TypeError):
            has_common_pattern(123)

    def test_upprepning_case_insensitive(self):
        assert has_common_pattern("AAAtest") is True

    def test_inga_upprepningar_ger_false(self):
        assert has_common_pattern("aabbcc") is False
