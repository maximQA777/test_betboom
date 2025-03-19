import allure
from selene import browser, have, by
from selene.support.conditions import be

class Authorization:
    CSS_OPEN_AUTH = '.Button-sc-zdin7l-0.Button__TransparentButton-sc-zdin7l-1'

    @classmethod
    @allure.step("Открываем главную страницу")
    def open(cls):
        browser.config.base_url = 'https://betboom.ru'
        browser.open('/')

    @allure.step("Открываем форму авторизации")
    def open_authorization(self):
        browser.element(self.CSS_OPEN_AUTH).click()

    @allure.step("Вводим номер телефона")
    def set_number(self, invalid_number):
        browser.element('.sc-eMshUc').type(invalid_number)

    @allure.step("Вводим пароль")
    def set_password(self, invalid_password):
        browser.element('input[name="password"]').type(invalid_password)
        browser.element('button[type=submit]').click()

    @allure.step("Проверяем текст ошибки")
    def check_error_text(self):
        browser.element(by.text("Обязательное поле")).should(have.text("Обязательное поле"))
        browser.element(by.text("Минимум 8 символов")).should(have.text("Минимум 8 символов"))


class BonusAndStocks:
    CSS_OPEN = '.ActionsTags__ActionsTagsItem-sc-1edm1fb-1.CkPrI'

    @allure.step("Открываем главную страницу")
    def open(cls):
        browser.config.base_url = 'https://betboom.ru'
        browser.open('/')

    @allure.step("Открываем раздел Акции и бонусы")
    def open_bonus(self):
        browser.element(by.text("Акции и бонусы")).click()

    @allure.step("Открываем раздел Клуб")
    def open_club(self):
        browser.all(self.CSS_OPEN)[2].click()

    @allure.step("Проверяем текст Приведи друга")
    def check_text_club(self):
        browser.element(by.text("Приведи друга")).should(have.text("Приведи друга"))

    @allure.step("Открываем раздел 'Статус'")
    def open_status(self):
        browser.all(self.CSS_OPEN)[1].click()

    @allure.step("Проверяем текст Boom Статус")
    def check_text_status(self):
        browser.element(by.text("Boom Статус")).should(have.text("Boom Статус"))


class Sport:
    GAME_LIST_SELECTOR = '.swiper.swiper-module.swiper-initialized.swiper-horizontal.swiper-free-mode.Edqq1-98b74d03.swiper-backface-hidden'
    CSS_OPEN_SPORT = '.Header__HeaderNavigation-sc-w4usz4-3.ehvUxm'

    @allure.step("Открываем главную страницу")
    def open(cls):
        browser.config.base_url = 'https://betboom.ru'
        browser.open('/')

    @classmethod
    @allure.step("Открываем раздел Киберспорт")
    def open_sports(cls):
        browser.element(cls.CSS_OPEN_SPORT).should(have.text('Киберспорт')).click()

    @allure.step("Проверяем текст в списке игр")
    def check_text_in_game_list(self, text):
        browser.element(self.GAME_LIST_SELECTOR).should(be.visible)
        browser.element(self.GAME_LIST_SELECTOR).should(have.text(text))

    @allure.step("Проверяем текст 'CS2'")
    def check_text_cs2(self):
        self.check_text_in_game_list('CS2')

    @allure.step("Проверяем текст 'Dota 2'")
    def check_text_dota2(self):
        self.check_text_in_game_list('Dota 2')

    @allure.step("Проверяем текст 'LoL'")
    def check_text_lol(self):
        self.check_text_in_game_list('LoL')

    @allure.step("Проверяем текст 'Valorant'")
    def check_text_valorant(self):
        self.check_text_in_game_list('Valorant')

    @allure.step("Проверяем текст 'ML'")
    def check_text_ml(self):
        self.check_text_in_game_list('ML')

    @allure.step("Проверяем текст 'KoG'")
    def check_text_kog(self):
        self.check_text_in_game_list('KoG')

    @allure.step("Проверяем текст 'Call of Duty'")
    def check_text_call_of_duty(self):
        self.check_text_in_game_list('Call of Duty')

    @allure.step("Проверяем текст 'Rocket League'")
    def check_text_rocket(self):
        self.check_text_in_game_list('Rocket League')

    @allure.step("Проверяем текст 'SC1'")
    def check_text_sc1(self):
        self.check_text_in_game_list('SC1')