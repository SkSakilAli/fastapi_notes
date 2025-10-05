from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

#Function for the task we want to do in Background

def write_message(email: str, message: str=""):
    with open("log.txt", mode ="w") as email_file:
      content = f"email for {email}: {message}"
      email_file.write(content)

@app.post("/send-notification/{email_id}")
async def send_notification(email_id: str, user_message: dict, background_task: BackgroundTasks):
    if not user_message:
       message = "Some random Message"
    else:
        message = user_message
    background_task.add_task(write_message, email_id, user_message)
#background_task.add_task(function_identifier, parameters_of_functions)
    return {"status":"Success"}


