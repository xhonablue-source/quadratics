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

# Custom CSS for professional styling
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
    .formula-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        font-family: 'Courier New', monospace;
    }
    .performance-metric {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem;
    }
    .university-level {
        border-left: 4px solid #667eea;
        background: #f8f9fa;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for progress tracking
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
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

initialize_session_state()

# Enhanced achievement system
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
    
    for achievement, criteria in achievements_criteria.items():
        if criteria and achievement not in st.session_state.achievements:
            new_achievements.append(achievement)
            st.session_state.achievements.append(achievement)
    
    return new_achievements

# Calculate user level based on total points
def calculate_user_level():
    total_points = (st.session_state.total_problems_solved * 5 + 
                   st.session_state.optimization_score + 
                   len(st.session_state.research_projects) * 25 +
                   st.session_state.peer_collaborations * 2 +
                   len(st.session_state.standards_mastered) * 10)
    
    if total_points < 50:
        return "Novice", 1
    elif total_points < 150:
        return "Intermediate", 2
    elif total_points < 300:
        return "Advanced", 3
    elif total_points < 500:
        return "Expert", 4
    else:
        return "Master", 5

# Main header with updated name
st.markdown("""
<div class="main-header">
    <h1>🏆 MathCraft Sports Pro: Quadratics & Athletic Performance</h1>
    <h3>Master Quadratic Functions Through Real-World Sports Applications</h3>
    <p>Completing the Square • Vertex Form • Parabolic Trajectories • Sports Analytics • Standards-Aligned Learning</p>
</div>
""", unsafe_allow_html=True)

# Enhanced student profile setup
if not st.session_state.student_name:
    with st.container():
        st.markdown("""
        <div class="standards-box">
        <h2>👋 Welcome to MathCraft Sports Pro: Quadratics & Athletic Performance!</h2>
        <p>Master quadratic functions through engaging sports applications while meeting rigorous academic standards.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📋 Student Profile")
            name = st.text_input("Student Name:", placeholder="Enter your full name", key="name_input")
            
            # Enhanced grade level selection
            grade_level = st.selectbox("Grade Level:", 
                                     ["8th Grade", "9th Grade (Algebra 1)", "10th Grade (Geometry)", 
                                      "11th Grade (Algebra 2)", "12th Grade (Pre-Calculus)",
                                      "College Freshman", "College Sophomore", "Advanced Placement"])
            
            # Comprehensive standards selection
            standards_focus = st.selectbox("Educational Standards:", [
                "Common Core State Standards (CCSS)",
                "Next Generation Science Standards (NGSS)", 
                "Texas Essential Knowledge and Skills (TEKS)",
                "California State Standards",
                "International Baccalaureate (IB)",
                "Advanced Placement (AP) Standards",
                "Australian Curriculum",
                "UK National Curriculum",
                "Ontario Curriculum (Canada)",
                "University/College Level"
            ])
        
        with col2:
            st.markdown("### 🎯 Learning Focus")
            
            # Sports interests
            interests = st.multiselect("Sports of Interest:", 
                                     ["Basketball", "Soccer", "Tennis", "Football", "Golf", 
                                      "Baseball", "Track & Field", "Swimming", "Volleyball", 
                                      "Hockey", "Archery", "Other"],
                                     default=["Basketball"])
            
            # Mathematical focus areas
            math_focus = st.multiselect("Quadratic Function Focus Areas:", [
                "Completing the Square",
                "Vertex Form",
                "Factoring Quadratics", 
                "Quadratic Formula",
                "Graphing Parabolas",
                "Real-World Applications",
                "Optimization Problems",
                "Systems with Quadratics"
            ], default=["Completing the Square", "Vertex Form"])
            
            # Learning style
            learning_style = st.selectbox("Preferred Learning Style:", [
                "Visual (Graphs & Charts)",
                "Kinesthetic (Hands-On)",
                "Analytical (Step-by-Step)",
                "Collaborative (Group Work)",
                "Independent (Self-Paced)"
            ])
        
        institution = st.text_input("School/Institution:", placeholder="School name (optional)")
        
        if st.button("🚀 Begin Quadratic Mastery Journey!", type="primary") and name:
            st.session_state.student_name = name
            st.session_state.grade_level = grade_level
            st.session_state.standards_focus = standards_focus
            st.session_state.sports_interests = interests
            st.session_state.math_focus = math_focus
            st.session_state.learning_style = learning_style
            st.session_state.institution = institution
            st.rerun()

# Enhanced sidebar navigation and progress
st.sidebar.title("🎯 Quadratics Navigation")
if st.session_state.student_name:
    user_level, level_num = calculate_user_level()
    st.sidebar.markdown(f"**Welcome, {st.session_state.student_name}!** 👋")
    st.sidebar.markdown(f"*{st.session_state.grade_level} • {st.session_state.standards_focus}*")
    st.sidebar.markdown(f"*Level {level_num} {user_level}*")

# Standards-aligned navigation
section = st.sidebar.selectbox(
    "Select Learning Module:",
    [
        "📚 Quadratic Theory Hub",
        "🔬 Interactive Lab", 
        "🏀 Sports Analysis Center",
        "📊 Real Data Analytics",
        "🎯 Optimization Studio",
        "🔬 Research Projects",
        "🏆 Performance Dashboard",
        "📖 Standards & Resources",
        "👥 Collaboration Center",
        "🎓 Standards Tracker"
    ]
)

# Enhanced settings with standards focus
st.sidebar.markdown("---")
st.sidebar.markdown("### ⚙️ Learning Settings")

# Standards-based difficulty
if "Common Core" in st.session_state.standards_focus:
    difficulty_options = ["Algebra 1 (9th)", "Geometry (10th)", "Algebra 2 (11th)", "Pre-Calc (12th)", "College"]
elif "AP" in st.session_state.standards_focus:
    difficulty_options = ["AP Algebra", "AP Calculus AB", "AP Calculus BC", "AP Statistics"]
else:
    difficulty_options = ["Beginner", "Intermediate", "Advanced", "University", "Graduate"]

st.session_state.difficulty_level = st.sidebar.selectbox("Difficulty Level:", difficulty_options)

st.session_state.current_sport = st.sidebar.selectbox(
    "Primary Sport Focus:",
    ["Basketball", "Soccer", "Tennis", "Football", "Golf", "Baseball", "Track & Field", "Volleyball"]
)

# Standards mastery tracking
st.sidebar.markdown("### 📋 Standards Mastered")
if st.session_state.standards_mastered:
    for standard in list(st.session_state.standards_mastered)[:3]:
        st.sidebar.success(f"✅ {standard}")
else:
    st.sidebar.info("Complete activities to master standards!")

# Enhanced progress tracking
st.sidebar.markdown("### 📈 Progress Overview")
col1, col2 = st.sidebar.columns(2)
with col1:
    st.metric("Problems", st.session_state.total_problems_solved)
    st.metric("Standards", len(st.session_state.standards_mastered))
    st.metric("Level", level_num)
with col2:
    st.metric("Points", st.session_state.optimization_score)
    st.metric("Projects", len(st.session_state.research_projects))
    st.metric("Achievements", len(st.session_state.achievements))

# Session time
session_time = time.time() - st.session_state.session_start
hours, remainder = divmod(session_time, 3600)
minutes, _ = divmod(remainder, 60)
st.sidebar.metric("Session Time", f"{int(hours):02d}:{int(minutes):02d}")

# Display recent achievements
if st.session_state.achievements:
    st.sidebar.markdown("### 🏆 Recent Achievements")
    for achievement in st.session_state.achievements[-3:]:
        st.sidebar.markdown(f'<div class="achievement-badge">{achievement}</div>', unsafe_allow_html=True)

# Quick actions
st.sidebar.markdown("### ⚡ Quick Actions")
if st.sidebar.button("📊 View Standards Progress"):
    section = "🎓 Standards Tracker"
if st.sidebar.button("🔬 Practice Quadratics"):
    section = "🔬 Interactive Lab"

# Check for new achievements
new_achievements = check_achievements()
for achievement in new_achievements:
    st.sidebar.success(f"🏆 New Achievement: {achievement}!")

# Simple interactive demonstration
st.markdown("### 🎯 Quick Quadratics Demo")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Adjust the quadratic function:**")
    a = st.slider("Coefficient a", -2.0, 2.0, -0.5, 0.1)
    b = st.slider("Coefficient b", -5.0, 5.0, 2.0, 0.5)
    c = st.slider("Coefficient c", -10.0, 10.0, 5.0, 0.5)
    
    if a != 0:
        h = -b / (2 * a)
        k = a * h**2 + b * h + c
        
        st.markdown(f"""
        **Standard Form:** f(x) = {a}x² + {b}x + {c}
        
        **Vertex Form:** f(x) = {a}(x - {h:.2f})² + {k:.2f}
        
        **Vertex:** ({h:.2f}, {k:.2f})
        """)

with col2:
    if a != 0:
        # Create simple plot
        fig, ax = plt.subplots(figsize=(8, 6))
        
        x = np.linspace(h - 5, h + 5, 100)
        y = a * x**2 + b * x + c
        
        ax.plot(x, y, 'blue', linewidth=3, label=f'f(x) = {a}x² + {b}x + {c}')
        ax.plot(h, k, 'ro', markersize=10, label=f'Vertex ({h:.2f}, {k:.2f})')
        
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('Quadratic Function Visualization')
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        st.pyplot(fig)

# Progress tracking
if st.session_state.student_name:
    st.session_state.total_problems_solved += 1
    st.session_state.standards_mastered.add("A-SSE.A.2")

st.markdown("---")
st.markdown("""
### 🎓 MathCraft Sports Pro: Quadratics & Athletic Performance

**Standards-Aligned Learning:**  
✅ Common Core State Standards Aligned  
✅ Real-World Sports Applications  
✅ Interactive Problem Solving  
✅ Progress Tracking & Assessment  

*Transform quadratic functions education through engaging sports mathematics!*
""")
