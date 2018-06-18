#_*_ coding: utf-8 _*_
import random

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware as _UserAgentMiddleware

class UserAgentMiddleware(_UserAgentMiddleware):
    User_agent_list = [
            
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 ",
                "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                  "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                    "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"


            ]
    def process_request(self,request,spider):
        request.headers.setdefault('User-Agent',random.choice(self.User_agent_list))

