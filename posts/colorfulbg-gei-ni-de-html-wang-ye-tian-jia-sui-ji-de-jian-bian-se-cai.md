---
title: 'ColorfulBG——给你的 HTML 网页添加随机的渐变色彩'
date: 2024-02-06 11:33:24
tags: [微型项目]
published: true
hideInList: false
feature: /post-images/colorfulbg-gei-ni-de-html-wang-ye-tian-jia-sui-ji-de-jian-bian-se-cai.png
isTop: false
---
# `ColorfulBG` 渐变填充——为你的网页添加一个漂亮的背景

此项目含有多种渐变颜色集：

|          源文件           |                          解释                          |                             链接                             |                          压缩版链接                          |
| :-----------------------: | :----------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|      `./255mod3.js`       |               包含了所有颜色的三分之一。               | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/mFytppKIMlYAwsWOCelwhDGf1QxHz0FI/255mod3.js) | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/iUuiTqwRmORLpuJD5nvU4th2YWF4vv0H/255mod3.min.min.js) |
|      `./255mod5.js`       |               包含了所有颜色的五分之一。               | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/vOSmBFC5WJ04rBufHBED2akQHiGN2Fx9/255mod5.js) | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/7IpNv6ubgXs8IPI0oXuadSc6D2WOzGJH/255mod5.min.js) |
|      `./255mod10.js`      |               包含了所有颜色的十分之一。               | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/f4iND4bR4X0zvR9skfProsxvUJckSBxP/255mod10.js) | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/z91uf0GD8q5X7GgTvIwaMLQnUDPIuwGU/255mod10.min.js) |
|   `./chinese_painting.js`    |                  常用的中国国画色彩。                  | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/31vlMNHAdVcrzmir25m7jDeodzmzPT3o/chinese_painting.js) | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/ndl1j1soaNy3eJ4FMMVsYRJtTjwB38R3/chinese_painting.min.js) |
| `./chinese_tradition.js`  |                  常用的中国传统色彩。                  | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/EzPRYy5llBG4YqmCsF1UsAQ6gBg3J20a/chinese_tradition.js) | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/6ey9dBjvbinKbzdlFBfFQ3HML0DmOCBi/chinese_tradition.min.js) |
| `./japanese_tradition.js` |                  常用的日本传统色彩。                  | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/oIS7TkGa9RwiQCciBvXn8a6KMAIPYO2b/japanese_tradition.js) | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/XnzimtsPVgqneSUukC4OQpKlyJbmaPkK/japanese_tradition.min.js) |
|     `./dark_mode.js`      |              深色模式，其中的颜色比较暗。              | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/MnXlAbcd93QqKh7snn6rMYlCHe9vGjbc/dark_mode.js) | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/DtPGIdn9MjnLU8RDTvOKOQ0fa260Sdtc/dark_mode.min.js) |
|     `./light_mode.js`     |             浅色模式，其中的颜色比较明亮。             | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/VIgw7dMgAmQ6XcrKbaFvTBkPsHtId3iQ/light_mode.js) | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/IpvEePn3bWhuCyPscNHF4Yq63nOAkjoi/light_mode.min.js) |
|       `./bright.js`       |                     最明亮的色彩。                     | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/tW7FAn6y9GrdsHGKSGB4Uz4m9vmz8GWk/bright.js) | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/kvrAplKfk7aWvRXilttF4iA7XC9ER6GO/bright.min.js) |
|      `./classic.js`       | 包含了常用的中国国画色彩、中国传统色彩和日本传统色彩。 | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/HqCEpXlQhriaXwhlmIpAByKv39SHuTsc/classic.js) | [CDN](https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/2ahD0gXGeW4QUABiEqOJ9VclChVhHUSR/classic.min.js) |

欢迎测试！
部分颜色来自网络（<https://tool.lu/>），如果侵犯了您的权利，请告知。

---

用法：

```html
<body>
  <!-- 你的代码。 -->
  <script src="https://lc-gluttony.s3.amazonaws.com/0zpMrNotfBZq/2ahD0gXGeW4QUABiEqOJ9VclChVhHUSR/classic.min.js"></script>
</body>
```

考虑到网络连接可能不畅，建议您慎用 `255mod3` 等大型颜色集，一般情况下 `classic` 应该就够用了（包含了上千种颜色），除非您对颜色有更多要求。

> 警告：
> 务必要把此 `<script>` 标签放在  `<body>` 内，否则程序将无法运行。
> 或者使用本地版，美化之后添加 `DOMContentLoaded` 监听器。
---

效果展示：

![](https://daoxi365.github.io/tech-blog//post-images/1720755596854.png)

![](https://daoxi365.github.io/tech-blog//post-images/1720755677713.png)

![](https://daoxi365.github.io/tech-blog//post-images/1720756462654.png)

这些图片的背景色都来自 `classic.js`。

---

利用 Python 生成颜色集。
这种色彩集并不一定是从 `#000000` 到 `#ffffff` 的，可以自行修改。如我的[主站](/) 就是使用了浅色调色彩集（从 `#c8c8c8` 到 `#ffffff`）。

```python
# Author: PanDaoxi

rgb2hex = lambda r, g, b: "#{:02x}{:02x}{:02x}".format(r, g, b)
colorSet = ""
cnt = 0

for r in range(0, 256, 10):
    for g in range(0, 256, 10):
        for b in range(0, 256, 10):
            if not (cnt % 10) and cnt:
                colorSet += "\n"
            colorSet += '"%s", ' % rgb2hex(r, g, b)
            cnt += 1

with open("colorset.txt", "w", encoding="utf-8") as f:
    f.write(colorSet[: len(colorSet) - 1])
```

![](https://daoxi365.github.io/tech-blog//post-images/1720765627257.png)

得到色彩集之后就可以放到相应 js 文件里的 `colors` 数组了。

```javascript
var colors = [
    // 放置色彩集
    
];

function getRandom(arr) {
    var result = [];
    for (var i = 0; i < arr.length && result.length < 3; i++) {
        if (!result.includes(i)) {
            var randomIndex = Math.floor(Math.random() * arr.length);
            
            while (result.includes(randomIndex)) {
                randomIndex = Math.floor(Math.random() * arr.length);
            }
            
            result[i] = arr[randomIndex];
        }
    }
    return result;
}

var tmp = getRandom(colors);
document.addEventListener("DOMContentLoaded", () => {
    var html = document.getElementsByTagName("html")[0];
    // 随机选取 3 个颜色
    html.style.background = `linear-gradient(120deg, ${tmp[0]}, ${tmp[1]}, ${tmp[2]})`;
});
```

如果需要 CDN，分发至 Leancloud 某一应用的文件即可。