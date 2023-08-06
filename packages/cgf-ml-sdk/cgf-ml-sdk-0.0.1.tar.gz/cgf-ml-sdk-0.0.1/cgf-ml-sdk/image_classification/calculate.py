import numpy as np

# 计算混淆矩阵
def confusion_matrix(real_ann_path, pred_ann_path, classes):
    class_nums = len(classes)
    matrix = np.zeros((class_nums, class_nums))
    file_lists = [['' for _ in range(class_nums)] for _ in range(class_nums)]
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
            predict_data.update({line[:ri]:int(line[ri+1:].split(',')[0])})
            # print(predict_data[line[0]])

    with open(real_ann_path, 'r') as real_annotation:
        for real_i, line in enumerate(real_annotation):
            ri = line.rstrip().rfind(' ')
            image_path = line[:ri]

            y_true = annotation_data[image_path]
            y_pred = predict_data[image_path]
            if y_true >= 195:
                continue
            matrix[y_pred][y_true] += 1
            if real_i > 0:
                file_lists[y_pred][y_true] += ','
            file_lists[y_pred][y_true] += str(image_path).replace('/home/ml_space', '{workspace}')

    return matrix, file_lists



# 绘制混淆矩阵，计算指标，写入文本
def save_result(real_ann_path, pred_ann_path, classes, beta=1):
    matrix, file_lists = confusion_matrix(real_ann_path, pred_ann_path, classes)
    tables = []
    table = {"tableName": "查准率，查全率，F1值，精确值，平均精度"}
    for index in range(len(classes)):
        label = classes[index]
        if matrix[index][index] == 0:
            precision = 0
            recall = 0
            f_beta = 0
            accuaracy = 0
        else:
            precision = matrix[index][index] / sum(matrix[index])
            recall = matrix[index][index] / sum(matrix)[index]
            f_beta = (1 + beta * beta) * precision * recall / (beta * beta * precision + recall + 0.00001)
            accuaracy = matrix[index][index] / (sum(matrix[index]) + sum(matrix)[index] - matrix[index][index])
        res_dic = {"precision": precision,
                   "recall": recall,
                   "F1_score": f_beta,
                   "accuaracy": accuaracy}
        table[label] = res_dic
    tables.append(table)
    # 混淆矩阵绘制
    table = {"tableName": "混淆矩阵"}
    i = 0
    for i in range(len(matrix)):
        row = matrix[i]
        label = classes[i]
        key = 'predict_' + label
        res_dic = {}
        for j in range(len(row)):
            num = row[j]
            label = classes[j]
            data = {'num': int(num), 'fileList': sorted(list(set(file_lists[i][j].split(','))))}
            res_dic['real_' + label] = data

        table[key] = res_dic
        i += 1
    tables.append(table)
    result = {"tables": tables}
    return result


if __name__ == '__main__':

    # evaluation(matrix, ['car', 'swimming pool'])
    result = save_result('../data/dataset/test.txt', '../data/dataset/1588671934.969735.txt',
                         'plane,ship,storage-tank,baseball-diamond,tennis-court,basketball-court,ground-track-field,harbor,bridge,large-vehicle,small-vehicle,helicopter,roundabout,soccer-ball-field,swimming-pool'.split(','))
    # print(result)
