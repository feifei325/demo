class ListNode:
    """链表节点类"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    """链表类，支持基本操作和查询功能"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, val):
        """在链表末尾添加元素"""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, val):
        """在链表开头添加元素"""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert(self, index, val):
        """在指定位置插入元素"""
        if index < 0 or index > self.size:
            raise IndexError("索引超出范围")
        
        if index == 0:
            self.prepend(val)
            return
        
        new_node = ListNode(val)
        current = self.head
        for i in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete(self, val):
        """删除第一个匹配的元素"""
        if not self.head:
            return False
        
        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def delete_at(self, index):
        """删除指定位置的元素"""
        if index < 0 or index >= self.size:
            raise IndexError("索引超出范围")
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        
        current = self.head
        for i in range(index - 1):
            current = current.next
        
        current.next = current.next.next
        self.size -= 1
    
    def find(self, val):
        """查找元素，返回第一个匹配的索引"""
        current = self.head
        index = 0
        
        while current:
            if current.val == val:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def find_all(self, val):
        """查找所有匹配的元素，返回索引列表"""
        indices = []
        current = self.head
        index = 0
        
        while current:
            if current.val == val:
                indices.append(index)
            current = current.next
            index += 1
        
        return indices
    
    def get(self, index):
        """获取指定位置的元素"""
        if index < 0 or index >= self.size:
            raise IndexError("索引超出范围")
        
        current = self.head
        for i in range(index):
            current = current.next
        
        return current.val
    
    def contains(self, val):
        """检查链表是否包含指定元素"""
        return self.find(val) != -1
    
    def count(self, val):
        """统计指定元素出现的次数"""
        count = 0
        current = self.head
        
        while current:
            if current.val == val:
                count += 1
            current = current.next
        
        return count
    
    def is_empty(self):
        """检查链表是否为空"""
        return self.head is None
    
    def length(self):
        """获取链表长度"""
        return self.size
    
    def clear(self):
        """清空链表"""
        self.head = None
        self.size = 0
    
    def to_list(self):
        """将链表转换为Python列表"""
        result = []
        current = self.head
        
        while current:
            result.append(current.val)
            current = current.next
        
        return result
    
    def reverse(self):
        """反转链表"""
        prev = None
        current = self.head
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        self.head = prev
    
    def __str__(self):
        """字符串表示"""
        if not self.head:
            return "[]"
        
        result = []
        current = self.head
        while current:
            result.append(str(current.val))
            current = current.next
        
        return " -> ".join(result)
    
    def __len__(self):
        """支持len()函数"""
        return self.size
    
    def __iter__(self):
        """支持迭代"""
        current = self.head
        while current:
            yield current.val
            current = current.next


def demo():
    """链表使用示例"""
    print("=== 链表查询功能演示 ===\n")
    
    # 创建链表
    ll = LinkedList()
    
    # 添加元素
    print("1. 添加元素:")
    for val in [1, 3, 2, 3, 4, 3, 5]:
        ll.append(val)
    print(f"链表内容: {ll}")
    print(f"链表长度: {len(ll)}\n")
    
    # 查询操作
    print("2. 查询操作:")
    search_val = 3
    
    # 查找第一个匹配
    first_index = ll.find(search_val)
    print(f"查找值 {search_val} 的第一个位置: {first_index}")
    
    # 查找所有匹配
    all_indices = ll.find_all(search_val)
    print(f"查找值 {search_val} 的所有位置: {all_indices}")
    
    # 检查是否包含
    contains = ll.contains(search_val)
    print(f"链表是否包含 {search_val}: {contains}")
    
    # 统计出现次数
    count = ll.count(search_val)
    print(f"值 {search_val} 出现的次数: {count}")
    
    # 获取指定位置的元素
    index = 2
    value_at_index = ll.get(index)
    print(f"索引 {index} 处的值: {value_at_index}\n")
    
    # 其他操作
    print("3. 其他操作:")
    print(f"链表是否为空: {ll.is_empty()}")
    print(f"转换为列表: {ll.to_list()}")
    
    # 迭代
    print("迭代链表:", end=" ")
    for val in ll:
        print(val, end=" ")
    print("\n")
    
    # 反转链表
    print("4. 反转链表:")
    print(f"反转前: {ll}")
    ll.reverse()
    print(f"反转后: {ll}")


if __name__ == "__main__":
    demo()