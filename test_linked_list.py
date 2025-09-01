from linked_list import LinkedList, ListNode


class TestLinkedList:
    """链表单元测试"""
    
    def setup_method(self):
        """每个测试方法前的设置"""
        self.ll = LinkedList()
    
    def test_init(self):
        """测试链表初始化"""
        assert self.ll.head is None
        assert self.ll.size == 0
        assert len(self.ll) == 0
        assert self.ll.is_empty()
    
    def test_append(self):
        """测试追加元素"""
        self.ll.append(1)
        assert self.ll.head.val == 1
        assert self.ll.size == 1
        assert len(self.ll) == 1
        assert not self.ll.is_empty()
        
        self.ll.append(2)
        assert self.ll.head.val == 1
        assert self.ll.head.next.val == 2
        assert self.ll.size == 2
    
    def test_prepend(self):
        """测试前置插入"""
        self.ll.prepend(1)
        assert self.ll.head.val == 1
        assert self.ll.size == 1
        
        self.ll.prepend(2)
        assert self.ll.head.val == 2
        assert self.ll.head.next.val == 1
        assert self.ll.size == 2
    
    def test_insert(self):
        """测试指定位置插入"""
        # 在空链表插入
        self.ll.insert(0, 1)
        assert self.ll.head.val == 1
        assert self.ll.size == 1
        
        # 在末尾插入
        self.ll.insert(1, 3)
        assert self.ll.get(1) == 3
        
        # 在中间插入
        self.ll.insert(1, 2)
        assert self.ll.to_list() == [1, 2, 3]
        
        # 测试边界条件
        try:
            self.ll.insert(-1, 0)
            assert False, "应该抛出IndexError"
        except IndexError:
            pass
        
        try:
            self.ll.insert(4, 0)
            assert False, "应该抛出IndexError"
        except IndexError:
            pass
    
    def test_delete(self):
        """测试删除元素"""
        # 从空链表删除
        assert not self.ll.delete(1)
        
        # 添加元素后删除
        for val in [1, 2, 3, 2, 4]:
            self.ll.append(val)
        
        # 删除头部元素
        assert self.ll.delete(1)
        assert self.ll.to_list() == [2, 3, 2, 4]
        
        # 删除中间元素
        assert self.ll.delete(3)
        assert self.ll.to_list() == [2, 2, 4]
        
        # 删除不存在的元素
        assert not self.ll.delete(5)
        
        # 删除重复元素（只删除第一个）
        assert self.ll.delete(2)
        assert self.ll.to_list() == [2, 4]
    
    def test_delete_at(self):
        """测试按索引删除"""
        for val in [1, 2, 3, 4, 5]:
            self.ll.append(val)
        
        # 删除头部
        self.ll.delete_at(0)
        assert self.ll.to_list() == [2, 3, 4, 5]
        
        # 删除中间
        self.ll.delete_at(1)
        assert self.ll.to_list() == [2, 4, 5]
        
        # 删除末尾
        self.ll.delete_at(2)
        assert self.ll.to_list() == [2, 4]
        
        # 测试边界条件
        try:
            self.ll.delete_at(-1)
            assert False, "应该抛出IndexError"
        except IndexError:
            pass
        
        try:
            self.ll.delete_at(2)
            assert False, "应该抛出IndexError"
        except IndexError:
            pass
    
    def test_find(self):
        """测试查找功能"""
        # 空链表查找
        assert self.ll.find(1) == -1
        
        # 添加元素后查找
        for val in [1, 3, 2, 3, 4]:
            self.ll.append(val)
        
        assert self.ll.find(1) == 0
        assert self.ll.find(3) == 1  # 返回第一个匹配
        assert self.ll.find(4) == 4
        assert self.ll.find(5) == -1  # 不存在
    
    def test_find_all(self):
        """测试查找所有匹配"""
        # 空链表
        assert self.ll.find_all(1) == []
        
        # 添加元素后查找
        for val in [1, 3, 2, 3, 4, 3]:
            self.ll.append(val)
        
        assert self.ll.find_all(1) == [0]
        assert self.ll.find_all(3) == [1, 3, 5]
        assert self.ll.find_all(5) == []
    
    def test_get(self):
        """测试按索引获取元素"""
        for val in [10, 20, 30, 40]:
            self.ll.append(val)
        
        assert self.ll.get(0) == 10
        assert self.ll.get(1) == 20
        assert self.ll.get(3) == 40
        
        # 测试边界条件
        try:
            self.ll.get(-1)
            assert False, "应该抛出IndexError"
        except IndexError:
            pass
        
        try:
            self.ll.get(4)
            assert False, "应该抛出IndexError"
        except IndexError:
            pass
    
    def test_contains(self):
        """测试包含检查"""
        assert not self.ll.contains(1)
        
        for val in [1, 2, 3]:
            self.ll.append(val)
        
        assert self.ll.contains(1)
        assert self.ll.contains(2)
        assert self.ll.contains(3)
        assert not self.ll.contains(4)
    
    def test_count(self):
        """测试元素计数"""
        assert self.ll.count(1) == 0
        
        for val in [1, 2, 1, 3, 1, 2]:
            self.ll.append(val)
        
        assert self.ll.count(1) == 3
        assert self.ll.count(2) == 2
        assert self.ll.count(3) == 1
        assert self.ll.count(4) == 0
    
    def test_clear(self):
        """测试清空链表"""
        for val in [1, 2, 3]:
            self.ll.append(val)
        
        assert not self.ll.is_empty()
        self.ll.clear()
        assert self.ll.is_empty()
        assert self.ll.head is None
        assert self.ll.size == 0
    
    def test_to_list(self):
        """测试转换为列表"""
        assert self.ll.to_list() == []
        
        values = [1, 2, 3, 4, 5]
        for val in values:
            self.ll.append(val)
        
        assert self.ll.to_list() == values
    
    def test_reverse(self):
        """测试反转链表"""
        # 空链表反转
        self.ll.reverse()
        assert self.ll.to_list() == []
        
        # 单个元素反转
        self.ll.append(1)
        self.ll.reverse()
        assert self.ll.to_list() == [1]
        
        # 多个元素反转
        self.ll.clear()
        for val in [1, 2, 3, 4, 5]:
            self.ll.append(val)
        
        self.ll.reverse()
        assert self.ll.to_list() == [5, 4, 3, 2, 1]
    
    def test_str_representation(self):
        """测试字符串表示"""
        assert str(self.ll) == "[]"
        
        self.ll.append(1)
        assert str(self.ll) == "1"
        
        self.ll.append(2)
        self.ll.append(3)
        assert str(self.ll) == "1 -> 2 -> 3"
    
    def test_iteration(self):
        """测试迭代功能"""
        values = [1, 2, 3, 4, 5]
        for val in values:
            self.ll.append(val)
        
        result = []
        for val in self.ll:
            result.append(val)
        
        assert result == values
    
    def test_length(self):
        """测试长度功能"""
        assert len(self.ll) == 0
        
        for i in range(5):
            self.ll.append(i)
            assert len(self.ll) == i + 1


