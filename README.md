# mcp-ai-agent

这是一个基于 Model Control Protocol (MCP) 的 AI Agent 服务端实现，支持图像识别和翻译工具调用。

## 📦 功能

- ✅ 图像识别（vision-agent/inference）
- ✅ 英文 → 中文翻译（vision-agent/translate）
- ✅ 支持标准 JSON-RPC 协议通信
- ✅ FastAPI + WebSocket 集成

## 📁 目录结构
mcp-ai-agent/
│
├── mcp_server.py             # 原有 MCP 服务端逻辑
├── web_server.py             # 新增网页服务端逻辑（FastAPI + 模板渲染）
├── agent.py                  # AI Agent 核心逻辑
├── tools/                    
│   ├── vision.py
│   └── translate.py
├── templates/
│   └── index.html            # 网页模板
├── static/
│   └── style.css             # 可选样式文件
├── uploads/                  # 临时保存上传的图片
├── requirements.txt
└── README.md


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
