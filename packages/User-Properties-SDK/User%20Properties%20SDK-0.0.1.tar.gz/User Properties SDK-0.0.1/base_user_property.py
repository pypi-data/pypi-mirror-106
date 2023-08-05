from api_client import get_request_session
import urlparse

class Base:
    def __init__(self,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs

    def get_user_session(self,url=None,max_retries=1):
        return get_request_session(url)

    def authenticate_user(self,user_session,user_api_user,user_api_password):
        user_session.auth = (user_api_user,user_api_password)
        return user_session
    
    def get_url(self,base_url,path=None,user_id=None):
        url = urlparse.urljoin(
            urlparse.urljoin(base_url,path,str(user_id))
        )
        return url
    

