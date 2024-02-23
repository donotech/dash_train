#pip install pyspark
import os
from pyspark.sql import SparkSession
from dash import Dash, html, dash_table

os.environ['JAVA_HOME'] = "C:\\software\\microsoft-jdk-17.0.10-windows-x64\\jdk-17.0.10+7"
os.environ['HADOOP_HOME'] = 'C:\\software\\winutils'
#

filepath = "C:\\devraj\\pyspark_training\\datasets\\dw_dataset\\sales_1.csv"
#"C:\\Training\\pyspark_skai\\datasets\\dw_dataset"

spark = SparkSession.builder.appName("rdd_one").master("local[*]").getOrCreate()
raw_df = spark.read.option("header", "true").option("inferSchema", "true").csv(filepath)


raw_df.show()
pd = raw_df.toPandas()
print(pd)


app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data from Spark'),
    dash_table.DataTable(data=pd.to_dict('records'), page_size=10)
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
