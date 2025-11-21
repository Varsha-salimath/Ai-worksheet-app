# 🌟 **InfinityLearn AI Worksheet Generator**  
_Revolutionizing worksheet creation with AI_

<p align="center">
  <img src="https://img.shields.io/badge/Powered%20By-Google%20Gemini%20AI-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Built%20With-Streamlit-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Tracking-Langfuse%20v3-purple?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/PDF%20Generation-ReportLab-green?style=for-the-badge"/>
</p>

---

## 🚀 **About the Project**

The **InfinityLearn AI Worksheet Generator** is an intelligent, fast, and easy-to-use platform that creates **high-quality, curriculum-aligned worksheets** for students from **Grade 1 to Grade 12**.

Built using **Google Gemini**, it generates:
- Thought-provoking questions  
- Clean, beautifully formatted PDFs  
- Optional answer keys  
- Subject & chapter-specific content  

Designed for teachers, parents, coaching institutes, and students.

---

## ✨ **Key Features**

### 🔹 **AI-Powered Question Generation**
Generate worksheets instantly using **Google Gemini AI** with customizable:
- Grade  
- Subject  
- Chapter  
- Difficulty  
- Number of Questions  

---

### 🔹 **Beautiful PDF Export**
Automated PDF creation with:
- Clean structured formatting  
- Optional answer key  
- InfinityLearn branding  
- Custom file name  
- Download button  

---

### 🔹 **Langfuse v3 Analytics**
The app integrates **Langfuse v3** for:
- Tracing  
- Event logging  
- Usage analytics  
- Cost optimization monitoring  

---

### 🔹 **Modern UI with Streamlit**
- Responsive layout  
- Smooth animations  
- Styled components  
- User-friendly flow  

---

## 🛠 **Tech Stack**

| Component | Technology |
|----------|------------|
| Frontend UI | Streamlit |
| AI Engine | Google Gemini API |
| PDF Engine | ReportLab |
| Usage Analytics | Langfuse v3 |
| Language | Python |
| Deployment | Streamlit Cloud |

---

## 📸 **Screenshots**

> _Add screenshots here after deploying_

```
![Home Page](screenshots/homepage.png)
![Form Page](screenshots/form.png)
![Generated PDF Preview](screenshots/pdf_preview.png)
```

---

## 📦 **Project Structure**

```
Ai-worksheet-app/
│── app.py  
│── requirements.txt  
│── .streamlit/
│     └── runtime.txt
│── services/
│     ├── gemini_service.py
│     ├── pdf_service.py
│     ├── langfuse_helper.py
│── components/
│     ├── worksheet_form.py
│── utils/
│     ├── data.py
│── assets/
│     └── icons, styles
```

---

## ⚙️ **Installation (Local Setup)**

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Varsha-salimath/Ai-worksheet-app.git
cd Ai-worksheet-app
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add your API keys in `.env`

```
GOOGLE_API_KEY="your_key"
LANGFUSE_PUBLIC_KEY="your_public_key"
LANGFUSE_SECRET_KEY="your_secret_key"
LANGFUSE_HOST="https://hipaa.cloud.langfuse.com"
```

### 5️⃣ Run the app

```bash
streamlit run app.py
```

---

## ☁️ **Deploying to Streamlit Cloud**

1. Push your project to GitHub  
2. Go to **share.streamlit.io**  
3. Select repo → choose branch **main**  
4. Set main file: `app.py`  
5. Add Streamlit secrets  

🎉 Done! Your app will go live instantly.

---

## 🔐 **Environment Variables**

Add these in **Streamlit → Settings → Secrets**:

```
GOOGLE_API_KEY = "your_key"
LANGFUSE_PUBLIC_KEY = "your_key"
LANGFUSE_SECRET_KEY = "your_key"
LANGFUSE_HOST = "https://hipaa.cloud.langfuse.com"
```

---

## 🧪 **Gemini Prompting Strategy**

The system uses:
- Smart contextual prompts  
- Chapter-wise question generation  
- AI-driven parsing  
- Clean formatting pipeline  

---

## 🤝 **Contributing**

Pull requests are welcome!  
Please open an issue if you want a new feature.

---

## 📄 License

This project is owned & maintained by **Varsha Salimath – Infinity Learn**.  
All rights reserved © 2025.

---

## ⭐ **Support the Project**

If you like this project:

✔️ Star the repo ⭐  
✔️ Share with educators  
✔️ Suggest new features  

---

## 💬 Need Help?
Email: `salimathvarsha7@gmail.com`  
InfinityLearn EdTech

---
##💛 Author

Varsha Salimath

AI Engineer | InfinityLearn
For queries: Reach out anytime!
