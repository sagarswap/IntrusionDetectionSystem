import pandas as pd
import numpy as np

data1=pd.read_csv("./data/input/labelled_training_data.csv", index_col=False)
data2=pd.read_csv("./data/input/labelled_validation_data.csv", index_col=False)
data3=pd.read_csv("./data/input/labelled_testing_data.csv", index_col=False)
data=pd.concat([data1, data2, data3], axis=0)
data['proID']=np.where(data['processId']<3, 0, 1)
data['parID']=np.where(data['parentProcessId']<3, 0, 1)
data['userID']=np.where(data['userId']<1000, 0, 1)
data['montNamesp']=np.where(data['mountNamespace']==4026531840, 0, 1)
en1=pd.get_dummies(data['processName'])
en2=pd.get_dummies(data['hostName'])
data=data.drop(columns=['timestamp', 'parentProcessId', 'processId', 'userId', 'eventName', 'hostName', 'args', 'processName', 'mountNamespace', 'stackAddresses'], axis=1)
data=pd.concat([data, en1, en2], axis=1)
print(data.shape)
data.to_csv("./data/output/processed_data.csv", index=False)