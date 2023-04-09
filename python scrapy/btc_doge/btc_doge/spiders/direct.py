import scrapy
from ..items import QuizItems

class direct(scrapy.Spider):
    name = 'direct'
    start_urls = ['https://mcqsnts.com/current-affairs-mcqs']
    
    def parse(self,response):
        quiz = QuizItems()
        for q in range(1,11):
            ques = response.xpath(f'(//strong)[{q}]/text()').get()
            opt = response.xpath(f'(//ul[@class = "ans-options"])[{q}]/li/text()').getall()
            ans = response.xpath(f'(//*[@class = "ans-options"])[{q}]/li[@class = "correct"]/text()').get()
            quiz['ans'] = ans
            quiz['opt'] = opt
            quiz['ques'] = ques
            
            yield quiz        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# ans_list = []
# length = len(response.xpath('//strong/text()').getall())
# anslen = int(0)
# #            //strong contains questions 
# for a in range( 1 , len(response.xpath('//strong/text()').getall())+1 ):
#     ans = response.xpath(f'(//*[@class = "ans-options"])[{a}]/li/text()').getall()
#     if ans:
#         anslen += 1
#         ans_list.append(ans)

# yield {
#     # "Titless" : response.xpath('//strong/text()').getall(),
#     "answers": ans_list,
#     "__________length ____" : length,
#     "_______Ans length ____" : anslen,
# }