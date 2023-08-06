
'''
样例
func_map = {
    'omc':{
        'path1':[函数对象,timeout],
        'path2':[函数对象,timeout]
    },
    'ofc':{
        'path1':[函数对象,timeout]
    }
}
'''


class FMap:
    def __init__(self):
        self.func_map = {}

    def add_map(self,app,path,func,timeout):
        if app not in self.func_map:
            self.func_map[app]= {path:[func,timeout]}
        else:
            t_dict = self.func_map[app]
            t_dict[path]=[func,timeout]
            self.func_map[app] = t_dict


    def get_map(self):
        return self.func_map





fm = FMap()