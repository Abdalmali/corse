
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class facebook_web:

    
    def __init__(self) :
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-gpu")
        self.browser = webdriver.Chrome(options=self.chrome_options)
        


    def  loginUserName(self,email,password):
        """
        log in whti pass email and password
        chek if login secsee or not 
        """

    
        self.browser.get("https://www.facebook.com")
        print("Page title was '{}'".format(self.browser.title))
        if self.browser.title == 'Log into Facebook':
            try:
                mail=self.browser.find_element(By.XPATH,'//*[@id="email"]')
                mail.send_keys(email)
                time.sleep(2)
                passs=self.browser.find_element(By.XPATH ,'//*[@id="pass"]')
                passs.send_keys(password)
                login_box =self. browser.find_element(By.XPATH, '//*[@id="loginbutton"]')
                login_box.click()
                time.sleep(4)
            finally:
                
                title=self.browser.title
                if title =='facebook':
                    print('log in secuss')
                    return True
                else:
                    error_element = self.browser.find_element(By.XPATH,'//*[@id="error_box"]/div[1]')
                    error_message = error_element.text 
                    print('faild login ',error_message)
                    self.browser.quit()
                    return False
        

    
            

    
    def loginSession(self,session_path):
        """
        pass the session file with json and have list of name and value for all session
        """
        list_session=self.reade_seassion(session_path)

        print(list_session)

        
        self.browser.get("https://www.facebook.com")
        print("Page title was '{}'".format(self.browser.title))

        

        if self.browser.title== 'Log into Facebook':
            try:
                for cookie in list_session:
                    self.browser.add_cookie(cookie)
                  
            finally:
                self.browser.get("https://www.facebook.com") 
                print("Page title was '{}'".format(self.browser.title))  
                tiitle=self.browser.title
                if tiitle=='Log into Facebook':
                    print('log in faild cheak the session')
                    return False
                else:
                    print('log in seccses')   
                    return True 

        

     


    def reade_seassion(self,session_path):
        with open(session_path, 'r', encoding='utf-8') as file:
            # قراءة المحتوى من الملف
            content = file.read()
        
            # تحويل المحتوى إلى كائن JSON
            data = json.loads(content)
            print(type(data))
     
            return data


    def pup_post(self,post):
        try:
            post_box=self.browser.find_element(By.XPATH ,'//*[@id="mount_0_0_IF"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span')
            post_box.click()
            time.sleep(2)
            write_box=self.browser.find_element(By.XPATH ,'//*[@id="mount_0_0_IF"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/p')
            write_box.send_keys(post)
            time.sleep(2)
            send=self.browser.find_element(By.XPATH ,'//*[@id="mount_0_0_IF"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div')
            send.click()

            
        finally:
            time.sleep(2)
            self.browser.quit()
        
  
    def pup_image():
        pass
    def pup_storis():
        pass
    def get_ditals():
        pass


test=facebook_web()
test.loginUserName()            