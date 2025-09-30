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

# 61. Department-wise salary percent contribution to company
spark.sql("""
SELECT department,
       ROUND(SUM(salary) * 100 / (SELECT SUM(salary) FROM employees), 2) AS pct_share
FROM employees
GROUP BY department
""").show()

# 62. Employees who are in top 10% earners
spark.sql("""
SELECT * FROM (
  SELECT *, NTILE(10) OVER (ORDER BY salary DESC) decile
  FROM employees
) WHERE decile = 1
""").show()

# 63. Find year with maximum hires
spark.sql("""
SELECT YEAR(joining_date) yr, COUNT(*) cnt
FROM employees
GROUP BY YEAR(joining_date)
ORDER BY cnt DESC
LIMIT 1
""").show()

# 64. Average salary by designation across locations
spark.sql("""
SELECT designation, location, AVG(salary) avg_sal
FROM employees
GROUP BY designation, location
""").show()

# 65. Employees who joined same month (ignore year)
spark.sql("""
SELECT MONTH(joining_date) mon, COLLECT_LIST(name) emp_list
FROM employees
GROUP BY MONTH(joining_date)
HAVING COUNT(*) > 1
""").show()

# 66. Gender ratio per department
spark.sql("""
SELECT department,
       SUM(CASE WHEN gender='M' THEN 1 ELSE 0 END) males,
       SUM(CASE WHEN gender='F' THEN 1 ELSE 0 END) females
FROM employees
GROUP BY department
""").show()

# 67. Running total of salary by joining date
spark.sql("""
SELECT name, joining_date, salary,
       SUM(salary) OVER (ORDER BY joining_date) AS running_total
FROM employees
""").show()

# 68. Employees earning more than average of their location
spark.sql("""
SELECT e.* FROM employees e
JOIN (SELECT location, AVG(salary) avg_sal FROM employees GROUP BY location) t
ON e.location = t.location
WHERE e.salary > t.avg_sal
""").show()

# 69. Show youngest (latest joined) employee in each department
spark.sql("""
SELECT * FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY department ORDER BY joining_date DESC) rn
  FROM employees
) WHERE rn = 1
""").show()

# 70. Highest paid female employee
spark.sql("""
SELECT * FROM employees
WHERE gender='F'
ORDER BY salary DESC
LIMIT 1
""").show()

# 71. Highest paid male employee
spark.sql("""
SELECT * FROM employees
WHERE gender='M'
ORDER BY salary DESC
LIMIT 1
""").show()

# 72. Department with max female employees
spark.sql("""
SELECT department, COUNT(*) cnt
FROM employees
WHERE gender='F'
GROUP BY department
ORDER BY cnt DESC
LIMIT 1
""").show()

# 73. Employees whose salary is multiple of 5000
spark.sql("SELECT * FROM employees WHERE salary % 5000 = 0").show()

# 74. Show employees with salary ranks (dense rank)
spark.sql("""
SELECT name, salary, DENSE_RANK() OVER (ORDER BY salary DESC) rank
FROM employees
""").show()

# 75. Find 3rd lowest salary
spark.sql("""
SELECT salary FROM (
  SELECT DISTINCT salary, RANK() OVER (ORDER BY salary ASC) rnk
  FROM employees
) WHERE rnk = 3
""").show()

# 76. Employees earning exactly company average
spark.sql("""
SELECT * FROM employees
WHERE salary = (SELECT ROUND(AVG(salary)) FROM employees)
""").show()

# 77. List employees grouped by location
spark.sql("SELECT location, COLLECT_LIST(name) names FROM employees GROUP BY location").show()

# 78. Department with highest salary range (max-min)
spark.sql("""
SELECT department, MAX(salary)-MIN(salary) AS sal_range
FROM employees
GROUP BY department
ORDER BY sal_range DESC
LIMIT 1
""").show()

# 79. Employees earning same as their manager
spark.sql("""
SELECT e.name, e.salary, m.name AS manager
FROM employees e
JOIN employees m ON e.manager_id=m.emp_id
WHERE e.salary = m.salary
""").show()

