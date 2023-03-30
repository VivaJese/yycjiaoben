# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 20:06:03 2021

@author: 19818513531@139.com
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 16:56:21 2021

@author: yc
"""
import threading
import requests
import re
import os
import time
import sys
from requests.packages import urllib3
urllib3.disable_warnings()
import math
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Value

import base64
from xml.dom.minidom import parse
import xml.dom.minidom


import time
import datetime
start_cookie=''



proxies = { "http": "http://127.0.0.1:10809", "https": "127.0.0.1:10809", }
body_test = """<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body><CBFMBusinessRefHisAlarmGetList xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://tempuri.org/"><areaID>865</areaID><countryID>880</countryID><customerSLA /><keyword></keyword><startTime>2022-06-07T00:00:00</startTime><endTime>2022-06-07T23:00:00</endTime><elementtype>ALL</elementtype><professionalType>ALL</professionalType><alarmTimespan>0.5-10000000</alarmTimespan><hasImep i:nil="true" /><customerCode></customerCode><assignOrder /><orderNo></orderNo><prdInstanceFlge></prdInstanceFlge><V_IS_OVERTIME i:nil="true" /><V_IS_VIP_CUSTOMERS /><suit><AdvancedSearchSql></AdvancedSearchSql><CustomerGroupIDs /><EnableCustomizedSearch>false</EnableCustomizedSearch></suit><zqImepColIsVisible>true</zqImepColIsVisible><commonImepColIsVisible>false</commonImepColIsVisible><v_ZQ_SERIAL_ID></v_ZQ_SERIAL_ID><v_CUST_SERVICE_NO></v_CUST_SERVICE_NO><v_CUSTOMER_NAME></v_CUSTOMER_NAME><v_has_ct_order></v_has_ct_order><v_ct_order></v_ct_order><v_pro_alarm>是</v_pro_alarm><sortSql></sortSql><startIndex>1</startIndex><endIndex>31</endIndex><log><CookieUserId i:nil="true" /><ID>-1</ID><OP_USER>10023</OP_USER><MODULE_NAME>业务监控(历史数据查询)</MODULE_NAME><FUNCTION_NAME>历史告警查询</FUNCTION_NAME><OP_METHOD>查询</OP_METHOD><OLD_VALUE></OLD_VALUE><NEW_VALUE></NEW_VALUE><OP_DATE>2022-06-07T17:13:35.8709747+08:00</OP_DATE><IP>10.71.156.95</IP><COMPUTER_NAME>10.71.156.95</COMPUTER_NAME><QUERY_KEY></QUERY_KEY><OP_RESULT>-1</OP_RESULT><OP_CONTENT>地区:杭州市;县市:余杭区;开始时间:2022/6/7 0:00;结束时间:2022/6/7 23:00;客户服务等级:;业务类型:;业务保障等级:;告警种类:;是否有工单:;工单号:;关键字:;产品实例标识:;</OP_CONTENT><RETURN_DATA_NUM>-1</RETURN_DATA_NUM><PLATFORM>10.71.156.95</PLATFORM></log></CBFMBusinessRefHisAlarmGetList></s:Body></s:Envelope>"""
class HttpsClient:
 
    def __init__(self):
        pass
 
    @staticmethod
    def get(_url, _json):
        _resp = requests.get(_url, _json, verify=False,proxies=proxies)
        return _resp
        
    @staticmethod
    def https_post(_url, _json_dict):
        _resp = requests.post(_url, _json_dict, verify=False,proxies=proxies)
        return _resp.text
 
    @staticmethod
    def https_post_with_header(_url, _json_dict, _headers):
        #print(_json_dict)
        _resp = requests.post(_url, data=_json_dict, headers=_headers, verify=False,proxies=proxies)
        return _resp
 

    
def view_bar(num, total):
    rate = float(num) / float(total)
    rate_num = int(rate * 100)
    r = '\r[%s%s]%d%% 进行中的数量:%d' % ("="*rate_num, " "*(100-rate_num), rate_num, num )
    sys.stdout.write(r)
    sys.stdout.flush()
    

