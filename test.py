from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession.builder.getOrCreate()
#Command....
schema = SstructType([
    StructField('CustomerID', IntegerType(), False),
    StructField('FirstName', StringType(), False),
    StructField('LastName', StringType(), False)
])

data = [
    [1000, 'Mathijs', 'Ousterhout-Rijntjes'],
    [1001, 'Joost', 'van Brunswijk'],
    [1002, 'Stan', 'Bokencamp']
]

customer = spark.Create.DataFrame(data, schema)
customer.show()