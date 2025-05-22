# agent1.py

import cv2
import numpy as np
import torch
from torchvision import transforms, models


class AIAgent:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"[INFO] 使用设备: {self.device}")

        # 加载预训练模型
        self.model = models.resnet50(weights="IMAGENET1K_V1").eval().to(self.device)

        # ImageNet 分类标签
        with open("imagenet_classes.txt", "r") as f:
            self.labels = [line.strip() for line in f.readlines()]

        # 图像预处理
        self.transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def perceive(self, image_path):
        """
        输入图片路径，返回识别结果
        :param image_path: str
        :return: dict of detected objects with confidence
        """
        image = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        input_tensor = self.transform(image_rgb).unsqueeze(0).to(self.device)

        with torch.no_grad():
            output = self.model(input_tensor)

        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        top5_prob, top5_idx = torch.topk(probabilities, 5)

        detections = []
        for i in range(top5_prob.size(0)):
            label = self.labels[top5_idx[i]]
            prob = top5_prob[i].item()
            detections.append({"label": label, "confidence": prob})

        return {
            "detections": detections
        }
