---
title: '利用“Enjoy 静态下载站生成工具”发布你的网站'
date: 2023-02-06 00:00:00
tags: [微型项目]
published: true
hideInList: false
feature: /post-images/enjoy-jing-tai-xia-zai-zhan-sheng-cheng-gong-ju.jpeg
isTop: false
---
项目地址：<https://github.com/PanDaoxi/enjoy-static-website-generator>
DEMO：<https://pandaoxi.github.io/enjoy-static-website-generator>

![](https://daoxi365.github.io/tech-blog//post-images/1689661088258.png)

软件截图及使用方法：

![](https://daoxi365.github.io/tech-blog//post-images/1689660863707.png)

选择一个文件夹后，软件提示“完成”。
您可以在软件的根目录下 `files` 文件夹中发现已经制作成功的下载站。
您可以将该文件夹下的内容上传至 `GitHub/Gitee/Coding Pages` 或 `Netlify App` 展示静态页面。

> $\text{Tips\ } 1$：软件制作出文件夹的的默认自述文档为 `欢迎使用 Enjoy 静态资源站生成工具`。如果您想自定义网站文件夹的自述文档内容（显示在页面下方），请在该文件夹下创建文件 `README.md`，使用 `Markdown` 语法编写文档。完成后需重新制作下载站。
> $\text{Tips\ } 2$：如果您不喜欢当前下载站的默认样式，可以调整**软件根目录**下 `template.html` 的内容，需要按照注释修改。
> $\text{Tips\ } 3$：如果简易版 GUI 满足不了您的需求，可以尝试利用 Python 修改 `main.py`。也可以新建另一文档，引入软件包并自行编写程序。