import json
from .calculate import *

class EvalOut(object):
    """
    gt_image: numpy矩阵数据的真实标签 n*H*W n为数量 标签为 0~(n-1) (带背景)
    pre_image: numpy矩阵与gt_image对应的预测结果，同为 n*H*W n为数量 标签为 0~(n-1) (带背景)
    num_class: 类别数量
    class_name: 类别名 字典结构 {int（0-（n-1））：String，int：String}
    save_path: json文件存储路径
    """
    # 初始化数据
    def __init__(self, gt, pre, num_class, class_name, save_path):
        gt_image = None
        pre_image = None
        for i in range(len(pre)):
            if i == 0:
                pre_image = pre[i]
                gt_image = gt[i]
            else:
                pre_image = np.concatenate((pre_image,pre[i]),axis=0)
                    # torch.cat((pre_image, pre[i]), 0)
                gt_image = np.concatenate((gt_image,gt[i]),axis=0)
                    # torch.cat((gt_image, gt[i]), 0)
        self.gt_image = gt_image
        self.pre_image = pre_image
        self.num_class = num_class
        self.class_name = class_name
        self.save_path = save_path

    # 评估预测结果
    def getEvaluate(self):
        return self.calToJson(self.gt_image, self.pre_image, self.num_class)

    # 计算指标输出为Json
    def calToJson(self, gt_image, pre_image, num_class):
        cal = semanteme_division_cal(num_class)
        cal.set_confusion(gt_image, pre_image)

        PA = cal.Pixel_Accuracy()

        MPA_all = cal.Pixel_Accuracy_Class()
        # print(MPA_all)
        MPA = np.nanmean(MPA_all)

        MIou_all = cal.Mean_Intersection_Over_Union()
        # print(MIou_all)
        MIou = np.nanmean(MIou_all)

        FWIou = cal.Frequency_Weighted_Intersection_Over_Union()

        self.PA = PA
        self.MPA_all = MPA_all
        self.MPA = MPA
        self.MIou_all = MIou_all
        self.MIou = MIou
        self.FWIou = FWIou
        return PA, MPA_all, MPA, MIou_all, MIou, FWIou

    # 输出为Json文件
    def save(self):
        self.getEvaluate()

        jsonpath = self.save_path
        jsonobj = open(jsonpath, 'w')
        contjson = {}
        contjson["tables"] = []
        table = {}
        table["tableName"] = "像素准确率；平均像素准确率；平均交并比；频权交并比"
        table["all_class"] = {"PA": self.PA, "MPA": self.MPA, "MIou": self.MIou, "FWIou": self.FWIou}
        for i in range(len(self.MPA_all)):
            table[self.class_name[i]] = {"PA": self.MPA_all[i], "MPA": None, "MIou": self.MIou_all[i], "FWIou": None}
        contjson["tables"].append(table)
        json.dump(contjson, jsonobj)

