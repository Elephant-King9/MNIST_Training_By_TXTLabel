import os
for i in range(10):
    # 文件夹路径
    folder_path = f'../datasets/mnist_png/training/{i}'
    # 生成的txt文件保存路径
    output_folder = '../datasets/mnist_png/labels'

    # 获取文件夹中的所有文件名
    file_list = os.listdir(folder_path)

    # 遍历文件名列表
    for filename in file_list:
        # 构造txt文件名，与图片名称一致但扩展名为.txt
        txt_filename = filename.split('.')[0] + '.txt'

        # 文件夹名称就是txt文件内容
        content = folder_path.split('/')[-1]

        # 写入txt文件
        with open(os.path.join(output_folder, txt_filename), 'w') as file:
            file.write(content)