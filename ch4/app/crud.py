from fastapi import FastAPI
app = FastAPI()

data ={
    1 : {
        "Name" : "Sk Sakil Ali",
        "Age" : "21",
        "Class" :"3rd"
    },
  2 : {
     "Name" : "Sk Sakil Ali",
    "Age" : "21",
    "Class" :"3rd"
    }
}
current_id = 2

@app.get("/user/{user_id}")
async def get_user(user_id: int):
         return data[user_id]

@app.post("/user/add/{user_id}")
async def add_user(user_id: int, data_to_add: dict):
        data[user_id] = data_to_add
        print(data)
        return { "Status":"Successful"}

@app.delete("/user/delete/{user_id}")
async def user_delete(user_id:int):
        del data[user_id]
        print(data)
        return {
                "UserID":user_id,
                "Status":"Successfully Deleted"
        }