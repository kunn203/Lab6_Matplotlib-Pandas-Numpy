import pandas as pd 
df = pd.read_csv('D:\Python\Ex Python\Lab6\Automobile_data.csv')
'''
#Xuất toàn bộ thông tin file 
print(df)
#Xuất 6 dòng đầu tiên của file
print(df.head(6))
#Xuất 7 dòng cuối cùng của file
print(df.tail(7))
#Xuất thông tin của dữ liệu
print(df.info())
'''

df = df.dropna()
'''
#Xuất ra màn hình tên công ty có xe ô tô đắt nhất
df = df[['company','price']][df.price == df['price'].max()]
print(df)


#Xuất ra thông tin chi tiết cảy tất cả xe thuộc hãng Toyota
car_Manufacturers = df.groupby('company')
toyotaDF = car_Manufacturers.get_group('toyota')
print(toyotaDF)

#Đếm số xe của hãng 
count_company = df[['company']].value_counts()
print(count_company)

#Hiển thị giá xe cao nhất của mỗi hãng
max_price = df.groupby('company')['price'].max()
print(max_price)
'''
