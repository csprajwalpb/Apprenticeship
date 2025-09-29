from pyspark.sql import SparkSession
 
spark = SparkSession.builder.appName("FixTest").getOrCreate()
 
print("Spark running with Python at:", spark.sparkContext.pythonExec)
print("Spark version:", spark.version)
 
spark.stop()