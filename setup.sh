#!/bin/bash

# 安装 Python（如果需要）

# 创建并激活虚拟环境
echo "Creating and activating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# 安装依赖库
echo "Installing required packages..."
# 如果下载过慢，可以设置代理--proxy http://127.0.0.1:7890
pip3 install -r ./packages.txt --proxy http://127.0.0.1:7898

echo "Setup complete."
