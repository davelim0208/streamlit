import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Streamlit UI
st.title("Linear Graphs App")

# Create a dictionary to map button labels to linear functions
button_functions = {
    "Graph 1": lambda x: 2 * x,
    "Graph 2": lambda x: 3 * x,
    "Graph 3": lambda x: -2 * x,
    "Graph 4": lambda x: 0.5 * x,
    "Graph 5": lambda x: -1 * x
}

# Create a selectbox to choose a graph
selected_graph = st.selectbox("Select a graph:", list(button_functions.keys()))

# Create a button to display the selected graph
if st.button("Show Graph"):
    x = np.linspace(-10, 10, 100)
    y = button_functions[selected_graph](x)

    # Create a DataFrame for plotting
    df = pd.DataFrame({'x': x, 'y': y})

    # Plot the graph
    plt.figure(figsize=(8, 6))
    plt.plot(df['x'], df['y'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(selected_graph)
    st.pyplot(plt)

