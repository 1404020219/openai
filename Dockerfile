# 使用官方 Python 镜像作为基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 拷贝本地代码到容器内
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露服务运行端口（FastAPI 默认使用 8000）
EXPOSE 8000

# 启动命令（运行 FastAPI 服务）
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
