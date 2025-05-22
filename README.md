# mcp-ai-agent

这是一个基于 Model Control Protocol (MCP) 的 AI Agent 服务端实现，支持图像识别和翻译工具调用。

## 📦 功能

- ✅ 图像识别（vision-agent/inference）
- ✅ 英文 → 中文翻译（vision-agent/translate）
- ✅ 支持标准 JSON-RPC 协议通信
- ✅ FastAPI + WebSocket 集成

## 📁 目录结构
mcp-ai-agent/ │ ├── mcp_server.py # MCP 服务端入口 ├── mcp_client.py # 客户端测试脚本 ├── agent.py # AI Agent 核心逻辑 ├── requirements.txt # 所需依赖库 │ └── tools/ # 工具模块目录 ├── vision.py # 图像识别工具 └── translate.py # 翻译工具

## 🔧 使用方式
bash
启动服务端
uvicorn mcp_server:app --reload
新终端中运行客户端
python mcp_client.py

最终建议的 Git 操作流程
# 初始化
git init

# 添加远程仓库
git remote add origin <your-repo-url>

# 添加文件
git add .
git commit -m "feat: initial commit"

# 推送主分支
git branch -M main
git push -u origin main
