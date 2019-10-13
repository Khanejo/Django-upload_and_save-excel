from django.shortcuts import render
import openpyxl
import pandas as pd

def index(request):
    if "GET" == request.method:
        return render(request, 'myapp/index.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size
        xl = pd.ExcelFile(excel_file)
        names =xl.sheet_names
        df = xl.parse(names[0])       
        writer = pd.ExcelWriter('output1.xlsx')
        df.to_excel(writer,sheet_name='sheet1',index=False)
        writer.save()        

        return render(request, 'myapp/index.html', { })









