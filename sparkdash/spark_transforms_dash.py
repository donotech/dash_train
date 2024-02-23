#pip install pyspark
import os
from pyspark.sql import SparkSession
from dash import Dash, html, dash_table
from pyspark.sql.functions import lit

os.environ['JAVA_HOME'] = "C:\\software\\microsoft-jdk-17.0.10-windows-x64\\jdk-17.0.10+7"
os.environ['HADOOP_HOME'] = 'C:\\software\\winutils'
#

#filepath = "C:\\devraj\\pyspark_training\\datasets\\dw_dataset\\sales_1.csv"
root_path = "C:\\devraj\\pyspark_training\\datasets\\dw_dataset\\"
cubed_data_path = "file:///C:/spark_out/cubed_data"
#"C:\\Training\\pyspark_skai\\datasets\\dw_dataset"

spark = SparkSession.builder.appName("rdd_one").master("local[*]").getOrCreate()


def read_csv(path):
    filepath = f'{root_path}{os.sep}{path}'
    raw_df = spark.read.option("header", "true").option("inferSchema", "true").csv(filepath)
    return raw_df


def read_store_sales(store_id: int):
    filepath = f'{root_path}{os.sep}sales_{store_id}.csv'
    raw_df = spark.read.option("header", "true").option("inferSchema", "true").csv(filepath)
    store_df = raw_df.withColumn("store_id", lit(store_id)).withColumn("discount", raw_df['total_amount'] - raw_df.item_qty * raw_df.unit_price)
    return store_df


def store_cubed_data():

    df1 = read_store_sales(1)
    df2 = read_store_sales(2)
    df3 = read_store_sales(3)

    dfUnion = df1.union(df2).union(df3)
    dfUnion.createOrReplaceTempView("store_table")
    dfUnitDiscount = spark.sql("select *, discount/item_qty as unit_discount from store_table")

    dfProduct = read_csv('product_meta.csv')
    dfStore = read_csv('store_meta.csv')
    dfJoined = dfUnitDiscount.join(dfProduct, dfUnitDiscount['item_id'] == dfProduct['item_id'], 'left_outer')\
        .join(dfStore, dfUnitDiscount['store_id'] == dfStore['store_id'], 'left_outer')

    agg_dict = {"total_amount": "sum", "item_qty": "sum", "discount": "sum"}
    dfCube = dfJoined.cube("store_city", "product_type", "product_name", "date_of_sale").agg(agg_dict)
    dfCube.show()

    dfCube.write.parquet(cubed_data_path)


dfCubed = spark.read.parquet(cubed_data_path)
dfCubed.createOrReplaceTempView("cubed_table")


def get_total_sales_cube(filter_column):
    cols = ["store_city", "product_type", "product_name", "date_of_sale"]
    sql = list(map(lambda x: f"{x} is null" if x != filter_column else f"{x} is not null", cols))
    sql = "select * from cubed_table where " + " and ".join(sql)
    print(sql)
    df = spark.sql(sql)
    return df.toPandas()


df = get_total_sales_cube('store_city')
print(df)

# raw_df.show()
# pd = raw_df.toPandas()
# print(pd)
#
#
# app = Dash(__name__)
#
# # App layout
# app.layout = html.Div([
#     html.Div(children='My First App with Data from Spark'),
#     dash_table.DataTable(data=pd.to_dict('records'), page_size=10)
# ])
#
# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)
