class Node: 
	def __init__(self, value=0, next=None):
		self.value = value
		self.next = next

class LinkedList(object): 
    def __init__(self):
        self.head = None
        self.tail = None
        self.next = None
        self.len = 0
        
    def append(self, value): # O(n)
        new_node = Node(value)
        self.len += 1
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while (current.next):
                current = current.next
            current.next = new_node
            self.tail = new_node
        
    def get(self, idx): # O(n)
        current = self.head
        for _ in range(idx):
            current = current.next
    
        return current.value
    
    def insert_at(self, idx, value): # O(n)
        new_node = Node(value)
        
        if self.head is None: # 링크드리스트가 비어있을 때
            self.head = new_node
            self.tail = new_node
            
        elif idx > self.len: # 범위 바깥에 삽입할 때
            print('링크드리스트의 범위를 벗어났습니다.\n')
            
        elif idx == self.len: # 리스트의 끝에 삽입할 때
            self.tail.next = new_node
            self.tail = new_node
            
        else: # 연산이 정상적으로 이루어질 때
            current = self.head
            for _ in range(idx-1):
                current = current.next
            
            tmp = current # 이전 노드 저장
            current = current.next # 다음 노드 이동
            new_node.next = current # 새 노드를 다음 노드에 연결
            tmp.next = new_node # 이전 노드를 새 노드에 연결
        
        
    def remove_at(self, idx): # O(n)

        if self.head is None:
            print('삭제할 노드가 없습니다.\n')
            
        elif idx == 0:
            self.head = self.head.next
            self.len -= 1
            
        elif idx >= self.len:
            print('링크드리스트의 범위를 벗어났습니다.\n')
            
        else:
            current = self.head
            
            for _ in range(idx-1):
                current = current.next # 삭제 이전 노드까지 이동

            if current.next.next is None: # 마지막 노드를 삭제하는 경우 tail 업데이트
                self.tail = current
                
            current.next = current.next.next # 삭제 다음 노드를 바로 연결
            self.len -= 1
        
    def insert_back(self, value): # O(1)
        new_node = Node(value)
        self.len += 1
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
    
    def remove_back(self):
        if self.head is None:
            print('삭제할 노드가 없습니다.')
        
        if self.head.next is None:  # 리스트에 노드가 하나만 있는 경우
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next.next:  # 마지막에서 두 번째 노드까지 이동
                current = current.next
            current.next = None  # 마지막 노드 삭제
            self.tail = current  # 새로운 tail 업데이트
        self.len -= 1
                

    def print(self, idx = 0):
        print("====== Linked List ======")
        current = self.head
        while(current):
            if current.next is not None :
                str_value = str(current.value)
                str_next = str(current.next)[-12:-1]
            else :
                str_value = str(current.value)
                str_next = str(current.next)
            print(" Node(" + str_value + ")=", end='')
            print("(" + str_value + "," + str_next + ")")
            current = current.next
        print("=========================\n")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.print()

ll.insert_at(idx=8, value=9)
ll.print()


ll.insert_at(idx=1, value=9)

ll.print()