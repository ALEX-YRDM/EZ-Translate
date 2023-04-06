# EZ-Translate

## QuickStart

- 进入http://api.fanyi.baidu.com/，申请认证通用翻译API 仅需验证身份证信息即可获得每月100w字符的免费额度
- 修改Translate.py中的appid和passwd为你自己的
- src为源语言 tar为目标语言。具体的语言字符代号可查阅百度翻译开发文档
- 确认导入相应依赖后运行即可 （推荐虚拟环境使用，PyCharm+Anaconda)

## Function

* 当检测到系统剪切板内容变化即可调用API实时翻译，打印结果到控制台

## To do

* 增加其他平台的API 有道云 谷歌云 Bing翻译
* 开发GUI  客户端或者网页