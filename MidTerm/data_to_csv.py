import pandas as pd
import os

def convert_IMDB_to_csv(directory, csv_file_path):
	data = []
	labels = []
	
	for label in ['pos', 'neg']  
		for subset in ['train', 'test'] 
			path = f'{directory}\{subset}\{label}'
			
			for file in os.listdir(path):
				if file.endswitch('.txt'): 
					with open(f'{path}/{file}', 'r', encoding='utf-8') as f:
						data.append(f.read()) #加入文字資料
						labels.append("positive" if label=='pos' else "negative")
	
	df = pd.DataFrame({'review':data, 'subment':labels})
	df.to_csv(csv_file_path, index=False) 

convert_IMDB_to_csv('aclImdb', 'imdb_data.csv')
