# Health Management App
Welcome to the Health Management App! This application provides an all-in-one solution for managing health-related tasks. It uses Google's Gemini Pro Vision API for advanced image analysis and chat capabilities. The app is developed using Streamlit for a simple and interactive user experience.

---
## Features
**1. Medical Chatbot**
  **Functionality:** A chatbot powered by Gemini Pro to answer medical-related questions.
  **How to Use:**
   - Navigate to the "Medical Chatbot" section in the sidebar.
   - Type your question into the input box and click Ask the question.
   - Get real-time responses from the chatbot.
     
**2. Vital Image Analysis**
**Functionality:** Analyze medical images to identify anomalies, diseases, or health issues.
**How to Use:**
 - Navigate to the "Vital Image Analysis" section in the sidebar.
 - Upload a medical image (JPG/PNG).
 - Click Generate the analysis to get detailed insights, including:
   1. Detailed Analysis
   2. Findings Report
   3. Recommendations
   4. Treatment Suggestions
      
**3. Calorie Calculator**
**Functionality:** Analyze food images to calculate total calories and assess the healthiness of meals.
**How to Use:**
  - Navigate to the "Calorie Calculator" section in the sidebar.
  - Upload a food image (JPG/PNG).
  - Click Tell me the total calories to get:
    1. Breakdown of calories for each food item.
    2. Advice for a healthier lifestyle.
---
## Technologies Used
- **Python**
- **Streamlit:** Interactive UI
- **Pillow (PIL):** Image processing
- **Google Generative AI (Gemini Pro Vision):** For advanced image and chat capabilities
- **dotenv:** Manage environment variables
---
## Installation
1. Clone the repository:

```bash
git clone https://github.com/your-repo/health-management-app.git
cd health-management-app
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```
3. Create a .env file and add your Google API key:
```bash
GOOGLE_API_KEY=your_google_api_key
```
4. Run the app:

```bash
streamlit run app.py
```
---
## Example Screenshots
