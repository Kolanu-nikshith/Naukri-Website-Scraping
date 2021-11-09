import scrapy
from naukri_analysts.items import JobItem
from scrapy.loader import ItemLoader

class JobDetails(scrapy.Spider):
	name='naukri_jobs'
	start_urls=['https://www.naukri.com/data-analyst-jobs-in-delhi-ncr','https://www.naukri.com/data-analyst-jobs-in-delhi-ncr-2']

	def parse(self,response):
		jobs_list=response.css('.row')
		for job in jobs_list:
			job_loader=ItemLoader(JobItem(),selector=job)
			job_loader.add_css('job_title','span.content > ul > li::attr(title)')
			job_loader.add_css('experience','span.content >.exp::text')
			job_loader.add_css('location','.content >.loc>span::text')
			job_loader.add_css('company_name','.content>.orgRating>.org::text')
			job_loader.add_css('keyskills','span.content > div > div > span.skill::text')
			job_loader.add_css('link','span.content>ul>li>a::attr(href)')
			job_loader.add_css('job_description','span.content>div.more>span.desc::text')
			job_loader.add_css('salary','div.other_details>span.salary::text')
			yield job_loader.load_item()
			
			
			