import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\prajw\AppData\Local\Programs\Python\Python310\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\prajw\AppData\Local\Programs\Python\Python310\python.exe"


from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# ---------------------------------------------------------
# Step 1: Start SparkSession
# ---------------------------------------------------------
spark = SparkSession.builder \
    .appName("EmployeeScenarios") \
    .master("local[*]") \
    .getOrCreate()

print("✅ Spark Session Started - Version:", spark.version)

# ---------------------------------------------------------
# Step 2: Define Sample Data
# ---------------------------------------------------------
data = [
    (101, "Alice Johnson", "HR", "Manager", 95000, "2016-03-15", None, "F", 42, "New York"),
    (102, "Bob Smith", "IT", "Lead", 120000, "2015-06-01", 101, "M", 45, "San Francisco"),
    (103, "Carol Lee", "Finance", "Analyst", 70000, "2018-09-10", 102, "F", 30, "New York"),
    (104, "David Kim", "IT", "Developer", 85000, "2019-11-20", 102, "M", 28, "San Jose"),
    (105, "Eva Green", "HR", "Executive", 60000, "2020-01-05", 101, "F", 27, "Boston"),
    (106, "Frank Zhao", "IT", "Developer", 90000, "2017-05-12", 102, "M", 33, "San Francisco"),
    (107, "Grace Park", "Sales", "Manager", 110000, "2014-02-01", None, "F", 48, "Chicago"),
    (108, "Hank Miller", "Sales", "Executive", 65000, "2019-07-22", 107, "M", 31, "Chicago"),
    (109, "Ivy Wang", "Finance", "Lead", 98000, "2013-10-30", 101, "F", 50, "New York"),
    (110, "Jake Long", "IT", "Intern", 30000, "2021-06-01", 106, "M", 23, "San Jose"),
    (111, "Kumar Patel", "Ops", "Manager", 88000, "2012-12-12", None, "M", 51, "Mumbai"),
    (112, "Lina Torres", "Ops", "Executive", 52000, "2018-08-13", 111, "F", 29, "Mumbai"),
    (113, "Mohan Das", "Finance", "Analyst", 72000, "2020-02-14", 109, "M", 32, "Delhi"),
    (114, "Nora White", "HR", "Lead", 80000, "2011-05-05", 101, "F", 54, "Boston"),
    (115, "Omar Ali", "IT", "DevOps", 105000, "2016-11-11", 102, "M", 38, "San Francisco"),
    (116, "Priya Singh", "Sales", "Executive", 63000, "2020-10-10", 107, "F", 26, "Delhi"),
    (117, "Quinn Park", "Finance", "CFO", 200000, "2009-01-01", None, "M", 60, "New York"),
    (118, "Rita Verma", "IT", "Developer", 88000, "2017-07-07", 106, "F", 34, "San Jose"),
    (119, "Samir Khan", "Sales", "Lead", 93000, "2013-03-03", 107, "M", 46, "Chicago"),
    (120, "Tina Roy", "Ops", "Executive", 54000, "2019-04-01", 111, "F", 30, "Mumbai"),
    (121, "Uma Rao", "HR", "Executive", 58000, "2021-01-15", 114, "F", 25, "Boston"),
    (122, "Vikram Kohli", "IT", "Lead", 115000, "2012-06-06", 102, "M", 49, "San Francisco"),
    (123, "Wendy Zhou", "Finance", "Analyst", 71000, "2018-12-12", 109, "F", 31, "New York"),
    (124, "Xavier Fox", "Sales", "Executive", 67000, "2021-03-03", 119, "M", 28, "Chicago"),
    (125, "Yasmin Noor", "IT", "Developer", 89000, "2016-09-09", 115, "F", 35, "San Francisco"),
    (126, "Zack Lee", "Ops", "Lead", 76000, "2014-04-04", 111, "M", 44, "Mumbai"),
    (127, "Asha Menon", "Finance", "Executive", 62000, "2022-05-05", 117, "F", 27, "Delhi"),
    (128, "Bruno Silva", "IT", "Developer", 84000, "2017-09-09", 122, "M", 36, "San Francisco"),
    (129, "Chloe Brown", "HR", "Analyst", 68000, "2019-02-02", 114, "F", 29, "Boston"),
    (130, "Derek O'Neil", "Sales", "Lead", 98000, "2010-10-10", 107, "M", 52, "Chicago")
]

schema = StructType([
    StructField("emp_id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("department", StringType(), False),
    StructField("designation", StringType(), False),
    StructField("salary", IntegerType(), False),
    StructField("join_date", StringType(), False),
    StructField("manager_id", IntegerType(), True),
    StructField("gender", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("city", StringType(), True)
])

# ---------------------------------------------------------
# Step 3: Create DataFrame
# ---------------------------------------------------------
df = spark.createDataFrame(data, schema) \
          .withColumn("join_date", F.to_date("join_date", "yyyy-MM-dd"))

# Register as table & cache
df.createOrReplaceTempView("employees")
employees = df.cache()

# ---------------------------------------------------------
# Step 4: Show first few rows
# ---------------------------------------------------------
print("\n👀 Sample Employee Data:")
employees.show(5, truncate=False)

# Keep Spark alive until explicitly stopped
spark.stop()
