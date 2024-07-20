#!/usr/bin/python

import json
import requests

class EufyAPIClient:

    def __init__(self):

        self.token = None
        self.endpoint = "home-api.eufylife.com/v1"
        self.client_id = "eufy-app"
        self.client_secret = "8FHf22gaTKu7MZXqz5zytw"

    def request_url(self, call, method="GET", **kwargs):

        """ Request URL based on the input parameters

        :param call: API call
        :param method: HTTP method
        :param **kwargs: Kwargs to pass to request
        :return response: Response from http request
        """

        # Form URL
        url = f"https://{self.endpoint}{call}"

        # Ensure headers are set correctly
        headers = kwargs.pop('headers', {})
        if self.token:
            headers['token'] = self.token

        # Set the default headers for JSON requests if not provided
        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        # Make the request
        response = requests.request(method, url, headers=headers, **kwargs)

        # Handle response
        if response.status_code in (200, 201):

            # Convert to JSON
            if 'Content-Type' in response.headers and 'application/json' in response.headers['Content-Type']:
                response = response.json()

                # Error if res_code not equal to 1
                if response['res_code'] != 1:
                    raise Exception(f"Error occured: {response['message']}")

            else:

                response = response.text

            return response
        else:
            raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

    def authenticate(self, email, password):

        """Authenticate with the Eufy API and store the access token.
        
        :param email: Email address
        :paramm password: Password
        """

        # Create payload
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "email": email,
            "password": password
        }

        # Create headers
        headers = {
            'category': 'Health',
        }

        # Request URL
        response = self.request_url("/user/v2/email/login",
                                    method="POST",
                                    headers=headers,
                                    json=payload
        )

        # Set access token
        self.token = response.get('access_token')

    def get_devices(self):

        """ Get the list of devices from the Eufy API.

        :rtype: dict
        """

        # Send request
        return self.request_url("/device/")

    def query_device_data(self, device_id):

        """ Get device data based on device identifier

        :param device_id: Device ID
        :rtype: dict
        """

        # Send request
        return self.request_url(f"/device/{device_id}/data")

def main():

    """ Main calling functio """

    # Email and password used for authentication
    email = ""
    password = ""

    # Create an instance of the EufyAPIClient
    eufy_client = EufyAPIClient()

    # Authenticate with the API
    eufy_client.authenticate(email, password)

    # Fetch devices and output
    devices = eufy_client.get_devices()
    print(json.dumps(devices, indent=4))

    # Fetch device data based on device id and output
    device_data = eufy_client.query_device_data("device_id")
    print(json.dumps(device_data, indent=4))

if __name__ == "__main__":

    main()
