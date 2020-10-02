import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings
from spiders.ArticleSpider import ArticleSpider
import jsonlines
import argparse

def main():
    parser = argparse.ArgumentParser(description='Specifying parameters for websites to scrape')
    parser.add_argument('websites', metavar='Website', nargs='+',
            help='what websites to scrape, it needs to the name attribute in params.jl exactly, or specify \'all\'')
    parser.add_argument('file', metavar='file',
            help='file to extract into')
    args = parser.parse_args()
    websites = args.websites
    file = args.file
    settings = get_project_settings()
    settings.set('FEED_URI', file)

    process = CrawlerProcess(settings)

    params = []
    with jsonlines.open('params.jl') as reader:
        for param in reader:
                params.append(param)
    if websites == ['all']:
        for param in params:
            process.crawl(ArticleSpider, **param)
    else:
        for param in params:
            if param['name'] in websites:
                process.crawl(ArticleSpider, **param)    
    process.start() 

if __name__ == "__main__":
        main()

