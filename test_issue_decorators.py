import allure
from selene import browser, have
from selene.support.shared.jquery_style import s


@allure.title("Проверка текста ссылки первой ошибки в репозитории используя @allure.step")
@allure.description("Шаги с декоратором @allure.step")
@allure.tag("UI")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Gleb T")
@allure.link("https://github.com/", name="Website")
@allure.issue("ISSUE-123")
@allure.testcase("TMS-458")
def test_issue_link_with_decorators():
    steps = Steps()
    steps.open_browser()
    steps.open_issues_tab()
    steps.check_link()


class Steps:
    @allure.step("Open Repo link")
    def open_browser(self):
        browser.open("/Glebezy/lesson-10")

    @allure.step("Open issues tab")
    def open_issues_tab(self):
        s("#issues-tab").click()

    @allure.step("Check issue link")
    def check_link(self):
        s("#issue_1_link").should(have.text("First issue"))