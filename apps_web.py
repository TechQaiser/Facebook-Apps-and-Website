import requests,bs4,re,os,sys

class apps_and_web():
    def __init__(self, url, cookie):
        self.url = url
        self.cookie = cookie
        self.fetcher = requests.Session()
        self.apps = []
    def active_apps(self):
        try:
            result = self.fetcher.get(self.url,cookies={'cookies':self.cookie})
            getch = bs4.BeautifulSoup(result.text, "html.parser")
            if 'These are apps' in getch.prettify():
                asd = getch.find_all('h3')
                ___io_bs4_level = re.findall('class="dm(.*?)</a>', str(asd))
                if len(___io_bs4_level) > 0:
                    print(" \033[1;32mActive Apps And Websites Found For This ID \033[0m ")
                else:
                    print(" \033[1;35mNot Found Active Apps And Websites Found For This ID \033[0m ")
                for _mirch in ___io_bs4_level:
                    a_p = _mirch.split('>')[-1]
                    self.apps.append(a_p)
                date = re.findall('dp">(.*?)<',str(asd))
                for lo_op in range(len(date)):
                    print(" {}. {} | {}".format(lo_op+1,self.apps[lo_op],date[lo_op]))
            elif not 'Logout' in getch.prettify():
                sys.exit('\033[1;91minvalid cookies\033[0m')
            else:
                print("\033[1;31m There Is No Apps & Websites In This ID")
        except Exception as e:
            print(e)
    def expire_apps(self):
        try:
            result = self.fetcher.get(self.url,cookies={'cookies':self.cookie})
            getch = bs4.BeautifulSoup(result.text, "html.parser")
            if 'These are apps' in getch.prettify():
                asd = getch.find_all('h3')
                ___io_bs4_level = re.findall('class="dm(.*?)</a>', str(asd))
                if len(___io_bs4_level) > 0:
                    print(" \033[1;33mEXpire Apps And Websites Found For This ID \033[0m ")
                else:
                    print(" \033[1;35mNot Found EXpire Apps And Websites Found For This ID \033[0m ")
                for _mirch in ___io_bs4_level:
                    a_p = _mirch.split('>')[-1]
                    self.apps.append(a_p)
                date = re.findall('dp">(.*?)<',str(asd))
                for lo_op in range(len(date)):
                    print(" {}. {} | {}".format(lo_op+1,self.apps[lo_op],date[lo_op]))
        except Exception as e:
            print(e)

if __name__ == '__main__':
    os.system('cls')
    cookies = input("    paste cookie of id to check apps and web\n cookie here : ")
    run=apps_and_web('https://free.facebook.com/settings/apps/tabbed/?tab=active',cookies)
    run.active_apps()
    run=apps_and_web('https://free.facebook.com/settings/apps/tabbed/?tab=inactive',cookies)
    run.expire_apps()