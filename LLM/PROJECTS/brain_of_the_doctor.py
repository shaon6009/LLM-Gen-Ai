import os
import base64
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

def encode_image(image_path):   
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_image_with_query(query, model, encoded_image=None):
    client = Groq()  
    messages = []

    if encoded_image:
        messages.append({
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
            ]
        })
    else:
        messages.append({
            "role": "user",import os
import base64
import streamlit as st
from groq import Groq

GROQ_API_KEY = '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'

def encode_image(image_path):   
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_image_with_query(query, model, encoded_image=None):
    client = Groq(api_key=GROQ_API_KEY)  
    messages = []

    if encoded_image:
        messages.append({
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
            ]
        })
    else:
        messages.append({
            "role": "user",
            "content": [{"type": "text", "text": query}]
        })

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

def main():
    st.set_page_config(page_title="AI Medical Assistant", page_icon="🩺", layout="wide")

    st.title("🩺 AI Medical Assistant 🩺")

    st.markdown("Welcome to the **AI Medical Assistant**! You can interact by either typing a query or uploading an image for analysis.")

    choice = st.radio("Choose your interaction mode:", ('Text', 'Image'), key="interaction_type")

    if choice == "Text":
        st.subheader("Ask a health-related question:")
        query = st.text_input("Type your query here:")
        if query:
            model = "llama3-70b-8192"
            response = analyze_image_with_query(query, model)
            st.write(f"🩺 **AI Response:** {response}")


    elif choice == "Image":
        st.subheader("Upload an image for analysis:")
        image_file = st.file_uploader("Upload an image (jpg, jpeg, png):", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
        
        if image_file:
            image_size = image_file.size / 1024  
            if image_size > 512:  
                st.error("Please upload an image smaller than 512 KB.")
            else:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
                query = "Analyze this image"
                model = "llama3-70b-8192"
                response = analyze_image_with_query(query, model, encoded_image)

                st.image(image_file, caption="Uploaded Image", use_column_width=True)
                st.write(f"🩺 **AI Response:** {response}")

    continue_chat = st.radio("Do you need more info or have all the info?", ('Yes', 'No'))
    if continue_chat == 'No':
        st.write("🩺 **Thank you for using the AI Assistant!**")
    
if __name__ == "__main__":
    main()

            "content": [{"type": "text", "text": query}]
        })

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

def main():
    st.set_page_config(page_title="AI Medical Assistant", page_icon="🩺", layout="wide")

    st.title("🩺 AI Medical Assistant 🩺")

    st.markdown("Welcome to the **AI Medical Assistant**! You can interact by either typing a query or uploading an image for analysis.")

    choice = st.radio("Choose your interaction mode:", ('Text', 'Image'), key="interaction_type")

    if choice == "Text":
        st.subheader("Ask a health-related question:")
        query = st.text_input("Type your query here:")
        if query:
            model = "llama3-70b-8192"
            response = analyze_image_with_query(query, model)
            st.write(f"🩺 **AI Response:** {response}")


    elif choice == "Image":
        st.subheader("Upload an image for analysis:")
        image_file = st.file_uploader("Upload an image (jpg, jpeg, png):", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
        
        if image_file:
            image_size = image_file.size / 1024  
            if image_size > 512:  
                st.error("Please upload an image smaller than 512 KB.")
            else:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
                query = "Analyze this image"
                model = "llama3-70b-8192"
                response = analyze_image_with_query(query, model, encoded_image)

                st.image(image_file, caption="Uploaded Image", use_column_width=True)
                st.write(f"🩺 **AI Response:** {response}")

    continue_chat = st.radio("Do you need more info or have all the info?", ('Yes', 'No'))
    if continue_chat == 'No':
        st.write("🩺 **Thank you for using the AI Assistant!**")
    
if __name__ == "__main__":
    main()
