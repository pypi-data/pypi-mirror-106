import json
import numpy as np
import cv2
import os

from .calculate import save_result as SAVE_RESULT


class EvalOut():
    '''
    annotation_path: 测试集标注文件绝对路径
    save_file_path: 结果文件绝对路径
    y_pred: 预测标签
    y_score: 预测标签置信度
    labels: 标签名称数组
    '''
    def __init__(self, annotation_path, save_file_path, y_pred, y_score, labels):
        self.annotation_path = annotation_path
        self.y_pred = y_pred
        self.y_score = y_score
        self.labels = labels
        self.save_file_path = save_file_path
    

    '''
    保存测试结果
    '''
    def save(self):
        print("saving result...")
        self._save_all_lines(self.annotation_path, self.save_file_path, self.y_pred, self.y_score)
        info = self._save_details(self.annotation_path, self.save_file_path, self.labels, self.y_score)

        with open(self.save_file_path,'w')as f:
            json.dump(info,f)
        print("saving result successful")


    """
    传入预测结果，直接保存到result.json中
    """
    def _save_all_lines(self, annotation_path, save_file_path, y_pred, y_score):
        path_list = []
        with open(annotation_path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                ri = line.rstrip().rfind(' ')
                if ri == -1:
                    print("error image path: {}".format(line))
                    continue
                path_list.append(line[:ri])

        if len(path_list) != len(y_pred):
            raise IndexError("path_list length not equal to y_pred length, path_len:{} pred_len:{}".format(len(path_list), len(y_pred)))

        # 保存所有图片的预测结果
        with open(save_file_path, 'w', encoding='utf-8') as f:
            for i, img_path in enumerate(path_list):
                line = img_path + ' ' + str(y_pred[i]) + ',' + str(y_score[i])
                f.write(line+'\n')


    def _save_details(self, real_ann_path, pred_ann_path, labels, y_score):
        # 
        info = SAVE_RESULT(real_ann_path, pred_ann_path, labels)

        annotation_data = {}
        predict_data = {}
        # 读入标注数据
        with open(real_ann_path,'r',encoding='utf-8') as f:
            # 对每个图片来处理
            for line in f:
                ri = line.rstrip().rfind(' ')
                annotation_data.update({line[:ri]:int(line[ri+1:])})
                # print(annotation_data[line[0]])
        
        # 读入预测数据
        with open(pred_ann_path,'r',encoding='utf-8') as f:
            # 对每个图像来处理
            for line in f:
                ri = line.rstrip().rfind(' ')
                predict_data.update({line[:ri]:(int(line[ri+1:].split(',')[0]), float(line[ri+1:].split(',')[1]))})
        
        
        json_data = {'tableName':'测试标注结果'}
        # 将两者数据进行求iou的共同区域>threshold=0.5 且种类相同则为正确预测
        for img_path in annotation_data:
            annotation = annotation_data[img_path]
            predict = predict_data.get(img_path, (-1, 0.0))

            json_data.update({img_path:{}})
            json_data[img_path].update({'dataset_annot':{}})
            json_data[img_path].update({'evaluate_annot':{}})
            json_data[img_path].update({'error_annot':{}})

            json_data[img_path]['dataset_annot'].update({'num':1})
            json_data[img_path]['dataset_annot'].update({'annotations':[]})

            json_data[img_path]['evaluate_annot'].update({'num':1})
            json_data[img_path]['evaluate_annot'].update({'annotations':[]})
            

            json_data[img_path]['dataset_annot']['annotations'].append({
                'code':annotation,
                'label':labels[annotation]
            })
            json_data[img_path]['evaluate_annot']['annotations'].append({
                'code':predict[0],
                'label':labels[predict[0]],
                'confidence':predict[1]
            })
        
        info['tables'].append(json_data)
        return info

        

        


    