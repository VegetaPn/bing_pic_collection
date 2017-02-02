# bing_pic_collection
必应图片收集脚本  

Windows下桌面背景自动更新脚本(间隔: 8 hours)

2017.02.02: 更新，适配新版必应网站
2016.04.18: 添加Windows下桌面背景自动更新

1. 当日必应图片收集: 直接运行collect_pics.py
当前的必应搜索背景图片将按照当前日期命名，保存至collection/images文件夹中

2. Windows下桌面背景自动更新:
  - 前台运行: daily_up_windows_background.py
  - 后台运行: daily_up_windows_background.pyw
  - 后台关闭: 任务管理器 -- 结束进程: pythonw
