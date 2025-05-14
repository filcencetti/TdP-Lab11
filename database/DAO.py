from database.DB_connect import DBConnect
from model.product import Product


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getProducts():
        conn = DBConnect.get_connection()

        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                    FROM go_products"""
        cursor.execute(query,)

        for row in cursor:
            result.append(Product(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(color,year):
        conn = DBConnect.get_connection()

        result = []
        cursor = conn.cursor()
        query = """select g1.Product_number, g2.Product_number, count(distinct g1.`Date`)
                    from go_daily_sales g1
                    join go_daily_sales g2 on g1.Retailer_code = g2.Retailer_code and g1.Product_number != g2.Product_number and g1.`Date` = g2.`Date`
                    join go_products gp1 on g1.Product_number =  gp1.Product_number and gp1.Product_color = %s
                    join go_products gp2 on g2.Product_number =  gp2.Product_number and gp2.Product_color = %s
                    where year(g2.`Date`) = %s
                    group by g1.Product_number, g2.Product_number"""
        cursor.execute(query, (color,color,year))

        for row in cursor:
            result.append(*row)

        cursor.close()
        conn.close()
        return result

