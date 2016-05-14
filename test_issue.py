import unittest
import requests
import xmltodict


class TestGetIssue(unittest.TestCase):

    def setUp(self):
        self.base_url = 'https://codespace-api.myjetbrains.com/youtrack/rest'
        self.creds = ('root', 'c11desp@ce')

    def test_get_issue(self):
        url = self.base_url + '/issue/' + 'API-1'
        response = requests.get(url, auth=self.creds)
        response_dict = xmltodict.parse(response.text)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response_dict['issue']['@id'], 'API-1')

    def test_get_nonexisted_issue(self):
        url = self.base_url + '/issue/' + 'ZZZ'

        response = requests.get(url, auth=self.creds)
        self.assertEquals(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
