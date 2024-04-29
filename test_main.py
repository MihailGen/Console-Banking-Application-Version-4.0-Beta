from main import account_creation
from main import apply_trans
from main import money_withdr
from main import moneyadd
from main import pass_check
from main import trans_filtering_logics
from main import postponed_trigger
from main import postponed_to_file
from main import check_login_and_passw
from main import hash_to_file
from main import check_log
from main import hash_funct
from main import client_from_file
from main import transaction_from_file
from main import transactionfout


transactions = {
    "Ot Vasi": 100,
    "Ot Juri": 200
}

def test_transactionfout():
    assert transactionfout(transactions) == True

def test_transaction_from_file():
    assert transaction_from_file() == transactions

def test_client_from_file():
    assert client_from_file() == ("Test", "Test", 0, "Test", 1000, 0)

def test_hash_funct():
    assert hash_funct("1") == "4949"

def test_check_log():
    assert check_log("MiHa") == True

def test_hash_to_file():
    assert hash_to_file("4949", "MiHa") == True

def test_check_login_and_passw():
    assert check_login_and_passw("MiHa", "1") == True


def test_postponed_to_file_big():
    assert postponed_to_file("MiHa", "VajaPupj", 1200) == True

def test_postponed_to_file():
    assert postponed_to_file("MiHa", "VajaPupj", 200) == False


def test_postponed_trigger():
    assert postponed_trigger("MiHa") == True

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
