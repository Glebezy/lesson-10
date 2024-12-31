import allure
from selene import browser, have
from selene.support.shared.jquery_style import s


@allure.title("Проверка текста ссылки первой ошибки в репозитории используя allure.step")
@allure.description("Лямбда шаги через with allure.step")
@allure.tag("UI")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Gleb T")
@allure.link("https://github.com/", name="Website")
@allure.issue("ISSUE-123")
@allure.testcase("TMS-457")
def test_issue_link_with_step():
    with allure.step("Open Repo link"):
        browser.open("/Glebezy/lesson-10")
    with allure.step("Open issues tab"):
        s("#issues-tab").click()
    with allure.step("Check issue link"):
        s("#issue_1_link").should(have.text("First issue"))