def login():
    url = "http://10.211.255.7/WebService/ICSLAWebService.asmx"
    
    timestamp = time.time()     # 当前时间戳
    strtime = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(timestamp))
    op_time=strtime+".6536902+08:00"
    
    payload = "<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\"><s:Body><SmGetLoginUser xmlns:i=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns=\"http://tempuri.org/\"><loginName>15267053000</loginName><password>3018C83EEBDDFEB8C1F5290881276E5D</password><log><CookieUserId i:nil=\"true\" /><ID>-1</ID><OP_USER>15267053000</OP_USER><MODULE_NAME>Sys</MODULE_NAME><FUNCTION_NAME>Sys</FUNCTION_NAME><OP_METHOD>验证登录</OP_METHOD><OLD_VALUE></OLD_VALUE><NEW_VALUE></NEW_VALUE><OP_DATE>"+op_time+"</OP_DATE><QUERY_KEY></QUERY_KEY><OP_RESULT>-1</OP_RESULT><OP_CONTENT></OP_CONTENT><RETURN_DATA_NUM>-1</RETURN_DATA_NUM></log></SmGetLoginUser></s:Body></s:Envelope>"
    headers = {
      'Accept': '*/*',
      'Referer': 'http://10.211.255.7/ClientBin/ICSLA.xap?v=2014811040',
      'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.5',
      'Content-Length': '682',
      'Content-Type': 'text/xml; charset=utf-8',
      'SOAPAction': '"http://tempuri.org/SmGetLoginUser"',
      'Accept-Encoding': 'gzip, deflate',
      'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Tablet PC 2.0)',
      'Host': '10.211.255.7',
      'Proxy-Connection': 'Keep-Alive',
      'Pragma': 'no-cache',
      'Cookie': 'X-User-Data=HQG25cYwcTv7h8XHMLCoptitaht5H+vPIVZqazSam8VCHrMEghS+PWapQL1uySSe3oUR3nCSY2lvoHNBzMCEXnjqrTN8knMBOEicigeZxs+4gniuHtc+uga7zR69MKREeosn5pwWk0utqPX5OszPmefgjkAxczHUEu4U5inMg0D68w4eeSy4NMsPWWn+pz+sTxfWERDMHdqz06bP0VubFj9qcx8TyHVAHiiARObGBiOC7zY36NxCMeewq8Itq/pHiYui0FJT7ZqzG6GzNDfa2w==; ASP.NET_SessionId=zwmpxmppf0j2sxdllropkahn; X-User-Data=HQG25cYwcTv7h8XHMLCopmdtoaptJEShnboFELQ95cr4sLhtgYoorkt0P/JlqbZKWPGYWYXYogpgjB3K5QU4YcMFGU/mQw/R2bN8eG8sy9pvpF4P2HdKZnBr/gKpGOHTSbMp13m/5eMjV2RF6HzmOtdpYyPSDOWf81WXECpCCwPCwNERhYd+FQckHjjwGEgtbE13+IG7mX8Nlir3GNl29WgFmwGDLJWjzZa0gthiDKkBbXM3jj4dmWmeTj9OgSj1VW7WHcfw/ElOYNJulFBV7w=='
    }
    
    
    payload2=payload.encode("utf-8").decode("latin1")
    response = requests.request("POST", url, headers=headers, data=payload2)
    
    #print(response.text)
    
    #print(response.content)
    html_set_cookie = requests.utils.dict_from_cookiejar(response.cookies)
    print('login_cookie')
    print(html_set_cookie['X-User-Data'])
    print('-------------------------------')
    return html_set_cookie['X-User-Data']
    


