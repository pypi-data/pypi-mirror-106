import core.utils as utils
import json
import numpy as np
import cv2
import os

from .calculate import save_result
# import cgf_ml_sdk.object_detection.calculate as cal
# from object-detection.ca import target as cal


# import calculation


class EvalOut(object):
    """
    docstring
    """

    """
    传入testout的path，保存在此路径下
    file_path:最后保存的文件的地址
    annotation_path:标注文件的路径
    types:对应的类别,[swiming pool,car]
    """

    def __init__(self, annotation_path, bboxes, types, file_path):
        self.file_path = file_path
        self.annotation_path = annotation_path
        self.types = types
        self.bboxes = bboxes

    '''
    保存测试结果和结果相比标注的错误对比
    '''

    def save(self, threshold=0.1):
        open(self.file_path, 'w').close()
        self.save_all_lines()
        self.save_constrast(os.path.splitext(self.file_path)[0] + '.json', threshold)

    """
    设置类型信息
    """

    def set_img_path(self, img_path):
        self.img_path = img_path

    """
    设置单张图片预测结果
    """

    def set_data(self, data):
        self.data = data

    """
    将一张图片的所有标注信息单行存储
    """

    def save_one_line(self):
        with open(self.file_path, 'a', encoding='utf-8') as f:
            line = self.img_path
            for i, item in enumerate(self.data):
                # 开头路径
                # print(self.data[0],self.data[1])
                # print(item[0], item[1], item[2], item[3], item[4], item[5])
                line = line + ' ' + ','.join(
                    [str(item[0]), str(item[1]), str(item[2]), str(item[3]), str(item[4]), str(int(item[5]))])
            f.write(line + '\n')

    """
    传入预测的结果值bboxes，直接保存到result.json中
    """

    def save_all_lines(self):
        path_list = []
        with open(self.annotation_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip('\n').split(' ')
                path_list.append(line[0])

        # 保存所有图片的预测结果
        for i, img_path in enumerate(path_list):
            self.set_img_path(img_path)
            self.set_data(self.bboxes[i])
            self.save_one_line()

    """
    给出标注框选的可视化
    """

    def show_annotation(self):
        with open(self.annotation_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip('\n').split(' ')
                img_path = line[0]
                img = cv2.imread(img_path)
                for i, item in enumerate(line[1:]):
                    item = item.split(',')
                    red = (0, 0, 255)
                    cv2.rectangle(img, (int(float(item[0])), int(float(item[1]))),
                                  (int(float(item[2])), int(float(item[3]))), red)
                cv2.imwrite('annotation.png', img)
                img = cv2.imread(img_path)
                # cv2.waiteKey()

    """
    给出预测框选的可视化
    """

    def show_precit(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip('\n').split(' ')
                img_path = line[0]
                img = cv2.imread(img_path)
                for i, item in enumerate(line[1:]):
                    item = item.split(',')
                    red = (0, 0, 255)
                    cv2.rectangle(img, (int(float(item[0])), int(float(item[1]))),
                                  (int(float(item[2])), int(float(item[3]))), red)
                cv2.imwrite('./lziqi_test_show/' + img_path, img)
                img = cv2.imread(img_path)
                # cv2.waiteKey()

    """
    保存annotation和预测之间的差异
    """

    def save_constrast(self, file_path, threshold):
        #
        info = save_result(self.annotation_path, self.file_path, self.types)

        annotation_data = {}
        predict_data = {}

        # 读入标注数据
        with open(self.annotation_path, 'r', encoding='utf-8') as f:
            # 对每个图片来处理
            for line in f:
                line = line.strip('\n').strip().split(' ')
                annotation = []
                for i, item in enumerate(line[1:]):
                    item = item.split(',')
                    annotation.append(item)
                annotation_data.update({line[0]: annotation})
                # print(annotation_data[line[0]])

        # 读入预测数据
        with open(self.file_path, 'r', encoding='utf-8') as f:
            # 对每个图像来处理
            for line in f:
                line = line.strip('\n').strip().split(' ')
                predict = []
                for i, item in enumerate(line[1:]):
                    item = item.split(',')
                    predict.append(item)
                predict_data.update({line[0]: predict})
                # print(predict_data[line[0]])

        json_data = {'tableName': '测试标注结果'}
        # 将两者数据进行求iou的共同区域>threshold=0.5 且种类相同则为正确预测
        for img_path in annotation_data:
            annotation = annotation_data[img_path]
            predict = predict_data[img_path]

            json_data.update({img_path: {}})
            json_data[img_path].update({'dataset_annot': {}})
            json_data[img_path].update({'evaluate_annot': {}})
            json_data[img_path].update({'error_annot': {}})

            json_data[img_path]['dataset_annot'].update({'num': len(annotation)})
            json_data[img_path]['dataset_annot'].update({'annotations': []})

            json_data[img_path]['evaluate_annot'].update({'num': len(predict)})
            json_data[img_path]['evaluate_annot'].update({'annotations': []})

            for j in enumerate(predict):
                json_data[img_path]['evaluate_annot']['annotations'].append({
                    'xmin': predict[j[0]][0],
                    'ymin': predict[j[0]][1],
                    'xmax': predict[j[0]][2],
                    'ymax': predict[j[0]][3],
                    'code': predict[j[0]][5],
                    'label': self.types[int(predict[j[0]][5])],
                    'confidence': predict[j[0]][4]
                })

            # 对一张图片的每一个标注
            ok_set = set()
            error_set = set()
            for i in enumerate(annotation):
                json_data[img_path]['dataset_annot']['annotations'].append({
                    'xmin': annotation[i[0]][0],
                    'ymin': annotation[i[0]][1],
                    'xmax': annotation[i[0]][2],
                    'ymax': annotation[i[0]][3],
                    'code': annotation[i[0]][4],
                    'label': self.types[int(annotation[i[0]][4])]
                })

                for j in enumerate(predict):
                    # 不满足条件则加入error_list
                    iou = utils.bboxes_iou(np.array([float(i) for i in annotation[i[0]][:4]]),
                                           np.array([float(i) for i in predict[j[0]][:4]]))
                    if iou > threshold and annotation[i[0]][4] == predict[j[0]][5]:
                        ok_set.add(j[0])
                    else:
                        error_set.add(j[0])
            for i in error_set.copy():
                if i in ok_set:
                    error_set.remove(i)
            json_data[img_path]['error_annot'].update({'num': len(error_set)})
            json_data[img_path]['error_annot'].update({'error_no': list(error_set)})

        info['tables'].append(json_data)
        # json_data.update(info)
        # 保存对比结果和混淆矩阵等信息
        with open(file_path, 'w')as f:
            json.dump(info, f)

