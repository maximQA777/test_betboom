
from page_object.page import Authorization, BonusAndStocks, Sport, Registration, GameChecker


def test_sport24():
    sport24_page = GameChecker()
    sport24_page.open()

    sport24_page.check_express37()
    sport24_page.check_express38()
    sport24_page.check_nard()



def test_auth():
    authorization_page = Authorization()
    authorization_page.open()

    authorization_page.open_authorization()
    authorization_page.set_number('12344')
    authorization_page.set_password('1223')
    authorization_page.check_error_text()


def test_registration():
    registration_page = Registration()
    registration_page.open()
    registration_page.open_registration()
    registration_page.check_regist_sber()
    registration_page.check_regist_Tbank()




def test_bonus_stocks():
    bonus_stocks = BonusAndStocks()
    bonus_stocks.open()

    bonus_stocks.open_bonus()
    bonus_stocks.open_club()
    bonus_stocks.check_text_club()
    bonus_stocks.open_status()
    bonus_stocks.check_text_status()

def test_check_cyper_spotr():
    sport = Sport()
    sport.open()

    sport.open_sports()
    sport.check_text_cs2()
    sport.check_text_dota2()
    sport.check_text_rocket()
    sport.check_text_valorant()
    sport.check_text_ml()
    sport.check_text_kog()
    sport.check_text_call_of_duty()
    sport.check_text_sc1()



















