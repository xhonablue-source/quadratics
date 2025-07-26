"Determining peak performance conditions in athletic events"
                   ],
                   "assessment_criteria": [
                       "Completes the square accurately for any quadratic",
                       "Transforms to (x-p)² = q form correctly",
                       "Uses completed square form to solve equations",
                       "Applies technique to optimization problems"
                   ],
                   "mastery_levels": {
                       "Beginning": "Completes square for x² + bx + c with even b values",
                       "Developing": "Completes square for any monic quadratic",
                       "Proficient": "Completes square for any quadratic expression",
                       "Advanced": "Applies completing square to multi-step optimization"
                   }
               },
               "F-IF.C.7.a": {
                   "full_text": "Graph linear and quadratic functions and show intercepts, maxima, and minima.",
                   "quadratic_focus": "Students graph quadratic functions and identify key features including vertex, intercepts, and axis of symmetry.",
                   "sports_applications": [
                       "Graphing athlete performance over time",
                       "Visualizing trajectory paths in various sports",
                       "Analyzing optimal performance windows"
                   ],
                   "assessment_criteria": [
                       "Accurately graphs quadratic functions",
                       "Identifies and labels vertex, intercepts, axis of symmetry",
                       "Connects graph features to real-world meaning"
                   ],
                   "mastery_levels": {
                       "Beginning": "Graphs simple quadratics using table of values",
                       "Developing": "Graphs quadratics and identifies basic features",
                       "Proficient": "Graphs efficiently using vertex form and key features",
                       "Advanced": "Analyzes complex sports data through graphical interpretation"
                   }
               },
               "F-IF.C.8.a": {
                   "full_text": "Use the process of factoring and completing the square in a quadratic function to show zeros, extreme values, and symmetry of the graph, and interpret these in terms of a context.",
                   "quadratic_focus": "Students use completing the square to reveal and interpret key features of quadratic functions.",
                   "sports_applications": [
                       "Finding optimal angles for maximum range in projectile sports",
                       "Determining peak performance timing in training cycles",
                       "Analyzing symmetry in bilateral athletic movements"
                   ],
                   "assessment_criteria": [
                       "Uses completing the square to find vertex form",
                       "Interprets vertex as maximum/minimum in context",
                       "Explains symmetry and its meaning in applications",
                       "Connects algebraic and graphical representations"
                   ],
                   "mastery_levels": {
                       "Beginning": "Identifies vertex from completed square form",
                       "Developing": "Interprets vertex meaning in simple contexts",
                       "Proficient": "Analyzes all key features and their contextual meaning",
                       "Advanced": "Synthesizes multiple representations for complex problem solving"
                   }
               }
           },
           "Mathematical Practices": {
               "MP1": {
                   "full_text": "Make sense of problems and persevere in solving them.",
                   "quadratic_focus": "Students analyze sports performance problems involving quadratics and persist through multi-step solutions.",
                   "sports_applications": [
                       "Breaking down complex trajectory optimization problems",
                       "Analyzing multi-variable athletic performance scenarios",
                       "Persisting through challenging equipment design calculations"
                   ]
               },
               "MP2": {
                   "full_text": "Reason abstractly and quantitatively.",
                   "quadratic_focus": "Students move flexibly between abstract quadratic expressions and quantitative sports contexts.",
                   "sports_applications": [
                       "Connecting abstract vertex form to concrete optimal performance",
                       "Interpreting coefficients in terms of physical sports parameters",
                       "Reasoning about units and scale in athletic measurements"
                   ]
               },
               "MP4": {
                   "full_text": "Model with mathematics.",
                   "quadratic_focus": "Students create and use quadratic models to represent sports phenomena.",
                   "sports_applications": [
                       "Developing trajectory models for various sports",
                       "Creating performance optimization models for athletes",
                       "Building equipment efficiency models using quadratics"
                   ]
               },
               "MP7": {
                   "full_text": "Look for and make use of structure.",
                   "quadratic_focus": "Students recognize quadratic structure and use it strategically in sports applications.",
                   "sports_applications": [
                       "Recognizing parabolic patterns in sports data",
                       "Using quadratic structure to predict performance trends",
                       "Leveraging symmetry properties in bilateral sports analysis"
                   ]
               }
           }
       }
       
       # Interactive standards explorer
       standards_category = st.selectbox("Standards Category:", 
                                       ["High School Algebra", "Mathematical Practices"])
       
       if standards_category in detailed_standards:
           for standard_id, standard_info in detailed_standards[standards_category].items():
               with st.expander(f"📋 {standard_id}: {standard_info.get('full_text', '')[:60]}..."):
                   
                   # Full standard text
                   st.markdown(f"**Full Standard:** {standard_info['full_text']}")
                   
                   # Quadratic focus
                   if 'quadratic_focus' in standard_info:
                       st.markdown(f"**Quadratic Functions Focus:** {standard_info['quadratic_focus']}")
                   
                   # Sports applications
                   if 'sports_applications' in standard_info:
                       st.markdown("**Sports Applications:**")
                       for app in standard_info['sports_applications']:
                           st.markdown(f"• {app}")
                   
                   # Assessment criteria
                   if 'assessment_criteria' in standard_info:
                       st.markdown("**Assessment Criteria:**")
                       for criteria in standard_info['assessment_criteria']:
                           st.markdown(f"✓ {criteria}")
                   
                   # Mastery levels
                   if 'mastery_levels' in standard_info:
                       st.markdown("**Mastery Progression:**")
                       for level, description in standard_info['mastery_levels'].items():
                           if level == "Advanced":
                               st.success(f"**{level}:** {description}")
                           elif level == "Proficient":
                               st.info(f"**{level}:** {description}")
                           elif level == "Developing":
                               st.warning(f"**{level}:** {description}")
                           else:
                               st.error(f"**{level}:** {description}")
                   
                   # Check if student has mastered this standard
                   if standard_id in st.session_state.standards_mastered:
                       st.success("🏆 You have demonstrated mastery of this standard!")
                   else:
                       st.info("💪 Complete activities to demonstrate mastery of this standard.")
   
   elif resource_type == "Assessment Rubrics":
       st.markdown("### 📊 Standards-Based Assessment Rubrics")
       
       st.markdown("""
       **Use these rubrics to assess student mastery of quadratic functions through sports applications.**
       """)
       
       rubric_focus = st.selectbox("Rubric Focus Area:", [
           "Completing the Square Mastery",
           "Vertex Form Applications", 
           "Sports Problem Solving",
           "Mathematical Communication",
           "Technology Integration"
       ])
       
       if rubric_focus == "Completing the Square Mastery":
           st.markdown("""
           #### 🎯 Completing the Square Mastery Rubric (A-REI.B.4.a)
           """)
           
           rubric_data = {
               "Criteria": [
                   "Process Accuracy",
                   "Method Understanding", 
                   "Application to Sports",
                   "Error Analysis",
                   "Communication"
               ],
               "Exemplary (4)": [
                   "Completes square flawlessly for any quadratic, including complex coefficients",
                   "Explains why each step works and connects to vertex form properties",
                   "Applies technique to solve complex sports optimization problems independently",
                   "Identifies and corrects errors, explains common misconceptions",
                   "Uses precise mathematical language and multiple representations"
               ],
               "Proficient (3)": [
                   "Completes square accurately for most quadratics with minor computational errors",
                   "Demonstrates solid understanding of the process and its purpose",
                   "Applies to sports problems with guidance, makes connections to optimization",
                   "Recognizes some errors and attempts corrections",
                   "Communicates clearly using appropriate mathematical vocabulary"
               ],
               "Developing (2)": [
                   "Completes square for simple cases, struggles with complex coefficients",
                   "Shows partial understanding, may skip steps or use shortcuts incorrectly",
                   "Applies to basic sports problems with significant support",
                   "Limited error recognition, difficulty with self-correction",
                   "Basic communication with some mathematical language"
               ],
               "Beginning (1)": [
                   "Attempts process but makes frequent errors, may not reach vertex form",
                   "Shows minimal understanding of why the process works",
                   "Cannot apply to sports contexts without extensive guidance",
                   "Unaware of errors, does not attempt corrections",
                   "Limited mathematical communication, relies on informal language"
               ]
           }
           
           # Display as interactive table
           rubric_df = pd.DataFrame(rubric_data)
           st.dataframe(rubric_df, use_container_width=True)
           
           # Assessment tools
           st.markdown("#### 🔧 Assessment Tools")
           
           col1, col2 = st.columns(2)
           with col1:
               st.markdown("""
               **Quick Assessment Questions:**
               1. Complete the square: 2x² + 12x + 10
               2. A basketball trajectory follows h(x) = -0.05x² + 1.2x + 6. Find the maximum height.
               3. Explain why completing the square reveals the vertex.
               4. What errors do you see in this work? [Show common mistake]
               """)
           
           with col2:
               st.markdown("""
               **Performance Task:**
               Design an optimal basketball shot using completing the square to:
               - Find the peak height of the trajectory
               - Determine the optimal release distance
               - Explain your mathematical reasoning
               - Compare different shooting angles
               """)
       
       elif rubric_focus == "Sports Problem Solving":
           st.markdown("""
           #### 🏀 Sports Application Problem Solving Rubric
           """)
           
           sports_rubric = {
               "Mathematical Modeling": [
                   "Creates sophisticated quadratic models from sports scenarios with appropriate variables and constraints",
                   "Develops accurate quadratic models with minor gaps in variable identification",
                   "Creates basic quadratic models with guidance and some inaccuracies",
                   "Struggles to create appropriate mathematical models from sports contexts"
               ],
               "Problem Solving Strategy": [
                   "Selects and applies optimal strategies, shows multiple solution paths",
                   "Uses appropriate strategies effectively, may show one primary solution method",
                   "Uses strategies with guidance, shows partial understanding of approach",
                   "Limited strategy use, requires significant support to make progress"
               ],
               "Sports Context Integration": [
                   "Seamlessly integrates mathematical solutions with sports reality, considers practical constraints",
                   "Makes clear connections between math and sports, considers most practical aspects",
                   "Makes basic connections between math and sports with some guidance",
                   "Struggles to connect mathematical solutions to sports contexts"
               ],
               "Optimization Analysis": [
                   "Identifies and explains optimal conditions using vertex form, considers trade-offs",
                   "Finds optimal conditions accurately, explains significance in sports context",
                   "Identifies optimal conditions with support, basic explanation of meaning",
                   "Cannot identify or explain optimal conditions in sports applications"
               ]
           }
           
           for criteria, levels in sports_rubric.items():
               st.markdown(f"**{criteria}:**")
               col1, col2, col3, col4 = st.columns(4)
               with col1:
                   st.success(f"**Exemplary (4):** {levels[0]}")
               with col2:
                   st.info(f"**Proficient (3):** {levels[1]}")
               with col3:
                   st.warning(f"**Developing (2):** {levels[2]}")
               with col4:
                   st.error(f"**Beginning (1):** {levels[3]}")
               st.markdown("---")
   
   elif resource_type == "Lesson Plan Templates":
       st.markdown("### 📝 Standards-Aligned Lesson Plan Templates")
       
       lesson_type = st.selectbox("Lesson Template Type:", [
           "Completing the Square Introduction",
           "Sports Optimization Project",
           "Real Data Analysis Lesson",
           "Technology Integration",
           "Assessment & Review"
       ])
       
       if lesson_type == "Completing the Square Introduction":
           st.markdown("""
           #### 📋 Lesson Plan: Introduction to Completing the Square through Basketball
           
           **Grade Level:** 9-11 (Algebra 1/2)  
           **Duration:** 50 minutes  
           **Standards:** A-REI.B.4.a, F-IF.C.8.a, MP1, MP4, MP7
           """)
           
           lesson_plan = {
               "Learning Objectives": [
                   "Students will complete the square for quadratic expressions",
                   "Students will convert quadratic functions to vertex form", 
                   "Students will interpret the vertex in sports contexts",
                   "Students will apply completing the square to optimize basketball shot trajectories"
               ],
               "Materials Needed": [
                   "Basketball or ball for demonstration",
                   "Graphing technology (calculators or computers)",
                   "Student worksheet with practice problems",
                   "Real basketball trajectory data (optional)",
                   "Poster paper for group work"
               ],
               "Lesson Sequence": [
                   "**Hook (5 min):** Basketball shot demonstration - 'What makes the perfect shot?'",
                   "**Explore (10 min):** Graph basketball trajectory data, notice parabolic shape",
                   "**Explain (15 min):** Introduce completing the square with basketball equation",
                   "**Elaborate (15 min):** Students practice with guided worksheet",
                   "**Evaluate (5 min):** Quick exit ticket on vertex interpretation"
               ],
               "Assessment Strategies": [
                   "Formative: Circulate during practice, check student work",
                   "Formative: Exit ticket asking for vertex interpretation",
                   "Summative: Problem set including sports applications",
                   "Performance: Students create their own sports optimization problem"
               ],
               "Differentiation": [
                   "Advanced: Explore multiple sports, compare optimization strategies",
                   "On-level: Follow guided practice with basketball focus",
                   "Struggling: Use algebra tiles or area models for visual support",
                   "ELL: Provide vocabulary support and visual representations"
               ],
               "Technology Integration": [
                   "Graphing calculators for visualization",
                   "Online trajectory simulators",
                   "Spreadsheet software for data analysis",
                   "Interactive quadratic manipulatives"
               ],
               "Extension Activities": [
                   "Research optimal shooting angles for different players",
                   "Compare trajectories across different sports",
                   "Design equipment based on quadratic optimization",
                   "Create presentation on sports mathematics"
               ]
           }
           
           for section, items in lesson_plan.items():
               st.markdown(f"**{section}:**")
               for item in items:
                   st.markdown(f"• {item}")
               st.markdown("")
           
           # Downloadable resources
           st.markdown("#### 📥 Downloadable Resources")
           st.info("""
           **Available Resources:**
           - Student practice worksheet with basketball problems
           - Teacher answer key with step-by-step solutions
           - Assessment rubric aligned to standards
           - Extension project guidelines
           - Technology setup instructions
           """)
   
   elif resource_type == "Professional Development":
       st.markdown("### 👨‍🎓 Professional Development Resources")
       
       pd_focus = st.selectbox("Professional Development Focus:", [
           "Teaching Quadratics through Sports",
           "Standards-Based Assessment",
           "Technology Integration",
           "Research-Based Practices",
           "Differentiation Strategies"
       ])
       
       if pd_focus == "Teaching Quadratics through Sports":
           st.markdown("""
           #### 🏆 Professional Development: Sports-Based Quadratic Instruction
           """)
           
           # PD module structure
           pd_modules = {
               "Module 1: Mathematical Foundations": {
                   "Duration": "2 hours",
                   "Objectives": [
                       "Review quadratic function concepts and representations",
                       "Master completing the square technique", 
                       "Understand connections between algebraic and graphical features",
                       "Practice common student misconceptions and remediation"
                   ],
                   "Activities": [
                       "Hands-on completing the square practice",
                       "Error analysis workshop",
                       "Multiple representations exploration",
                       "Standards alignment mapping"
                   ]
               },
               "Module 2: Sports Applications": {
                   "Duration": "3 hours", 
                   "Objectives": [
                       "Explore authentic sports contexts for quadratic applications",
                       "Develop sports-based problem sequences",
                       "Create real-world connections for student engagement",
                       "Design performance-based assessments"
                   ],
                   "Activities": [
                       "Sports trajectory analysis workshop",
                       "Problem development collaborative session",
                       "Assessment design practice",
                       "Technology tools exploration"
                   ]
               },
               "Module 3: Implementation Strategies": {
                   "Duration": "2 hours",
                   "Objectives": [
                       "Plan unit sequences with sports integration",
                       "Develop differentiation strategies",
                       "Create assessment rubrics and tools", 
                       "Build parent and administrator communication"
                   ],
                   "Activities": [
                       "Unit planning workshop",
                       "Differentiation strategy sharing",
                       "Assessment calibration",
                       "Implementation planning"
                   ]
               }
           }
           
           for module, details in pd_modules.items():
               with st.expander(f"📖 {module} - {details['Duration']}"):
                   st.markdown("**Learning Objectives:**")
                   for obj in details['Objectives']:
                       st.markdown(f"• {obj}")
                   
                   st.markdown("**Workshop Activities:**")
                   for activity in details['Activities']:
                       st.markdown(f"• {activity}")
           
           # Certification pathway
           st.markdown("#### 🎓 Certification Pathway")
           st.info("""
           **MathCraft Sports Pro Certification Requirements:**
           ✓ Complete all three professional development modules  
           ✓ Implement sports-based quadratic unit in classroom  
           ✓ Submit reflection portfolio with student work samples  
           ✓ Participate in peer observation and feedback cycle  
           ✓ Present at local or regional mathematics conference  
           
           **Benefits:**
           - 15 professional development hours
           - Digital badge for LinkedIn/resume
           - Access to exclusive resources and community
           - Priority support for implementation
           """)

