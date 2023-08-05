import urlparse
import ujson as json
from glogger import get_logger
from base_user_property import Base

logger = get_logger

class UserProperties(Base):
    base_url = None

    def __init__(self,url):
        self.base_url = url
    
    def initialize_session(self,user_api_user,user_api_password):
        user_session = self.get_user_session(self.base_url)
        user_session = self.authenticate_user(user_api_user,user_api_password)
        return user_session

    def get_user_properties_by_user_id(self,user_session,user_id=None,headers=None):
        if headers is None:
            headers = {}
        
        if not user_id:
            logger.error("Null user is passed for getting user properties")

        url = self.get_url(self.base_url,'/v1/user/user_property/',user_id)

        headers = {
            'x-gr-uid' : str(user_id),
            'Ignore-Cache' : headers.get('Ignore-Cache'.upper(),'False'),
        }

        response = user_session.request(
            'GET',url=url,headers=headers,timeout=0.5
        )

        if response.status_code == 200:
            response_dict = json.loads(response.content)

            logger.debug(
                "Get User Property Servide response for user id",
                user_api_response="response: %s" % response_dict,
                user_id=user_id
            )
            return response_dict['property_data']
        elif response.status_code in [500, 502, 503, 504]:
            raise errors.ServiceUnavailableException(
                response.status_code, "User Property Service not responding"
            )
        else:
            raise errors.APIException(
                response.status_code, "Unknown Error {}".format(response.content)
            )