import torch
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split

class FetchDataset(Dataset):
    def __init__(self, X, Y, x_dtype = torch.float32, y_dtype = torch.float32):
        self.X = X
        self.Y = Y
        self.x_dtype = x_dtype
        self.y_dtype = y_dtype

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return {
            'x' : torch.tensor(self.X[idx], dtype = self.x_dtype),
            'y' : torch.tensor(self.Y[idx], dtype = self.y_dtype)
        }

def get_dataloader(X, Y, batch_size = 32, *args, **kwargs):
    dataset = FetchDataset(X, Y)
    return DataLoader(dataset, batch_size = batch_size, *args, **kwargs)

def get_dataloader_splits(X, Y, test_size = 0.25, random_state = 0, stratify_on_y = True, batch_size = 32, valid_split = False, test_to_valid_ratio = 0.3, *args, **kwargs):
    if stratify_on_y:
        x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state = random_state, stratify = Y, test_size = test_size)
    else:
        x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state = random_state, test_size = test_size)
    
    train_dataset = FetchDataset(x_train, y_train)
    trainloader = DataLoader(train_dataset, batch_size = batch_size, *args, **kwargs)

    if valid_split:
        x_valid, x_test, y_valid, y_test = train_test_split(x_test, y_test, random_state = random_state, test_size = test_to_valid_ratio, stratify = y_test)

        valid_dataset = FetchDataset(x_valid, y_valid)
        validloader = DataLoader(valid_dataset, batch_size = batch_size, *args, **kwargs)

        test_dataset = FetchDataset(x_test, y_test)
        testloader = DataLoader(test_dataset, batch_size = batch_size, *args, **kwargs)
        return trainloader, validloader, testloader

    else:
        test_dataset = FetchDataset(x_test, y_test)
        testloader = DataLoader(test_dataset, batch_size = batch_size, *args, **kwargs)
        return trainloader, testloader