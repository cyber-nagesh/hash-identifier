import hashlib

from hash_identifier import identify


def h(algo, text="hello"):
    return hashlib.new(algo, text.encode()).hexdigest()


def test_md5():
    assert "MD5 / NTLM" in identify(h("md5"))


def test_sha1():
    assert identify(h("sha1")) == ["SHA-1"]


def test_sha256():
    assert identify(h("sha256")) == ["SHA-256"]


def test_sha512():
    assert identify(h("sha512")) == ["SHA-512"]


def test_bcrypt():
    sample = "$2b$12$" + "a" * 53
    assert identify(sample) == ["bcrypt"]


def test_sha512crypt():
    assert identify("$6$somesalt$abcdefghijklmnop") == ["SHA-512crypt"]


def test_argon2():
    sample = "$argon2id$v=19$m=65536,t=3,p=4$c29tZXNhbHQ$abcdefgh"
    assert identify(sample) == ["Argon2"]


def test_uppercase_hex():
    assert identify(h("sha1").upper()) == ["SHA-1"]


def test_whitespace_is_stripped():
    assert identify("  " + h("sha256") + "\n") == ["SHA-256"]


def test_invalid_input():
    assert identify("not-a-hash") == []


def test_empty_input():
    assert identify("") == []
