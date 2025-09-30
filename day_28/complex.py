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

# 21. Department with highest average salary
spark.sql("""
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 1
""").show()

# 22. Find 2nd highest salary
spark.sql("""
SELECT salary FROM (
  SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) rnk
  FROM employees
) WHERE rnk = 2
""").show()

# 23. Employees hired in 2018
spark.sql("SELECT * FROM employees WHERE YEAR(joining_date) = 2018").show()

# 24. Employees grouped by same manager
spark.sql("SELECT manager_id, COLLECT_LIST(name) AS team FROM employees GROUP BY manager_id").show()

# 25. Salary difference (max - min)
spark.sql("SELECT MAX(salary) - MIN(salary) AS salary_diff FROM employees").show()

# 26. Employees with 'Manager' in designation
spark.sql("SELECT * FROM employees WHERE designation LIKE '%Manager%'").show()

# 27. Employee count per location
spark.sql("SELECT location, COUNT(*) AS cnt FROM employees GROUP BY location").show()

# 28. Highest salary employee in each department
spark.sql("""
SELECT e.*
FROM employees e
JOIN (SELECT department, MAX(salary) AS max_sal FROM employees GROUP BY department) t
ON e.department = t.department AND e.salary = t.max_sal
""").show()

# 29. Managers earning less than their subordinates
spark.sql("""
SELECT m.name AS manager, m.salary AS manager_salary, e.name AS employee, e.salary AS employee_salary
FROM employees m
JOIN employees e ON m.emp_id = e.manager_id
WHERE e.salary > m.salary
""").show()

# 30. Employees in top 50% salary bracket
spark.sql("""
SELECT * FROM (
  SELECT *, NTILE(2) OVER (ORDER BY salary DESC) half
  FROM employees
) WHERE half = 1
""").show()

# 31. Employees earning above department average
spark.sql("""
SELECT e.* FROM employees e
JOIN (SELECT department, AVG(salary) AS avg_sal FROM employees GROUP BY department) t
ON e.department = t.department
WHERE e.salary > t.avg_sal
""").show()

# 32. Show employees ranked by salary within department
spark.sql("""
SELECT emp_id, name, department, salary,
RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_in_dept
FROM employees
""").show()

# 33. Count employees joined after 2015 per department
spark.sql("""
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE joining_date > '2015-01-01'
GROUP BY department
""").show()

# 34. Find employees who joined on weekend
spark.sql("SELECT * FROM employees WHERE DAYOFWEEK(joining_date) IN (1,7)").show()

# 35. Department with maximum employees
spark.sql("""
SELECT department, COUNT(*) cnt
FROM employees
GROUP BY department
ORDER BY cnt DESC
LIMIT 1
""").show()

# 36. Employees earning in top 3 salaries
spark.sql("""
SELECT * FROM employees
WHERE salary IN (SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 3)
""").show()

# 37. Employees who do not report to anyone (manager_id NULL)
spark.sql("SELECT * FROM employees WHERE manager_id IS NULL").show()

# 38. Employees grouped by gender and department
spark.sql("SELECT department, gender, COUNT(*) cnt FROM employees GROUP BY department, gender").show()

# 39. Find employees who joined in the last 3 years
spark.sql("SELECT * FROM employees WHERE YEAR(CURRENT_DATE()) - YEAR(joining_date) <= 3").show()

# 40. Employees working in New York and earning > 60k
spark.sql("SELECT * FROM employees WHERE location = 'New York' AND salary > 60000").show()

# 41. Employees who have same salary
spark.sql("""
SELECT salary, COLLECT_LIST(name) AS employees
FROM employees
GROUP BY salary
HAVING COUNT(*) > 1
""").show()

# 42. Percentage of employees per department
spark.sql("""
SELECT department, (COUNT(*) * 100 / (SELECT COUNT(*) FROM employees)) AS percentage
FROM employees
GROUP BY department
""").show()

# 43. Find cumulative salary per department
spark.sql("""
SELECT department, SUM(salary) OVER (PARTITION BY department ORDER BY salary) cum_salary, name, salary
FROM employees
""").show()

# 44. Average tenure (years) of employees
spark.sql("SELECT AVG(YEAR(CURRENT_DATE()) - YEAR(joining_date)) AS avg_tenure FROM employees").show()

# 45. Find employees with salary greater than company average
spark.sql("""
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
""").show()

# 46. List employees ordered by joining year
spark.sql("""
SELECT *, YEAR(joining_date) AS join_year
FROM employees
ORDER BY join_year ASC
""").show()

# 47. Show department and its highest + lowest salary
spark.sql("""
SELECT department,
MAX(salary) AS max_sal,
MIN(salary) AS min_sal
FROM employees
GROUP BY department
""").show()

# 48. Employees who are earning equal to department average
spark.sql("""
SELECT e.* FROM employees e
JOIN (SELECT department, ROUND(AVG(salary)) AS avg_sal FROM employees GROUP BY department) t
ON e.department = t.department
WHERE e.salary = t.avg_sal
""").show()

# 49. Rank employees globally by salary
spark.sql("""
SELECT name, salary, RANK() OVER (ORDER BY salary DESC) global_rank
FROM employees
""").show()

# 50. Median salary per department
spark.sql("""
SELECT department, PERCENTILE(salary, 0.5) AS median_sal
FROM employees
GROUP BY department
""").show()
