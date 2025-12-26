import pandas as pd
import torch
import numpy as np
import random
from transformers import AutoTokenizer
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
import torch.nn as nn
import torch.optim as optim
from trainer import Trainer

def set_seeds(seed):
	random.seed(seed) #設定Python標準酷的亂數生成種子
	np.random.seed(seed) #設定Numpy亂數生成種子
	torch.manual_seed(seed) #設定Pytorch的CPU亂數種子
	if torch.cuda.is_available():
		torch.cuda.manual_seed(seed) #設定Pytorch在單個GPU上的亂數種子
		torch.cuda.manual_seed_all(seed) #設定Pytorch在所有GPU上的亂數種子
	
	torch.backends.cudnn.benchmark = False #禁用cuDNN的基準測試功能
	torch.backends.cudnn.deterministic = True #強制cuDNN使用確定性演算法

set_seeds(2526)	
#讀取CSV資料
df = pd.read_csv('imdb_data.csv')

#讀取文章、情緒欄位
reviews = df['review'].values
sentments = df['sentiment'].values

#將情緒資料轉換成數字資料
labels = (sentiments == 'positvie').astype('float32')

#讀取別人使用BPE斷詞所建立的Tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
input_datas = tokenizer(reviews[:2].tolist(), max_length=10, truncation=True, padding="longest", return_tensors='pt')

#觀看結果
print('Tokenizer輸出: ')
print(input_datas)




class IMDB(Dataset):
	def __init__(self, x, y, tokenizer):
		self.x = x
		self.y = y
		self.tokenizer = tokenizer
	
	def __getitem__(self, index):
		return self.x[index], self.y[index]
	
	def __len__(self):
		return len(self.x)
	
	def collate_fn(self, batch):
		batch_x, batch_y = zip(*batch)
		input_ids = self.tokenizer(batch_x, max_length=512, truncation=True, padding='longest', return_tensors='pt').input_ids[:, 1:-1] #移除[CLS]、[SEP]
		labels = torch.tensor(batch_y)
		return {'input_ids': input_ids, 'labels': labels}

#分割資料集
x_train, x_valid, y_train, y_valid = train_test_split(reviews, labels, train_size=0.8, random_state=46, shuffle=True)

#建立Dataset
trainset = IMDB(x_train, y_train, tokenizer)
testset = IMDB(x_valid, y_valid, tokenizer)

#DataLoader
train_loader = DataLoader(trainset, batch_size=32, shuffle=True, num_workers=0, pin_memory=True, collate_fn=trainset.collate_fn)
valid_loader = DataLoader(validset, batch_size=32, shuffle=True, num_workers=0, pin_memory=True, collate_fn=validset.collate_fn)



class TimeSeriesModel(nn.Module):
	def __init__(self, vocab_size, embedding_dim, hidden_size, padding_idx, num_layers=1, bidirection=True, model_type='LSTM'):
		super().__init__()
		self.criterion = nn.BCELoss() #定義損失函數
		self.embedding = nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)
		
		#切換模型
		rnn_models = {'LSTM': nn.LSTM, 'GRU': nn.GRU, 'RNN': nn.RNN}
		self.series_model = rnn_models.get(model_type, nn.LSTM)(
			embedding_dim,
			hidden_size,
			num_layers = num_layers,
			bidirectional = bidirectional, 
			batch_first = True
		)
		
		#如果是雙向運算，則最終的hidden_size會變成2倍
		hidden = hidden_size*2 if bidirectional else hidden_size
		
		self.fc = nn.Linear(hidden, 1)
		self.sigmoid = nn.Sigmoid()
		
	def forward(self, **kwarge):
		#取得輸入資料
		input_ids = kwargs['input_ids'] 
		labels = kwargs['labels']
		
		emb_out = self.embedding(input_ids) #轉換成詞嵌入向量
		
		#時間序列模型進行運算
		output, h_n = self.seires_model(emb_out) #output:(batch_size, seq_len, hidden_size*2)
		h_t = output[:, -1, :] #(batch_size, 1, hidden_size*2)
		y_hat = self.sigmoid(self.fc(h_t)) #(batch_size, 1)
		
		#回傳loss、logit
		return self.criterion(y_hat.view(-1), labels), y_hat

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#建立模型，並搬到設備上
model = TimeSeriesModel(
	vocab_size = len(tokenizer), 
	embedding_dim = 50, 
	hidden_size = 32, 
	model_type = 'LSTM',
	padding_idx = tokenizer.pad_token_id
).to(device)

#定義優化器
optimizer = optim.Adam(model.parameters(), lr=1e-3)


trainer = Trainer(
	epochs = 100, 
	train_loader = train_loader, 
	valid_loader = valid_loader,
	model = model, 
	optimizer = optimizer, 
	device = device
)

#讀取最佳的模型
model.load_state_dict(torch.load('model.ckpt'))

#切換成評估模式
model.eval()

total_correct = 0
total_samples = 0

with torch.no_grad():
	for input_data in valid_loader:
		input_datas = {k: v.to(device) for k, v in input_data.items()}
		_, logit = model(**input_datas)
		
		pred = (logit > 0.5).long() #將步林值轉換為整數(0、1)
		labels = input_datas['labels']
		
		total_correct += torch.sum(pred.view(-1) == labels).item()
		total_samples += labels.size(0)
		
accuracy = total_correct / total_samples
print(f'Validation Accuracy: {accuracy*100:.3d}%'}	
