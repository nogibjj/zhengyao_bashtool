from databricks import sql
import os


def querydb(query="SELECT * FROM default.netflix1_csv LIMIT 2"):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result

def querybydirector(director):
    query = "SELECT * FROM default.netflix1_csv WHERE director=" + "'" + director + "'" + " LIMIT 10"
    print(query)
    querydb(query)

def sortbyyear(director):
    query = "SELECT * FROM default.netflix1_csv WHERE director=" + "'" + director + "'" "ORDER BY release_year ASC" + " LIMIT 10"
    print(query)
    querydb(query)