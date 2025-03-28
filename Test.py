import streamlit as st
import matplotlib.pyplot as plt

st.title("Minecraft不知道")

# Function to draw the map
def draw_map():
    plt.figure()
    plt.plot([0, 10], [0, 10], label="Path 1", color='blue')
    plt.plot([0, 10], [10, 0], label="Path 2", color='red')
    plt.title("Minecraft Map Guide")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    st.pyplot(plt.gcf())
    plt.close()

# Render the map
draw_map()