# 80. Employees who are managers themselves
spark.sql("SELECT DISTINCT m.* FROM employees m JOIN employees e ON m.emp_id = e.manager_id").show()

# 81. Employees who never managed anyone
spark.sql("""
SELECT * FROM employees
WHERE emp_id NOT IN (SELECT DISTINCT manager_id FROM employees WHERE manager_id IS NOT NULL)
""").show()

# 82. Employees joined in last N years (e.g. 5 years)
spark.sql("""
SELECT * FROM employees
WHERE YEAR(CURRENT_DATE()) - YEAR(joining_date) <= 5
""").show()

# 83. Department wise highest tenured employee
spark.sql("""
SELECT * FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY department ORDER BY joining_date ASC) rn
  FROM employees
) WHERE rn=1
""").show()

# 84. Show employee salary percentile
spark.sql("""
SELECT name, salary,
       PERCENT_RANK() OVER (ORDER BY salary) perc_rank
FROM employees
""").show()

# 85. Count employees whose name length > 4
spark.sql("SELECT COUNT(*) FROM employees WHERE LENGTH(name) > 4").show()

# 86. Employees whose name ends with 'a'
spark.sql("SELECT * FROM employees WHERE name LIKE '%a'").show()

# 87. Employees with designation not containing 'Manager'
spark.sql("SELECT * FROM employees WHERE designation NOT LIKE '%Manager%'").show()

# 88. Department salary standard deviation
spark.sql("SELECT department, STDDEV(salary) AS stddev FROM employees GROUP BY department").show()

# 89. Rank employees in each department by joining date
spark.sql("""
SELECT name, department, joining_date,
       RANK() OVER (PARTITION BY department ORDER BY joining_date) rank
FROM employees
""").show()

# 90. Employee with max salary per location
spark.sql("""
SELECT e.* FROM employees e
JOIN (SELECT location, MAX(salary) max_sal FROM employees GROUP BY location) t
ON e.location=t.location AND e.salary=t.max_sal
""").show()

# 91. Find department with most managers
spark.sql("""
SELECT department, COUNT(*) cnt
FROM employees
WHERE designation LIKE '%Manager%'
GROUP BY department
ORDER BY cnt DESC
LIMIT 1
""").show()

# 92. Employees whose name contains exactly 5 letters
spark.sql("SELECT * FROM employees WHERE LENGTH(name)=5").show()

# 93. Find difference between employee salary and department avg
spark.sql("""
SELECT name, department, salary,
       salary - AVG(salary) OVER (PARTITION BY department) diff_from_avg
FROM employees
""").show()

# 94. Rank employees globally by tenure
spark.sql("""
SELECT name, joining_date,
       RANK() OVER (ORDER BY joining_date ASC) tenure_rank
FROM employees
""").show()

# 95. Count of employees hired each month
spark.sql("""
SELECT MONTH(joining_date) month, COUNT(*) cnt
FROM employees
GROUP BY MONTH(joining_date)
ORDER BY month
""").show()

# 96. Department with minimum avg salary
spark.sql("""
SELECT department, AVG(salary) avg_sal
FROM employees
GROUP BY department
ORDER BY avg_sal ASC
LIMIT 1
""").show()

# 97. Employee with salary just above company average
spark.sql("""
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary ASC
LIMIT 1
""").show()

# 98. Find location with highest salary expenditure
spark.sql("""
SELECT location, SUM(salary) total_sal
FROM employees
GROUP BY location
ORDER BY total_sal DESC
LIMIT 1
""").show()

# 99. Show top 3 earliest joiners overall
spark.sql("SELECT * FROM employees ORDER BY joining_date ASC LIMIT 3").show()

# 100. Employees whose salary is in top 20% of their department
spark.sql("""
SELECT * FROM (
  SELECT *, NTILE(5) OVER (PARTITION BY department ORDER BY salary DESC) nt
  FROM employees
) WHERE nt=1
""").show()
