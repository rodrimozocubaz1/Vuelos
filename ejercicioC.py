from pyspark.sql import SparkSession

# Crea una sesión de Spark
spark = SparkSession.builder.getOrCreate()

# Lee el archivo CSV en un DataFrame
df = spark.read.csv("hdfs:///user/maria_dev/data_vf/data_vuelos", inferSchema=True)

# Imprime el contenido del DataFrame
df.show()

