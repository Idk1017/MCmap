#import modules
import matplotlib.pyplot as plt
import streamlit as st
import json
import os

#Plotting functions
def points():
    for point in data["points"]:
        x,y,name=point
        plt.scatter(x,y,label=name,color="black",marker="x",s="3")

def overworld():
    for area in data["area"]:
        x1,y1,x2,y2,color,name=area
        vertex=[[x1,y1],[x1,y2],[x2,y2],[x2,y1]]
        for coordinate in vertex:
            x,y=coordinate
            plt.plot(x=x,y=y,color=color,label=name,alpha=0.5)
            
def nether():
    x_pos,x_neg,y_pos,y_neg=data["lines"]
    plt.plot([x_pos,x_neg],[0,0],color="blue",linewidth=3,marker=None)
    plt.plot([0,0],[y_pos,y_neg],color="blue",linewidth=3,marker=None)
    
    for sublines in data["sublines"]:
        x1,y1,x2,y2=sublines
        plt.plot([x1,x2],[y1,y2],color="blue",marker=None)

def endworld():
    for endcity in data["endcity"]:
        x,y,ship,description=endcity
        plt.scatter(x=x,y=y,label=f"Ship:{ship}",color="black",marker="x",s=3)

#Load commands
def load():
    if os.path.exists(COMMANDS_FILE):
        with open(COMMANDS_FILE,"r") as f:
            return json.load(f)
    else:
        return {}

#Save commands
def save():
    with open(COMMANDS_FILE,"w") as f:
        json.dump(thisdict,f)

#Main
def draw_map():
    query_params=st.query_params
    map_name=query_params.get("map","overworld")
    thisdict=load()
    data=load().get(map_name,{})

    plt.figure()
    if not data:
        st.write("NOT FOUND")
    else:
        points()
        if map_name=="overworld":
            overworld()
        elif map_name=="nether":
            nether()
        elif map_name=="endworld":
            endworld()

    plt.title(f"Map Guide:{map_name.capitalize()}")
    plt.xlabel("X-coordinate")
    plt.ylabel("Z-coordinate")
    plt.legend()##
    plt.grid(True)
    plt.axis("equal")
    st.pyplot(plt.gcf())
    plt.close()

COMMANDS_FILE="commands.json"
draw_map()
