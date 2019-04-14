from scraper.scraper import scrape_jobs, get_driver

if __name__ == '__main__':
    driver = get_driver()
    # , 'software engineer',
    job_titles = ['data scientist', 'software engineer',
                  'data engineer', 'python developer', 'javascript developer']
    # 'data engineer', 'software developer', 'front-end developer']
    for job in job_titles:
        print(scrape_jobs(driver, job))
    driver.quit()
    # print(scrape_jobs(get_driver()))
