from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure GenerativeAI library
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to initialize Gemini LLM chat
def initialize_chat():
    model = genai.GenerativeModel("gemini-pro")
    return model.start_chat(history=[])


# Function to get response from Gemini LLM chat
def get_gemini_response(chat, question):
    response = chat.send_message(question, stream=True)
    return response


# Function to load Google Gemini Pro Vision API And get response for medical image analysis
def get_gemini_response_image(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text


# Function to prepare uploaded image for analysis
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


# Initialize Streamlit app
st.set_page_config(page_title="Health Management App")


# Define main content of the app
def main():
    st.title("Health Management App")
    st.write("""
    Welcome to the Health Management App! This app provides two main functionalities:

    1. Medical Chatbot: A chatbot powered by Gemini Pro for answering medical-related questions.

    2. Vital Image Analysis: Analyze medical images to identify anomalies, diseases, or health issues.

    Please select an option from the sidebar to get started.
    """)

    # Add navigation sidebar
    page = st.sidebar.radio("Navigate", ["Home", "Medical Chatbot", "Vital Image Analysis"])

    if page == "Home":
        st.write("Welcome to the Health Management App!")
    elif page == "Medical Chatbot":
        st.subheader("Medical Chatbot")
        chat = initialize_chat()  # Initialize chat
        chat_history = st.session_state.get('chat_history', [])
        question = st.text_input("Input: ", key="input")
        if st.button("Ask the question"):
            response = get_gemini_response(chat, question)
            for chunk in response:
                st.write(chunk.text)
                chat_history.append(("You", question))
                chat_history.append(("Bot", chunk.text))
    elif page == "Vital Image Analysis":
        st.subheader("Vital Image Analysis")
        input_prompt = """
        As a skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a renowned hospital. your expertise is crucial in identifying any anomalies, disease, or health issues that may be present in the images.

        Your Responsibilities include:

        1. Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings
        2. Findings Report: Document all observed anomalies or signs of disease. Clearly articulate these findings in an structured format
        3. Recommendation and Next steps: Based on your analysis, suggest potential next steps, including further tests or treatments as applicable
        4. Treatment Suggestion: If appropriate, recommend possible treatment options or intervention

        Important Notes:
        1. Scope of Response: Only respond if the image pertains to human health issues.
        2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on provided images.'
        3. Disclaimer: Accompany your analysis with the disclaimer: "Consult with a doctor before making any decisions"
        4. Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis, adhering to the structured approach outlined above.
        5. Always provide the answers in English.

        Please provide me an output response with these 4 headings: Detailed Analysis, Findings Report, Recommendation and Next steps, Treatment Suggestion. Mostly give responses in bullet points and always remember to put the disclaimer at the end.
        """
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image.", width=250)
            submit = st.button("Generate the analysis")
            if submit:
                image_data = input_image_setup(uploaded_file)
                response = get_gemini_response_image("", image_data, input_prompt)
                st.subheader("The Response is")
                st.write(response)


if __name__ == "__main__":
    main()
