import torch
from torchvision import transforms
from PIL import Image
import timm
import numpy as np

# 设备设置：使用 GPU 如果可用
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 加载训练好的模型
model = timm.create_model('efficientnet_b0', pretrained=False, num_classes=8)
model.load_state_dict(torch.load(r'E:\Dataset\competition\model\epoch99.pth', map_location=device))
model.to(device)
model.eval()  # 切换到评估模式

# 定义数据预处理（与训练时一致）
data_transforms = transforms.Compose([
    transforms.Resize((448, 224)),  # 调整大小
    transforms.ToTensor(),  # 转换为 Tensor
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])  # 标准化
])

# 预测函数
def predict_image(image_path, model, threshold=0.3):
    """
    对单张图片进行多标签分类预测
    :param image_path: 图片路径
    :param model: 训练好的 PyTorch 模型
    :param threshold: 预测标签的阈值（默认为 0.5）
    :return: 预测的标签概率和最终标签
    """
    # 加载并预处理图片
    image = Image.open(image_path).convert('RGB')
    image = data_transforms(image).unsqueeze(0)  # 添加 batch 维度
    
    # 发送到设备
    image = image.to(device)
    
    # 关闭梯度计算，加速推理
    with torch.no_grad():
        logits = model(image)  # 获取原始 logits
        probs = torch.sigmoid(logits)  # 经过 Sigmoid 得到概率
        probs = probs.cpu().numpy().flatten()  # 转换为 NumPy 数组

    # 应用阈值，生成最终的二进制预测结果
    predictions = (probs > threshold).astype(int)

    return probs, predictions

# 预测标签的类别名（与你的数据集对应的标签列名）
label_columns = ['N', 'D', 'G', 'C', 'A', 'H', 'M', 'O']

# 测试图片路径
image_path =r'E:\Dataset\competition\Dataset\1662.jpg'  # 替换为你的图片路径

# 进行预测
probs, predictions = predict_image(image_path, model)

# 打印预测结果
print("类别概率：")
for label, prob in zip(label_columns, probs):
    print(f"{label}: {prob:.4f}")
    
print("\n最终预测标签：")
for label, pred in zip(label_columns, predictions):
    print(f"{label}: {pred}")

