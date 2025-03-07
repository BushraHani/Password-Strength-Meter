import streamlit as st
import re
# password strength check conditions:
# min 8 chars,digit,upper case,lower case & special characters

#set the app
st.set_page_config(page_title="password strength checker ", page_icon="",layout="centered")


st.title("🔐Password Strength Meter")
st.write("🕵️Enter your password below to check its Security Level.")

#Set the page
def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:    
        feedback.append("❌Password must be at least **8 characters**.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:    
        feedback.append("❌Password must contain **upper n  lower case letter**.")
        
    if re.search(r"[!@#$%^&*(),.?:{}|<>]", password):  
        score += 1
    else:
        feedback.append("❌password must contain at least one **special character (!@#$%^&*(),.?\":{}|<>)**.")
        
    if re.search(r"\d", password):
        score += 1
    else:     
        feedback.append("❌password must contain at least **one digit(0-9)**.")  
            
    #Display the feedback   
    if score == 4:
        st.success("**👍🏻Strong Password**  - Your Password is Secure!")
    elif score == 3 :
        st.info("**🔍Consider Strong Password**.") 
    else:
        st.error("⁉️ **Week Pasword**")  
        
    if feedback:
        with st.expander("**🔍Improve Your Password**."):
             for item in feedback:  # loop through each feedback item and display it in an expander
                 st.write(item)  
password = st.text_input("Enter Your Password:", type="password", help="🔐Ensure your password is strong")              
 
#Button
if st.button("▶️Enter Password"):
    if password:
        check_password_strength(password)
    else:
        st.warning("**⛔Please Enter Your Password First!**")    
        
            
        
