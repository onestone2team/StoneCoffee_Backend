from django.apps import AppConfig
from machine.recommend import save_dataframe
import pandas as pd
from product.models import Product


class SaveData(AppConfig):
    name = 'product'

    def ready(self):
        ## data 저장
        products = Product.objects.all()
        id = []
        product_name = []
        aroma_grade = []
        acidity_grade = []
        sweet_grade = []
        body_grade = []
        for product in products:
            if product.category.id == 1:
                id.append(product.id)
                product_name.append(product.product_name)
                aroma_grade.append(product.aroma_grade)
                acidity_grade.append(product.acidity_grade)
                sweet_grade.append(product.sweet_grade)
                body_grade.append(product.body_grade)
        newdata = {}
        newdata["num"]=id
        newdata["name_ko"]=product_name
        newdata["aroma_grade"]=aroma_grade
        newdata["acidity_grade"]=acidity_grade
        newdata["sweet_grade"]=sweet_grade
        newdata["body_grade"]=body_grade
        df = pd.DataFrame(newdata)
        df.to_csv("./machine/dbdata.csv", index=False, encoding='cp949')
        save_dataframe()
        pass