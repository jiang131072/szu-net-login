import argparse
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import schedule


def test():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options)
    driver.get(url)

    title = driver.title

    driver.close()
    # get title
    if title in ("注销页", "Logout page"):
        return True
    else:
        return False


def run(username, password):
    options = webdriver.ChromeOptions()

    # https://www.selenium.dev/blog/2023/headless-is-going-away/
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options)
    driver.get(url)

    if test():
        print("已登录")
    else:
        print("尝试登录")
        in_usn = driver.find_element(By.NAME, "DDDDD")
        in_pwd = driver.find_element(By.NAME, "upass")
        btm_login = driver.find_element(By.NAME, "0MKKey")

        in_usn.send_keys(username)
        in_pwd.send_keys(password)
        btm_login.click()
        if test(url):
            print("登录成功")
        else:
            print("登录失败，稍后再试")
    driver.close()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("location", type=str, help="where are you? (dorm/ta)")
    parser.add_argument("username", type=str)
    parser.add_argument("password", type=str)
    args = parser.parse_args()

    global url
    if args.location == "dorm":
        url = "http://172.30.255.42"
    elif args.location == "ta":
        url = "http://drcom.szu.edu.cn"
    else:
        print("无效地址。宿舍区：dorm，教学区：ta")
        exit(1)

    username = args.username
    password = args.password

    run(username, password)
    schedule.every(1).minutes.do(run, username, password)

    while True:
        try:
            schedule.run_pending()
            time.sleep(10)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
