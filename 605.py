#============ 605: 种花问题 =============#
'''
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。
示例 1:
输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
示例 2:
输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
注意:
数组内已种好的花不会违反种植规则。
输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。
'''
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        zero_counts = []
        counts = 0
        for n_ in flowerbed:
            if n_ == 0:
                counts += 1
            elif n_ == 1 and counts > 0:
                zero_counts.append(counts)
                counts = 0
            else:
                pass
        
        if counts > 0:
            zero_counts.append(counts)

        if zero_counts == []:
            if n == 0:
                return True
            else:
                return False
        elif len(zero_counts) == 1:
            if flowerbed[0] == 0:
                zero_counts[0] += 1
            if flowerbed[-1] == 0:
                zero_counts[-1] += 1
        else:
            if flowerbed[0] == 0:
                zero_counts[0] += 1
            if flowerbed[-1] == 0:
                zero_counts[-1] += 1

        max_f = 0
        for count in zero_counts:
            if count % 2 == 0:
                max_f += count // 2 - 1
            else:
                max_f += count // 2
        
        if n <= max_f:
            return True
        else:
            return False
        