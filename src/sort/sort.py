
class sort:
    """
    排序算法类，包括选择排序、冒泡排序、插入排序、归并排序等排序算法
    """
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def bubble_sort(src_list: list) -> None:
        """
        冒泡排序, 加入提前结束标志
        :param src_list: 被排序列表
        :return: 直接在src_list改变列表顺序，无返回值
        """
        for i in range(len(src_list)):
            exchange_flag = False
            for j in range(len(src_list) - i - 1):
                if src_list[j] > src_list[j + 1]:
                    src_list[j], src_list[j+1] = src_list[j+1], src_list[j]
                    exchange_flag = True
            if not exchange_flag:
                break

    @staticmethod
    def select_sort(src_list: list) -> None:
        """
        选择排序，每次选择一个最小值放到当前位置
        :param: src_list: 被排序列表
        :return: 直接在src_list改变列表顺序，无返回值
        """
        for i in range(len(src_list) - 1):
            value = src_list[i]
            index = i
            for j in range(i+1, len(src_list)):
                if value > src_list[j]:
                    value = src_list[j]
                    index = j
            src_list[i], src_list[index] = src_list[index], src_list[i]

    @staticmethod
    def insert_sort(src_list: list, sorted_num: int) -> None:
        """
        插入排序，增量方法
        :param src_list: 被排序列表
        :param sorted_num: 已排序数量
        :return: 直接在src_list改变列表顺序，无返回值
        """
        for i in range(sorted_num, len(src_list)):
            key = src_list[i]
            j = i - 1
            while j >= 0 and src_list[j] > key:
                src_list[j+1] = src_list[j]
                j -= 1
            src_list[j+1] = key

    @staticmethod
    def merge(src_list: list, p: int, q: int, r: int) -> None:
        """
        数组归并
        :param src_list: 被归并列表
        :param p: left数组起始index
        :param q: left数组结束index，q+1: right数组起始index
        :param r: right数组结束index
        :return: 在scr_list做归并操作，无返回值
        """
        left = [src_list[i] for i in range(p, q+1)]
        right = [src_list[i] for i in range(q+1, r+1)]
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                src_list[p+i+j] = right[j]
                j += 1
            else:
                src_list[p+i+j] = left[i]
                i += 1
        if i < len(left):
            for k in range(0, len(left) - i):
                src_list[p+i+j+k] = left[i+k]
        else:
            for k in range(0, len(right) - j):
                src_list[p+i+j+k] = right[j+k]



    @staticmethod
    def merge_sort(scr_list: list, p: int, r: int) -> None:
        """
        归并排序
        :param scr_list: 被排序列表
        :param p: 要排序段的起始index
        :param r: 要排序段的结束index
        :return: 直接在scr_list修改数组，无返回值
        """
        if p < r:
            q = (p + r) // 2
            sort.merge_sort(scr_list, p, q)
            sort.merge_sort(scr_list, q+1, r)
            sort.merge(scr_list, p, q, r)


if __name__ == "__main__":
    insert = [31, 41, 59, 26, 41, 58]
    bubble = insert.copy()
    select = insert.copy()
    merge = insert.copy()
    sort.insert_sort(insert, 3)
    print('insert sort: ', insert)
    sort.bubble_sort(bubble)
    print('bubble sort: ', bubble)
    sort.bubble_sort(select)
    print('select sort: ', select)
    sort.merge_sort(merge, 0, 5)
    print('merge sort: ', merge)
