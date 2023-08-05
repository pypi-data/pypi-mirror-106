
from src.httpexecutor.http_client import HttpClient
from src.driver.device_capabilities import DeviceCapabilities
from src.driver.base_driver import BaseDriver
from src.driver.finder import Finder
from src.exceptions.session_not_started_exception import SessionNotStartedException
from src.driver.options import Options
from src.driver.screen import Screen


class VizioRemoteAuthorizer(BaseDriver):
    pass

    http_client = None
    device_ip_address = None

    """
	Initiates the Vizio remote authorizer.

	:param server_url: String - The url your server is listening at, i.e. http://localhost:port
	:param device_ip_address: String - The Tizen TV device IP address.
	"""

    def __init__(self, server_url, device_ip_address):
        self.http_client = HttpClient(server_url)
        self.device_ip_address = device_ip_address

    """
	Initiates the Vizio remote and waits for the user to manually authorize the
	device. When this call is the Vizio TV will display a pairing code and a command prompt will 
	open on their machine awaiting this input.
	The user will have 60 seconds to enter the pairing code that displays on their Vizio TV Screen. 
	Once accepted, an authentication code will be returned to the user.
	This auth token can be passed to the 'DeviceAPIToken' capability
	for future remote control commands on future driver sessions. 
	This api token will be valid for all sessions unless the user re-invokes this method.
	
	:raises RemoteInteractException: If the remote control fails to authorize.
    """

    def authorize(self):
        session = {}
        session['action'] = 'authorize_remote'
        session['platform'] = 'vizio'
        session['device_ip'] = self.device_ip_address
        response_obj = self.__handler(
            self.http_client.post_to_server('remote', session))
        return response_obj['device_api_token']

    def __handler(self, session_json):
        if session_json['results'] != 'success':
            raise RemoteInteractException(session_json['results'])
        return session_json
