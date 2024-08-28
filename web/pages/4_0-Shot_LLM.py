import streamlit as st
st.title("Zero-shot Model Page")
st.write("We proceeded to try to use Large Language Models (LLMs) to analyse our retinal fundus images.")
st.subheader("About LLMs")
st.write("LLMs are a form of Generative Artificial Intelligence (GenAI) model that comprehends and generates language text that can be comprehended by a human. They are used in almost if not all GenAI Chatbots that dominate school life, including ChatGPT by OpenAI and Google's Gemini AI.")
st.write("Recent advances in LLM technology has allowed some LLMs to have vision capabilities, i.e., they are able to receive image inputs, interpret these images and output understandable text about the image.")
st.subheader("About Zero-shot learning")
st.write("Zero-shot learning refers to the model being given images not shown during training and classifying them. In this case, we used a LLM model with vision capabilities, and gave it a small testing dataset of retinal fundus images to gauge its proficiency in diagnosing the diseases.")
st.write("The model we used was Chatgpt-4o, with temperature set to 0 (same for few-shot learning as well). Temperature is a parameter that influences how creative it is, and in this case we need the outputs to be logical and predictable, so a low temperature is required. In the prompt, the model was instructed to only respond with the name of the disease for easy validation.")
st.subheader("Limitations of Zero-shot learning")
st.write("Due to the lack of exposure to the images, the machine is prone to misinterpreting the image and giving an incorrect diagnosis. This is especially apparent in eye disease detection due to the similarities between the two images (all are retinal fundus images and look generally similar).")
st.write("As the machine does not have a reference prompt template, the machine may not generate the prompt in the format requested by the user, which may pose problems in understanding and explainability.")