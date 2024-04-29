# szu-drcom-login

一个使用Webdriver接口运行无头浏览器绘画完成校园网登录的脚本

## 使用

```bash
usage: szu-drcom-login [-h] location username password

positional arguments:
  location    登录位置（宿舍或教学区），对应dorm/ta
  username    账号
  password    密码

options:
  -h, --help  show this help message and exit
```

## 安装

在发布界面下载最新的wheel包文件，然后执行`pipx install <whl file>`即可（注意，需要首先安装pipx）。也可使用`pip install <whl file>`直接安装到环境中。

## 注意事项

1. 无网络状态下尝试登录会短暂卡住，并输出一些和googlelabs等相关的连接失败警告。
  - 这是因为Selenium的Webdriver并不是直接打包在wheel文件中，而需要在运行时下载更新。
  - 在没有登录网络的情况下自然会连接失败。
  - 为了保证功能正常，建议安装好之后先测试一次，以便检查账号登录情况并缓存Webdriver可执行文件。
2. 代理
  - 宿舍区由于是内网IP直连，使用任何形式的代理都没有影响。
  - 教学区的登录情况没有经过充分测试。建议关闭代理的DoH并建议将登录网址置入绕过白名单。