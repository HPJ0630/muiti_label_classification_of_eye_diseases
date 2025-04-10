from PySide6.QtCore import Qt, QPoint, QThread, Signal, QTimer, QDateTime
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QMessageBox, QTableWidget, QTableWidgetItem, QFileDialog
from Ui_new import Ui_Form 
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import cv2
import numpy as np
from PySide6.QtGui import QPixmap, QImage
from datetime import datetime
import torch
import timm
from torchvision import transforms
from datetime import datetime
import os
import re
import pandas as pd
import openpyxl
from openpyxl.styles import Alignment
import ui_rc
import oss2
import time

class CustomWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.left_img = None # 左眼图片
        self.right_img = None # 右眼图片
        self.id = 0
        self.worker = None
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # self.append_log(f"使用设备{self.device}")
        self.label_16.setText(f"使用设备：{self.device}")
        self.model = timm.create_model('efficientnet_b0', pretrained=False, num_classes=8)
        self.model.load_state_dict(torch.load(r'best.pth', map_location=self.device)) # 加载模型
        self.model.to(self.device)
        self.model.eval()  # 切换到评估模式
        # 定义数据预处理
        self.data_transforms = transforms.Compose([
            transforms.Resize((448, 224)),  # 调整大小,双目图像，所以是448*224
            transforms.ToTensor(),  # 转换为 Tensor
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])  # 标准化
        ])
        # self.label_columns = ['N', 'D', 'G', 'C', 'A', 'H', 'M', 'O'] 
        self.label_columns = ['正常', '糖尿病', '青光眼', '白内障', 'AMD', '高血压', '近视', '其他眼疾']

        self.upload_thread = None
        
        # 设置无边框窗口
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 使窗口背景透明（可选）
        # 设置表格列宽
        self.tableWidget.setColumnWidth(0, 60)
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(2, 245)
        self.tableWidget.setColumnWidth(3, 245)
        self.tableWidget.setColumnWidth(4, 130)
        # self.tableWidget.setStyleSheet("QTableWidget::item { text-align: center; }")
        # self.tableWidget.setStyleSheet("QTableWidget::item:nth-child(4) { text-align: center; }")

        self.pushButton.setCursor((Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setCursor((Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setCursor((Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setCursor((Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setCursor((Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setCursor((Qt.CursorShape.PointingHandCursor))

        # 定时器 用于更新系统时间
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

        # 连接按钮功能
        self.mininum_button.clicked.connect(self.showMinimized)  # 最小化
        self.close_button.clicked.connect(self.close)  # 关闭窗口
        self.pushButton.clicked.connect(self.select_left_image)  # 选择左侧图片
        self.pushButton_2.clicked.connect(self.select_right_image)  # 选择右侧图片
        self.pushButton_5.clicked.connect(self.predict)  # 单词预测
        self.pushButton_8.clicked.connect(self.predict_folder)  # 批量预测文件夹
        self.pushButton_6.clicked.connect(self.save_result)  # 保存结果
        self.pushButton_7.clicked.connect(self.show_about)  # 清空表格

        # 记录鼠标起始位置
        self.dragging = False
        self.offset = QPoint()

    def update_time(self):
        # 获取当前时间并格式化
        current_time = QDateTime.currentDateTime()
        time_str = current_time.toString("yyyy-MM-dd hh:mm:ss")
        
        # 更新时间标签
        self.time_label.setText(time_str)

    def mousePressEvent(self, event):
        """鼠标按下事件：记录起始拖动点"""
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.globalPosition().toPoint() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        """鼠标移动事件：计算新的窗口位置"""
        if self.dragging and event.buttons() == Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self.offset)
            event.accept()

    def mouseReleaseEvent(self, event):
        """鼠标释放事件：停止拖动"""
        if event.button() == Qt.LeftButton:
            self.dragging = False
            event.accept()

    def select_left_image(self):
        """弹窗选择左眼图片的方式：选择文件或拍摄"""
        msg_box = QMessageBox()
        msg_box.setWindowTitle("选择图片来源")
        msg_box.setText("请选择图片的获取方式")
        select_button = msg_box.addButton("选择本地图片", QMessageBox.AcceptRole)
        capture_button = msg_box.addButton("拍摄图片", QMessageBox.ActionRole)
        cancel_button = msg_box.addButton("取消", QMessageBox.RejectRole)

        msg_box.exec()

        if msg_box.clickedButton() == select_button:
            # 选择本地图片
            image_path, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "Image Files (*.png *.jpg *.bmp *.jpeg *.gif)")
            if image_path:
                self.left_img = Image.open(image_path)
                self.left_img_path = image_path
                self.lineEdit_3.setText(image_path)
                self.append_log(f"左眼图片已加载：{image_path}")
            else:
                self.left_img = None

        elif msg_box.clickedButton() == capture_button:
            # 拍摄图片
            captured_path = self.capture_image_from_camera()
            if captured_path:
                self.left_img = Image.open(captured_path)
                self.left_img_path = captured_path
                self.lineEdit_3.setText(captured_path)
                self.append_log(f"左眼图片已拍摄并加载：{captured_path}")
            else:
                self.append_log("未拍摄图片或拍摄取消")
                self.left_img = None
        else:
            self.append_log("用户取消了图片选择")

    def capture_image_from_camera(self):
        """使用摄像头拍照，按回车拍照，按q退出"""
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            self.append_log("摄像头打开失败")
            return None

        self.append_log("摄像头已打开:按下Enter键拍照,按下q键退出")

        while True:
            ret, frame = cap.read()
            if not ret:
                continue
            cv2.imshow("拍摄图片", frame)
            key = cv2.waitKey(1)

            if key == ord('q'):
                # self.append_log("已退出拍摄")
                break
            elif key == 13:  # 回车键
                # 保存图片
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                filename = f"captured_{timestamp}.jpg"
                save_path = os.path.abspath(filename)
                cv2.imwrite(save_path, frame)
                self.append_log(f"图片已保存为：{save_path}")
                cap.release()
                cv2.destroyAllWindows()
                return save_path

        cap.release()
        cv2.destroyAllWindows()
        return None


    def select_right_image(self):
        """弹窗选择右眼图片的方式：选择文件或拍摄"""
        msg_box = QMessageBox()
        msg_box.setWindowTitle("选择图片来源")
        msg_box.setText("请选择右眼图片的获取方式")
        select_button = msg_box.addButton("选择本地图片", QMessageBox.AcceptRole)
        capture_button = msg_box.addButton("拍摄图片", QMessageBox.ActionRole)
        cancel_button = msg_box.addButton("取消", QMessageBox.RejectRole)

        msg_box.exec()

        if msg_box.clickedButton() == select_button:
            # 选择本地图片
            image_path, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "Image Files (*.png *.jpg *.bmp *.jpeg *.gif)")
            if image_path:
                self.right_img = Image.open(image_path)
                self.right_img_path = image_path
                self.lineEdit_4.setText(image_path)
                self.append_log(f"右眼图片已加载：{image_path}")
            else:
                self.right_img = None

        elif msg_box.clickedButton() == capture_button:
            # 拍摄图片
            captured_path = self.capture_image_from_camera()
            if captured_path:
                self.right_img = Image.open(captured_path)
                self.right_img_path = captured_path
                self.lineEdit_4.setText(captured_path)
                self.append_log(f"右眼图片已拍摄并加载：{captured_path}")
            else:
                self.append_log("未拍摄右眼图片或拍摄取消")
                self.right_img = None
        else:
            self.append_log("用户取消了右眼图片选择")

    def predict(self):
        """预测单张"""
        if self.left_img and self.right_img:  # 如果左右两侧都有图片
            self.append_log(f"开始检测...")
            merged_image = self.show_concat_image(self.left_img, self.right_img, show_flag = True)   # 显示拼接后的图片
            prob, predictions = self.predict_image(merged_image, self.model)  # 预测图片
            prob_lst = prob.tolist()
            # print(prob_lst)
            predictions_lst = predictions.tolist()
            if prob_lst.index(max(prob_lst)) == 0:
                predictions_lst = [1, 0, 0, 0, 0, 0, 0, 0]
            else:
                predictions_lst[0] = 0
            if predictions_lst == [0, 0, 0, 0, 0, 0, 0, 0]:
                predictions_lst[prob_lst.index(max(prob_lst))] = 1
            prob = np.array(prob_lst)
            predictions = np.array(predictions_lst)
            # print(predictions)
            prediction_result = [self.label_columns[i] for i in range(len(predictions)) if predictions[i] == 1]
            prediction_result = ", ".join(prediction_result)
            # print(prediction_result)
            self.append_log(f"预测结果：{prediction_result}")  # 显示预测结果
            prediction_result = prediction_result.replace(", ", "\n")
            self.label_2.setText(f"{prediction_result}")  # 显示预测结果
            now = datetime.now()  # 获取当前时间
            formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")  # 格式化时间
            if self.tableWidget.rowCount() < self.id+2:  # 如果表格行数小于当前记录数，则添加新行
                self.tableWidget.insertRow(self.tableWidget.rowCount())
            self.tableWidget.setItem(self.id+1, 0, QTableWidgetItem(str(self.id)))
            self.tableWidget.setItem(self.id+1, 1, QTableWidgetItem(str(formatted_time)))
            self.tableWidget.setItem(self.id+1, 2, QTableWidgetItem(str(self.left_img_path)))
            self.tableWidget.setItem(self.id+1, 3, QTableWidgetItem(str(self.right_img_path)))
            self.tableWidget.setItem(self.id+1, 4, QTableWidgetItem(str(prediction_result)))
            self.id += 1
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # 设置弹窗图标
            msg.setWindowTitle("提示")  # 弹窗标题
            msg.setText("请先选择左右眼图片")  # 弹窗提示内容
            msg.setStandardButtons(QMessageBox.Ok)  # 设置弹窗按钮
            msg.exec()  # 显示弹窗

    def predict_folder(self):
        """选择文件夹并启动预测线程"""
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if not folder_path:
            return

        # 创建并启动 Worker 线程
        self.worker = PredictWorker(folder_path, self.model, self.label_columns,
                                    self.show_concat_image, self.predict_image)

        # 连接信号到 UI 线程
        self.worker.result_signal.connect(self.update_table)
        self.worker.log_signal.connect(self.append_log)
        self.worker.finished_signal.connect(self.on_prediction_finished)

        self.worker.start()  # 启动线程

    def update_table(self, num, formatted_time, left_img_path, right_img_path, prediction_result):
        """更新表格数据"""
        if self.tableWidget.rowCount() < self.id + 2:
            self.tableWidget.insertRow(self.tableWidget.rowCount())

        self.tableWidget.setItem(self.id + 1, 0, QTableWidgetItem(str(self.id)))
        self.tableWidget.setItem(self.id + 1, 1, QTableWidgetItem(str(formatted_time)))
        self.tableWidget.setItem(self.id + 1, 2, QTableWidgetItem(str(left_img_path)))
        self.tableWidget.setItem(self.id + 1, 3, QTableWidgetItem(str(right_img_path)))
        self.tableWidget.setItem(self.id + 1, 4, QTableWidgetItem(str(prediction_result)))
        self.id += 1

    def on_prediction_finished(self):
        """线程任务完成后执行的操作"""
        self.append_log("所有图片检测完成！")
        self.worker = None

    def show_about(self):
        QMessageBox.about(self, "关于系统", "开发者：黄培杰\n开发时间：2025.03.20至2025.03.27\n版本：v1.0.0")

    # def predict_folder(self):
    #     """批量预测文件夹内的图片"""
    #     folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")  # 选择文件夹
    #     if not folder_path:
    #         return  # 如果用户未选择文件夹，则返回

    #     self.append_log("开始批量检测...")
    #     pattern = re.compile(r"(\d+)_([a-z]+)\.jpg")  # 正则匹配 "num_left.jpg" 和 "num_right.jpg"
        
    #     # 查找所有符合格式的图片
    #     image_dict = {}
    #     for file_name in os.listdir(folder_path):
    #         match = pattern.match(file_name)
    #         if match:
    #             num, side = match.groups()
    #             num = int(num)
    #             if num not in image_dict:
    #                 image_dict[num] = {}
    #             image_dict[num][side] = os.path.join(folder_path, file_name)

    #     # 遍历字典，拼接和预测
    #     for num, pair in sorted(image_dict.items()):
    #         if "left" in pair and "right" in pair:
    #             left_img_path = pair["left"]
    #             right_img_path = pair["right"]
                
    #             # 读取图像（替代 self.load_image）
    #             left_img = cv2.imread(left_img_path)
    #             right_img = cv2.imread(right_img_path)

    #             if left_img is None or right_img is None:
    #                 self.append_log(f"跳过 {num}，无法读取图片")
    #                 continue

    #             self.append_log(f"正在检测 {num}...")

    #             # 拼接图像
    #             merged_image = self.show_concat_image(left_img, right_img, False)

    #             # 进行预测
    #             _, predictions = self.predict_image(merged_image, self.model)
    #             prediction_result = [self.label_columns[i] for i in range(len(predictions)) if predictions[i] == 1]
    #             prediction_result = ", ".join(prediction_result)

    #             self.append_log(f"{num} 预测结果：{prediction_result}")

    #             # 格式化结果
    #             prediction_result_display = prediction_result.replace(", ", "\n")
    #             # self.label_2.setText(f"{prediction_result_display}")  # 显示预测结果

    #             now = datetime.now()
    #             formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    #             if self.tableWidget.rowCount() < self.id+2:  # 如果表格行数小于当前记录数，则添加新行
    #                 self.tableWidget.insertRow(self.tableWidget.rowCount())
    #             self.tableWidget.setItem(self.id+1, 0, QTableWidgetItem(str(self.id)))
    #             self.tableWidget.setItem(self.id+1, 1, QTableWidgetItem(str(formatted_time)))
    #             self.tableWidget.setItem(self.id+1, 2, QTableWidgetItem(str(left_img_path)))
    #             self.tableWidget.setItem(self.id+1, 3, QTableWidgetItem(str(right_img_path)))
    #             self.tableWidget.setItem(self.id+1, 4, QTableWidgetItem(str(prediction_result_display)))
    #             self.id += 1

    #     self.append_log("批量检测完成！")

    def show_concat_image(self, left_img, right_img, show_flag):
        """显示左右眼拼接图片"""
        if left_img is not None and right_img is not None:  # 确保左右眼图片存在
            left_img = np.array(left_img)
            right_img = np.array(right_img)
            eye_image = [left_img, right_img]
            padding = 20
            eye_sizes = []

            # 裁剪图片，确保眼球区域一致
            for i, img in enumerate(eye_image):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                _, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
                contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                if contours:
                    largest_contour = max(contours, key=cv2.contourArea)
                    x, y, w, h = cv2.boundingRect(largest_contour)
                    x = max(0, x - padding)
                    y = max(0, y - padding)
                    w = min(img.shape[1] - x, w + 2 * padding)
                    h = min(img.shape[0] - y, h + 2 * padding)
                    eye_image[i] = img[y:y+h, x:x+w]  # 裁剪图像
                    eye_sizes.append((w, h))

            # 计算目标高度（取最大值）
            target_height = max(eye_sizes[0][1], eye_sizes[1][1])

            # 按比例调整宽度，保证高度对齐
            left_resized = cv2.resize(eye_image[0], (int(eye_sizes[0][0] * (target_height / eye_sizes[0][1])), target_height))
            right_resized = cv2.resize(eye_image[1], (int(eye_sizes[1][0] * (target_height / eye_sizes[1][1])), target_height))

            # 水平拼接图片
            merged_image = np.hstack((left_resized, right_resized))
            merged_image_bgr = cv2.cvtColor(merged_image, cv2.COLOR_RGB2BGR)  # 转换为 BGR 格式
            # cv2.imshow("Merged Image", merged_image)
            # cv2.imwrite("merged_image.jpg", merged_image)
            pixmap = QPixmap.fromImage(QImage(merged_image.data, merged_image.shape[1], merged_image.shape[0], merged_image.shape[1] * 3, QImage.Format_RGB888))
            label_width = self.label_13.width()
            label_height = self.label_13.height()
            scaled_pixmap = pixmap.scaled(label_width, label_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            if show_flag:
                self.label_13.setPixmap(scaled_pixmap)
            return merged_image_bgr
            # # 统一两个图像的眼球大小
            # target_width = max(eye_sizes[0][0], eye_sizes[1][0])  # 选择最大的宽度
            # target_height = max(eye_sizes[0][1], eye_sizes[1][1])  # 选择最大的高度
            # # 调整两个眼球的大小，使它们一致
            # left_resized = cv2.resize(eye_image[0], (target_width, target_height))
            # right_resized = cv2.resize(eye_image[1], (target_width, target_height))
            # # 拼接图片
            # merged_image = np.hstack((left_resized, right_resized))
            # # print(type(merged_image))
            # # 显示拼接后的图片在ui中
            # pixmap = QPixmap.fromImage(QImage(merged_image.data, merged_image.shape[1], merged_image.shape[0], merged_image.shape[1] * 3, QImage.Format_RGB888))
            # label_width = self.label_13.width()
            # label_height = self.label_13.height()
            # scaled_pixmap = pixmap.scaled(label_width, label_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # self.label_13.setPixmap(scaled_pixmap)
            # return merged_image

    def upload_to_oss(self, local_file_path, object_name):
        """
        在后台线程中上传文件
        """
        # 创建后台线程
        self.upload_thread = UploadThread(local_file_path, object_name)

        # 连接上传完成的信号
        self.upload_thread.upload_finished.connect(self.on_upload_finished)
        self.upload_thread.upload_one_file.connect(self.append_log)

        # 启动线程
        self.upload_thread.start()

    def on_upload_finished(self, message):
        """
        上传完成后的回调，更新 UI
        """
        # 在这里更新 UI，例如显示弹窗，提示上传结果
        print(message)  # 打印结果或显示到界面

    def append_log(self, message):
        """向日志窗口添加新日志，并加上时间戳"""
        current_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")  # 获取当前时间
        log_message = f"{current_time} {message}"  # 拼接时间和日志内容
        self.textBrowser.append(log_message)  # 显示日志

    def predict_image(self, image, model, threshold=0.3):
        """
        对单张图片进行多标签分类预测
        :param image_path: 图片路径
        :param model: 训练好的 PyTorch 模型
        :param threshold: 预测标签的阈值（默认为 0.5）
        :return: 预测的标签概率和最终标签
        """
        # 加载并预处理图片
        # image = Image.open(image_path).convert('RGB')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 转换为 RGB 格式
        image = Image.fromarray(image)  # 转换为 PIL Image 格式
        image = self.data_transforms(image).unsqueeze(0)  # 添加 batch 维度
        # 发送到设备
        image = image.to(self.device)
        # 关闭梯度计算，加速推理
        with torch.no_grad():
            logits = model(image)  # 获取原始 logits
            probs = torch.sigmoid(logits)  # 经过 Sigmoid 得到概率
            probs = probs.cpu().numpy().flatten()  # 转换为 NumPy 数组
        # 应用阈值，生成最终的二进制预测结果
        predictions = (probs > threshold).astype(int)
        return probs, predictions

    def save_result(self):
        """保存检测结果"""
        # 选择保存文件路径
        file_path, _ = QFileDialog.getSaveFileName(self, "保存为 Excel", "", "Excel 文件 (*.xlsx)")
        file_name = os.path.basename(file_path)
        # print(file_path, file_name)

        if not file_path:
            return  # 用户取消保存

        if not file_path.endswith(".xlsx"):
            file_path += ".xlsx"  # 确保文件名有 .xlsx 后缀

        # 提取表格数据
        row_count = self.tableWidget.rowCount()
        col_count = self.tableWidget.columnCount()

        data = []
        headers = ['序号', '时间', '左眼路径', '右眼路径', '预测结果']  # 获取表头

        for row in range(1, row_count):  # 从第二行开始（假设第一行是表头）
            row_data = []
            for col in range(col_count):
                item = self.tableWidget.item(row, col)
                row_data.append(item.text() if item else "")  # 处理空单元格
            data.append(row_data)

        # 转换为 DataFrame 并保存为 Excel
        df = pd.DataFrame(data, columns=headers)

        # 保存为 Excel 文件
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, header=True, sheet_name='Sheet1')

            # 获取 worksheet 对象
            worksheet = writer.sheets['Sheet1']

            # 自动调整列宽
            for col in worksheet.columns:
                max_length = 0
                column = col[0].column_letter  # 获取列字母
                for cell in col:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(cell.value)
                    except:
                        pass
                adjusted_width = (max_length + 5)  # 给列宽加上少许额外空间
                worksheet.column_dimensions[column].width = adjusted_width

            # 设置居中对齐
            for row in worksheet.iter_rows():
                for cell in row:
                    cell.alignment = Alignment(horizontal='center', vertical='center')

        self.append_log(f"表格数据已保存至 {file_path}")

        # 显示是否上传的确认框
        reply = QMessageBox.question(self, '上传结果', '诊断结果已保存本地\n是否上传至OSS？',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.upload_to_oss(file_path, file_name)  # 调用上传文件的方法（需要你自己实现upload_result）

# 批量检测线程
class PredictWorker(QThread):
    result_signal = Signal(int, str, str, str, str)  # 用于更新表格
    log_signal = Signal(str)  # 用于更新日志
    finished_signal = Signal()  # 任务完成信号

    def __init__(self, folder_path, model, label_columns, show_concat_image, predict_image):
        super().__init__()
        self.folder_path = folder_path
        self.model = model
        self.label_columns = label_columns
        self.show_concat_image = show_concat_image
        self.predict_image = predict_image

    def run(self):
        """线程执行函数"""
        self.log_signal.emit("开始批量检测...")
        pattern = re.compile(r"(\d+)_([a-z]+)\.jpg")  # 匹配 "num_left.jpg" 和 "num_right.jpg"

        image_dict = {}
        for file_name in os.listdir(self.folder_path):
            match = pattern.match(file_name)
            if match:
                num, side = match.groups()
                num = int(num)
                if num not in image_dict:
                    image_dict[num] = {}
                image_dict[num][side] = os.path.join(self.folder_path, file_name)

        for num, pair in sorted(image_dict.items()):
            if "left" in pair and "right" in pair:
                left_img_path = pair["left"]
                right_img_path = pair["right"]

                left_img = cv2.imread(left_img_path)
                right_img = cv2.imread(right_img_path)

                if left_img is None or right_img is None:
                    self.log_signal.emit(f"跳过 {num}，无法读取图片")
                    continue

                # self.log_signal.emit(f"正在检测 {num}...")

                merged_image = self.show_concat_image(left_img, right_img, show_flag = False)
                merged_image = cv2.cvtColor(merged_image, cv2.COLOR_RGB2BGR)  # 转换为 BGR 格式
                # cv2.imshow("Merged Image", merged_image)
                # cv2.waitKey(0)

                prob, predictions = self.predict_image(merged_image, self.model)
                prob_lst = prob.tolist()
                predictions_lst = predictions.tolist()
                if prob_lst.index(max(prob_lst)) == 0:
                    predictions_lst = [1, 0, 0, 0, 0, 0, 0, 0]
                else:
                    predictions_lst[0] = 0
                if predictions_lst == [0, 0, 0, 0, 0, 0, 0, 0]:
                    predictions_lst[prob_lst.index(max(prob_lst))] = 1
                prob = np.array(prob_lst)
                predictions = np.array(predictions_lst)
                # if prob.index(max(prob)) == 0:
                #     predictions = [1, 0, 0, 0, 0, 0, 0, 0]
                # else:
                #     predictions[0] = 0
                # print(f"{num} 预测结果：{predictions}")
                prediction_result = [self.label_columns[i] for i in range(len(predictions)) if predictions[i] == 1]
                prediction_result = ", ".join(prediction_result)
                # print(f"{num} 预测结果：{prediction_result}")
                self.log_signal.emit(f"{num} 预测结果：{prediction_result}")

                formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                self.result_signal.emit(num, formatted_time, left_img_path, right_img_path, prediction_result)

        self.log_signal.emit("批量检测完成！")
        self.finished_signal.emit()

# 上传阿里云OSS线程
class UploadThread(QThread):
    """
    后台线程处理上传操作
    """
    upload_one_file = Signal(str)  # 上传单个文件完成的信号
    upload_finished = Signal(str)  # 全部上传完成的信号

    def __init__(self, local_file_path, object_name, parent=None):
        super().__init__(parent)
        self.local_file_path = local_file_path
        self.object_name = object_name

    def run(self):
        """
        后台线程运行的上传任务
        """
        try:
            # 配置 AccessKey 和 Bucket 信息
            bucket_name = ''  # OSS Bucket 名称
            access_key_id = ''  # 阿里云 AccessKey ID
            access_key_secret = ''  # 阿里云 AccessKey Secret
            endpoint = ''  # OSS 区域 Endpoint

            auth = oss2.Auth(access_key_id, access_key_secret)
            bucket = oss2.Bucket(auth, endpoint, bucket_name)

            # 获取当前时间戳，作为根目录
            current_time = datetime.now()
            formatted_time = current_time.strftime("%y%m%d%H%M%S")

            # 上传表格文件
            headers = {'x-oss-object-acl': 'public-read'}
            bucket.put_object_from_file(formatted_time + '/' + self.object_name, self.local_file_path, headers=headers)
            self.upload_one_file.emit(f"成功上传结果表格{self.object_name}到OSS!")

            # 读取 Excel 文件
            df = pd.read_excel(self.local_file_path)

            # 创建图片存放的目录路径
            image_folder = formatted_time + '/image/'

            # 遍历表格中的每一行，上传图片
            for index, row in df.iterrows():
                left_eye_path = row['左眼路径']
                right_eye_path = row['右眼路径']

                # 上传左眼图片
                if os.path.exists(left_eye_path):
                    left_image_name = os.path.basename(left_eye_path)
                    left_oss_path = image_folder + left_image_name
                    bucket.put_object_from_file(left_oss_path, left_eye_path, headers=headers)

                # 上传右眼图片
                if os.path.exists(right_eye_path):
                    right_image_name = os.path.basename(right_eye_path)
                    right_oss_path = image_folder + right_image_name
                    bucket.put_object_from_file(right_oss_path, right_eye_path, headers=headers)

                # 打印每次上传的文件
                self.upload_one_file.emit(f"成功上传左眼图片{left_image_name}和右眼图片{right_image_name}到OSS!")
                # print(f"上传左眼图片 {left_image_name} 和右眼图片 {right_image_name} 到 OSS 完成")

            # 上传完成后发出信号
            self.upload_one_file.emit(f"所有图片上传完成！")
            # self.upload_finished.emit(f"上传到 OSS 完成, 文件夹路径为: {formatted_time}")

        except Exception as e:
            self.upload_finished.emit(f"上传到 OSS 失败: {e}")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = CustomWindow()
    window.show()
    sys.exit(app.exec())
