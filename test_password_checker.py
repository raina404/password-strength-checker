import pytest
from password_checker import check_strength


def test_empty_password():
    r = check_strength("")
    assert r.score == 0
    assert r.label == "Very Weak"
    assert any("empty" in f.lower() for f in r.feedback)


def test_very_short():
    r = check_strength("abc")
    assert r.score < 20
    assert r.label == "Very Weak"
    assert any("short" in f.lower() for f in r.feedback)


def test_common_password():
    r = check_strength("password")
    assert r.score <= 10
    assert any("commonly" in f.lower() for f in r.feedback)


def test_common_password_case_insensitive():
    r = check_strength("PASSWORD")
    assert r.score <= 10


def test_missing_uppercase():
    r = check_strength("alllowercase1!")
    assert any("uppercase" in f.lower() for f in r.feedback)


def test_missing_lowercase():
    r = check_strength("ALLUPPERCASE1!")
    assert any("lowercase" in f.lower() for f in r.feedback)


def test_missing_digit():
    r = check_strength("NoDigitsHere!")
    assert any("number" in f.lower() for f in r.feedback)


def test_missing_special():
    r = check_strength("NoSpecialChars1")
    assert any("special" in f.lower() for f in r.feedback)


def test_sequential_chars():
    r = check_strength("abcPassword1!")
    assert any("sequential" in f.lower() for f in r.feedback)


def test_sequential_digits():
    r = check_strength("Pass123word!")
    assert any("sequential" in f.lower() for f in r.feedback)


def test_repeated_chars():
    r = check_strength("Paaasword1!")
    assert any("repeated" in f.lower() for f in r.feedback)


def test_strong_password():
    r = check_strength("T!g3r$XmP#9qLw")
    assert r.score >= 60
    assert r.label in ("Strong", "Very Strong")
    assert r.feedback == []


def test_very_strong_password():
    r = check_strength("K@9mVz#2Lp!wQr8&")
    assert r.score >= 80
    assert r.label == "Very Strong"


def test_score_clamped():
    r = check_strength("a" * 100)
    assert 0 <= r.score <= 100


def test_labels():
    labels = {"Very Weak", "Weak", "Fair", "Strong", "Very Strong"}
    for pw in ["a", "abc1234!", "Hello1!", "T!g3r$XmP#9q", "K@9mVz#2Lp!wQr8&"]:
        assert check_strength(pw).label in labels


def test_long_password_scores_higher_than_short():
    short = check_strength("Ab1!")
    long_ = check_strength("Ab1!" * 4)
    assert long_.score >= short.score
