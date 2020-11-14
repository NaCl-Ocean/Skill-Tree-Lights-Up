import numpy as np

class TreeNode:
    def __init__(self, ndims, vector, left=None, right=None):
        self.ndims = ndims
        self.vector = vector
        self.left = left
        self.right = right
    

class KdTree:
    def __init__(self, vectors, k, ndim=1,ord=None):
        self.vectors = vectors
        self.root = None
        self.ndims = ndim
        self.ord = ord
        self.k = k
        self._construt_kdtree(dim=1,vectors = self.vectors,node=None,dir=None)
    

    def _construt_kdtree(self, dim, vectors, node, dir):
        # 直到区域中没有实例点时，停止
        if vectors.shape[0] == 0:
            return
        
        n_median = np.median(vectors[:,dim-1])
        min_dis_index = np.argmin(np.abs(vectors[:,dim-1]-n_median))
        current_node = TreeNode(ndims=self.ndims, vector=vectors[min_dis_index,:])
        if node is not None:
            if dir == 'left':
                node.left = current_node
            else:
                node.right  = current_node
        else:
            # root node
            self.root = current_node

        n_median = vectors[min_dis_index,dim-1]
        left_points = vectors[vectors[:,dim-1]<n_median,:]
        right_points = vectors[vectors[:,dim-1]>n_median,:]
        if dim==self.ndims:
            dim = 1
        
        self._construt_kdtree(dim+1,vectors=left_points,node=current_node,dir='left')
        self._construt_kdtree(dim+1, vectors=right_points, node=current_node,dir='right')


    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        print(root.vector)
        self._inorder(root.right)
    
    def inorder(self):
        self._inorder(self.root)

    
    
    def search_nearsetpoint(self, root, target, dim, nearsetpoint):

        if root.right is None and root.left is None and nearsetpoint is None:
            return root
        
        if root.right is None and root.left is None and nearsetpoint is not None:
            current_distance = np.linalg.norm(target-root.vector,ord=self.ord)
            nearest_distance = np.linalg.norm(target-nearsetpoint.vector,ord=self.ord)
            if nearest_distance > current_distance:
                return root
            else:
                return nearsetpoint

        if dim == self.ndims:
            next_dim = 1
        else:
            next_dim = dim + 1
        
        if target[dim-1] < root.vector[dim-1]:
            nearsetpoint = self.search_nearsetpoint(root.left, target, next_dim, nearsetpoint)
        else:
            nearsetpoint = self.search_nearsetpoint(root.right, target, next_dim, nearsetpoint)
        
        # if current distance < nearset distance, then nearset point is current point
        current_distance = np.linalg.norm((root.vector-target),self.ord)
        nearset_distance = np.linalg.norm((nearsetpoint.vector-target),self.ord)
        if current_distance < nearset_distance:
            nearsetpoint = root
            nearset_distance = current_distance
        split_distance = np.abs(target[dim-1]-root.vector[dim-1])
        if split_distance > nearset_distance:
            return nearsetpoint
        else:
            if target[dim-1] < root.vector[dim-1]:
                nearsetpoint_ = self.search_nearsetpoint(root.left, target, next_dim, nearsetpoint)
            else:
                nearsetpoint_ = self.search_nearsetpoint(root.right, target, next_dim, nearsetpoint)
            current_distance_ = np.linalg.norm((nearsetpoint_.vector-target),self.ord)
            if current_distance_ < nearset_distance:
                return nearsetpoint_
            else:
                return nearsetpoint
        return nearsetpoint

    
    
    
    def searchTree(self,root,target,mode='nearest'):
        assert mode in ['nearest','nearest_k']
        if mode == 'nearest':
            nearsetpoint = self.search_nearsetpoint(self.root,target = target,dim=1, nearesetpoint=None)
            return nearsetpoint
        else:
            k_nearsetpoints = []
            k_nearsetpoints= self.search_k_neighbor(self.root, target, 
                                                    dim=1, nearestpoints = k_nearsetpoints)
            return k_nearsetpoints

    def search_k_neighbor(self, root, target, dim, nearestpoints):
        if root.left is None and root.right is None:
            if len(nearestpoints) < self.k:
                nearestpoints.append(root)
            if len(nearestpoints) >= self.k:
                max_nearsetpoints_distance, max_distance_index = self.get_max_distance(
                                                                        nearestpoints, target)
                current_distance = np.linalg.norm(target-root.vector,self.ord)
                if current_distance < max_nearsetpoints_distance:
                    nearestpoints[max_distance_index] = root
            return nearestpoints
        
        if dim == self.ndims:
            next_dim = 1
        else:
            next_dim = dim + 1
        
        if target[dim-1] < root.vector[dim-1]:
            nearsetpoints = self.search_k_neighbor(root.left, target, next_dim, nearsetpoints)
        else:
            nearsetpoints = self.search_k_neighbor(root.right, target, next_dim, nearsetpoints)
        
        if len(nearestpoints) < self.k:
            nearestpoints.append(root)
        else:
            current_distance = np.linalg.norm((root.vector-target),self.ord)
            max_nearsetpoints_distance, max_distance_index = self.get_max_distance(nearestpoints, target)
            if current_distance < max_nearsetpoints_distance:
                nearsetpoints[max_distance_index] = root
        
    
        max_nearsetpoints_distance,_ = self.get_max_distance(nearsetpoints,target)
        split_distance = np.abs(target[dim-1]-root.vector[dim-1])
        if split_distance > max_nearsetpoints_distance:
            return nearsetpoints
        else:
            if target[dim-1] < root.vector[dim-1]:
                nearsetpoints = self.search_k_neighbor(root.left, target, next_dim, nearsetpoints)
            else:
                nearestpoints = self.search_k_neighbor(root.right, target, next_dim, nearsetpoints)
            return nearestpoints
            
            


    def get_max_distance(self,nearestpoints, target):
        nearsetpoints_vector = np.concatenate([node.vector for node in nearestpoints])
        nearestpoints_distance = np.linalg.norm(nearsetpoints_vector-target,ord=self.ord)
        max_nearsetpoints_distance = np.max(nearestpoints_distance)
        max_nearsetpoint_index = np.argmax(nearestpoints_distance)
        return max_nearsetpoints_distance, max_nearsetpoint_index
        

if __name__ == '__main__':
    vectors = np.array([[7,2],[2,3],[9,6],[4,7],[8,1],[5,4]])
    kdtree = KdTree(vectors,k=2, ndim=2)
    node = kdtree.root
    #kdtree.inorder()
    nearsetpoint = kdtree.searchTree(kdtree.root, np.array([3,4.5]))
    print(f'nearsetpoint:{nearsetpoint.vector}')
    
    

