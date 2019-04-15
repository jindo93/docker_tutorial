from scraper.scraper import scrape_jobs, get_driver
from time import time
import sys

if __name__ == '__main__':
    start = time()
    driver = get_driver()
    # job_titles = ['data scientist', 'software engineer',
    #               'data engineer', 'python developer', 'javascript developer']
    print('Start scraping 100 data for: ', sys.argv[1]+sys.argv[2])
    scrape_jobs(driver, sys.argv[1]+sys.argv[2])
    # for job in job_titles:
    #     print('Start scraping 100 data for "{0}"'.format(job))
    #     local_start = time()
    #     scrape_jobs(driver, job)
    #     local_end = time()
    #     print('It took ', local_end-local_start,
    #           ' seconds to get data for: "{0}"'.format(job), '\n')
    driver.quit()
    print('Close driver! \n')
    end = time()
    print("It took ", end-start, " time to get data for ",
          sys.argv[1]+sys.argv[2])
    #print("It took total of ", end-start, " time to get all data \n")
