from flask import Flask, render_template, send_from_directory

UPLOAD_FOLDER =r'C:\Users\KAli02\Desktop\Master_Thesis\Code\FlaskApp\static'
BASE_URL = r'http://127.0.0.1:5000/static/'
date='2016-08-24'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('header.html')


@app.route('/category-based-analysis/')
def category():
    p1=BASE_URL+'category_totalProduct'+date+'.png'
    p2=BASE_URL+'category_offeredProduct'+date+'.png'
    p3=BASE_URL+'category_offeredPercentage'+date+'.png'
    p4=BASE_URL+'category_colorNoproducts'+date+'.png'
    p5=BASE_URL+'category_sizeproducts'+date+'.png'
    p6=BASE_URL+'category_x_size_xitemsold'+date+'.png'
    p7=BASE_URL+'category_x_size_xrevenue'+date+'.png'
    p8 = BASE_URL+'category_totalProduct'+date+'.png'
    p9 = BASE_URL+'category_offeredProduct'+date+'.png'
    p10 =BASE_URL+'category_offeredPercentage'+date+'.png'
    p11 =BASE_URL+'category_colorNoproducts'+date+'.png'
    p12 =BASE_URL+'category_sizeproducts'+date+'.png'
    p13 =BASE_URL+'category_x_size_xitemsold'+date+'.png'
    p14 =BASE_URL+'category_x_size_xrevenue'+date+'.png'

    return render_template('category.html',p1=p1,p2=p2,p3=p3,p4=p4,p5=p5,p6=p6,p7=p7,p8=p8,p9=p9,p10=p10,p11=p11,p12=p12,p13=p13,p14=p14)

@app.route('/brand-based-analysis/')
def brand():
    p1 = BASE_URL+'brand_totalProduct'+date+'.png'
    p2 = BASE_URL+'brand_offeredProduct'+date+'.png'
    p3 = BASE_URL+'brand_offeredPercentage'+date+'.png'
    p4 = BASE_URL+'brand_colorNoproducts'+date+'.png'
    p5 = BASE_URL+'brand_sizeproducts'+date+'.png'
    p6 = BASE_URL+'brand_x_size_xitemsold'+date+'.png'
    p7 = BASE_URL+'brand_x_size_xrevenue'+date+'.png'
    p8 = BASE_URL+'brand_totalProduct'+date+'.png'
    p9 = BASE_URL+'brand_offeredProduct'+date+'.png'
    p10 =BASE_URL+'brand_offeredPercentage'+date+'.png'
    p11 =BASE_URL+'brand_colorNoproducts'+date+'.png'
    p12 =BASE_URL+'brand_sizeproducts'+date+'.png'
    p13 =BASE_URL+'brand_x_size_xitemsold'+date+'.png'
    p14 =BASE_URL+'brand_x_size_xrevenue'+date+'.png'

    return render_template('brand.html',p1=p1,p2=p2,p3=p3,p4=p4,p5=p5,p6=p6,p7=p7,p8=p8,p9=p9,p10=p10,p11=p11,p12=p12,p13=p13,p14=p14)

@app.route('/product-based-analysis/')
def product():
    p1 = 'productOnOffer'+date+'.png'
    p2 = 'discountPercentage'+date+'.png'
    return render_template('Product.html',p1=p1,p2=p2)

@app.route('/api-based-analysis/')
def api():
    p1 = 'tran-revenue-'+date+'.png'
    p2 = 'offerPercentage'+date+'.png'
    p3 = 'itemSold'+date+'.png'
    p4 = 'products'+date+'.png'
    p5 = 'tran-revenue-'+date+'.png'
    p6 = 'offerPercentage'+date+'.png'
    p7 = 'itemSold'+date+'.png'
    p8 = 'products'+date+'.png'
    return render_template('api.html',p1=p1,p2=p2,p3=p3,p4=p4,p5=p5,p6=p6,p7=p7,p8=p8)


if __name__ == '__main__':
    app.run(debug=True)