def getCookie(start_cookie):
    url = "http://10.211.255.7/WebService/ICSLAWebService.asmx"
    
    payload = "<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\"><s:Body><SmLoginRemove xmlns:i=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns=\"http://tempuri.org/\"><userName>15267053000</userName></SmLoginRemove></s:Body></s:Envelope>"
    headers = {
      'Accept': '*/*',
      'Referer': 'http://10.211.255.7/ClientBin/ICSLA.xap?v=2014811040',
      'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.5',
      'Content-Type': 'text/xml; charset=utf-8',
      'SOAPAction': '"http://tempuri.org/SmLoginRemove"',
      'Accept-Encoding': 'gzip, deflate',
      'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Tablet PC 2.0)',
      'Host': '10.211.255.7',
      'Proxy-Connection': 'Keep-Alive',
      'Pragma': 'no-cache',
      'Cookie': 'ASP.NET_SessionId=am2gycqkamwh0j10xj1id1m3; X-User-Data=HQG25cYwcTv7h8XHMLCoptitaht5H+vPIVZqazSam8VCHrMEghS+PWapQL1uySSe3oUR3nCSY2lvoHNBzMCEXnjqrTN8knMBOEicigeZxs+4gniuHtc+uga7zR69MKREeosn5pwWk0utqPX5OszPmU3RMNsJ0xApRrQwuvNJg+ebC/l150v6y2a43eUiUd5YM9x0RNYiK5rZqXtRo7wr6NMvkw/+n5+ecfBpRerklrFlM4V9nFQuMuhIW0mZeRwVBngFZcWbrJpNTnn4woAKEw==; X-User-Data=HQG25cYwcTv7h8XHMLCoptitaht5H+vPIVZqazSam8VCHrMEghS+PWapQL1uySSe3oUR3nCSY2lvoHNBzMCEXnjqrTN8knMBOEicigeZxs+4gniuHtc+uga7zR69MKREeosn5pwWk0utqPX5OszPmfHbG3+jfP28ayFw0RPv2nBPBvPADBzV8SapXx72py+0Bkt23Ldi0TlTDcyR+NtV7e85EqhRuh4Q7aT8AdmcOQIHNS9smqznhtZaZkDSKm2ggnuCdX08KSCxk4R45cZpzw=='
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    html_set_cookie = requests.utils.dict_from_cookiejar(response.cookies)
    print(html_set_cookie)
    

    if html_set_cookie =={} :
        html_set_cookie = start_cookie
    else: 
        html_set_cookie=html_set_cookie['X-User-Data']
    
    return html_set_cookie
    
def sendMessage(title,content):
    
    
    #token=['074bc2c4406e409d947836360f7e25ab','b2d32504613c4d849b5a26068acb2de8','7c25780943a643a7b091a8007ebe2ad1','ce42c6adf730424591d64c79eda12f42','00693363ac2a400085b8dd215dcf9512','50ce8af6a0ab45148eb25fa88c6595f1','a0e47b1e31f24ccf9506c4c63c244ac5','e6622f5e890c48a48321442442a8a7ef','d50c966f9e414ef1aaf1571ae4bb9363']
    token=[]
    for i in range(1,len(token)):
        token_num=i
        url="http://www.pushplus.plus/send?token="+token[token_num]+"&title="+title+"&content="+content+"&template=txt"
        HttpsClient.get(url,'')
        
        print(title)
        print('消息已发送')
        print(content)

def getList(cookie,mod):
    in_headers = {
      'accept': '*/*',
      'referer': 'http://10.211.255.7/ClientBin/ICSLA.xap?v=2014811040',
      'accept-language': 'zh-Hans-CN,zh-Hans;q=0.5',
      'content-length': '1907',
      'content-type': 'text/xml; charset=utf-8',
      'soapaction': '"http://tempuri.org/CBFMBusinessRefHisAlarmGetList"',
      'accept-encoding': 'gzip, deflate',
      'user-agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Tablet PC 2.0)',
      'host': '10.211.255.7',
      'proxy-connection': 'Keep-Alive',
      'pragma': 'no-cache',
      'cookie': 'X-User-Data='+cookie
    }
    timestamp = time.time()     # 当前时间戳
    strtime = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(timestamp))
    strdate = time.strftime("%Y-%m-%d", time.localtime(timestamp))
    print('当前时间'+strtime)
    startTime=strdate+'T00:00:00'
    print('star_time'+startTime)
    endTime=strdate+'T23:59:59'
    alarmTimespan='0.05-10000000'
    # 时间戳转字符串格式时间
    
    OP_DATE = strtime+'.0271483+08:00'
    #print(OP_DATE)
    
    endIndex = '200'
    
    #print(result.content)
    #print(result.content.decode('utf-8'))
    if mod==1:
        payload = "<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\"> \
        <s:Body><CBFMBusinessRefHisAlarmGetList xmlns:i=\"http://www.w3.org/2001/XMLSchema-instance\" \
        xmlns=\"http://tempuri.org/\"><areaID>865</areaID><countryID>880</countryID><customerSLA /><keyword></keyword><startTime>"+startTime+"</startTime><endTime>"+endTime+"</endTime><elementtype>ALL</elementtype><professionalType>ALL</professionalType><alarmTimespan>"+alarmTimespan+"</alarmTimespan><hasImep i:nil=\"true\" /><customerCode></customerCode><assignOrder /><orderNo></orderNo><prdInstanceFlge></prdInstanceFlge><V_IS_OVERTIME i:nil=\"true\" /><V_IS_VIP_CUSTOMERS /><suit><AdvancedSearchSql></AdvancedSearchSql><CustomerGroupIDs /><EnableCustomizedSearch>false</EnableCustomizedSearch></suit><zqImepColIsVisible>true</zqImepColIsVisible><commonImepColIsVisible>false</commonImepColIsVisible><v_ZQ_SERIAL_ID></v_ZQ_SERIAL_ID><v_CUST_SERVICE_NO></v_CUST_SERVICE_NO><v_CUSTOMER_NAME></v_CUSTOMER_NAME><v_has_ct_order></v_has_ct_order><v_ct_order></v_ct_order><v_pro_alarm>是</v_pro_alarm><sortSql></sortSql><startIndex>1</startIndex><endIndex>"+endIndex+"</endIndex><log><CookieUserId i:nil=\"true\" /><ID>-1</ID><OP_USER>10023</OP_USER><MODULE_NAME>业务监控(历史数据查询)</MODULE_NAME><FUNCTION_NAME>历史告警查询</FUNCTION_NAME><OP_METHOD>查询</OP_METHOD><OLD_VALUE></OLD_VALUE><NEW_VALUE></NEW_VALUE><OP_DATE>"+OP_DATE+"</OP_DATE><IP>10.71.156.95</IP><COMPUTER_NAME>10.71.156.95</COMPUTER_NAME><QUERY_KEY></QUERY_KEY><OP_RESULT>-1</OP_RESULT><OP_CONTENT>地区:杭州市;县市:余杭区;开始时间:2022/6/8 0:00;结束时间:2022/6/8 23:59;客户服务等级:;业务类型:;业务保障等级:;告警种类:;是否有工单:;工单号:;关键字:;产品实例标识:;</OP_CONTENT><RETURN_DATA_NUM>-1</RETURN_DATA_NUM><PLATFORM>10.71.156.95</PLATFORM></log></CBFMBusinessRefHisAlarmGetList></s:Body></s:Envelope>"
        payload2=payload.encode("utf-8").decode("latin1")
        result=HttpsClient.https_post_with_header(in_url,payload2,in_headers)
        return result
    elif mod==2:
        alarmTimespan2='0.03-10000000'
        payload_2 = "<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\"> \
            <s:Body><CBFMBusinessRefHisAlarmGetList xmlns:i=\"http://www.w3.org/2001/XMLSchema-instance\" \
            xmlns=\"http://tempuri.org/\"><areaID>865</areaID><countryID>880</countryID><customerSLA /><keyword></keyword><startTime>"+startTime+"</startTime><endTime>"+endTime+"</endTime><elementtype>ALL</elementtype><professionalType>ALL</professionalType><alarmTimespan>"+alarmTimespan2+"</alarmTimespan><hasImep i:nil=\"true\" /><customerCode></customerCode><assignOrder><int>1</int></assignOrder><orderNo></orderNo><prdInstanceFlge></prdInstanceFlge><V_IS_OVERTIME i:nil=\"true\" /><V_IS_VIP_CUSTOMERS /><suit><AdvancedSearchSql></AdvancedSearchSql><CustomerGroupIDs /><EnableCustomizedSearch>false</EnableCustomizedSearch></suit><zqImepColIsVisible>true</zqImepColIsVisible><commonImepColIsVisible>false</commonImepColIsVisible><v_ZQ_SERIAL_ID></v_ZQ_SERIAL_ID><v_CUST_SERVICE_NO></v_CUST_SERVICE_NO><v_CUSTOMER_NAME></v_CUSTOMER_NAME><v_has_ct_order></v_has_ct_order><v_ct_order></v_ct_order><v_pro_alarm>否</v_pro_alarm><sortSql></sortSql><startIndex>1</startIndex><endIndex>"+endIndex+"</endIndex><log><CookieUserId i:nil=\"true\" /><ID>-1</ID><OP_USER>10023</OP_USER><MODULE_NAME>业务监控(历史数据查询)</MODULE_NAME><FUNCTION_NAME>历史告警查询</FUNCTION_NAME><OP_METHOD>查询</OP_METHOD><OLD_VALUE></OLD_VALUE><NEW_VALUE></NEW_VALUE><OP_DATE>"+OP_DATE+"</OP_DATE><IP>10.71.156.95</IP><COMPUTER_NAME>10.71.156.95</COMPUTER_NAME><QUERY_KEY></QUERY_KEY><OP_RESULT>-1</OP_RESULT><OP_CONTENT>地区:杭州市;县市:余杭区;开始时间:2022/6/8 0:00;结束时间:2022/6/8 23:59;客户服务等级:;业务类型:;业务保障等级:;告警种类:;是否有工单:;工单号:;关键字:;产品实例标识:;</OP_CONTENT><RETURN_DATA_NUM>-1</RETURN_DATA_NUM><PLATFORM>10.71.156.95</PLATFORM></log></CBFMBusinessRefHisAlarmGetList></s:Body></s:Envelope>"
        payload3=payload_2.encode("utf-8").decode("latin1")
        result2=HttpsClient.https_post_with_header(in_url,payload3,in_headers)
        return result2
    
    
    
