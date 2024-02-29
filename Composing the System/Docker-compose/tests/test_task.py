import string
import unittest
import random

import requests
import docker
from common.test_with_docker_compose import TestWithDockerCompose

client = docker.from_env()


class TestTask(TestWithDockerCompose):
    healthcheck_url = 'http://127.0.0.1:5000/items'

    async def test_get(self):
        try:
            response = requests.get('http://127.0.0.1:5001/items')
            print(response.status_code)
            print(response.text)
            self.assertEqual(200, response.status_code, msg=f"GET request resulted in an unexpected response code: {response.status_code}")
        except Exception as e:
            if isinstance(e, AssertionError):
                self.fail(msg=f"Unexpected response, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')

    async def test_post(self):
        try:
            device_id = ''.join(random.choices(string.ascii_lowercase, k=10))
            response = requests.post('http://127.0.0.1:5001/items', json={"id": f"{device_id}",
                                                                          "name": "UPDATEDUPDATEDUPDATED",
                                                                          "location": "location",
                                                                          "status": "off"})
            print(response.status_code)
            print(response.text)
            self.assertEqual(201, response.status_code, msg=f"Unexpected response code for POST {response.status_code}")
        except Exception as e:
            if isinstance(e, AssertionError):
                self.fail(msg=f"Unexpected response, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')

    async def test_put(self):
        try:
            response = requests.put('http://127.0.0.1:5001/items/002', json={"id": "002",
                                                                             "name": "Humidity_sensor",
                                                                             "location": "bedroom",
                                                                             "status": "off"})
            print(response.status_code)
            print(response.text)
            self.assertEqual(200, response.status_code, msg=f"PUT request resulted in an unexpected response code: {response.status_code}")
        except Exception as e:
            if isinstance(e, AssertionError):
                self.fail(msg=f"Unexpected response, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')

    async def test_delete(self):
        try:
            response = requests.delete('http://127.0.0.1:5001/items/100')
            print(response.status_code)
            print(response.text)
            self.assertEqual(404, response.status_code, msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
        except Exception as e:
            if isinstance(e, AssertionError):
                self.fail(msg=f"Unexpected response, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')
