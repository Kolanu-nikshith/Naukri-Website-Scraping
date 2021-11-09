import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='demodatbase')
cursor = mydb.cursor()

csv_data = csv.reader(file('naukri_dataanalytics.csv'))
for row in csv_data:

    cursor.execute('INSERT INTO DataAnalyst_ncr(job_title, \
          experience_req,company_name,link,keyskills,job_description,salary )' \
          'VALUES("%s", "%s", "%s","%s", "%s", "%s","%s", "%s")',
          row)
    cursor.execute('INSERT INTO location_jobs(location \
           )' \
          'VALUES("%s")',
          row)
#close the connection to the database.
mydb.commit()
cursor.close()
print ('Done')
