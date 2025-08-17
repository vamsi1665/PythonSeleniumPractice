from datetime import datetime
from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# html report
def pytest_html_report_title(report):
    report.title = "NopCommerce Automation Report"


# ✅ Add environment / metadata info at the top of the report
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.append("Project: Vamsi Framework")
    prefix.append("Module: Customers")
    prefix.append("Tester: Vamsi")
    prefix.append(f"Execution Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
