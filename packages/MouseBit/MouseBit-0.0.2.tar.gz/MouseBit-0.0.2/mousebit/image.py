import cv2
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Dataset
from sklearn.model_selection import train_test_split

class ImageClassificationDataset(Dataset):
    def __init__(self, image_paths, targets, transform, img_dtype = torch.float32, y_dtype = torch.float32):
        self.paths = image_paths
        self.targets = targets
        self.transform = transform

        self.img_dtype = img_dtype
        self.y_dtype = y_dtype

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, idx):
        target = self.targets[idx]

        image = cv2.imread(self.paths[idx])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = self.transform(image = image)['image']

        return {
            'x' : torch.tensor(image),
            'y' : torch.tensor(target, dtype = self.y_dtype)
        }

def get_dataloader(image_paths, y = None, batch_size = 32, transform = None, method = 'folder', *args, **kwargs):
    if method == 'folder':
        if transform is None:
            transform = transforms.Compose([
                transforms.ToTensor()
            ])
        
        dataset = datasets.ImageFolder(image_paths, transform = transform, *args, **kwargs)
        return DataLoader(dataset, batch_size = batch_size, *args, **kwargs)
    
    elif method == 'path':
        if transform is None:
            import albumentations as A
            from albumentations.pytorch import ToTensorV2
            
            transform = A.Compose([
                ToTensorV2()
            ])

        if y is None:
            raise Exception('None Y Exception: Please pass a valid target values with method = "path"')
        
        dataset = ImageClassificationDataset(image_paths, y, transform = transform)
        return DataLoader(dataset, batch_size = batch_size, *args, **kwargs)