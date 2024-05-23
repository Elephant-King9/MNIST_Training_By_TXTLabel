import os

from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms


class MyDataset(Dataset):
    def __init__(self, img_path, label_path, transform=None):
        self.img_path = img_path
        self.label_path = label_path
        data_path = os.path.join(self.img_path, 'training')
        self.transform = transform
        self.imgs = []
        for label in os.listdir(data_path):
            labels = os.path.join(data_path, label)
            if os.path.isdir(labels):
                for img in os.listdir(labels):
                    pre_img = os.path.join(labels, img)
                    self.imgs.append(pre_img)

    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, index):
        # ../datasets/mnist_png/training/.../1.png
        img = self.imgs[index]

        # 仅获取文件名
        # 1.png
        img_name = os.path.basename(img)
        img = Image.open(img).convert('L')
        if self.transform is not None:
            img = self.transform(img)
        # ../datasets/mnist_png/labels/1.txt
        label_dir = os.path.join(self.label_path, img_name.replace('.png', '.txt'))
        # 从文件中获取内容
        with open(label_dir, 'r') as f:
            label = f.read().strip()
        return img, label


if __name__ == '__main__':
    img_path = '../datasets/mnist_png'
    label_path = '../datasets/mnist_png/labels'
    dataset = MyDataset(img_path, label_path, transform=transforms.ToTensor())
    print(f'dataset[0]:\n{dataset[0]}')
