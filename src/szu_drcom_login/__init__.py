import argparse
import time

import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By

titles_ok = ("登录成功页", "Login success page", "注销页", "Logout page")

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")


def test(title: str):
    if title in titles_ok:
        return True
    else:
        return False


def login(username, password):
    driver = webdriver.Chrome(options)
    driver.get(url)

    if test(driver.title):
        print("已登录")
    else:
        print("尝试登录")

        # 勾选用户协议
        checkbox = driver.find_element(By.NAME, "C1")
        if not checkbox.is_selected():
            checkbox.click()

        # 账号 密码 登录
        driver.find_element(By.NAME, "DDDDD").send_keys(username)
        driver.find_element(By.NAME, "upass").send_keys(password)
        driver.find_element(By.NAME, "0MKKey").click()

        if test(driver.title):
            print("登录成功")
        else:
            print("登录失败，稍后再试")

    driver.close()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "location", type=str, help="登录位置（宿舍或教学区），对应 dorm/ta"
    )
    parser.add_argument("username", type=str, help="账号")
    parser.add_argument("password", type=str, help="密码")
    args = parser.parse_args()

    global url
    match args.location:
        case "dorm":
            url = "http://172.30.255.42"
        case "ta":
            url = "http://drcom.szu.edu.cn"
        case _:
            raise ValueError("无效地址")

    username = args.username
    password = args.password

    login(username, password)

    schedule.every(1).minutes.do(login, username, password)
    while True:
        try:
            schedule.run_pending()
            time.sleep(10)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
