# -*- coding: utf-8 -*-
import scrapy
from ..items import ZhaopinItem
import re
from datetime import datetime


class ZhaopinSpiderSpider(scrapy.Spider):
    name = 'zhaopin_spider'
    allowed_domains = ['51job.com']
    base_url = 'https://search.51job.com/list/000000,000000,0000,01,9,99,{},2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    job_lists = ['Java开发', 'UI设计师', 'Web前端', 'PHP', 'Python', 'Android', '美工', '深度学习', '算法工程师', 'Hadoop', 'Node.js',
                 '数据开发', '数据分析师', '数据架构', '人工智能', '区块链', '电气工程师', '电子工程师', 'PLC', '测试工程师', '设备工程师', '硬件工程师', '结构工程师',
                 '工艺工程师', '产品经理', '新媒体运营', '运营专员', '淘宝运营', '天猫运营', '产品助理', '产品运营', '淘宝客服', '游戏运营', '编辑']
    url_list = []
    number = 0
    for job in job_lists:
        url = base_url.format(job)
        url_list.append(url)
    start_urls = [
        'https://search.51job.com/list/000000,000000,0000,01,9,99,java开发,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=']

    # base_url = 'https://search.51job.com/list/000000,000000,0000,01,9,99,%2B,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='

    def parse(self, response):
        print('=' * 30)
        print(response.url)
        divs = response.xpath("//div[@class='j_joblist']/div[@class='e']")
        for div in divs:
            item = ZhaopinItem()
            try:
                item['post_type'] = self.job_lists[self.number]
                item['job'] = div.xpath(".//a/p[@class='t']/span[@class='jname at']/@title").get()
                time = div.xpath(".//a/p[@class='t']/span[@class='time']/text()").get().split('发布')[0]
                month,day = time.split('-')
                item['update_time'] = datetime(year=datetime.now().year, month=int(month), day=int(day)).strftime('%Y-%m-%d') #将datetime类型转为str类型
                try:
                    wage_str = div.xpath(".//a/p[@class='info']/span[@class='sal']/text()").get()
                    wage = re.match('(\d.*)-(\d.*)(\D)/(\D)', wage_str)
                    min_wage = wage.group(1)
                    max_wage = wage.group(2)
                    unit = wage.group(3)
                    unit2 = wage.group(4)
                    if unit2 == '月':
                        if unit == '万':
                            unit = 10000
                        if unit == '千':
                            unit = 1000
                        if unit == '百':
                            unit = 100
                        item['min_wage'] = float(min_wage) * unit
                        item['max_wage'] = float(max_wage) * unit
                    if unit2 == '年':
                        if unit == '万':
                            unit = 10000
                        if unit == '千':
                            unit = 1000
                        if unit == '百':
                            unit = 100
                        item['min_wage'] = float(min_wage) * unit/12
                        item['max_wage'] = float(max_wage) * unit/12
                except:
                    item['min_wage'] = 5000
                    item['max_wage'] = 8000
                job_message = div.xpath(".//a/p[@class='info']/span[@class='d at']/text()").get().split('|')
                item['city'] = job_message[0].strip().split('-')[0]
                item['job_place'] = job_message[0].strip()
                if len(job_message) == 4:
                    item['job_experience'] = job_message[1].strip()
                    item['education'] = job_message[-2].strip()
                if len(job_message) == 3:
                    item['job_experience'] = '无需经验'
                    item['education'] = job_message[-2].strip()
                if len(job_message) == 2:
                    item['job_experience'] = '无需经验'
                    item['education'] = '无学历要求'
                item['job_duty'] = '全职'
                job_benefits = div.xpath(".//a/p/@title").get()
                if job_benefits:
                    item['job_benefits'] = job_benefits
                else:
                    item['job_benefits'] = '五险一金 专业培训 定期体检 周末双休'
                item['company'] = div.xpath(".//div[@class='er']/a/@title").get()
                item['website'] = div.xpath(".//div[@class='er']/a/@href").get()
                item['logo'] = 'http://img09.zhaopin.com/2012/other/mobile/mi/companyLogo/03/default.png'
                item['number'] = div.xpath(".//div[@class='er']/a/@href").get().split('/')[-1].split('.')[0]
                company_message = div.xpath(".//div[@class='er']/p[@class='dc at']/text()").get().split('|')
                scale = company_message[-1].strip()
                if scale.endswith('人'):
                    item['scale'] = scale
                else:
                    item['scale'] = '50人'
                item['industry'] = div.xpath(".//div[@class='er']/p[@class='int at']/text()").get()
                yield item
            except Exception as e:
                self.logger.error("parse url:%s err:%s", response.url, e)
            # # 有可能中间混入其他url链接
            # try:
            #     url = re.match('.*jobs.51job.com/.*', url).group()
            #     yield scrapy.Request(url, callback=self.parse_item, dont_filter=True,
            #                          meta={'selenium': False})  # 防止重复爬取
            # except:
            #     pass
        current_number = int(response.xpath("//div[@class='p_in']/ul/li[@class='on']/div/text()").get())
        page_number = ''.join(response.xpath("//div[@class='rt rt_page']/text()").getall())
        total_page = int(re.sub('\s|/', '', page_number))
        if current_number < int(total_page*0.5):
            next_number = current_number + 1
            list1 = response.url.split('.html?')
            list2 = list1[0].split(',')
            list2[-1] = str(next_number)
            # 下一页url链接
            next_url = ','.join(list2) + '.html?' + list1[1]
            print(next_url)
            yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)
        else:
            print('=' * 30)
            print("开始爬取下一个工作了")
            print('=' * 30)
            self.number += 1
            if self.number < len(self.job_lists):
                yield scrapy.Request(self.url_list[self.number], callback=self.parse, dont_filter=True)

    # def parse_item(self, response):
    #     item = ZhaopinItem()
    #     try:
    #         item['url'] = response.url
    #         item['job'] = response.xpath("//div[@class='cn']/h1/text()").get()
    #         item['salary'] = response.xpath("//div[@class='cn']/strong/text()").get()
    #         item['company'] = response.xpath("//div[@class='cn']/p[@class='cname']/a[1]/text()").get()
    #         message = response.xpath("//div[@class='cn']/p[@class='msg ltype']/text()").getall()
    #         item['working_place'] = message[0].strip()
    #         item['experience'] = message[1].strip()
    #         item['educational'] = message[2].strip()
    #         item['job_category'] = response.xpath("//div[@class='mt10']/p[@class='fp'][1]/a/text()").get()
    #         job_keys = response.xpath("//div[@class='mt10']/p[@class='fp'][2]/a/text()").getall()
    #         item['job_keys'] = '、'.join(job_keys)
    #         job_description = ''.join(response.xpath("//div[@class='bmsg job_msg inbox']//text()").getall())
    #         item['job_description'] = re.sub('\s', '', job_description)
    #     except Exception as e:
    #         self.logger.error("parse url:%s err:%s", response.url, e)
    #     return item