class TestListNode:
    """链表节点测试"""
    
    def test_node_creation(self):
        """测试节点创建"""
        node = ListNode()
        assert node.val == 0
        assert node.next is None
        
        node2 = ListNode(5)
        assert node2.val == 5
        assert node2.next is None
        
        node3 = ListNode(10, node2)
        assert node3.val == 10
        assert node3.next == node2


def run_tests():
    """运行所有测试"""
    import sys
    
    # 简单的测试运行器
    test_class = TestLinkedList()
    node_test_class = TestListNode()
    
    test_methods = [method for method in dir(test_class) if method.startswith('test_')]
    node_test_methods = [method for method in dir(node_test_class) if method.startswith('test_')]
    
    passed = 0
    failed = 0
    
    print("运行链表测试...")
    print("=" * 50)
    
    # 运行链表测试
    for method_name in test_methods:
        try:
            test_class.setup_method()
            method = getattr(test_class, method_name)
            method()
            print(f"✓ {method_name}")
            passed += 1
        except Exception as e:
            print(f"✗ {method_name}: {e}")
            failed += 1
    
    # 运行节点测试
    for method_name in node_test_methods:
        try:
            method = getattr(node_test_class, method_name)
            method()
            print(f"✓ {method_name}")
            passed += 1
        except Exception as e:
            print(f"✗ {method_name}: {e}")
            failed += 1
    
    print("=" * 50)
    print(f"测试结果: {passed} 通过, {failed} 失败")
    
    if failed == 0:
        print("所有测试都通过了! 🎉")
    else:
        print(f"有 {failed} 个测试失败 ❌")
        sys.exit(1)


if __name__ == "__main__":
    run_tests()