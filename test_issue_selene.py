
import allure
from selene import browser, have
from selene.support.shared.jquery_style import s



@allure.title("Проверка текста ссылки первой ошибки в репозитории используя чистый Selene")
@allure.description("Чистый Selene (без шагов)")
@allure.tag("UI")
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "Gleb T")
@allure.link("https://github.com/", name="Website")
@allure.issue("ISSUE-123")
@allure.testcase("TMS-456")
def test_issue_link_with_selene():
    browser.open("/Glebezy/lesson-10")
    s("#issues-tab").click()
    s("#issue_1_link").should(have.text("First issue"))
