def aSao(start_node, stop_node):
 
        open_set = set(start_node) 
        closed_set = set()
        g = {} #Lưu trữ khoảng cách từ nút bắt đầu
        parents = {}#nút cha của nút con
 
        #khoảng cách của nút bắt đầu từ chính nó là 0
        g[start_node] = 0
        #start_node là nút gốc, không có nút cha
        #vì vậy start_node được đặt thành nút cha của chính nó
        parents[start_node] = start_node
         
         
        while len(open_set) > 0:
            n = None
 
            #nút có f() thấp nhất được tìm thấy
            for v in open_set:
                if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                    n = v
             
                     
            if n == stop_node or Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):
                    #các nút 'm' không có trong tập hợp đầu tiên và cuối cùng được thêm vào đầu tiên
                    #n được đặt là cha của nó
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight
                         
     
                    #đối với mỗi nút m, hãy so sánh khoảng cách của nó từ điểm bắt đầu, tức là g (m) đến
                    #từ đầu đến nút n
                    else:
                        if g[m] > g[n] + weight:
                            #update g(m)
                            g[m] = g[n] + weight
                            #thay đổi cha của m thành n
                            parents[m] = n
                             
                            #nếu m ở trong tập hợp đóng, hãy xóa và thêm vào để mở
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
 
            if n == None:
                print('Tìm kiếm thất bại')
                return None
 
            # nếu nút hiện tại là stop_node
            # sau đó bắt đầu tạo lại đường dẫn từ nó đến start_node
            if n == stop_node:
                path = []
 
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
 
                path.append(start_node)
 
                path.reverse()
 
                print('Tìm kiếm thành công: {}'.format(path))

                return path
 
 
            # xóa n khỏi open_list và thêm nó vào closed_list
            # bởi vì tất cả những get_neighbors xung quanh nút đó đã được kiểm tra
            open_set.remove(n)
            closed_set.add(n)
 
        print('Tìm kiếm thất bại')
        return None
         
#xác định hàm để trả về get_neighbors và khoảng cách của nó
#từ nút đã qua
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
#coi khoảng cách heuristic đã cho
#và hàm này trả về khoảng cách heuristic cho tất cả các nút
def heuristic(n):
        H_dist = {
            'A': 6,
            'B': 3,
            'C': 4,
            'D': 5,
            'E': 3,
            'F': 1,
            'G': 6,
            'H': 2,
            'I': 5,
            'J': 4,
            'K': 2,
            'L': 0,
            'M': 4,
            'N': 0,
            'O': 4,
        }
 
        return H_dist[n]
 
#Mô tả đồ thị
Graph_nodes = {
    'A': [('B', 2), ('C', 1) , ('D', 3)],
    'B': [('E', 1),('F', 4)],
    'C': [('G', 6),('H', 3)],
    'D': [('I', 2),('J', 4)],
    'E': None,
    'F': [('K', 2), ('L', 1) , ('M', 4)],
    'G': None,
    'H': [('N', 2),('O', 4)],
    'I': None,
    'J': None,
    'K': None,    
    'L': None,
    'M': None,
    'N': None,       
    'O': None,
}
aSao('A', 'O')
