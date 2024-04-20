from ensta import WebSession
import json


class insta:
    def __init__(self,session_dir:str) :
        """
        accespt json file  for  the seassion details
        """
        self.session_str=self.session_chang(session_dir)
        
        self.host = WebSession(self.session_str)

        self.cheak_authantcion=self.host.authenticated()
        print(self.cheak_authantcion)

    def  session_chang(self,session_dir):
          """
          read seassion detatils from json file and chang it to string
          """
          with open(session_dir, 'r', encoding='utf-8') as file:
          # قراءة المحتوى من الملف
              content = file.read()

   
              data = json.loads(content)

          see_json_str = json.dumps(data)    
          return see_json_str
    def up_loade_image(self,image_path,detale_image=''):
         """
         this function accespt image path and detale for image and post it
         """
         if self.cheak_authantcion:
                try:
                     image_id=self.host.upload_image(image_path)
                     self.host.pub_photo(image_id ,caption=detale_image)
                     return print('the image puplsh seccessus')
                except:
                     print('erorr to puplish the image chek the image path')
         else :
              print('erorr on authintaction pless check the seession detail')               



    def up_loade_reel(self, video_path ,video_image,detale_video=''):
         """
         this function accespt video path and detale and videoIMAGE for video and post it
         """
         if self.cheak_authantcion:
                try:
                     video_id=self.host.upload_video_for_reel(video_path, thumbnail=video_image)
                     self.host.pub_reel(video_id ,caption=detale_video)
                     return print('the video puplsh seccessus')
                except:
                     print('erorr to puplish the video chek the video path')
         else :
              print('erorr on authintaction pless check the seession detail')       
    
  




session_dir='session.json'


modle= insta(session_dir)

modle.up_loade_image('flder.jpg','الحمد الله بدايه حلوه')

        
