# szu-net-login

深圳大学教学区网络登录脚本

## 使用

```bash
usage: szu-net-login [-h] [--interval INTERVAL] [--username USERNAME] [--password PASSWORD]

深圳大学校园网自动登录工具（教学区）

options:
  -h, --help           show this help message and exit
  --interval INTERVAL  间隔时间
  --username USERNAME  账号。环境变量：SZU_NET_USERNAME
  --password PASSWORD  密码。环境变量：SZU_NET_PASSWORD

注：必须在已联网情况下执行一次，下载WebDriver执行无头登录操作
```

## 安装

在发布页下载最新whl包，并指定`pip/pipx install <YOUR_WHL_FILE>`安装即可

## 注意事项

需要在正常网络环境下登录一次来下载Webdriver