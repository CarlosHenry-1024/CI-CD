# 使用官方 Python 镜像作为基础镜像
# 基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装依赖
COPY environment.txt .
RUN pip install --no-cache-dir -r environment.txt

# 复制项目代码
COPY . .

# 切换到非 root 用户
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# 设置默认启动命令
CMD ["python", "app/main.py"]