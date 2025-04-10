import torch
from torchvision import transforms
from PIL import Image
import timm
import numpy as np
import os
import pandas as pd

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
    image = Image.open(image_path).convert('RGB')
    image = data_transforms(image).unsqueeze(0)  # 添加 batch 维度
    image = image.to(device)
    
    with torch.no_grad():
        logits = model(image)
        probs = torch.sigmoid(logits).cpu().numpy().flatten()
    
    predictions = (probs > threshold).astype(int)
    return predictions

# 预测标签的类别名
label_columns = ['N', 'D', 'G', 'C', 'A', 'H', 'M', 'O']

# 图片文件夹路径
image_folder = r'E:\Dataset\competition\test_image\test_concat'

# 结果保存路径
result_path = r'E:\Dataset\competition\test_image\result.xlsx'

# 存储结果
data = []

# 批量处理图片
for i in range(1, 501):  # 从 1 到 500
    image_path = os.path.join(image_folder, f"{i}.jpg")
    if os.path.exists(image_path):
        predictions = predict_image(image_path, model)
        data.append([i] + predictions.tolist())
        print(f"已处理 {i}.jpg")
    else:
        print(f"警告: {image_path} 不存在，跳过。")

# 转换为 DataFrame
df = pd.DataFrame(data, columns=['Image_ID'] + label_columns)

# 保存到 Excel
df.to_excel(result_path, index=False)

print(f"检测完成，结果已保存至 {result_path}")
