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

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        result_all = result.all()
        jobs = [u._asdict() for u in result_all]
        return jobs

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

    
    