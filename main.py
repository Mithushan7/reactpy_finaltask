from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient


@component
def MyCrud():
    ## Creating state
    alltodo = use_state([])
    name, set_name = use_state("")
    password, set_password = use_state(0)

    def mysubmit(event):
        newtodo = {"name": name, "password": password}

        # push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo])
        login(newtodo)  # function call to login function using the submitted data

    # looping data from alltodo to show on web

    list = [
        html.li(
            {
              
            },
            f"{b} => {i['name']} ; {i['password']} ",
        )
        for b, i in enumerate(alltodo.value)
    ]

    def handle_event(event):
        print(event)

    return html.div(
        {"style": {"padding": "10px"}},
        ## creating form for submission\
        html.form(
            {"on submit": mysubmit},
            html.h1("Login Form - ReactPy & Mongodb"),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Name",
                    "on_change": lambda event: set_name(event["target"]["value"]),
                }
            ),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Password",
                    "on_change": lambda event: set_password(event["target"]["value"]),
                }
            ),
            # creating submit button on form
            html.button(
                {
                    "type": "submit",
                    "on_click": event(
                        lambda event: mysubmit(event), prevent_default=True
                    ),
                },
                "Submit",
            ),
        ),
        html.ul(list),
    )


app = FastAPI()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import MongoClient
# line 3 and 4 are additionally done by me
from fastapi import FastAPI

app = FastAPI()



#copy and pasting the MongoDb URI
uri = "mongodb+srv://admin:123@cluster0.d2nrwcm.mongodb.net/"
client = MongoClient(uri)

#defining the database name and collection
db = client["Reactpy_Task01"]
collection = db["main"]

#checking the connection 
try:
    client.admin.command("ping")
    print("Sucessfully connected Mongodb")
except Exception as e:
    print(e)