def getInfo(Element,id):
    info =''
    if Element.getElementsByTagName(id).item(0).firstChild !=None:
        info = Element.getElementsByTagName(id).item(0).firstChild.data
    else: info = 'NULL'
    return info

def dealIt(start_cookie):
    count=0
    count2=0
    info_push=''
    info_push2=''
    new_flag=''
    new_flag2=''
    ALL_FLAG=0
    ALL_FLAG2=0
    
    new_cookie=getCookie(start_cookie)
    #start_cookie=new_cookie
    result=getList(new_cookie,1)
    result2=getList(new_cookie,2)
    
    reason_select=['主干光纤断或OLT检测不到预期的光信号（LOS）','分支光纤断或OLT检测不到ONT的预期的光信号(LOSi/LOBi)','ETH_LOS','[GPON告警]ONU信号丢失']
    
    DOMTree_header = xml.dom.minidom.parseString(result.content.decode('utf-8'))
    DOMTree_header2 = xml.dom.minidom.parseString(result2.content.decode('utf-8'))
    
    collection = DOMTree_header.documentElement
    collection2 = DOMTree_header2.documentElement
    #if collection.hasAttribute("Body"):
    #    print ("Root element : %s" % collection.getAttribute("Body"))
    
    
    
    
    all_data = collection.getElementsByTagName('CBFM_BS_REF_HIS_ALARM')
    all_data2 = collection2.getElementsByTagName('CBFM_BS_REF_HIS_ALARM')
    #print(all_data)
    print('搜索到的工程告警数量'+str(len(all_data)))
    print('搜索到的非工程告警数量'+str(len(all_data2)))
    
    if len(all_data)==0 and len(all_data2)==0:
        
        print(result.content.decode('utf-8'))
        print('掉线重新登录!')
        new_cookie=login()
        
        
        
    for temp_data in all_data:
        id_test = getInfo(temp_data,'ID')
        
        '''
        id_test = temp_data.getElementsByTagName('ID').item(0).firstChild.data
        AlarmEquipment = temp_data.getElementsByTagName('AlarmEquipment').item(0).firstChild.data#故障OLT
        Localinfo = temp_data.getElementsByTagName('Localinfo').item(0).firstChild.data #定位信息
        AlarmTitle = temp_data.getElementsByTagName('AlarmTitle').item(0).firstChild.data#故障原因
        AssociateReference = temp_data.getElementsByTagName('AssociateReference').item(0).firstChild.data#电路名称
        EventTime = temp_data.getElementsByTagName('EventTime').item(0).firstChild.data#告警发生时间
        ClearTime = temp_data.getElementsByTagName('ClearTime').item(0).firstChild.data#清除时间
        AlarmUniqueFlag = temp_data.getElementsByTagName('AlarmUniqueFlag').item(0).firstChild.data#告警标识
        ClearUniqueFlag = temp_data.getElementsByTagName('ClearUniqueFlag').item(0).firstChild.data#清除标识
        '''
        id_test = getInfo(temp_data,'ID')
        AlarmEquipment = getInfo(temp_data,'AlarmEquipment')#故障OLT
        Localinfo = getInfo(temp_data,'Localinfo') #定位信息
        AlarmTitle = getInfo(temp_data,'AlarmTitle')#故障原因
        AssociateReference = getInfo(temp_data,'AssociateReference')#电路名称
        EventTime = getInfo(temp_data,'EventTime')#告警发生时间
        ClearTime = getInfo(temp_data,'ClearTime')#清除时间
        AlarmUniqueFlag = getInfo(temp_data,'AlarmUniqueFlag')#告警标识
        ClearUniqueFlag = getInfo(temp_data,'ClearUniqueFlag')#清除标识
        ALARM_DURATION = getInfo(temp_data, 'ALARM_DURATION')#持续时长
        
        for reason in reason_select:
            
            if reason==AlarmTitle and ClearTime=='NULL':
                is_new=1
                info = str('------告警信息------'+'\nid: '+ id_test +'\nOLT: '+ AlarmEquipment + '\n定位信息: '+ Localinfo+'\n电路名称: '+ AssociateReference+'\n故障原因: '+ AlarmTitle+'\n发生时间: '+EventTime+'清除时间: '+ ClearTime + '持续时长: '+ ALARM_DURATION)
                print('----------------------')
                print(info)
                file=open('list.txt','r')
                for line in file.readlines():
                    #print(line)
                    temp_flag = line.strip('\n')
                    #print('temp_flag'+temp_flag)
                    #print('AlarmUniqueFlag'+AlarmUniqueFlag)
                    if temp_flag==AlarmUniqueFlag:
                        print('非新工程告警')
                        is_new=0
                        break
                file.close()
                if is_new==1:
                    file=open('list.txt','a')
                    file.write(str(AlarmUniqueFlag+'\n'))
                    file.close()
                    info_push=info_push + info +'\n'
                    new_flag=new_flag+'\n'+AlarmUniqueFlag
                    count=count+1
                    print('新工程告警！！！')
                    ALL_FLAG=1
                    
    for temp_data in all_data2:
        id_test = getInfo(temp_data,'ID')
        
        '''
        id_test = temp_data.getElementsByTagName('ID').item(0).firstChild.data
        AlarmEquipment = temp_data.getElementsByTagName('AlarmEquipment').item(0).firstChild.data#故障OLT
        Localinfo = temp_data.getElementsByTagName('Localinfo').item(0).firstChild.data #定位信息
        AlarmTitle = temp_data.getElementsByTagName('AlarmTitle').item(0).firstChild.data#故障原因
        AssociateReference = temp_data.getElementsByTagName('AssociateReference').item(0).firstChild.data#电路名称
        EventTime = temp_data.getElementsByTagName('EventTime').item(0).firstChild.data#告警发生时间
        ClearTime = temp_data.getElementsByTagName('ClearTime').item(0).firstChild.data#清除时间
        AlarmUniqueFlag = temp_data.getElementsByTagName('AlarmUniqueFlag').item(0).firstChild.data#告警标识
        ClearUniqueFlag = temp_data.getElementsByTagName('ClearUniqueFlag').item(0).firstChild.data#清除标识
        '''
        id_test = getInfo(temp_data,'ID')
        AlarmEquipment = getInfo(temp_data,'AlarmEquipment')#故障OLT
        Localinfo = getInfo(temp_data,'Localinfo') #定位信息
        AlarmTitle = getInfo(temp_data,'AlarmTitle')#故障原因
        AssociateReference = getInfo(temp_data,'AssociateReference')#电路名称
        EventTime = getInfo(temp_data,'EventTime')#告警发生时间
        ClearTime = getInfo(temp_data,'ClearTime')#清除时间
        AlarmUniqueFlag = getInfo(temp_data,'AlarmUniqueFlag')#告警标识
        ClearUniqueFlag = getInfo(temp_data,'ClearUniqueFlag')#清除标识
        ALARM_DURATION = getInfo(temp_data, 'ALARM_DURATION')#持续时长
        
        for i in range(1):
            
            if ClearTime=='NULL':
                is_new=1
                info = str('------告警信息------'+'\nid: '+ id_test +'\nOLT: '+ AlarmEquipment + '\n定位信息: '+ Localinfo+'\n电路名称: '+ AssociateReference+'\n故障原因: '+ AlarmTitle+'\n发生时间: '+EventTime+'清除时间: '+ ClearTime + '持续时长: '+ ALARM_DURATION)
                print('----------------------')
                print(info)
                file=open('list_gc.txt','r')
                for line in file.readlines():
                    #print(line)
                    temp_flag = line.strip('\n')
                    #print('temp_flag'+temp_flag)
                    #print('AlarmUniqueFlag'+AlarmUniqueFlag)
                    if temp_flag==AlarmUniqueFlag:
                        print('非新非工程告警')
                        is_new=0
                        break
                file.close()
                if is_new==1:
                    file=open('list_gc.txt','a')
                    file.write(str(AlarmUniqueFlag+'\n'))
                    file.close()
                    info_push2=info_push2 + info +'\n'
                    new_flag2=new_flag2+'\n'+AlarmUniqueFlag
                    count2=count2+1
                    print('新非工程告警！！！')
                    ALL_FLAG2=1
    
    if ALL_FLAG==1:
        info_title='新增工程告警'+str(count)+'个'
        print(info_push)
        sendMessage(info_title,info_push)
        
    
    if ALL_FLAG2==1:
        info_title2='新增非工程告警'+str(count2)+'个'
        print(info_push2)
        sendMessage(info_title2,info_push2)

    return new_cookie



