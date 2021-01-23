from openpyxl import Workbook, load_workbook

wb2 = load_workbook("筛选的微博分阶段评论.xlsx")
sheetactive = wb2.active
for i in range(65,77):
    a=0
    for row in sheetactive[chr(i)]:
        if row.value is None:
            b=0
        else:
            a=a+1
    print(a-1)