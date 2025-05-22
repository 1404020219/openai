# tools/vision.py
from agent1 import AIAgent

_ai_agent = None

async def inference(image_path: str):
    global _ai_agent
    if _ai_agent is None:
        _ai_agent = AIAgent()
    result = _ai_agent.perceive(image_path)
    return {
        "name": "vision-agent/inference",
        "content_type": "text/plain",
        "content": {
            "text": "\n".join([f"{det['label']}: {det['confidence']:.2f}" for det in result["detections"]])
        }
    }