if __name__ == '__main__':
    
    
    
    
    in_url="http://10.211.255.7/WebService/ICSLAWebService.asmx"

   
    start_cookie=login()

    
    
    while(1):
        #start_cookie=login()
        timestamp = time.time()     # 当前时间戳
        #strtime = time.strftime("now time：%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
        strtime = time.strftime('%H{h}%M{m}%S{s}').format(h='时',m='分',s='秒')
        try:
            start_cookie=dealIt(start_cookie)
        except Exception as e:
            print('发生异常'+strtime)
            print(e)
            print("-----------------")
            
            
            
                
        
        #print('\x1b[2K')
        #print(strtime)
        time.sleep(60)
    
    
    
    
    
    
    
    #print (temp_data.getElementsByTagName('ID').firstChild.data)
    
    '''
    strat_time = collection.getElementsByTagName('startTime')[0]
    print ("strat_time: %s" % strat_time.childNodes[0].data)
    end_time = collection.getElementsByTagName('endTime')[0]
    print ("end_time: %s" % end_time.childNodes[0].data)
    now_time = collection.getElementsByTagName('OP_DATE')[0]
    print ("now_time: %s" % now_time.childNodes[0].data)
    strat_index = collection.getElementsByTagName('startIndex')[0]
    print ("strat_index: %s" % strat_index.childNodes[0].data)
    end_index = collection.getElementsByTagName('endIndex')[0]
    print ("end_index: %s" % end_index.childNodes[0].data)
    #end_index.setAttribute('endIndex','2')
    end_index.childNodes[0].data='2'
    end_index = collection.getElementsByTagName('endIndex')[0]
    print ("end_index: %s" % end_index.childNodes[0].data)
    
    with open('header_xml_mf.xml', 'w') as f:
        DOMTree_header.writexml(f, addindent='', encoding='utf-8')
        
    in_body=open("header_xml_mf.xml","r",encoding='utf-8')
    
    '''
    
    
    '''
    in_body_str=str(body_test)
    in_body_str.encode("gb2312").decode("latin1").encode("utf-8").decode("latin1")
    
    result=HttpsClient.https_post_with_header(in_url,in_body_str,in_headers) 
    print(result.content.decode('gbk'))
    '''
    
    '''
    DOMTree_result=xml.dom.minidom.parse(result.text)
    with open('header_xml_mf.txt', 'w') as f:
        DOMTree_result.writexml(f, addindent='', encoding='gb2312')
    '''
    '''
    DOMTree = xml.dom.minidom.parse("movies.xml")
    collection = DOMTree.documentElement
    if collection.hasAttribute("shelf"):
        print ("Root element : %s" % collection.getAttribute("shelf"))0
    '''
    #os.system("pause")
    

