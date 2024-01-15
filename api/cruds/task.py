from sqlalchemy.ext.asyncio import AsyncSession
from typing import List,Tuple,Optional


from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.task as task_model
#dbのやつ
import api.schemas.task as task_schema
#apiのスキーマ

async def create_task(
        db:AsyncSession,task_create:task_schema.TaskCreate
)->task_model.Task:
#->で関数の返り値の型を言ってる
    task=task_model.Task(**task_create.dict())
    #apiのスキーマとして受け取ったtitleをdbモデルに変換
    #idはauto_incrementが設定されているので、引数に取らない
    db.add(task)
    await db.commit()
    #dbにコミットする
    await db.refresh(task)
    #逆にdbからの変更をtaskオフジェクトに反映させてる。
    #整合性を保つ
    return task


async def get_tasks_with_done(db:AsyncSession)->List[Tuple[int,str,bool]]:
    result:Result=await(
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Done.id.isnot(None).label("done"),
                #doneのidがNoneでないなら新たなラベルdoneにTrueを入れる
                #そうでないならFalseを入れる
            ).outerjoin(task_model.Done)
        )
    )
    return result.all()

async def get_task(db:AsyncSession,task_id:int)->Optional[task_model.Task]:
    result:Result=await db.execute(
        select(
            task_model.Task
        ).filter(
            task_model.Task.id==task_id
        )
        #引数にとったidのtaskのみを取り出す
    )
    task:Optional[Tuple[task_model.Task]]=result.first()
    #resultで取得したリストの一つ目を代入
    return task[0] if task is not None else None
    #taskがNoneでないならtask[0]を返し、NoneならNoneを返す

async def update_task(
    db:AsyncSession,task_create:task_schema.TaskCreate,original:task_model.Task
)->task_model.Task:
    original.title=task_create.title
    #変更を加える
    db.add(original)
    await db.commit()
    #変更をdbに反映
    await db.refresh(original)
    return original

async def delete_task(db:AsyncSession,original:task_model.Task)->None:
    await db.delete(original)
    await db.commit()