import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random
import time
from datetime import datetime, timedelta

# Configure page
st.set_page_config(
    page_title="MathCraft Sports Pro | Quadratics & Athletic Performance",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 2.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .section-header {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .standards-box {
        background: linear-gradient(145deg, #e8f5e8 0%, #f0f8ff 100%);
        border: 2px solid #4caf50;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    .achievement-badge {
        background: linear-gradient(45deg, #ff6b6b, #feca57);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin: 0.25rem;
    }
</style>
""", unsafe_allow_html=True)

# Session state init
def initialize_session_state():
    defaults = {
        'student_name': '',
        'course_level': 'High School',
        'grade_level': '9th Grade',
        'standards_focus': 'Common Core',
        'sports_interests': [],
        'research_focus': 'Performance Optimization',
        'total_problems_solved': 0,
        'sports_analyzed': set(),
        'achievements': [],
        'session_start': time.time(),
        'trajectory_points': 0,
        'optimization_score': 0,
        'research_projects': [],
        'peer_collaborations': 0,
        'current_sport': 'Basketball',
        'difficulty_level': 'Intermediate',
        'real_data_analyzed': False,
        'university_modules_completed': set(),
        'study_groups_joined': [],
        'research_papers_read': 0,
        'peer_reviews_completed': 0,
        'mentorship_sessions': 0,
        'standards_mastered': set()
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

initialize_session_state()

# Achievement logic
def check_achievements():
    new_achievements = []
    achievements_criteria = {
        "Quadratic Explorer": st.session_state.total_problems_solved >= 1,
        "Sports Analyst": len(st.session_state.sports_analyzed) >= 3,
        "Optimization Expert": st.session_state.optimization_score >= 50,
        "Research Scholar": len(st.session_state.research_projects) >= 1,
        "Team Player": st.session_state.peer_collaborations >= 5,
        "Standards Master": len(st.session_state.standards_mastered) >= 5,
        "Data Scientist": st.session_state.real_data_analyzed,
        "Quadratics Olympian": st.session_state.total_problems_solved >= 25,
        "Collaborative Learner": len(st.session_state.study_groups_joined) >= 2,
        "Academic Reader": st.session_state.research_papers_read >= 5,
        "Peer Reviewer": st.session_state.peer_reviews_completed >= 3,
        "Common Core Champion": "Common Core" in st.session_state.standards_focus,
        "Advanced Modeler": st.session_state.optimization_score >= 100,
        "Multi-Sport Expert": len(st.session_state.sports_analyzed) >= 5
    }
    for achievement, passed in achievements_criteria.items():
        if passed and achievement not in st.session_state.achievements:
            st.session_state.achievements.append(achievement)
            new_achievements.append(achievement)
    return new_achievements

def calculate_user_level():
    points = (st.session_state.total_problems_solved * 5 +
              st.session_state.optimization_score +
              len(st.session_state.research_projects) * 25 +
              st.session_state.peer_collaborations * 2 +
              len(st.session_state.standards_mastered) * 10)
    if points < 50:
        return "Novice", 1
    elif points < 150:
        return "Intermediate", 2
    elif points < 300:
        return "Advanced", 3
    elif points < 500:
        return "Expert", 4
    else:
        return "Master", 5

# Header
st.markdown("""
<div class="main-header">
    <h1>🏆 MathCraft Sports Pro: Quadratics & Athletic Performance</h1>
    <h3>Master Quadratic Functions Through Real-World Sports Applications</h3>
    <p>Completing the Square • Vertex Form • Parabolic Trajectories • Sports Analytics • Standards-Aligned Learning</p>
</div>
""", unsafe_allow_html=True)

# Student profile onboarding
if not st.session_state.student_name:
    with st.container():
        st.markdown("""
        <div class="standards-box">
        <h2>👋 Welcome to MathCraft Sports Pro!</h2>
        <p>Master quadratic functions through sports applications while meeting rigorous academic standards.</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Student Name:", placeholder="Enter your full name")
            grade_level = st.selectbox("Grade Level:", [
                "8th Grade", "9th Grade (Algebra 1)", "10th Grade (Geometry)",
                "11th Grade (Algebra 2)", "12th Grade (Pre-Calculus)",
                "College Freshman", "College Sophomore", "Advanced Placement"
            ])
            standards_focus = st.selectbox("Educational Standards:", [
                "Common Core", "NGSS", "TEKS", "California State Standards",
                "IB", "AP Standards", "Australian Curriculum", 
                "UK National Curriculum", "Ontario Curriculum", "University"
            ])
        with col2:
            interests = st.multiselect("Sports of Interest:", [
                "Basketball", "Soccer", "Tennis", "Football", "Golf", 
                "Baseball", "Track & Field", "Swimming", "Volleyball"
            ], default=["Basketball"])
            math_focus = st.multiselect("Quadratic Focus Areas:", [
                "Completing the Square", "Vertex Form", "Factoring", 
                "Quadratic Formula", "Graphing", "Applications",
                "Optimization", "Systems with Quadratics"
            ], default=["Vertex Form"])
            learning_style = st.selectbox("Preferred Learning Style:", [
                "Visual", "Kinesthetic", "Analytical", "Collaborative", "Independent"
            ])
        institution = st.text_input("School/Institution:", placeholder="Optional")

        if st.button("🚀 Begin Quadratic Mastery Journey!") and name:
            st.session_state.student_name = name
            st.session_state.grade_level = grade_level
            st.session_state.standards_focus = standards_focus
            st.session_state.sports_interests = interests
            st.session_state.math_focus = math_focus
            st.session_state.learning_style = learning_style
            st.session_state.institution = institution
            st.rerun()

# Sidebar
st.sidebar.title("📌 Navigation")
if st.session_state.student_name:
    user_level, level_num = calculate_user_level()
    st.sidebar.markdown(f"👋 Hello, **{st.session_state.student_name}**")
    st.sidebar.markdown(f"🎓 *{st.session_state.grade_level}*")
    st.sidebar.markdown(f"📘 *{st.session_state.standards_focus}*")
    st.sidebar.markdown(f"🏅 Level {level_num} – {user_level}")

section = st.sidebar.selectbox("Go To Module", [
    "📚 Quadratic Theory Hub", "🔬 Interactive Lab", 
    "🏀 Sports Analysis Center", "📊 Real Data Analytics",
    "🎯 Optimization Studio", "🔬 Research Projects", 
    "🏆 Performance Dashboard", "📖 Standards & Resources", 
    "👥 Collaboration Center", "🎓 Standards Tracker"
])

difficulty_opts = {
    "Common Core": ["Algebra 1", "Geometry", "Algebra 2", "Pre-Calc", "College"],
    "AP Standards": ["AP Algebra", "AP Calculus AB", "AP Statistics"]
}
default_diff = difficulty_opts.get(st.session_state.standards_focus, ["Beginner", "Intermediate", "Advanced", "University"])
st.session_state.difficulty_level = st.sidebar.selectbox("Difficulty:", default_diff)
st.session_state.current_sport = st.sidebar.selectbox("Sport:", [
    "Basketball", "Soccer", "Football", "Baseball", "Track & Field", "Tennis", "Swimming"
])

# Sidebar stats
st.sidebar.markdown("### 📈 Progress")
st.sidebar.metric("Problems", st.session_state.total_problems_solved)
st.sidebar.metric("Standards", len(st.session_state.standards_mastered))
st.sidebar.metric("Points", st.session_state.optimization_score)

# Time tracking
elapsed = time.time() - st.session_state.session_start
h, rem = divmod(elapsed, 3600)
m, _ = divmod(rem, 60)
st.sidebar.metric("Time", f"{int(h):02}:{int(m):02}")

# Achievements
if st.session_state.achievements:
    st.sidebar.markdown("### 🏆 Achievements")
    for a in st.session_state.achievements[-3:]:
        st.sidebar.markdown(f'<div class="achievement-badge">{a}</div>', unsafe_allow_html=True)

# Quick Launch
st.sidebar.markdown("### ⚡ Quick Start")
if st.sidebar.button("Go to Lab"):
    section = "🔬 Interactive Lab"
if st.sidebar.button("Track Standards"):
    section = "🎓 Standards Tracker"

# Route content based on selected section
if section == "🔬 Interactive Lab":
    st.header("🔬 Interactive Quadratic Lab")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎛 Quadratic Controls")
        a = st.slider("a", -2.0, 2.0, -0.5, 0.1)
        b = st.slider("b", -5.0, 5.0, 2.0, 0.5)
        c = st.slider("c", -10.0, 10.0, 5.0, 0.5)

        if a != 0:
            h = -b / (2 * a)
            k = a * h**2 + b * h + c
            st.markdown(f"**Standard Form**: f(x) = {a}x² + {b}x + {c}")
            st.markdown(f"**Vertex Form**: f(x) = {a}(x - {h:.2f})² + {k:.2f}")
            st.markdown(f"**Vertex**: ({h:.2f}, {k:.2f})")

    with col2:
        if a != 0:
            x = np.linspace(h - 5, h + 5, 100)
            y = a * x**2 + b * x + c
            fig, ax = plt.subplots()
            ax.plot(x, y, label='Trajectory')
            ax.plot(h, k, 'ro', label='Vertex')
            ax.grid(True)
            ax.legend()
            st.pyplot(fig)

    st.session_state.total_problems_solved += 1
    st.session_state.standards_mastered.add("A-SSE.A.2")

elif section == "🎓 Standards Tracker":
    st.header("🎓 Standards You've Mastered")
    if st.session_state.standards_mastered:
        for s in sorted(st.session_state.standards_mastered):
            st.success(f"✅ {s}")
    else:
        st.warning("Complete activities to master standards!")

elif section == "📚 Quadratic Theory Hub":
    st.header("📚 Theory Hub: What are Quadratics?")
    st.markdown("""
    Quadratic functions model curved motion – like a basketball in flight!  
    Standard form is `f(x) = ax² + bx + c`, where `a`, `b`, and `c` are real numbers and `a ≠ 0`.
    """)

elif section == "🏆 Performance Dashboard":
    st.header("🏆 Performance Overview")
    st.metric("Problems Solved", st.session_state.total_problems_solved)
    st.metric("Optimization Score", st.session_state.optimization_score)
    st.metric("Projects", len(st.session_state.research_projects))
    st.metric("Achievements", len(st.session_state.achievements))

else:
    st.info("Select a learning module from the sidebar to begin.")

# New achievements check
for ach in check_achievements():
    st.sidebar.success(f"🏅 New: {ach}")