'''
    new_result=HttpsClient.get(url2,json_dict)
    new_result_text=new_result.text
    #print(new_result_text)
    if new_result.status_code!=200:
        print('----------刷新配置失败----------')
        print('请检查您的网络连接或联系作者')
        print('----------尝试默认配置中----------')
    else:
        print('----------刷新配置成功----------')
        str_url2 = base64.b64decode(new_result_text).decode("utf-8")
        temp=str_url2.find(']')
        MB_each=float(str_url2[1:temp])
        contentID=str_url2[temp+1:temp+33]
        Authorization=str_url2[temp+33:]
        print('单文件大小为'+str(MB_each)+'MB')
        #print(Authorization)
        print(contentID)
        
    while(all_tasks<=0):
        
            temp = input("请输入需要消耗的流量,示例 10（单位为GB无需输入）:")
        
            try:
                if float(temp)>0:
                    
                    all_tasks=math.ceil(float(temp)*1024/MB_each)
                    run_same_time=math.ceil(4096/MB_each)
                    print('总下载次数'+str(all_tasks)+'次')
                    print('预计使用流量：%.2f GB' % (float(MB_each)*all_tasks/1024.0))
                    
            except Exception as e:
                print(e)
                print('请输入纯数字')

    
    pool = ThreadPoolExecutor(max_workers=run_same_time)
 
    
 
       
    for i in range(all_tasks):
        
        args =[i,all_tasks]
        status_code=pool.submit(lambda p: work(*p), args)
        status_count.append(status_code)

    pool.shutdown()

    for futures in status_count:
        #print(futures.result())
        if futures.result()==200:
            succeed+=1
        else:
            losed+=1
    
    
    #print(status_count)
    print('\n成功数量'+str(succeed))
    print('失败数量'+str(losed))
    print('使用流量：%.2f GB' % (float(MB_each)*succeed/1024.0))
    print('执行完成')
'''
    

  
    
