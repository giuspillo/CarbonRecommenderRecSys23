import os
import time


models = ['Pop', 'ItemKNN', 'BPR', 'DMF', 'FISM',
			'NAIS', 'SLIMElastic', 'NeuMF', 'MultiDAE',
			'NGCF', 'DGCF', 'LightGCN', 'SGL', 
			'CKE', 'CFKG', 'KGCN', 'KTUP', 'RippleNet']

datasets = ['amazon_books_60core_kg', 'movielens', 'mind']
counter = 0

for dataset in datasets:
	for model in models:

		counter += 1
		cmd = 'python full_model.py --dataset='+dataset+' --model='+model+' --counter='+str(counter)
		os.system(cmd)

		# once a model has been executed, sleep for a couple of seconds
		time.sleep(5)
	time.sleep(10)