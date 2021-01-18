from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#
# class MyBot:
#     def __init__(self):
#         user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
#
#         self.options = webdriver.ChromeOptions()
#         self.options.headless = True
#         self.options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
#         self.options.add_argument(f'user-agent={user_agent}')
#         self.options.add_argument("--window-size=1920,1080")
#         self.options.add_argument('--ignore-certificate-errors')
#         self.options.add_argument('--allow-running-insecure-content')
#         self.options.add_argument("--disable-extensions")
#         self.options.add_argument("--proxy-server='direct://'")
#         self.options.add_argument("--proxy-bypass-list=*")
#         self.options.add_argument("--start-maximized")
#         self.options.add_argument('--disable-gpu')
#         self.options.add_argument('--disable-dev-shm-usage')
#         self.options.add_argument('--no-sandbox')
#         self.driver = webdriver.Chrome(executable_path="E:\\Software\\chromedriver_win32\\chromedriver.exe",
#                                        options=self.options)
#
#         self.driver.get("https://google.com")
#
#         self.driver.get_screenshot_as_file("screenshot.png")
#         print(self.driver.title)
#
# MyBot()

# options = webdriver.ChromeOptions()
# options.headless = True
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# driver.implicitly_wait(10)
# driver.get('http://google.com')
# print(driver.title, '**************')


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class MyBot:
    def __init__(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"

        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')

        # this below line specify the executable_path automatically
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.options)

        '''
        This line respecify the executable file that is notpresent in your coputer thats why it fails.
        i.e 
        self.driver = webdriver.Chrome(executable_path="E:\\Software\\chromedriver_win32\\chromedriver.exe",options=self.options)
        '''

        self.driver.get("https://google.com")

        self.driver.get_screenshot_as_file("screenshot.png")
        print(self.driver.title)


MyBot()