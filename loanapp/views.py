from django.shortcuts import render
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
# Create your views here.
def home(request,pred=None):
    filename = 'model.pkl'
    model = pickle.load(open(filename, 'rb'))
    if request.method=='POST':
        married=request.POST['Y']
        depent=request.POST['op1']
        education=request.POST['op2']
        emp=request.POST['rd1']
        apincome=int(request.POST['aincome'])
        coincom=int(request.POST['bincome'])
        loanamount = float(request.POST['LoanAmount'])
        lterm = float(request.POST['lterm'])
        credit = float(request.POST['bincome'])
        proarea=request.POST['op3']

        train=[[married,depent,education,emp,apincome,coincom,loanamount,lterm,credit,proarea]]
        df=pd.DataFrame(train, columns =[['Married', 'Dependents', 'Education','Self_Employed', 'ApplicantIncome', 'CoapplicantIncome','LoanAmount', 'Loan_Amount_Term', 'Credit_History','Property_Area']])
        cnvtoint = ['Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']
        train=df
        for i in cnvtoint:
            le = preprocessing.LabelEncoder()
            train[[i]] = le.fit_transform(train[[i]].astype('str'))
        print(train.dtypes)
        pred = model.predict(train)




    return render(request,'index.html',{'data':pred})