# Footer with comprehensive educational impact
st.markdown("---")
st.markdown("""
<div class="standards-box">
<h3>🎓 Educational Impact & Standards Mastery</h3>

<strong>📊 Learning Outcomes Achieved:</strong><br>
✅ Master completing the square through engaging sports applications<br>
✅ Convert between standard, vertex, and factored forms of quadratics<br>
✅ Apply mathematical optimization to real-world athletic scenarios<br>
✅ Interpret mathematical results in practical sports contexts<br>
✅ Develop problem-solving skills through authentic applications<br><br>

<strong>📋 Standards Alignment Summary:</strong><br>
- <strong>A-SSE.A.2:</strong> Use structure of expressions for strategic rewriting<br>
- <strong>A-SSE.B.3.a:</strong> Factor quadratics to reveal zeros and intercepts<br>
- <strong>A-REI.B.4.a:</strong> Master completing the square technique<br>
- <strong>F-IF.C.7.a:</strong> Graph quadratics showing key features<br>
- <strong>F-IF.C.8.a:</strong> Use vertex form to analyze quadratic properties<br>
- <strong>MP1, MP2, MP4, MP7:</strong> Mathematical practices through sports modeling<br><br>

<strong>🎯 Assessment & Mastery Tracking:</strong><br>
Interactive progress monitoring aligned to standards expectations<br>
Performance-based assessments using authentic sports scenarios<br>
Differentiated learning paths for diverse student needs<br>
Real-time feedback and adaptive challenge levels<br><br>

<strong>💡 Professional Impact:</strong><br>
Increase student engagement through relevant applications<br>
Meet rigorous academic standards through innovative teaching<br>
Prepare students for STEM careers and advanced mathematics<br>
Build 21st-century problem-solving and critical thinking skills
</div>
""", unsafe_allow_html=True)

