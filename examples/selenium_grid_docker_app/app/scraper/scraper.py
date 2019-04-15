#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from .indeed_page import IndeedPage


def get_driver():
    options = Options()
    options.add_argument('--headless')
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['version'] = "73.0.3683.86"

    # TODO Comment out if using selenium-grid and docker
    # driver = webdriver.Chrome(
    #     desired_capabilities=capabilities,
    #     options=options
    # )

    # TODO Comment out if testing for local data scraping
    driver = webdriver.Remote(
        command_executor='http://142.93.185.176:4444/wd/hub',
        desired_capabilities=capabilities,
        options=options
    )
    driver.set_window_size(1440, 900)
    print('Got driver! \n')
    return driver


def scrape_jobs(driver, job_title):

    ip = IndeedPage(driver=driver)
    ip.go()
    ip.search_input.input_text(job_title)
    ip.search_job_button.click()

    job_details = []

    while ip.next_page_button:
        job_details.extend(ip.get_job_details(ip.get_job_cards))
        ip.next_page_button.click_next_page()

        try:
            ip.popup.click()
        except:
            pass
        if len(job_details) > 100:
            return job_details
    return None
