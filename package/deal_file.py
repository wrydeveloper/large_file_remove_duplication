import os
# 进行文件去重

class LargeFileRemoveDuplication:

    def __init__(self, oldfilepath, newfilepath, split_count=10, author='wry', temp_dir = 'temp_dir/'):
        self.oldfilepath = oldfilepath
        self.split_count  = split_count
        self.newfilepath = newfilepath
        self.author = author
        self.temp_dir = temp_dir

        handle_file, files = self.generate_file()
        self.calcu_hash(handle_file)
        self.close_file(handle_file)
        self.data_uniq(files)

    # tip1 生成分割保存的文件
    def generate_file(self):
        # files存储路径
        #
        handle_file, files = [], []
        temp_file_path_isexists = os.path.exists(self.temp_dir)
        if not temp_file_path_isexists:
            os.makedirs(self.temp_dir)

        for i in range(self.split_count):
            dir = self.temp_dir + 'split_' + str(i)
            files.append(dir)
            f = open(dir, 'w')
            handle_file.append(f)

        return handle_file, files

    # tip2把内容分摊到各个文件
    def calcu_hash(self,  handle_file):
        with open(self.oldfilepath, 'r') as f:
            for line in f:
                handle_file[hash(line)%self.split_count-1].write(line)

    # tip3 把各个文件关闭
    def close_file(self, handle_file):
        for i in range(len(handle_file)):
            handle_file[i].close()

    # tip4 从各个文件中读取，去重
    def data_uniq(self, files):
        dataset = dict()
        new_file = open(self.newfilepath, 'w')
        for filename in files:
            f = open(filename, 'r')
            for line in f:
                dataset[line] = 1

            f.close()
            for key in dataset.keys():
                new_file.write(key)

            dataset = {}

        new_file.close()