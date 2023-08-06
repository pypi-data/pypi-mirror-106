import json
import socket
import urllib.request
from typing import List

import arrow
import codefast as cf
import twitter
from bs4 import BeautifulSoup

from .config import decode, fast_text_decode, fast_text_encode
from .oss import Bucket
from .utils import githup_upload

socket.setdefaulttimeout(3)


class Network:
    @classmethod
    def is_good_proxy(cls, proxy: str) -> bool:
        """Check whether this proxy is valid or not"""
        try:
            pxy = {'http': proxy}
            proxy_handler = urllib.request.ProxyHandler(pxy)
            opener = urllib.request.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            sock = urllib.request.urlopen(
                'http://www.google.com')  # change the url address here
        except urllib.error.HTTPError as e:
            print('Error code: ', e.code)
            return False
        except Exception as detail:
            print("ERROR:", detail)
            return False
        return True

    def ipcheck(self, proxy: str) -> None:
        if self.is_good_proxy(proxy):
            print("")


class Twitter(twitter.Api):
    def __init__(self):
        super(Twitter,
              self).__init__(consumer_key=decode('consumer_key'),
                             consumer_secret=decode('consumer_secret'),
                             access_token_key=decode('access_token'),
                             access_token_secret=decode('access_token_secret'),
                             proxies={'http': decode('http_proxy')})

    def hi(self):
        print('Hi, Twitter.')

    def post_status(self, text: str, media=[]):
        resp = self.api.PostUpdate(text, media=media)
        print("Text  : {}\nMedia : {}\nResponse:".format(text, media))
        cf.say(resp)

    def post(self, args: list):
        ''' post_status wrapper'''
        assert isinstance(args, list)

        text, media = '', []
        media_types = ('.png', '.jpeg', '.jpg', '.mp4', '.gif')

        for e in args:
            if cf.file.exists(e):
                if e.endswith(media_types):
                    media.append(e)
                else:
                    text += cf.file.read(e)
            else:
                text += e
        self.post_status(text, media)


class Douban:
    @classmethod
    def query_film_info(cls, dblink: str) -> str:
        soup = BeautifulSoup(cf.net.get(dblink).text, 'lxml')
        film_info = soup.find('script', {
            'type': "application/ld+json"
        }).contents[0].strip().replace('\n', '')
        dbinfos = json.loads(film_info)
        poster = dbinfos['image'].replace('.webp', '.jpg').replace(
            's_ratio_poster', 'l')
        cf.utils.shell('curl -o poster.jpg {}'.format(poster))
        cf.logger.info('// poster.jpg downloaded')

        html = ""
        with open('info.txt', 'w') as f:
            html += "#" + dbinfos['name'].rstrip() + "\n\n"
            info = soup.find('div', {'id': 'info'})
            for l in info.__str__().split("br/>"):
                text = BeautifulSoup(l, 'lxml').text.lstrip()
                if any(e in text
                       for e in ('导演', '主演', '季数', 'IMDb', '编剧', '又名')):
                    continue
                if text:
                    if '类型' in text:
                        text = text.replace(': ', ': #').replace('/ ', '#')
                    html += "➖" + text + "\n"

            vsummary = soup.find('span', {"property": 'v:summary'})
            vsummary = '\n'.join(
                (l.lstrip() for l in vsummary.text.split('\n')))

            html += "➖豆瓣 ({}): {}".format(
                dbinfos.get('aggregateRating', {}).get('ratingValue', '/'),
                dblink) + "\n\n"

            html += " {} \n".format(vsummary)
            cf.logger.info(html)
            f.write(html)


class LunarCalendar:
    '''爬虫实现的农历'''
    @classmethod
    def display(cls, date_str: str = ""):
        year, month, day = arrow.now().format('YYYY-MM-DD').split('-')
        if date_str:
            year, month, day = date_str.split('-')[:3]
        print('Date {}-{}-{}'.format(year, month, day))

        r = cf.net.get(
            'https://wannianrili.51240.com/ajax/?q={}-{}&v=19102608'.format(
                year, month))

        s = BeautifulSoup(r.text, 'lxml')
        pairs = []
        for x in s.findAll('div', {'class': 'wnrl_k_you'}):
            for y in x.findAll(
                    'div', {
                        'class': [
                            'wnrl_k_you_id_biaoti', 'wnrl_k_you_id_wnrl_riqi',
                            'wnrl_k_you_id_wnrl_nongli'
                        ]
                    }):
                pairs.append(y.text)

        weekdays = ["星期" + w for w in "一二三四五六日"]
        for w in weekdays:
            print("{:<2} | {:<8}".format(' ', w), end="")
        print('\n' + '*' * 117)

        for w in weekdays:
            if not pairs[0].endswith(w):
                print("\033[30m{} | {}\033[0m".format(pairs[1], pairs[2]),
                      end="\t")
            else:
                break

        for j in range(0, len(pairs), 3):
            if day == pairs[j + 1]:
                print("\033[31m\033[1m{} | {}\033[0m".format(
                    pairs[j + 1], pairs[j + 2]),
                      end="\t")
            else:
                print("{} | {}".format(pairs[j + 1], pairs[j + 2]), end="\t")
            if pairs[j].endswith('星期日'):
                print('')
        print('')


class AutoProxy(Bucket):
    pac = '/tmp/autoproxy.pac'
    tmp = '/tmp/autoproxy_encrypted'

    @classmethod
    def query_rules(cls) -> List[str]:
        AutoProxy().download(cf.file.basename(cls.tmp), export_to=cls.tmp)
        text = cf.file.read(cls.tmp)
        return fast_text_decode(text).split('\n')

    @classmethod
    def sync2git(cls):
        f = cf.file.basename(cls.pac)
        cf.file.copy(cls.pac, f)
        githup_upload(f, shorten=False)
        cf.logger.info(f'{f} was synced to Github.')
        cf.file.rm(f)

    @classmethod
    def add(cls, url: str) -> None:
        rule_list = cls.query_rules()
        url = '  \"||{}\"'.format(url)
        if any(url in e for e in rule_list):
            cf.logger.info('{} was already included.'.format(url))
            return

        rule_list.insert(63, url)
        str_rules = '\n'.join(rule_list)
        text_new = fast_text_encode(str_rules)
        cf.file.write(text_new, cls.tmp)
        cf.file.write(str_rules, cls.pac)
        AutoProxy().upload(cls.tmp)
        cf.logger.info('{} added to rule list SUCCESS'.format(url))
        cls.sync2git()

    @classmethod
    def delete(cls, url: str) -> None:
        rule_list = cls.query_rules()
        url = '  \"||{}\"'.format(url)
        if url in rule_list:
            rule_list.remove(url)
            str_rules = '\n'.join(rule_list)
            str_rules_encrypted = fast_text_encode(str_rules)
            cf.file.write(str_rules_encrypted, cls.tmp)
            cf.file.write(str_rules, cls.pac)
            AutoProxy().upload(cls.tmp)
            cf.logger.info('{} removed from rule list SUCCESS'.format(url))
            cls.sync2git()
        else:
            cf.logger.info('{} was NOT included in rule list'.format(url))
