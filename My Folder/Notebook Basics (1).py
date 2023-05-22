# Databricks notebook source
print("Hello world")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "HELLO"

# COMMAND ----------

# MAGIC %md
# MAGIC # title
# MAGIC ## title
# MAGIC ### title 

# COMMAND ----------

# MAGIC %run ./Includes/setup

# COMMAND ----------

print(full)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('databricks-datasets')

# COMMAND ----------

display(files)

# COMMAND ----------


