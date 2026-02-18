import streamlit as st

# Page Configuration
st.set_page_config(page_title="AI Career Prep System", layout="wide")

# Title and Description
st.title("🚀 AI-Powered Career Prep & Interview System")
st.markdown("Prepare for your dream job with AI-driven mock interviews.")

# --- MODULE 1: Role Selector (15 Roles) ---
# roles = [
#     "Software Engineer", "Data Scientist", "Product Manager", 
#     "UX Designer", "DevOps Engineer", "Marketing Analyst",
#     "Business Analyst", "Cybersecurity Expert", "Cloud Architect",
#     "AI Engineer", "HR Specialist", "Sales Manager",
#     "Full Stack Developer", "Database Administrator", "Project Manager"
# ]

# with st.sidebar:
#     st.header("Settings")
#     selected_role = st.selectbox("Select Your Career Role:", roles)
#     st.write(f"**Target Role:** {selected_role}")
    
#     # Reset button for Session State
#     if st.button("Clear Chat"):
#         st.session_state.messages = []
#         st.rerun()

# # --- MODULE 1: Session State Management ---
# # User ki progress aur chat history ko save rakhne ke liye [1]
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # --- MODULE 1: Basic Chat Interface ---
# # User se input lene ke liye [1]
# if prompt := st.chat_input(f"Ask me anything about {selected_role} interview..."):
#     # User message ko UI mein dikhana
#     with st.chat_message("user"):
#         st.markdown(prompt)
    
#     # Session state mein message add karna
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     # AI Response placeholder (Yeh Module 3 aur 4 mein connect hoga)
#     response = f"Welcome! You've selected the {selected_role} role. Let's start your preparation."
    
#     with st.chat_message("assistant"):
#         st.markdown(response)
    
#     # Session state mein assistant message add karna
#     st.session_state.messages.append({"role": "assistant", "content": response})
# Module 1 ke Specs kaise poore hue?
# • GitHub repo + requirements.txt: Maine file list de di hai jo aap repo mein dalenge.
# • Streamlit app.py skeleton: Upar diya gaya code app.py ka base hai.
# • Role selector dropdown: Sidebar mein 15 roles ka dropdown implement kiya gaya hai.
# • Basic chat interface: st.chat_input aur st.chat_message ka use karke chat UI banayi gayi hai.
# • Session state management: st.session_state.messages ka istemal kiya gaya hai taaki refresh hone par chat history delete na ho.
# Agla Step: Ab aapko Module 2 par kaam karna hoga, jisme aapko 1,125 Q&A pairs wala JSON database taiyar karna hai. Kya aapko pata hai ki JSON structure kaisa hona chahiye ya main usme madad karoon?
# Ye fodeer github me banaya h me isi same foder ko vscode me kaise open karu

# GitHub par banaye gaye repository (folder) ko VS Code mein open karne ke liye aapko use Clone karna hoga. Sources mein iska direct manual nahi diya gaya hai, lekin Module 1 ke liye GitHub repo setup karna ek anivarya (essential) step hai.
# Yahan step-wise bataya gaya hai ki aap ise VS Code mein kaise open kar sakte hain (yeh jaankari sources se bahar ki hai, isliye ise dhyan se dekhein):
# Step 1: GitHub se Repository URL copy karein
# 1. Apne GitHub account par jayein aur us repository ko kholein jo aapne banayi hai.
# 2. Hare rang ke "<> Code" button par click karein.
# 3. HTTPS tab ke andar diye gaye URL ko copy kar lein (e.g., https://github.com/username/project-name.git).
# Step 2: VS Code mein Clone karein
# 1. VS Code open karein.
# 2. Ctrl + Shift + P (Mac par Cmd + Shift + P) dabayein aur search bar mein likhein: "Git: Clone".
# 3. Jo URL aapne copy kiya tha, use yahan paste kar dein aur Enter dabayein.
# 4. Ek folder select karein jahan aap is project ko save karna chahte hain.
# Step 3: VS Code mein Folder open karein
# • Clone poora hone ke baad, VS Code aap se
