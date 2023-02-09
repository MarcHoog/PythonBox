import requests
from json import JSONDecodeError
from typing import List, Dict

def download_cat(url:str, path:str):
    """
    Description:
    ------------
    
    Downloads a cat from a given url and saves it to the given path
    
    Parameters:
    -----------
    
    url: The url to download the cat from
    path: The path to save the cat to
    """
    
    req = requests.get(url)
    if req.ok:
        with open(path, 'wb') as file:
            file.write(req.content)
    else:
        raise Exception(req.status_code, req.reason)

class Result:
    """
    Description:
    ------------
    The Result class is used to return the result of a request.
    
    
    Parameters:
    ------------
    status_code: The status code of the request
    message: The message of the request
    data: The data of the request
 
    """
    
    def __init__(self,
                 status_code:int,
                 message: str = '',
                 data:List[Dict] = None
                 ) -> None:
        
        self.status_code:int = status_code
        self.message:str = message
        self.data = data if data else []

class UnkownUrl(Exception):
    pass

class Api:
    
    def __init__(self,
                 url='https://api.thecatapi.com') -> None:
        
        base_url = f"{url}/v1/images" if url[-1] != "/" else url[:-1] 
        self.url = base_url
        self.http_session = requests.Session()
        
        
    def search_cat(self):
        result = Request('{}/search'.format(self.url),
                          http_session=self.http_session
                          ).get()
       
        return result.data[0]
    
class Request:
    """
    Description:
    ------------ 
    The Request class is used to make requests to the API
    
    
    Parameters:
    ------------
    base: The base url of the request
    http_session: The http session to use for the request
    
    
    
    
    """
    def __init__(self,
                 base,
                 http_session:requests.Session = requests.Session(),
                 ):
        
        self.base = self.normalize_url(base)
        self.url = self.base
        self.http_session = http_session      
        
    def normalize_url(self,url):
        """
        Description:
        ------------
        Builds a url for post requests.
        Bassicly makes sure there is an / at the end of the url
        
        
        Parameters:
        -----------
        Url: The Url to normalize            
        """
        
        
        if url[-1] != "/":
            return f"{url}/"
    
        return url
        
    def get_base(self) -> dict:
        """
        Description:
        -----------------
        gets the Base url and returns the json response
        """
        
        headers = {
            "content-type":"application/json"   
        }
        
        req = self.http_session.get(
            self.base,
            headers = headers

        )
        
        if req.ok:
            return req.json()
        else:
            raise Exception(req)
        
    def _send(self,
              http_method:str,
              body:dict,
              extra_params:dict = None
              ):
        """
        Description:
        ------------
        sends and builds a request to the API
        
        
        Parameters:
        ------------
        http_method: The http method to use
        body: The body of the request
        extra_params: Extra parameters to add to the request        
        """
        
        
        if http_method in ['get']:
            headers = {'accept':'application/json'}
        elif http_method in ['post', 'put','delete']:
            raise Exception('Function not supported by the API')
            
        params = {}
        if extra_params:
            params.update(extra_params)
        
        try:    
            req = getattr(self.http_session, http_method)(
                self.url,headers=headers,params=params,json=body
            )
        except requests.exceptions.RequestException as e:
            raise Exception('Something went wrong') from e
        
        
        client_error = 499 >= req.status_code >= 400
        if client_error:
            if req.status_code == 400:
                raise UnkownUrl('The url you requested is not valid')
            raise Exception(req.status_code,req.reason)
        
        is_success = 299 >= req.status_code >= 200
        if is_success:            
            try:
                data = req.json()
            except (ValueError,JSONDecodeError) as e:
                raise Exception('The response is not valid json') from e
            return Result(req.status_code,message=req.reason,data=data)

        
        
        return req.json()
        
    def get(self,extra_params:dict=None,body:dict=None):
        """
        Description:
        ------------
        higher level function to send a get request
        
        Parameters:
        ------------
        extra_params: Extra parameters to add to the request
        body: The body of the request        
        
        """
        return self._send('get',extra_params=extra_params,body=body)       
                
if __name__ == '__main__':
    api = Api()
    print(api.search_cat())