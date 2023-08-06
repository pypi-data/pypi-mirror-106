import numpy as np

class semanteme_division_cal(object):
    # 初始化数据
    def __init__(self, num_class):
        self.num_class = num_class
        self.confusion = np.zeros((self.num_class,) * 2)

    # 计算像素准确率（PA）
    # acc = (TP + TN) / (TP + TN + FP + TN)
    def Pixel_Accuracy(self):
        PA = np.diag(self.confusion).sum() / \
              self.confusion.sum()
        return PA

    # 计算平均像素准确率（MPA）
    # acc = (TP) / TP + FP
    def Pixel_Accuracy_Class(self):
        MPA_all = np.diag(self.confusion) / \
              self.confusion.sum(axis=1)
        # MPA = np.nanmean(MPA_all)
        return MPA_all

    # 计算平均交并比（MIou）
    # Iou = TP / (TP + FP + FN)
    def Mean_Intersection_Over_Union(self):
        MIou_all = np.diag(self.confusion) / (
                np.sum(self.confusion, axis=1) + np.sum(self.confusion, axis=0) -
                np.diag(self.confusion))
        # MIou = np.nanmean(MIou_all)
        return MIou_all

    # 计算频权交并比（FWIou）
    # FWIou = [(TP + FN)/(TP + FP + TN + FN)] * [TP / (TP + FP + FN)]
    def Frequency_Weighted_Intersection_Over_Union(self):
        freq = np.sum(self.confusion, axis=1) / \
               np.sum(self.confusion)
        iu = np.diag(self.confusion) / (
                np.sum(self.confusion, axis=1) + np.sum(self.confusion, axis=0) -
                np.diag(self.confusion))

        FWIou = (freq[freq > 0] * iu[freq > 0]).sum()
        return FWIou

    # 生成矩阵
    def generate_matrix(self, gt_image, pre_image):
        mask = (gt_image >= 0) & (gt_image < self.num_class)
        label = self.num_class * gt_image[mask].astype('int') + pre_image[mask]

        label = label.astype(int)

        count = np.bincount(label, minlength=self.num_class ** 2)
        confusion = count.reshape(self.num_class, self.num_class)
        return confusion

    # 设置混淆矩阵
    def set_confusion(self, gt_image, pre_image):
        assert gt_image.shape == pre_image.shape
        self.confusion += self.generate_matrix(gt_image, pre_image)

