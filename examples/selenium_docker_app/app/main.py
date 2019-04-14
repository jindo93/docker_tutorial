from scraper.scraper import scrape_jobs, get_driver
from time import time

if __name__ == '__main__':
    start = time()
    driver = get_driver()
    job_titles = ['data scientist', 'software engineer',
                  'data engineer', 'python developer', 'javascript developer']
    for job in job_titles:
        local_start = time()
        print(scrape_jobs(driver, job))
        local_end = time()
        print('It took ', local_end-local_start,
              ' to get data for: "{0}"'.format(job))
    driver.quit()
    end = time()
    print("\n It took total of ", end-start, " time to get all data \n")
