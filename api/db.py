from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
#非同期につかう
from sqlalchemy.orm import sessionmaker,declarative_base
#セッションとかの基盤づくり

ASYNC_DB_URL="mysql+aiomysql://root@db:3306/demo?charset=utf8"
#mysqlとaiomysqlを使いますよ
#rootという名前で入りますよ
#3306ポートに繋ぎますよ
#demoというやつに繋ぎますよ

async_engine=create_async_engine(ASYNC_DB_URL,echo=True)
#エンジン(セッションの前の大元)を作りますよ
#↑に繋ぎますよ
#ログを出力しますよ

async_session=sessionmaker(
    autocommit=False,autoflush=False,bind=async_engine,class_=AsyncSession
)
#commit(DBに反映)をFalse
#flush(DBへの一時的な反映)をFalse
#基盤を指定
#非同期通信しますよ

Base=declarative_base()

async def get_db():
    async with async_session() as session:
        yield session
#withとすることでセッション作り終わったら終了
#yieldとすることで小出しにしてメモリを効率的に使えるらしい