from sqlalchemy import create_engine
from api.models.task import Base

DB_URL="mysql+pymysql://root@db:3306/demo?charset=utf8"
engine=create_engine(DB_URL,echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
#dbを作り直す関数
#drop_allでdbを削除
#create_allで新たに作る

if __name__=="__main__":
    reset_database()