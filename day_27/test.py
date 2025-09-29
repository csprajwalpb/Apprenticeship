from pyspark.sql import SparkSession
 
# Create Spark session
spark = SparkSession.builder.appName("TestPySpark").getOrCreate()
 
# Create sample data
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
columns = ["Name", "Age"]
 
# Create DataFrame
df = spark.createDataFrame(data, columns)
 
# Show DataFrame
df.show()
 
# Stop Spark
spark.stop()