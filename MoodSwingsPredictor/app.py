import streamlit as st
import pandas as pd
import csv
import os

# Feedback storage
feedback_file = 'combined_feedback.csv'

st.title("🧠 Mood Swings Predictor")
st.sidebar.header("Navigation")
app_mode = st.sidebar.radio("Choose Section", [
    "🏠 Home",
    "🩸 Menstruation Mood Predictor",
    "🌙 Menopause Mood Predictor",
    "📝 Feedback"
])

# Rule-based menstruation prediction
def predict_mood_menstruation(data):
    symptoms = ['Acne', 'Bloating', 'Backpain', 'Headache', 'Sagging Breasts']
    score = sum(1 for s in symptoms if data[s] == 'Yes')
    if data['Stress Level'] == 'High' or score >= 3 or data['Quality of Sleep'] == 'Poor':
        return 'Yes'
    return 'No'

# Rule-based menopause prediction
def predict_mood_menopause(data):
    flags = [
        data['Hot Flashes'] in ['Severe'],
        data['Night Sweats'] in ['Severe', 'Very Severe'],
        data['Weight Gain'] in ['Moderate'],
        data['Sleep Quality'] == 'Mild',
        data['Prior Mental Health Issues'] in ['Yes', 'Mild'],
        data['Social Life'] in ['Severe'],
        data['General Body Pains'] in ['Severe']
    ]
    if sum(flags) >= 2:
        return 'Yes'
    return 'No'

# Home Page
if app_mode == "🏠 Home":
    st.subheader("Welcome!")
    st.markdown("This app predicts whether a user is likely to experience **Mood Swings** based on symptoms associated with menstruation and menopause.")

# Menstruation Mood Swings Predictor
elif app_mode == "🩸 Menstruation Mood Predictor":
    st.subheader("🩸 Mood Swings Predictor (Menstruation Phase)")
    with st.form("menstruation_form"):
        age_group = st.selectbox("Age Group", ["Youngster", "Women"])
        regular_exercise = st.selectbox("Regular Exercise", ["Yes", "No"])
        balanced_diet = st.selectbox("Balanced Diet", ["Yes", "No"])
        stress_level = st.selectbox("Stress Level", ["Low", "Medium", "High"])
        acne = st.selectbox("Acne", ["Yes", "No"])
        bloating = st.selectbox("Bloating", ["Yes", "No"])
        backpain = st.selectbox("Backpain", ["Yes", "No"])
        headache = st.selectbox("Headache", ["Yes", "No"])
        sagging_breasts = st.selectbox("Sagging Breasts", ["Yes", "No"])
        quality_of_sleep = st.selectbox("Quality of Sleep", ["Good", "Average", "Poor"])
        menstrual_phase = st.selectbox("Menstrual Phase", ["Follicular", "Ovulation", "Luteal", "Menstruation"])
        submit = st.form_submit_button("Predict Mood Swings")

    if submit:
        input_data = {
            'Age Group': age_group,
            'Regular Exercise': regular_exercise,
            'Balanced Diet': balanced_diet,
            'Stress Level': stress_level,
            'Acne': acne,
            'Bloating': bloating,
            'Backpain': backpain,
            'Headache': headache,
            'Sagging Breasts': sagging_breasts,
            'Quality of Sleep': quality_of_sleep,
            'Menstrual Phase': menstrual_phase
        }
        prediction = predict_mood_menstruation(input_data)
        st.success(f"Predicted Mood Swings: **{prediction}**")
        if prediction == 'Yes':
            st.markdown("### 🌟 Suggestions for Mood Swings During Menstruation:")
            st.markdown("""
            - 🏃 Engage in regular physical activity.
            - 🥗 Eat a diet rich in whole foods and avoid sugar overload.
            - 🧘 Practice relaxation methods like yoga or breathing exercises.
            - 📒 Maintain a mood diary.
            - 🩺 Consult a doctor if swings are severe or disruptive.
            """)

