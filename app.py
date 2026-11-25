
import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Time Management System",
    page_icon="⏰",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

display_df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

model_df = pd.read_csv("processed_dataset.csv")

comparison = pd.read_csv("model_comparison.csv")

model = joblib.load("xgboost_model.pkl")

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("⏰ AI Time Management System")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "👤 User Profile",
        "✅ Task Management",
        "📅 Schedule Planner",
        "📊 Productivity Analytics",
        "🤖 AI Prediction",
        "ℹ️ About"
    ]
)

# ==========================================
# HOME PAGE
# ==========================================

if page == "🏠 Home":

    st.title("⏰ AI Time Management System")

    st.markdown("""
Welcome to the **AI Time Management System Dashboard**.

This application helps organizations monitor employee productivity,
analyze workforce data, manage schedules and tasks, and use Artificial
Intelligence to predict employee attrition.
""")

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Employees", len(display_df))
    c2.metric("Departments", int(display_df["Department"].nunique()))
    c3.metric("Job Roles", int(display_df["JobRole"].nunique()))

    try:
        acc = comparison.loc[
            comparison["Model"] == "XGBoost",
            "Accuracy"
        ].values[0]

        c4.metric("Model Accuracy", f"{acc:.2f}%")

    except:
        c4.metric("Model", "XGBoost")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Employee Distribution")

        fig = px.histogram(
            display_df,
            x="Department",
            color="Department",
            title="Employees by Department"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        st.subheader("Employee Age Distribution")

        fig = px.histogram(
            display_df,
            x="Age",
            nbins=20,
            title="Age Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Dataset Preview")

    st.dataframe(display_df.head(10), use_container_width=True)

# ==========================================
# USER PROFILE
# ==========================================

elif page == "👤 User Profile":

    st.title("👤 Employee Profile")

    employee = st.selectbox(
    "Select Employee",
    range(1, len(display_df)+1)
)


    emp = display_df.iloc[employee-1]

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Personal Details")

        st.write(f"**Age:** {emp['Age']}")
        st.write(f"**Gender:** {emp['Gender']}")
        st.write(f"**Department:** {emp['Department']}")
        st.write(f"**Job Role:** {emp['JobRole']}")
        st.write(f"**Education Field:** {emp['EducationField']}")

    with col2:

        st.subheader("Professional Details")

        st.write(f"**Monthly Income:** ${emp['MonthlyIncome']}")
        st.write(f"**Years at Company:** {emp['YearsAtCompany']}")
        st.write(f"**Total Working Years:** {emp['TotalWorkingYears']}")
        st.write(f"**Job Satisfaction:** {emp['JobSatisfaction']}")
        st.write(f"**Work-Life Balance:** {emp['WorkLifeBalance']}")

    st.divider()

    c1, c2, c3 = st.columns(3)

    c1.metric("Performance Rating", emp["PerformanceRating"])
    c2.metric("Environment Satisfaction", emp["EnvironmentSatisfaction"])
    c3.metric("Relationship Satisfaction", emp["RelationshipSatisfaction"])


# ==========================================
# TASK MANAGEMENT
# ==========================================

elif page == "✅ Task Management":

    st.title("✅ Task Management")

    task = st.text_input("Task Name")

    priority = st.selectbox(
        "Priority",
        ["High", "Medium", "Low"]
    )

    status = st.selectbox(
        "Status",
        ["Pending", "In Progress", "Completed"]
    )

    deadline = st.date_input("Deadline")

    progress = st.slider(
        "Task Progress",
        0,
        100,
        40
    )

    st.progress(progress)

    st.divider()

    st.write("### Task Summary")

    st.write("**Task:**", task)
    st.write("**Priority:**", priority)
    st.write("**Status:**", status)
    st.write("**Deadline:**", deadline)

    if progress == 100:
        st.success("Task Completed Successfully!")

    elif progress >= 70:
        st.info("Task is nearing completion.")

    else:
        st.warning("Task still requires attention.")


# ==========================================
# SCHEDULE PLANNER
# ==========================================

elif page == "📅 Schedule Planner":

    st.title("📅 Schedule Planner")

    meeting = st.text_input("Meeting / Task")

    meeting_date = st.date_input("Meeting Date")

    start_time = st.time_input("Start Time")

    end_time = st.time_input("End Time")

    task_type = st.selectbox(
        "Task Type",
        [
            "Meeting",
            "Coding",
            "Documentation",
            "Research",
            "Testing",
            "Presentation"
        ]
    )

    st.divider()

    work_hours = st.slider(
        "Planned Working Hours",
        1,
        12,
        8
    )

    productive_hours = st.slider(
        "Expected Productive Hours",
        1,
        work_hours,
        min(6, work_hours)
    )

    efficiency = round(productive_hours/work_hours*100,2)

    st.metric(
        "Expected Productivity",
        f"{efficiency}%"
    )

    st.progress(int(efficiency))

    st.divider()

    st.write("### Schedule Summary")

    st.write("**Task:**", meeting)
    st.write("**Task Type:**", task_type)
    st.write("**Date:**", meeting_date)
    st.write("**Start Time:**", start_time)
    st.write("**End Time:**", end_time)

    if efficiency >= 85:
        st.success("Excellent schedule!")

    elif efficiency >= 70:
        st.info("Good time allocation.")

    else:
        st.warning("Consider improving your schedule.")

# ==========================================
# PRODUCTIVITY ANALYTICS
# ==========================================

elif page == "📊 Productivity Analytics":

    st.title("📊 Productivity Analytics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Employees", len(display_df))
    c2.metric("Average Age", round(display_df["Age"].mean(),2))
    c3.metric("Average Income", round(display_df["MonthlyIncome"].mean(),2))
    c4.metric("Average Experience", round(display_df["YearsAtCompany"].mean(),2))

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        fig = px.histogram(
            display_df,
            x="JobSatisfaction",
            color="JobSatisfaction",
            title="Job Satisfaction Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.histogram(
            display_df,
            x="WorkLifeBalance",
            color="WorkLifeBalance",
            title="Work-Life Balance"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        fig = px.box(
            display_df,
            x="Department",
            y="MonthlyIncome",
            color="Department",
            title="Income by Department"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.histogram(
            display_df,
            x="OverTime",
            color="Attrition",
            barmode="group",
            title="Overtime vs Attrition"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    fig = px.scatter(
        display_df,
        x="YearsAtCompany",
        y="MonthlyIncome",
        color="Attrition",
        title="Experience vs Monthly Income"
    )

    st.plotly_chart(fig, use_container_width=True)


# ==========================================
# AI PREDICTION
# ==========================================

elif page == "🤖 AI Prediction":

    st.title("🤖 AI Employee Attrition Prediction")

    employee = st.selectbox(
        "Choose Employee",
        range(1, len(display_df)+1)
    )

    display_emp = display_df.iloc[employee-1]
    model_emp = model_df.iloc[employee-1]

    st.subheader("Selected Employee")

    st.dataframe(
        pd.DataFrame(display_emp).T,
        use_container_width=True
    )

    st.divider()

    if st.button("Predict"):

        X_input = model_emp.drop("Attrition")

        prediction = model.predict(pd.DataFrame([X_input]))[0]

        probability = model.predict_proba(
            pd.DataFrame([X_input])
        )[0]

        stay_probability = probability[0] * 100
        leave_probability = probability[1] * 100

        st.subheader("Prediction Result")

        if prediction == 1:

            st.error("⚠ High Risk of Attrition")

            st.metric(
                "Attrition Probability",
                f"{leave_probability:.2f}%"
            )

            st.progress(int(leave_probability))

            st.warning("""
### AI Recommendation

• Improve work-life balance

• Reduce overtime

• Encourage career development

• Conduct employee feedback sessions

• Recognize employee achievements
""")

        else:

            st.success("✅ Employee Likely to Stay")

            st.metric(
                "Retention Probability",
                f"{stay_probability:.2f}%"
            )

            st.progress(int(stay_probability))

            st.info("""
### AI Recommendation

• Continue employee engagement

• Maintain healthy work environment

• Encourage skill development

• Provide learning opportunities

• Reward consistent performance
""")

# ==========================================
# ABOUT PAGE
# ==========================================

elif page == "ℹ️ About":

    st.title("ℹ️ About AI Time Management System")

    st.markdown("""
## AI Time Management System

This project uses **Artificial Intelligence and Machine Learning**
to help organizations improve employee productivity and efficiently
manage their workforce.

### Features

- 👤 Employee Profile
- ✅ Task Management
- 📅 Schedule Planner
- 📊 Productivity Analytics
- 🤖 AI Prediction using XGBoost

---
""")

    st.subheader("Technology Stack")

    tech = pd.DataFrame({
        "Technology":[
            "Python",
            "Streamlit",
            "Pandas",
            "Plotly",
            "Scikit-Learn",
            "XGBoost",
            "Joblib"
        ],
        "Purpose":[
            "Programming Language",
            "Dashboard",
            "Data Processing",
            "Visualization",
            "Machine Learning",
            "Prediction Model",
            "Model Storage"
        ]
    })

    st.table(tech)

    st.divider()

    st.subheader("Model Performance")

    st.dataframe(
        comparison,
        use_container_width=True
    )

    st.divider()

    st.success("✅ Best Model: XGBoost")

    st.info("""
This dashboard predicts employee attrition using the trained
XGBoost model and provides insights through interactive
visualizations to assist managers in making informed decisions.
""")

    st.divider()

    st.caption("Developed as part of the AI Time Management System Project.")
