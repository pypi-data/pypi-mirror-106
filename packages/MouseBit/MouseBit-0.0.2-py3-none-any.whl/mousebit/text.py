import torch
from torch.utils.data import Dataset, DataLoader

class BertDataset(torch.utils.data.Dataset):
    def __init__(self, text, response, tokenizer, max_len = 50):
        self.text = text.to_numpy()
        self.response = response.to_numpy()
        self.tokenizer = tokenizer
        self.maxlen = max_len
    
    def __len__(self):
        return len(self.text)
    
    def __getitem__(self, idx):
        tokens = self.tokenizer.batch_encode_plus([self.text[idx]],
                                                  max_length = self.maxlen,
                                                  pad_to_max_length = True,
                                                  truncation = True)
        
        return {
            'seq_id': torch.tensor(tokens['input_ids'][0], dtype = torch.long),
            'mask': torch.tensor(tokens['attention_mask'][0], dtype = torch.long),
            'target': torch.tensor(self.response[idx], dtype = torch.long)
        }

def get_dataloader(text, response, tokenizer, batch_size = 32, *args, **kwargs):
    dataset = BertDataset(text, response, tokenizer)
    return DataLoader(dataset, batch_size = batch_size, *args, **kwargs)