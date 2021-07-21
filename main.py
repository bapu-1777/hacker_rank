class node:
    def init(self,data):
        self.data=data
        self.next=None
class ssl:
    def init(self):
        self.head=None
    def tra(self):
        if self.head==None:
            print("emty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" --> ")
                n=n.next
    def add_begin(self,data):
        n_node=node(data)
        n_node.next=self.head
        self.head=n_node
    def add_last(self,data):
        n_node=node(data)
        if self.head is None:
            self.head=n_node
        else:
            n = self.head
            while n.next is not None:
                n=n.next
            n.next=n_node
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.next
        if n is None:
            print("node is not present")
        else:
            n_node=node(data)
            n_node.next=n.next
            n.next=n_node
    def add_before(self,data,x):
        n = self.head
        if n.data==x:
            n_node=node(data)
            n_node.next=self.head
            self.head=n_node
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("node is not present")
        else:


ll1=ssl()
ll1.add_begin(10)
ll1.add_last(20)
ll1.add_begin(100)
ll1.add_after(5000,100)
ll1.tra()