from sqlalchemy import create_engine,text
import pymysql
import os
# creating an engine to connect to the database
key = "DB_DETAILS_JOV"
db_connection_string = os.getenv(key,default=None)

engine = create_engine(db_connection_string,
    connect_args={
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
}
})

#loads all the jobs from the data base and esatblishes a connection
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        result_all = result.all()
        jobs = [u._asdict() for u in result_all]
        return jobs

#loading a single job using the id that has been passed by the user 
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
        text(f"SELECT * FROM jobs WHERE id = :val"),
      {"val": id}
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
        
        
#In sqlalchemy we use :variable to define a variable and then we have to define the variable outside the arguement of the text

# #now taking the data out of the database using the engine
# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
    
#     result_all = result.all()
#     # print("TYPE OF RESULT_ALL",type(result_all),"\n")
#     # print(result_all,"\n")
#     # first_result = result_all[0]
#     # print("THE FIRST RESULT OF SQL:: ",first_result,"\n")
#     # print(type(first_result),"\n")
#     # first_result_dict = result_all[0]._asdict()
#     # print(type(first_result_dict),"\n")

    
    