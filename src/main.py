class Node:
 def __init__(self,k): self.k=k; self.l=self.r=None; self.h=1
class BST:
 def __init__(self): self.root=None
 def insert(self,k):
  c=0
  if not self.root:self.root=Node(k);return c
  n=self.root
  while 1:
   c+=1
   if k<n.k:
    if not n.l:n.l=Node(k);return c
    n=n.l
   elif k>n.k:
    if not n.r:n.r=Node(k);return c
    n=n.r
   else:return c
 def search(self,k):
  n=self.root;c=0
  while n:
   c+=1
   if n.k==k:return True,c
   n=n.l if k<n.k else n.r
  return False,c
 def height(self):
  def h(n):return 0 if not n else 1+max(h(n.l),h(n.r))
  return h(self.root)
 def walk(self,order):
  a=[]
  def f(n):
   if not n:return
   if order=='pre':a.append(n.k)
   f(n.l)
   if order=='in':a.append(n.k)
   f(n.r)
   if order=='post':a.append(n.k)
  f(self.root);return a
class AVL:
 def __init__(self):self.root=None
 def h(self,n):return n.h if n else 0
 def upd(self,n):n.h=1+max(self.h(n.l),self.h(n.r))
 def bf(self,n):return self.h(n.l)-self.h(n.r)
 def rr(self,y):
  x=y.l;t=x.r;x.r=y;y.l=t;self.upd(y);self.upd(x);return x
 def lr(self,x):
  y=x.r;t=y.l;y.l=x;x.r=t;self.upd(x);self.upd(y);return y
 def insert(self,k):
  c=[0]
  def add(n):
   if not n:return Node(k)
   c[0]+=1
   if k<n.k:n.l=add(n.l)
   elif k>n.k:n.r=add(n.r)
   else:return n
   self.upd(n);b=self.bf(n)
   if b>1 and k<n.l.k:return self.rr(n)
   if b< -1 and k>n.r.k:return self.lr(n)
   if b>1 and k>n.l.k:n.l=self.lr(n.l);return self.rr(n)
   if b< -1 and k<n.r.k:n.r=self.rr(n.r);return self.lr(n)
   return n
  self.root=add(self.root);return c[0]
 def search(self,k):
  n=self.root;c=0
  while n:
   c+=1
   if n.k==k:return True,c
   n=n.l if k<n.k else n.r
  return False,c
 def height(self):return self.h(self.root)
 def inorder(self):
  a=[]
  def f(n):
   if n:f(n.l);a.append(n.k);f(n.r)
  f(self.root);return a
class Hash:
 def __init__(self,m=67):self.t=[None]*m;self.collisions=0
 def insert(self,k):
  home=k%len(self.t); probes=0
  for i in range(len(self.t)):
   j=(home+i)%len(self.t)
   if self.t[j] is None:self.t[j]=k;return probes
   if self.t[j]==k:return probes
   probes+=1;self.collisions+=1
  raise Exception('table full')
 def search(self,k):
  home=k%len(self.t);c=0
  for i in range(len(self.t)):
   x=self.t[(home+i)%len(self.t)]
   if x is None:return False,c
   c+=1
   if x==k:return True,c
  return False,c
ids=[1042,1017,1093,1008,1064,1025,1111,1031,1078,1050,1003,1086,1022,1104,1047,1012,1069,1038,1099,1055,1006,1081,1029,1108,1044,1019,1072,1034,1090,1059,1001,1089,1020,1101,1049,1014,1061,1036,1096,1052]
b=BST();a=AVL();h=Hash()
for x in ids:b.insert(x);a.insert(x);h.insert(x)
print('Initial count:',len(ids),'Hash capacity:',len(h.t))
print('BST height:',b.height(),'AVL height:',a.height(),'Hash collisions:',h.collisions)
print('BST traversals inorder/preorder/postorder:',b.walk('in'),b.walk('pre'),b.walk('post'))
print('AVL inorder:',a.inorder())
for label,k in [('Successful',ids[17]),('Unsuccessful',9999)]:
 print(label,'ID',k)
 for name,s in [('BST',b),('AVL',a),('Hash',h)]:print(name,s.search(k))
print('Insertion experiment ID 1120')
print('BST insertion comparisons:',b.insert(1120),'AVL insertion comparisons:',a.insert(1120),'Hash collisions:',h.insert(1120))
for name,s in [('BST',b),('AVL',a),('Hash',h)]:print('After insert',name,s.search(1120))
print('Final heights BST/AVL:',b.height(),a.height())
