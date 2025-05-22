# client.py

import asyncio
import websockets
import json

async def test_mcp():
    uri = "ws://localhost:8000/mcp"
    async with websockets.connect(uri) as websocket:
        print("🔗 已连接到 MCP 服务端")

        # 初始化握手
        init_request = {
            "jsonrpc": "2.0",
            "id": "init",
            "method": "initialize",
            "params": {"capabilities": {}}
        }
        await websocket.send(json.dumps(init_request))
        response = await websocket.recv()
        print("🔧 初始化响应:", response)

        # 获取工具列表
        list_tools_request = {
            "jsonrpc": "2.0",
            "id": "list_tools",
            "method": "listTools",
            "params": {}
        }
        await websocket.send(json.dumps(list_tools_request))
        tools_response = await websocket.recv()
        print("📦 可用工具:", tools_response)

        # 调用图像识别
        inference_request = {
            "jsonrpc": "2.0",
            "id": "inference",
            "method": "callTool",
            "params": {
                "tool_name": "vision-agent/inference",
                "arguments": {"image_path": "test_images/test_image.jpg"}
            }
        }
        await websocket.send(json.dumps(inference_request))
        inference_result = await websocket.recv()
        print("🧠 推理结果:", inference_result)

        # 调用翻译
        translate_request = {
            "jsonrpc": "2.0",
            "id": "translate",
            "method": "callTool",
            "params": {
                "tool_name": "vision-agent/translate",
                "arguments": {"text": "A dog and a cat"}
            }
        }
        await websocket.send(json.dumps(translate_request))
        translate_result = await websocket.recv()
        decoded_result = json.loads(translate_result)
        print("🌍 翻译结果:", decoded_result)


asyncio.run(test_mcp())
