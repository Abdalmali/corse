# # from ensta import WebSession
# # import json
# # #aoutmairgj
# # username='abdalmalik.sawlan@gmail.com'
# # password='Abdalmalik77$$'
# # see={
# #     "session_id": "65353306695%3AzYgMay3cstXqoH%3A4%3AAYfmR_VtAter92KFzNlZzllGgBBhB2IAEXygZV1FkQ",
# #     "rur":"\"NAO\\05465353306695\\0541742326602:01f7dbd4413dd3d676e98369b52b2c054aa6db95393af9ef695c373bb74f6c777bcd15d3\"",
# #     "mid": "ZdNzmQALAAE-5uKuJikFbazCByoC",
# #     "user_id": "65353306695",
# #     "ig_did": "0098D3AA-400D-4191-8A5B-6F057A8A5083",
# #     "identifier": "abdalmalik.sawlan@gmail.com",
# #     "username": "aoutmairgj",
# #     "csrftoken":"mGrcUhFhGEXo1YhlcNHTg2mzqZmpGmR5"
# # }
# # see_json_str = json.dumps(see)
# # host = WebSession(see_json_str)

# # t=host.authenticated()
# # print(t)


# # video_id = host.upload_video_for_reel("IMG_20230518_152239_171.mp4", thumbnail="1.png")
# # image_id=host.upload_image('1.png')

# # host.pub_photo(image_id ,caption='finaly work')
# # host.pub_reel(
# #     video_id,
# #     caption="Enjoying the winter! ⛄"
# # )


# import json

# # افتح الملف JSON
# with open('facebook_session.json', 'r', encoding='utf-8') as file:
#     # قراءة المحتوى من الملف
#     content = file.read()

#     # تحويل المحتوى إلى كائن JSON
    
#     cookies = json.loads(content)

# # تخزين الأسماء والقيم في قائمة
# cookie_list = []
# for cookie in cookies:
#     name = cookie['name']
#     value = cookie['value']
#     cookie_list.append({'name': name, 'value': value})

# # طباعة القائمة
# for cookie in cookie_list:
#     print(cookie)

# # يمكنك الآن استخدام المتغير 'data' للوصول إلى المحتوى المخزن في الملف JSON
# # على سبيل المثال، إذا كان الملف JSON يحتوي على مفتاح 'اسم'، يمكنك الوصول إليه بهذا الشكل:
# print(cookie_list)
# #----------------------------------------------------facebook test------------------------------------------------



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import *
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# import time

# from bs4 import BeautifulSoup

# # class facebook_web:

    

    
#     #self.options.add_argument(r"--user-data-dir=C:\Users\Abdalmalek\AppData\Local\Google\Chrome for Testing\User Data")
        


        
# # driver_path=r'C:\Users\Abdalmalek\.cache\selenium\chromedriver\win64\119.0.6045.59\chromedriver.exe'
# # service=Service(executable_path=r'C:\Users\Abdalmalek\.cache\selenium\chromedriver\win64\119.0.6045.59\chromedriver.exe')
# # options=Options()
# # options.add_experimental_option("detach", True)
# # options.binary_location=r'C:\Users\Abdalmalek\.cache\selenium\chrome\win64\119.0.6045.59\chrome.exe'

# # options.add_argument(r"--user-data-dir=C:\Users\Abdalmalek\AppData\Local\Google\Chrome for Testing\User Data")
# # options.add_experimental_option("excludeSwitches", ["enable-automation"])
# # options.add_experimental_option('useAutomationExtension', True)
# # options.add_argument("--headless=new")
# # driver=webdriver.Chrome(service=service,options=options)

# #driver.get(f'https://www.facebook.com/')     
       


# service2 = Service(executable_path=r'C:\Users\Abdalmalek\.cache\selenium\chromedriver\win64\119.0.6045.59\chromedriver.exe')
# options2=Options()
# options2.add_experimental_option("detach", True)
# options2.binary_location = r'C:\Users\Abdalmalek\.cache\selenium\chrome\win64\119.0.6045.59\chrome.exe'
# options2.add_argument(r"--user-data-dir=C:\Users\Abdalmalek\AppData\Local\Google\Chrome for Testing\User Data")
# options2.add_experimental_option("excludeSwitches", ["enable-automation"])
# options2.add_experimental_option('useAutomationExtension', True)
# driver = webdriver.Chrome(service=service2,options=options2)
# driver.get(f'https://facebook.com')
# title=driver.title
# time.sleep(5)
# print(title)
# email=driver.find_element(By.XPATH,'//*[@id="email"]')
# email.send_keys('alisolan8@gmail.com')
# time.sleep(5)
# password=driver.find_element(By.XPATH ,'//*[@id="pass"]')
# password.send_keys('Abdalmalik77$$')
# time.sleep(5)

# driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()



# print(title)
# #test=facebook_web()
# # t='www.google.com'
# # # test.login(t)


# html_content = driver.page_source

# # إنشاء كائن BeautifulSoup لتنسيق السورس
# soup = BeautifulSoup(html_content, 'html.parser')

# # تنسيق السورس
# formatted_html = soup.prettify()

# # حفظ السورس المنسق في ملف
# with open("formatted_html.html", "w", encoding="utf-8") as file:
#     file.write(formatted_html)

# # إغلاق المتصفح
# driver.quit()
# #Log into Facebook

# error_element = driver.find_element(By.XPATH,'//*[@id="error_box"]/div[1]')
# error_message = error_element.text