# Session summary
if st.session_state.student_name:
   st.markdown(f"""
   ### 🏆 Session Summary for {st.session_state.student_name}
   
   **📈 Standards Progress:**
   - **Standards Mastered:** {len(st.session_state.standards_mastered)} of 10 core standards
   - **Problems Solved:** {st.session_state.total_problems_solved}
   - **Sports Analyzed:** {', '.join(st.session_state.sports_analyzed) if st.session_state.sports_analyzed else 'None yet'}
   - **Optimization Score:** {st.session_state.optimization_score} points
   - **Current Level:** Level {calculate_user_level()[1]} {calculate_user_level()[0]}
   
   **🎯 Next Learning Goals:**
   - Master remaining Common Core standards through sports applications
   - Complete advanced research projects using real sports data
   - Collaborate with peers on optimization challenges
   - Apply quadratic modeling to personal sports interests
   
   **🌟 Achievement Highlights:**
   {f"🏆 Recent Achievement: {st.session_state.achievements[-1]}" if st.session_state.achievements else "Complete your first activity to earn achievements!"}
   """)

# Export/save functionality
if st.session_state.student_name and len(st.session_state.standards_mastered) > 0:
   if st.button("📄 Generate Progress Report"):
       progress_report = f"""
       MATHCRAFT SPORTS PRO: QUADRATICS & ATHLETIC PERFORMANCE
       Student Progress Report
       
       Student: {st.session_state.student_name}
       Grade Level: {st.session_state.grade_level}
       Standards Focus: {st.session_state.standards_focus}
       Date: {datetime.now().strftime("%Y-%m-%d")}
       
       STANDARDS MASTERY:
       {chr(10).join([f"✓ {standard}" for standard in st.session_state.standards_mastered])}
       
       PERFORMANCE METRICS:
       - Problems Solved: {st.session_state.total_problems_solved}
       - Sports Analyzed: {len(st.session_state.sports_analyzed)}
       - Optimization Score: {st.session_state.optimization_score}
       - Research Projects: {len(st.session_state.research_projects)}
       
       ACHIEVEMENTS EARNED:
       {chr(10).join([f"🏆 {achievement}" for achievement in st.session_state.achievements])}
       
       Generated by MathCraft Sports Pro: Quadratics & Athletic Performance
       Standards-aligned mathematics education through sports applications
       """
       
       st.download_button(
           label="📥 Download Progress Report",
           data=progress_report,
           file_name=f"mathcraft_progress_{st.session_state.student_name.replace(' ', '_')}.txt",
           mime="text/plain"
       )
