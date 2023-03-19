import scrapy
from scrapy.crawler import CrawlerProcess
import json

links_output="./links.json"
class UnivBotSpider(scrapy.Spider):
    name = "univ_bot"
    start_urls = ["https://www.emolument.com/salary-reports/universities"]
    data = []

    def parse(self, response):
        # list[0], list[2], list[4], ...
        def divide_even_element(list):
            list_after = []
            for i, data in enumerate(list):
                if i % 2 == 0:
                    list_after.append(data)

            return list_after

        links = response.css("table").css("a::attr(href)").getall()
        # even: univ
        univs = response.css(
            "td.tree_depth_3").css("a::attr(title)").getall()

        links = divide_even_element(links)

        for i, link in enumerate(links):
            yield {
                "data":"https://www.emolument.com"+link
            }


class SalaryBotSpider(scrapy.Spider):
    name = "salary_bot"
    output = json.load(open(links_output, 'r'))
    start_urls = [data["data"]
                  for data in output]

    i = 0
    def parse(self, response):
        data_dic = {}
        start_urls=self.start_urls

        def code_formatter(list_before):
            i = 0
            list_after = []
            while i < len(list_before):
                # delete new line, tab, and \xa0
                data = list_before[i].replace("\n", "").replace(
                    "\t", "").replace("\xa0", "")
                if data != "":
                    list_after.append(data)
                i += 1

            return list_after

        activity = code_formatter(list(response.css(
            "h3.font-emo-bold").css("a[href]::text").getall()))

        degree = code_formatter(list(response.css(
            "td").css("h3[itemprop]::text").getall()))
        # bachelor data
        salary_types = activity+degree
        # dollers
        sample_salaries = code_formatter(list(response.css(
            "td").css("span[itemprop]::text").getall()))
        
        j=0
        for sample_salary in sample_salaries:
            major = {"salary_type": salary_types[j],
                     "sample_salary": sample_salaries[j]}
        
            data_dic[f"major{j}"] = major
            j += 1 
        self.j=0
        data_other = ({
            "link": response.request.url
        })

        data_dic["univ"] = data_other
        data_dicall = {"data": data_dic}

        yield data_dicall
