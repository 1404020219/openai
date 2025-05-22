# server.py

from fastapi import FastAPI, WebSocket
from fastapi.websockets import WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse

from tools.ocr import ocr
from tools.vision import inference
from tools.translate import translate
import json

app = FastAPI()


# 挂载静态文件目录（如 static/）
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get_ui():
    with open("static/index.html", "r") as f:
        return HTMLResponse(f.read())

@app.websocket("/mcp")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    async def receive() -> str:
        return await websocket.receive_text()

    async def send(message: str):
        await websocket.send_text(message)

    async def handle_message(message: str):
        try:
            request = json.loads(message)
            method = request.get("method")
            req_id = request.get("id")

            if method == "initialize":
                return {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"capabilities": {}}
                }

            elif method == "listTools":
                return {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": ["vision-agent/inference", "vision-agent/translate"]
                }

            elif method == "callTool":
                tool_name = request.get("params", {}).get("tool_name")
                arguments = request.get("params", {}).get("arguments", {})

                if tool_name == "vision-agent/inference":
                    return {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "result": await inference(**arguments)
                    }

                elif tool_name == "vision-agent/translate":
                    return {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "result": await translate(**arguments)
                    }

                elif tool_name == "vision-agent/ocr":
                    return {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "result": await ocr(**arguments)
                    }

                else:
                    return {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "error": {"code": -32601, "message": "Method not found"}
                    }

            else:
                return {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32601, "message": f"Unsupported method: {method}"}
                }

        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32603, "message": f"Internal error: {str(e)}"}
            }

    try:
        while True:
            message = await receive()
            print("📩 收到请求:", message)
            response = await handle_message(message)
            if response:
                await send(json.dumps(response))
    except WebSocketDisconnect:
        print("❌ 客户端断开连接")
