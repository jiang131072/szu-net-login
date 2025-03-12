import argparse
import time
import logging
import os

from selenium.webdriver import ChromeOptions as Options, Chrome as Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_chrome_options():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    return options


def check_login_status(driver: Browser):
    try:
        WebDriverWait(driver, 3).until(lambda d: "success" in d.current_url)
        return True
    except Exception:
        return False


def login(username, password):
    with Browser(options=get_chrome_options()) as driver:
        driver.get("https://net.szu.edu.cn/srun_portal_pc?ac_id=12")

        if check_login_status():
            logging.info("登录状态：已登录")
            return

        logging.info("登录状态：未登录")
        logging.info("行为：尝试登录")

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "login-accoun"))
            )

            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "login-account").click()

            if check_login_status(driver):
                logging.info("结果：登录成功")
            else:
                logging.info("结果：登录失败")

        except Exception as e:
            logging.error(f"错误: {e}")


def daemon(username, password, interval=60):
    while True:
        logging.info("行为：访问登录页面")
        login(username, password)
        time.sleep(interval)


def main():
    parser = argparse.ArgumentParser(
        description="深圳大学校园网自动登录工具（教学区）",
        epilog="注：必须在已联网情况下执行一次，下载WebDriver执行无头登录操作",
    )

    parser.add_argument("--interval", type=int, help="间隔时间")
    parser.add_argument(
        "--username",
        type=str,
        help="账号。环境变量：SZU_NET_USERNAME",
        default=os.getenv("SZU_NET_USERNAME"),
    )
    parser.add_argument(
        "--password",
        type=str,
        help="密码。环境变量：SZU_NET_PASSWORD",
        default=os.getenv("SZU_NET_PASSWORD"),
    )
    args = parser.parse_args()

    if not (args.username and args.password):
        logging.error("错误：没有获取到账号、密码")
        return

    if (interval := args.interval) and interval > 0:
        try:
            logging.info(f"行为：启动守护进程 [检查间隔={interval}s]")
            daemon(args.username, args.password, interval)
        except KeyboardInterrupt:
            logging.info("行为：退出")
            exit()
    else:
        login(args.username, args.password)


if __name__ == "__main__":
    main()
