from main import account_creation
from main import apply_trans
from main import money_withdr
from main import moneyadd
from main import pass_check
from main import trans_filtering_logics

transactions = {
    "Ot Vasi": 100,
    "Ot Juri": 200
}


def test_apply_trans_small_limit():
    assert apply_trans(100, 160, {
        "Ot Vasi": 100,
        "Ot Juri": 200,
        "Ot Sergeja dolg": 200
    }) == 100


def test_apply_trans():
    assert apply_trans(100, 400, {
        "Ot Vasi": 100,
        "Ot Juri": 200
    }) == 400


def test_trans_filtering_logics():
    assert trans_filtering_logics(transactions, 150) == True


def test_monyadd():
    assert moneyadd(1, 2, 6) == 3


def test_monyadd_smallLimit():
    assert moneyadd(1, 2, 2) == 1


def test_money_wthdrw_too_little_ballance():
    assert money_withdr(9, 100) == 9


def test_money_wthdrw():
    assert money_withdr(12, 4) == 8


def test_pass_check():
    assert pass_check("zzz", "zzzz") == False
    assert pass_check("zzz", "zzz") == True


def test_account_creation():
    assert account_creation() == True
