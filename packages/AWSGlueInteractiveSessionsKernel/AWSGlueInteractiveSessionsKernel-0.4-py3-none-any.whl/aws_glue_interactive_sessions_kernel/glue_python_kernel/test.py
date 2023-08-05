from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import DataFrame, Row
from awsglue.dynamicframe import DynamicFrame
from awsglue import DynamicFrame
glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session
job = Job(glueContext)
from pyspark.sql import Row
products1 = [
    {'product_id': '00001', 'product_name': 'Television'},
    {'product_id': '00002', 'product_name': 'USB charger'},
    {'product_id': '00003', 'product_name': 'Blender'}
]
df1 = spark.createDataFrame(Row(**x) for x in products1)
dyf1 = DynamicFrame.fromDF(df1, glueContext, "df2dyf")
#%%
dyf1.show()
#%%
dyf1.toDF().show()