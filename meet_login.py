from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CDM
from datetime import datetime
import schedule

driver = None

f = open("user.txt", "r")
lines = f.readlines()
f.close()
for i in range(4):
    lines[i] = lines[i].strip()
                
def Login_Google():
        
    global driver
    
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    
    opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic":    1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation":         1,
        "profile.default_content_setting_values.notifications":       1
    })
    args = ["hide_console", ]
    driver = webdriver.Chrome(service_args=args,chrome_options=opt,executable_path=CDM().install())
    
    url = "https://accounts.google.com/signin"
    mail = lines[0]
    password = lines[1]
    driver.get(url)
    sleep(2)
    driver.find_element_by_xpath('//input[@type="email"]').send_keys(mail)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    sleep(3)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_id("passwordNext").click()
    sleep(3)

def Login_Meet():
        
    crm_url = "http://crm.mingdao.edu.tw/crm/index.asp"
    
    user = lines[2]
    password = lines[3]
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    
    driver.get(crm_url)
    try:
        driver.find_element_by_xpath('//*[@id="showin_input"]').send_keys(user)
        driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[3]/td/form/table/tbody/tr[4]/td[2]/input').send_keys(password)
        driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[3]/td/form/table/tbody/tr[6]/td/input').click()
    except:
        pass

    driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[2]/table/tbody/tr[3]/td/table[1]/tbody/tr[2]/td[2]/div/a[1]').click()
    driver.close()
    sleep(5)
    driver.switch_to.window(driver.window_handles[-1])
    
    now = datetime.now()
    day = now.weekday() + 1
    time = now.hour * 60 + now.minute
    ctime = [555,615,675,730,855,915,975,1030]
    for i, k in enumerate(ctime):
        if k > time:
            time = i + 1
            break
    
    driver.find_element_by_xpath('//*[@id="F_{}_{}_P"]/div'.format(day, time)).click()
    sleep(1)
    meet_url = driver.find_element_by_xpath('//*[@id="popupContent"]').get_attribute('src')
    driver.get(meet_url)
    driver.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()
    meet_url = driver.find_element_by_xpath('//*[@id="main"]/div[3]/a').text
    driver.close()
            
    driver.switch_to.window(driver.window_handles[-1])
    html_source = driver.page_source
    while "發生錯誤" in html_source and datetime.now().minute <= 30:
        print("加入 Meet 失敗，可能因為會議尚未開始")
        print("五秒後重試")
        sleep(10)
        driver.get(meet_url)
    
    if "發生錯誤" in html_source:
        print("無法加入會議")
        return
    else:
        driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
        driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]').click()
    
    try:
        StopTime = ctime[time-1]
        NowTime = now.hour * 60 + now.minute
        while NowTime < StopTime:
            sleep(30)
            NowTime = now.hour * 60 + now.minute
        else:
            driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[1]/div[9]/div[10]/div[2]/div/div[6]/span/botton').click()
    except:
        return
    
def Login_Morning():

    crm_url = "http://crm.mingdao.edu.tw/crm/index.asp"
    
    user = lines[2]
    password = lines[3]
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    
    driver.get(crm_url)
    try:
        driver.find_element_by_xpath('//*[@id="showin_input"]').send_keys(user)
        driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[3]/td/form/table/tbody/tr[4]/td[2]/input').send_keys(password)
        driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[3]/td/form/table/tbody/tr[6]/td/input').click()
    except:
        pass

    driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[2]/table/tbody/tr[3]/td/table[1]/tbody/tr[2]/td[2]/div/a[1]').click()
    driver.close()
    sleep(5)
    driver.switch_to.window(driver.window_handles[-1])

    driver.find_element_by_xpath('//*[@id="F_{}_{}_P"]/div'.format(2,1)).click()
    sleep(1)
    meet_url = driver.find_element_by_xpath('//*[@id="popupContent"]').get_attribute('src')
    driver.get(meet_url)
    driver.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()
    meet_url = driver.find_element_by_xpath('//*[@id="main"]/div[3]/a').text
    driver.close()
            
    driver.switch_to.window(driver.window_handles[-1])
    html_source = driver.page_source
    while "發生錯誤" in html_source and datetime.now().minute <= 20:
        print("加入 Meet 失敗，可能因為會議尚未開始")
        print("十秒後重試")
        sleep(10)
        driver.get(meet_url)
    
    if "發生錯誤" in html_source:
        print("無法加入會議")
        return
    else:
        driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
        driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]').click()
    
    try:
        now = datetime.now()
        StopTime = 498
        NowTime = now.hour * 60 + now.minute
        while NowTime < StopTime:
            sleep(30)
            now = datetime.now()
            NowTime = now.hour * 60 + now.minute
        else:
            driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[1]/div[9]/div[10]/div[2]/div/div[6]/span/botton').click()
    except:
        return
    
def Login():
    if datetime.now().weekday() > 5:
        return
    Login_Google()
    Login_Meet()

def MorningRollCall():
    if datetime.now().weekday() > 5:
        return
    Login_Google()
    Login_Morning()

def run():
    schedule.every().day.at(f'08:15:00').do(MorningRollCall)
    schedule.every().day.at(f'08:24:00').do(Login)
    schedule.every().day.at(f'09:24:00').do(Login)
    schedule.every().day.at(f'10:24:00').do(Login)
    schedule.every().day.at(f'11:24:00').do(Login)
    schedule.every().day.at(f'13:24:00').do(Login)
    schedule.every().day.at(f'14:25:00').do(Login)
    schedule.every().day.at(f'15:24:00').do(Login)
    schedule.every().day.at(f'16:24:00').do(Login)
    while True:
        schedule.run_pending()
        sleep(1)

if __name__ == '__main__':
    run()