import argparse
import time

import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By


def test(title: str):
    if title in ("注销页", "Logout page"):
        return True
    else:
        return False


def login(username, password):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options)
    driver.get(url)

    if test(driver.title):
        print("已登录")
    else:
        print("尝试登录")
        # 账号 密码 登录按钮
        in_usn = driver.find_element(By.NAME, "DDDDD")
        in_pwd = driver.find_element(By.NAME, "upass")
        btm_login = driver.find_element(By.NAME, "0MKKey")

        # 勾选用户协议
        box_lgoin = driver.find_element(By.NAME, "C1")
        if not box_lgoin.is_selected():
            box_lgoin.click()

        in_usn.send_keys(username)
        in_pwd.send_keys(password)
        # box_lgoin.
        btm_login.click()
        if test(driver.title):
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
    match args.location:
        case "dorm":
            url = "http://172.30.255.42"
        case "ta":
            url = "http://drcom.szu.edu.cn"
        case _:
            raise ValueError("无效地址。宿舍区：dorm，教学区：ta")

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
