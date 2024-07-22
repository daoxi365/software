`404 not found`，是 HTTP 对网页错误情况返回的一种状态码，当用户在浏览器中输入网址时，服务器会根据输入的地址判断是否有对应的网页信息，如果没有对应信息，说明用户输入的可能是一串无效的链接，服务器就会向用户返回 `404 not found` 状态码，告诉用户没有找到对应的网页信息。

<!-- more -->

效果展示：
![](post-images/1718952960360.gif)

```html
<!-- Author: PanDaoxi -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
	<link rel="shortcut icon" href="https://daoxi365.github.io/tech-blog/favicon.ico">
	<link href="https://cdn.bootcdn.net/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet">
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #0078d7;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            user-select: none; /* 禁止选择文本 */
            overflow: hidden; /* 防止页面滚动 */
        }

        .window {
            width: 400px;
            border-radius: 8px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
            background-color: #ffffff;
            position: relative;
        }

        .title-bar {
            display: flex;
            align-items: center;
            padding: 10px;
            background-color: rgb(237, 245, 249);
            color: #000000;
            cursor: grab;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
        }

        .title-bar .title {
			font-family: 'Ubuntu';
            flex-grow: 1;
        }

        .title-bar .close {
			font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            width: 40px; /* 增大宽度 */
            height: 40px; /* 增大高度 */
            text-align: center;
            background-color: rgb(237, 245, 249); /* 默认背景色 */
            color: rgb(5, 7, 8); /* 默认 X 颜色 */
            cursor: pointer;
            transition: background-color 0.3s ease, color 0.3s ease;
            display: flex;
            justify-content: center;
            align-items: center;
            position: absolute; /* 使用绝对定位 */
            top: 0; /* 上边缘与 title-bar 对齐 */
            right: 0; /* 右边缘与 title-bar 对齐 */
            border-top-right-radius: 8px; /* 圆角 */
        }

        .title-bar .close:hover {
            background-color: rgb(221, 70, 10); /* 悬停时背景变红 */
            color: rgb(255, 255, 255); /* 悬停时 X 变白 */
        }

        .content {
            padding: 20px;
            text-align: left;
            overflow: hidden; /* 防止内容溢出 */
        }

        .error-container {
            display: flex;
            align-items: center;
            position: relative;
            margin-bottom: 20px;
            flex-wrap: wrap; /* 在小屏幕上换行 */
        }

        .error-icon {
			font-family: 'Segoe UI';
            background-color: rgb(221, 70, 10); /* 红色背景 */
            color: rgb(250, 250, 250); /* 白色图标 */
            width: 80px; /* 增大尺寸 */
            height: 80px; /* 增大尺寸 */
            display: flex;
            justify-content: center;
            align-items: center;
            margin-right: 15px;
            margin-bottom: 10px; /* 为小屏幕添加间距 */
            border-radius: 50%; /* 圆形设计 */
        }

        .error-icon i {
            font-size: 3em; /* 增大叉号大小 */
        }

        .error-details {
			font-family: 'Ubuntu';
            flex: 1; /* 占据剩余空间 */
            text-align: center;
        }

        .error-code {
            font-size: 2.5em;
            color: #0078d7;
        }

        .error-message {
            font-size: 1.2em;
            color: #000000;
        }

        @media (max-width: 480px) {
            .window {
                width: 90%;
            }

            .error-container {
                flex-direction: column;
                align-items: center;
                text-align: center;
            }

            .error-icon {
                margin-right: 0;
            }
        }
    </style>
</head>
<body>
    <div class="window" id="window">
        <div class="title-bar" id="title-bar">
            <div class="title">PanDaoxi's Tech-Blog</div>
            <div class="close" onclick="goBack()"><i class="fa fa-times"></i></div>
        </div>
        <div class="content">
            <div class="error-container">
                <div class="error-icon">
                    <i class="fa fa-times"></i> <!-- 红底白叉 -->
                </div>
                <div class="error-details">
                    <div class="error-code">404</div>
                    <div class="error-message">Page Not Found</div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // 使窗口可拖动
        const windowElement = document.getElementById('window');
        const titleBar = document.getElementById('title-bar');

        let isDragging = false;
        let offsetX, offsetY;

        titleBar.addEventListener('mousedown', (e) => {
            isDragging = true;
            offsetX = e.clientX - windowElement.getBoundingClientRect().left;
            offsetY = e.clientY - windowElement.getBoundingClientRect().top;
            document.addEventListener('mousemove', onMouseMove);
            document.addEventListener('mouseup', onMouseUp);
        });

        function onMouseMove(e) {
            if (!isDragging) return;
            const newLeft = e.clientX - offsetX;
            const newTop = e.clientY - offsetY;

            // 防止窗口移动到视口之外
            const windowWidth = windowElement.offsetWidth;
            const windowHeight = windowElement.offsetHeight;

            const minLeft = 0;
            const maxLeft = window.innerWidth - windowWidth;
            const minTop = 0;
            const maxTop = window.innerHeight - windowHeight;

            windowElement.style.position = 'absolute';
            windowElement.style.left = `${Math.max(minLeft, Math.min(newLeft, maxLeft))}px`;
            windowElement.style.top = `${Math.max(minTop, Math.min(newTop, maxTop))}px`;
        }

        function onMouseUp() {
            isDragging = false;
            document.removeEventListener('mousemove', onMouseMove);
            document.removeEventListener('mouseup', onMouseUp);
        }

        // 关闭窗口
        function goBack() {
            window.history.back();
        }
    </script>
</body>
</html>
```