# Menopause Mood Swings Predictor
elif app_mode == "🌙 Menopause Mood Predictor":
    st.subheader("🌙 Mood Swings Predictor (Menopause Phase)")
    with st.form("menopause_form"):
        age = st.number_input("Age", min_value=40, value=45)
        menopause_status = st.selectbox("Menopause Status", ["Premenopause", "Perimenopause", "Postmenopause"])
        irregular_menstruation = st.selectbox("Irregular Menstruation", ["Yes", "No"])
        vaginal_dryness = st.selectbox("Vaginal Dryness", ["Yes", "No"])
        hot_flashes = st.selectbox("Hot Flashes", ["Mild", "Moderate", "Severe"])
        chills = st.selectbox("Chills", ["No", "Mild", "Moderate", "Severe"])
        night_sweats = st.selectbox("Night Sweats", ["Mild", "Moderate", "Severe", "Very Severe"])
        weight_gain = st.selectbox("Weight Gain", ["No", "Mild", "Moderate"])
        metabolic_slowing = st.selectbox("Metabolic Slowing", ["No", "Moderate", "Yes"])
        severe_pms = st.selectbox("Severe PMS", ["No", "Mild", "Yes"])
        prior_mental_health_issues = st.selectbox("Prior Mental Health Issues", ["No", "Mild", "Yes"])
        diet_and_nutrition = st.selectbox("Diet and Nutrition", ["Balanced", "Unbalanced"])
        sleep_quality = st.selectbox("Sleep Quality", ["Mild", "Moderate"])
        physical_activity = st.selectbox("Physical Activity", ["Low", "Moderate", "High"])
        social_life = st.selectbox("Social Life", ["Mild", "Moderate", "Severe"])
        joint_pains = st.selectbox("Joint Pains", ["Yes", "No"])
        general_pains = st.selectbox("General Body Pains", ["No", "Mild", "Moderate", "Severe"])
        submit2 = st.form_submit_button("Predict Mood Swings")

    if submit2:
        input_data = {
            'Hot Flashes': hot_flashes,
            'Night Sweats': night_sweats,
            'Weight Gain': weight_gain,
            'Sleep Quality': sleep_quality,
            'Prior Mental Health Issues': prior_mental_health_issues,
            'Social Life': social_life,
            'General Body Pains': general_pains
        }
        prediction = predict_mood_menopause(input_data)
        st.success(f"Predicted Mood Swings: **{prediction}**")
        if prediction == 'Yes':
            st.markdown("### 🌟 Suggestions for Mood Swings During Menopause:")
            st.markdown("""
            - 🏃 Stay active with daily movement or walking.
            - 🍽️ Eat hormone-friendly foods like flaxseed, tofu, and leafy greens.
            - 🧘 Practice meditation or stress-relieving routines.
            - 🧑‍🤝‍🧑 Stay socially connected with family or friends.
            - 🩺 Consult a gynecologist for therapy or HRT.
            """)

# Feedback Section
elif app_mode == "📝 Feedback":
    st.subheader("Feedback Form")
    with st.form("feedback_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", 10, 100, 30)
        usefulness = st.selectbox("Was the app useful?", ["Yes", "No"])
        mood_swings = st.selectbox("Are you experiencing mood swings?", ["Yes", "No"])
        phase_type = st.radio("Which phase?", ["Menstruation", "Menopause"])
        medicine = st.text_input("Any medicines taken?")
        thoughts = st.text_area("Thoughts on Mood Swings")
        suggestion = st.text_area("Your Suggestions")
        submit = st.form_submit_button("Submit Feedback")

    if submit:
        file_exists = os.path.exists(feedback_file)
        with open(feedback_file, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['Name', 'Age', 'Usefulness', 'Mood Swings', 'Phase', 'Medicine', 'Thoughts', 'Suggestion'])
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                'Name': name,
                'Age': age,
                'Usefulness': usefulness,
                'Mood Swings': mood_swings,
                'Phase': phase_type,
                'Medicine': medicine,
                'Thoughts': thoughts,
                'Suggestion': suggestion
            })

        st.success("✅ Thank you for your feedback!")

        if mood_swings == "Yes":
            if phase_type == "Menstruation":
                st.markdown("### 🌟 Suggestions for Mood Swings During Menstruation:")
                st.markdown("""
                - Exercise regularly, eat balanced meals, and manage stress.
                - Try journaling, relaxation exercises, and seek medical help if needed.
                """)
            else:
                st.markdown("### 🌟 Suggestions for Mood Swings During Menopause:")
                st.markdown("""
                - Maintain physical activity, balanced nutrition, and emotional support.
                - Seek medical help if mood changes are affecting daily life.
                """)
