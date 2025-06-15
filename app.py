import streamlit as st
import numpy as np
import math

# Configure matplotlib for Streamlit
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
plt.style.use('default')  # Ensure consistent styling

import pandas as pd

st.set_page_config(page_title="MathCraft | Completing the Square", layout="wide")
st.title("🏆 MathCraft: Completing the Square with Sports Applications")

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.selectbox("Choose a section:", [
    "📚 Introduction", 
    "🔍 Interactive Method", 
    "🛠️ Physical Manipulatives", 
    "🏀 Sports Applications", 
    "📝 Problem Solving",
    "🎯 Performance Analysis"
])

if section == "📚 Introduction":
    st.markdown("""
    ### 🎯 What is Completing the Square?
    **Completing the square** is a powerful algebraic technique that transforms a quadratic expression into a perfect square trinomial plus a constant. This method reveals the vertex form of a parabola, making it easier to analyze maximum and minimum values - crucial for sports performance optimization!
    
    **The Process:**
    1. Start with: $ax^2 + bx + c$
    2. Factor out coefficient of $x^2$: $a(x^2 + \\frac{b}{a}x) + c$
    3. Complete the square: $a(x + \\frac{b}{2a})^2 - \\frac{b^2}{4a} + c$
    4. Vertex form: $a(x - h)^2 + k$ where vertex is $(h, k)$
    """)
    
    # Method comparison table
    st.markdown("""
    ### 📐 Completing the Square vs Other Methods
    | Method | Best For | Sports Application | Advantages |
    |--------|----------|-------------------|------------|
    | Completing the Square | Finding vertex/max-min | Optimal angle, peak height | Shows turning point clearly |
    | Factoring | Finding roots/zeros | Where ball hits ground | Quick for simple equations |
    | Quadratic Formula | Any quadratic | General solutions | Works for all quadratics |
    | Graphing | Visual analysis | Trajectory visualization | Shows entire motion path |
    """)
    
    # Visual demonstration
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🔧 Step-by-Step Example
        **Transform:** $x^2 + 6x + 5$
        
        1. **Identify the pattern:** $x^2 + 6x + ?$
        2. **Take half of linear coefficient:** $\\frac{6}{2} = 3$
        3. **Square it:** $3^2 = 9$
        4. **Add and subtract:** $x^2 + 6x + 9 - 9 + 5$
        5. **Factor perfect square:** $(x + 3)^2 - 4$
        
        **Result:** Vertex form reveals minimum at $x = -3$, value $= -4$
        """)
    
    with col2:
        # Create visual representation
        fig, ax = plt.subplots(figsize=(8, 6))
        
        x = np.linspace(-7, 1, 400)
        y = x**2 + 6*x + 5
        y_vertex = (x + 3)**2 - 4
        
        ax.plot(x, y, 'b-', linewidth=3, label='$x^2 + 6x + 5$')
        ax.plot(x, y_vertex, 'r--', linewidth=2, label='$(x + 3)^2 - 4$')
        ax.plot(-3, -4, 'ro', markersize=10, label='Vertex (-3, -4)')
        
        # Add grid squares to visualize "completing"
        ax.axvline(-3, color='gray', linestyle=':', alpha=0.7)
        ax.axhline(-4, color='gray', linestyle=':', alpha=0.7)
        
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Completing the Square Visualization')
        ax.grid(True, alpha=0.3)
        ax.legend()
        ax.set_ylim(-6, 10)
        
        st.pyplot(fig)

elif section == "🔍 Interactive Method":
    st.header("🔍 Interactive Completing the Square")
    
    st.markdown("""
    **Practice the method step-by-step with interactive controls!**
    Adjust the coefficients and watch how completing the square reveals the vertex form.
    """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Quadratic Coefficients")
        
        # Interactive controls for coefficients
        a = st.slider("Coefficient a", -5, 5, 1, 1, help="Coefficient of x²")
        if a == 0:
            a = 1  # Prevent division by zero
        b = st.slider("Coefficient b", -10, 10, 6, 1, help="Coefficient of x")
        c = st.slider("Coefficient c", -10, 10, 5, 1, help="Constant term")
        
        st.markdown(f"""
        **Original Form:**
        $y = {a}x^2 + {b}x + {c}$
        """)
        
        # Show step-by-step completion
        if st.checkbox("Show Steps", value=True):
            st.markdown("### Step-by-Step Process:")
            
            # Step 1: Factor out 'a' if needed
            if a != 1:
                st.markdown(f"**Step 1:** Factor out {a}")
                st.markdown(f"$y = {a}(x^2 + {b/a:.2f}x) + {c}$")
                b_over_a = b/a
            else:
                st.markdown("**Step 1:** No factoring needed (a = 1)")
                b_over_a = b
            
            # Step 2: Complete the square
            half_b = b_over_a / 2
            square_term = half_b ** 2
            
            st.markdown(f"**Step 2:** Complete the square")
            st.markdown(f"Half of linear coefficient: $\\frac{{{b_over_a:.2f}}}{2} = {half_b:.2f}$")
            st.markdown(f"Square it: $({half_b:.2f})^2 = {square_term:.2f}$")
            
            # Step 3: Add and subtract
            st.markdown(f"**Step 3:** Add and subtract {square_term:.2f}")
            if a != 1:
                st.markdown(f"$y = {a}(x^2 + {b_over_a:.2f}x + {square_term:.2f} - {square_term:.2f}) + {c}$")
            else:
                st.markdown(f"$y = x^2 + {b:.2f}x + {square_term:.2f} - {square_term:.2f} + {c}$")
            
            # Step 4: Factor and simplify
            h = -half_b
            k = c - a * square_term
            
            st.markdown(f"**Step 4:** Factor perfect square")
            st.markdown(f"$y = {a}(x - ({h:.2f}))^2 + {k:.2f}$")
            
            st.markdown(f"**Vertex Form:** $y = {a}(x - {h:.2f})^2 + {k:.2f}$")
            st.markdown(f"**Vertex:** $({h:.2f}, {k:.2f})$")
            
            # Interpretation
            if a > 0:
                st.success(f"**Minimum value:** {k:.2f} at x = {h:.2f}")
            else:
                st.success(f"**Maximum value:** {k:.2f} at x = {h:.2f}")
    
    with col2:
        # Create interactive plot
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Calculate vertex
        h = -b / (2 * a)
        k = a * h**2 + b * h + c
        
        # Plot the parabola
        x_range = max(abs(h) + 3, 5)
        x = np.linspace(h - x_range, h + x_range, 400)
        y = a * x**2 + b * x + c
        
        ax.plot(x, y, 'b-', linewidth=3, label=f'$y = {a}x^2 + {b}x + {c}$')
        
        # Mark vertex
        ax.plot(h, k, 'ro', markersize=12, label=f'Vertex ({h:.2f}, {k:.2f})')
        
        # Add vertex lines
        ax.axvline(h, color='red', linestyle='--', alpha=0.7, label=f'Axis of symmetry: x = {h:.2f}')
        ax.axhline(k, color='orange', linestyle='--', alpha=0.7, label=f'{"Min" if a > 0 else "Max"} value: y = {k:.2f}')
        
        # Add completing the square visualization
        if abs(h) < 10 and abs(k) < 50:  # Only if reasonable values
            # Draw "square" that was completed
            square_size = abs(b / (2 * a))
            if square_size < 3:  # Only for reasonable sizes
                rect_x = h - square_size/2
                rect_y = k
                rect = plt.Rectangle((rect_x, rect_y), square_size, square_size, 
                                   fill=False, edgecolor='green', linewidth=2, 
                                   label='Completed Square Concept')
                ax.add_patch(rect)
        
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title(f'Interactive Completing the Square\nVertex Form: y = {a}(x - {h:.2f})² + {k:.2f}')
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        # Set reasonable axis limits
        y_range = max(abs(k) + 10, 20)
        ax.set_ylim(k - y_range/2, k + y_range/2)
        
        st.pyplot(fig)
    
    # Practice problems
    st.markdown("---")
    st.subheader("🎯 Quick Practice")
    
    practice_problems = [
        {"problem": "$x^2 + 8x + 12$", "answer": "$(x + 4)^2 - 4$", "vertex": "(-4, -4)"},
        {"problem": "$x^2 - 6x + 5$", "answer": "$(x - 3)^2 - 4$", "vertex": "(3, -4)"},
        {"problem": "$2x^2 + 12x + 10$", "answer": "$2(x + 3)^2 - 8$", "vertex": "(-3, -8)"},
        {"problem": "$x^2 + 4x + 1$", "answer": "$(x + 2)^2 - 3$", "vertex": "(-2, -3)"}
    ]
    
    for i, prob in enumerate(practice_problems):
        with st.expander(f"Practice Problem {i+1}: Complete the square for {prob['problem']}"):
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Show Answer {i+1}"):
                    st.success(f"**Answer:** {prob['answer']}")
                    st.info(f"**Vertex:** {prob['vertex']}")
            with col2:
                st.markdown("**Hint:** Remember to take half of the x-coefficient, then square it!")

elif section == "🛠️ Physical Manipulatives":
    st.header("🛠️ Hands-On Activities & Physical Manipulatives")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🧩 Algebra Tiles", "📐 Geometric Models", "🎯 Sports Equipment", "📊 Data Collection"])
    
    with tab1:
        st.subheader("Algebra Tiles Method")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🧩 Physical Algebra Tiles:**
            - **Large squares**: $x^2$ terms
            - **Rectangles**: $x$ terms 
            - **Small squares**: Constant terms
            - **Goal**: Arrange into a perfect square
            
            **📦 DIY Materials:**
            - Cardboard or foam squares
            - Different colors for different terms
            - Magnetic backing for whiteboard use
            - Grid paper for organization
            """)
            
            st.markdown("""
            **🔧 Activity Steps:**
            1. **Layout**: Place tiles for original expression
            2. **Arrange**: Try to form a square pattern
            3. **Fill gaps**: Add tiles to complete square
            4. **Count**: Note how many extra tiles needed
            5. **Subtract**: Remove same number to balance
            """)
        
        with col2:
            st.markdown("""
            **🎯 Example: $x^2 + 6x + 5$**
            
            **Step 1 - Original Layout:**
            ```
            [X²]  [X] [X] [X]
                  [X] [X] [X]
                  [1][1][1][1][1]
            ```
            
            **Step 2 - Rearrange to Square:**
            ```
            [X²] [X] [X] [X]
            [X]  [1] [1] [1]
            [X]  [1] [1] [1]  
            [X]  [1] [1] [?]
            ```
            
            **Step 3 - Need 4 more units to complete!**
            Add 4, subtract 4: $(x+3)^2 - 4$
            """)
    
    with tab2:
        st.subheader("Geometric Visualization Models")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **📏 Square Construction Activity:**
            1. **Materials**: Graph paper, colored pencils, rulers
            2. **Draw**: Original expression as area model
            3. **Reshape**: Manipulate into perfect square
            4. **Measure**: Calculate added/subtracted area
            
            **🎨 Area Model Method:**
            - Draw rectangles with areas matching terms
            - Physically cut and rearrange pieces
            - Fill missing pieces to complete square
            - Visualize the algebraic manipulation
            """)
        
        with col2:
            st.markdown("""
            **📐 3D Models:**
            - **Wooden blocks**: Different sizes for terms
            - **LEGO bricks**: Build quadratic expressions
            - **Magnetic tiles**: Rearrangeable patterns
            - **Origami squares**: Folding demonstrations
            
            **🔍 Investigation Questions:**
            - What happens with negative coefficients?
            - How does the 'a' coefficient affect the model?
            - Can you predict the vertex without completing?
            """)
    
    with tab3:
        st.subheader("Sports Equipment Integration")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🏀 Basketball Court Geometry:**
            1. **Court layout**: Use court dimensions as coordinate system
            2. **Shot trajectory**: Model arc as parabola
            3. **Completing square**: Find optimal release point
            4. **Vertex analysis**: Determine peak height and distance
            
            **⚽ Soccer Field Applications:**
            - **Goal kick trajectories**: Parabolic paths
            - **Field positioning**: Optimal player placement
            - **Ball flight**: Wind resistance effects
            """)
        
        with col2:
            st.markdown("""
            **🎾 Tennis Applications:**
            - **Serve analysis**: Ball trajectory over net
            - **Court coverage**: Player movement optimization
            - **Spin effects**: Modified parabolic paths
            
            **🏈 Football Physics:**
            - **Punt trajectories**: Hang time vs distance
            - **Field goal attempts**: Angle optimization
            - **Passing routes**: Quarterback decision making
            """)
    
    with tab4:
        st.subheader("Data Collection Activities")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **📊 Sports Data Projects:**
            1. **Basketball shots**: Record arc height vs distance
            2. **Track and field**: Analyze jumping trajectories
            3. **Baseball**: Study ball flight paths
            4. **Golf**: Measure ball trajectory angles
            
            **📱 Technology Tools:**
            - **Video analysis**: Slow-motion trajectory tracking
            - **Phone apps**: Angle and distance measurement
            - **Sensors**: Motion capture devices
            - **Spreadsheets**: Data organization and analysis
            """)
        
        with col2:
            st.markdown("""
            **🎯 Investigation Process:**
            1. **Hypothesis**: Predict optimal angles/positions
            2. **Data collection**: Measure multiple trials
            3. **Analysis**: Fit quadratic models to data
            4. **Complete square**: Find vertex (optimal point)
            5. **Conclusion**: Compare prediction to reality
            
            **📈 Expected Outcomes:**
            - Discover optimal launch angles
            - Understand trade-offs (height vs distance)
            - Validate mathematical models with real data
            """)

elif section == "🏀 Sports Applications":
    st.header("🏀 Real-World Sports Applications")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🏀 Basketball", "⚽ Soccer", "🎾 Tennis", "🏈 Football"])
    
    with tab1:
        st.subheader("Basketball Trajectory Analysis")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🎯 Free Throw Optimization**
            
            **Problem Setup:**
            A basketball follows a parabolic path given by:
            $h(x) = -0.05x^2 + 0.6x + 6$
            
            Where:
            - $h$ = height (feet)
            - $x$ = horizontal distance (feet)
            - Player shoots from 6 feet high
            - Basket is 10 feet high, 15 feet away
            """)
            
            # Interactive basketball parameters
            release_height = st.slider("Release height (feet)", 5.0, 8.0, 6.0, 0.1)
            basket_distance = st.slider("Distance to basket (feet)", 10, 20, 15, 1)
            basket_height = 10.0  # Standard
            
            # Calculate trajectory coefficients
            # Using completing the square to find optimal trajectory
            a = st.slider("Trajectory coefficient a", -0.1, -0.01, -0.05, 0.005)
            b = st.slider("Initial velocity component", 0.3, 1.0, 0.6, 0.05)
            
            # Complete the square for trajectory
            h_vertex = -b / (2 * a)
            k_vertex = a * h_vertex**2 + b * h_vertex + release_height
            
            st.markdown(f"""
            **Trajectory Analysis:**
            - **Original form**: $h(x) = {a}x^2 + {b}x + {release_height}$
            - **Completing square**: $h(x) = {a}(x - {h_vertex:.1f})^2 + {k_vertex:.1f}$
            - **Peak height**: {k_vertex:.1f} feet
            - **Peak distance**: {h_vertex:.1f} feet
            - **Release angle**: {math.degrees(math.atan(b)):.1f}°
            """)
            
            # Check if shot makes it
            basket_height_at_distance = a * basket_distance**2 + b * basket_distance + release_height
            makes_shot = abs(basket_height_at_distance - basket_height) < 1.0
            
            if makes_shot:
                st.success(f"✅ Shot successful! Ball height at basket: {basket_height_at_distance:.1f} ft")
            else:
                st.error(f"❌ Shot misses! Ball height at basket: {basket_height_at_distance:.1f} ft (need 10 ft)")
        
        with col2:
            # Plot basketball trajectory
            fig, ax = plt.subplots(figsize=(10, 8))
            
            x = np.linspace(0, 20, 400)
            h = a * x**2 + b * x + release_height
            
            # Only plot positive heights
            valid_indices = h >= 0
            x_valid = x[valid_indices]
            h_valid = h[valid_indices]
            
            ax.plot(x_valid, h_valid, 'orange', linewidth=4, label='Ball trajectory')
            
            # Mark key points
            ax.plot(0, release_height, 'go', markersize=10, label=f'Release point (0, {release_height})')
            ax.plot(h_vertex, k_vertex, 'ro', markersize=10, label=f'Peak ({h_vertex:.1f}, {k_vertex:.1f})')
            ax.plot(basket_distance, basket_height, 'bs', markersize=12, label=f'Basket ({basket_distance}, {basket_height})')
            
            # Draw court elements
            ax.axhline(0, color='brown', linewidth=8, alpha=0.7, label='Court floor')
            ax.plot([basket_distance, basket_distance], [0, basket_height], 'k-', linewidth=6, alpha=0.7)
            
            # Highlight optimal region
            ax.axhspan(9, 11, xmin=basket_distance/20, xmax=(basket_distance+1)/20, alpha=0.2, color='green', label='Target zone')
            
            ax.set_xlabel('Horizontal Distance (feet)')
            ax.set_ylabel('Height (feet)')
            ax.set_title('Basketball Free Throw Trajectory Analysis')
            ax.grid(True, alpha=0.3)
            ax.legend()
            ax.set_xlim(0, 20)
            ax.set_ylim(0, max(k_vertex + 2, 12))
            
            st.pyplot(fig)
    
    with tab2:
        st.subheader("Soccer Ball Physics")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **⚽ Goal Kick Analysis**
            
            **Scenario**: Goalkeeper kicks ball from penalty area
            - **Goal**: Reach teammate 40 yards away
            - **Obstacles**: Opposing players (average height 6 feet)
            - **Constraint**: Ball must clear players and land accurately
            """)
            
            # Soccer parameters
            kick_angle = st.slider("Kick angle (degrees)", 15, 75, 45, 5)
            initial_velocity = st.slider("Initial velocity (ft/s)", 40, 80, 60, 2)
            
            # Convert to trajectory equation
            angle_rad = math.radians(kick_angle)
            v0x = initial_velocity * math.cos(angle_rad)
            v0y = initial_velocity * math.sin(angle_rad)
            
            # Trajectory: h(x) = x*tan(θ) - (g*x²)/(2*v₀²*cos²(θ))
            g = 32.2  # ft/s²
            
            # Converting to standard form for completing the square
            a_soccer = -g / (2 * initial_velocity**2 * math.cos(angle_rad)**2)
            b_soccer = math.tan(angle_rad)
            c_soccer = 0  # Starts at ground level
            
            # Complete the square
            h_vertex_soccer = -b_soccer / (2 * a_soccer)
            k_vertex_soccer = a_soccer * h_vertex_soccer**2 + b_soccer * h_vertex_soccer + c_soccer
            
            # Range calculation
            range_soccer = -b_soccer / a_soccer * 2  # Where ball lands
            
            st.markdown(f"""
            **Trajectory Equation:**
            $h(x) = {a_soccer:.6f}x^2 + {b_soccer:.3f}x$
            
            **Completed Square Form:**
            $h(x) = {a_soccer:.6f}(x - {h_vertex_soccer:.1f})^2 + {k_vertex_soccer:.1f}$
            
            **Performance Metrics:**
            - **Maximum height**: {k_vertex_soccer:.1f} feet
            - **Range**: {range_soccer:.1f} feet ({range_soccer/3:.1f} yards)
            - **Clears 6-foot players**: {'✅ Yes' if k_vertex_soccer > 6 else '❌ No'}
            - **Reaches 40-yard target**: {'✅ Yes' if range_soccer/3 >= 40 else '❌ No'}
            """)
        
        with col2:
            # Plot soccer trajectory
            fig, ax = plt.subplots(figsize=(10, 8))
            
            x_soccer = np.linspace(0, range_soccer, 400)
            h_soccer = a_soccer * x_soccer**2 + b_soccer * x_soccer
            
            # Only plot non-negative heights
            valid_soccer = h_soccer >= 0
            x_soccer_valid = x_soccer[valid_soccer]
            h_soccer_valid = h_soccer[valid_soccer]
            
            ax.plot(x_soccer_valid, h_soccer_valid, 'green', linewidth=4, label='Ball trajectory')
            
            # Mark key points
            ax.plot(0, 0, 'go', markersize=10, label='Kick point')
            ax.plot(h_vertex_soccer, k_vertex_soccer, 'ro', markersize=10, label=f'Peak ({h_vertex_soccer:.0f} ft, {k_vertex_soccer:.1f} ft)')
            ax.plot(range_soccer, 0, 'bo', markersize=10, label=f'Landing ({range_soccer:.0f} ft)')
            
            # Draw field elements
            ax.axhline(0, color='green', linewidth=6, alpha=0.5, label='Field')
            ax.axhline(6, color='red', linestyle='--', alpha=0.7, label='Player height (6 ft)')
            ax.axvline(120, color='blue', linestyle=':', alpha=0.7, label='Target (40 yards)')
            
            # Add opposing players
            for player_x in [30, 45, 60, 75]:
                if player_x < range_soccer:
                    ax.plot([player_x, player_x], [0, 6], 'r-', linewidth=4, alpha=0.6)
            
            ax.set_xlabel('Distance (feet)')
            ax.set_ylabel('Height (feet)')
            ax.set_title(f'Soccer Goal Kick Analysis - {kick_angle}° angle')
            ax.grid(True, alpha=0.3)
            ax.legend()
            ax.set_xlim(0, max(range_soccer + 20, 140))
            ax.set_ylim(0, max(k_vertex_soccer + 5, 20))
            
            st.pyplot(fig)
    
    with tab3:
        st.subheader("Tennis Serve Analysis")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🎾 Professional Tennis Serve**
            
            **Court Specifications:**
            - **Net height**: 3.5 feet at center
            - **Service box**: 21 feet deep
            - **Server height**: Variable (6-7 feet)
            - **Goal**: Clear net, land in service box
            """)
            
            # Tennis parameters
            serve_height = st.slider("Serve height (feet)", 6.0, 9.0, 7.5, 0.1)
            serve_speed = st.slider("Serve speed (mph)", 80, 140, 110, 5)
            serve_angle = st.slider("Serve angle (degrees down)", -10, 10, -2, 1)
            
            # Convert units and calculate trajectory
            serve_speed_fps = serve_speed * 1.467  # mph to ft/s
            angle_rad_tennis = math.radians(serve_angle)
            
            # Initial velocity components
            v0x_tennis = serve_speed_fps * math.cos(angle_rad_tennis)
            v0y_tennis = serve_speed_fps * math.sin(angle_rad_tennis)
            
            # Trajectory equation: h(x) = h₀ + x*tan(θ) - (g*x²)/(2*v₀²*cos²(θ))
            g = 32.2
            a_tennis = -g / (2 * serve_speed_fps**2 * math.cos(angle_rad_tennis)**2)
            b_tennis = math.tan(angle_rad_tennis)
            c_tennis = serve_height
            
            # Complete the square
            h_vertex_tennis = -b_tennis / (2 * a_tennis)
            k_vertex_tennis = a_tennis * h_vertex_tennis**2 + b_tennis * h_vertex_tennis + c_tennis
            
            # Check serve validity
            net_distance = 39  # feet to net
            service_box_distance = 60  # feet to service line
            
            height_at_net = a_tennis * net_distance**2 + b_tennis * net_distance + c_tennis
            height_at_service = a_tennis * service_box_distance**2 + b_tennis * service_box_distance + c_tennis
            
            clears_net = height_at_net > 3.5
            lands_in_box = height_at_service < 0 and height_at_service > -1
            
            st.markdown(f"""
            **Serve Analysis:**
            - **Speed**: {serve_speed} mph ({serve_speed_fps:.0f} ft/s)
            - **Trajectory**: $h(x) = {a_tennis:.6f}x^2 + {b_tennis:.3f}x + {serve_height}$
            - **Vertex form**: $h(x) = {a_tennis:.6f}(x - {h_vertex_tennis:.1f})^2 + {k_vertex_tennis:.1f}$
            
            **Performance Check:**
            - **Clears net** (3.5 ft): {'✅ Yes' if clears_net else '❌ No'} ({height_at_net:.1f} ft at net)
            - **Lands in service box**: {'✅ Yes' if lands_in_box else '❌ No'} ({height_at_service:.1f} ft at service line)
            - **Serve rating**: {'🔥 Ace!' if clears_net and lands_in_box else '⚠️ Fault'}
            """)
        
        with col2:
            # Plot tennis serve
            fig, ax = plt.subplots(figsize=(10, 8))
            
            x_tennis = np.linspace(0, 80, 400)
            h_tennis = a_tennis * x_tennis**2 + b_tennis * x_tennis + c_tennis
            
            ax.plot(x_tennis, h_tennis, 'purple', linewidth=4, label='Serve trajectory')
            
            # Mark key points
            ax.plot(0, serve_height, 'go', markersize=10, label=f'Serve point (0, {serve_height})')
            ax.plot(h_vertex_tennis, k_vertex_tennis, 'ro', markersize=8, label=f'Peak ({h_vertex_tennis:.0f}, {k_vertex_tennis:.1f})')
            
            # Draw court elements
            ax.axhline(0, color='brown', linewidth=6, alpha=0.7, label='Court surface')
            ax.axhline(3.5, xmin=0.45, xmax=0.55, color='black', linewidth=8, label='Net (3.5 ft)')
            ax.axvline(39, color='black', linestyle='-', linewidth=3, alpha=0.7, label='Net position')
            ax.axvline(60, color='blue', linestyle='--', linewidth=2, label='Service line')
            
            # Highlight service box
            ax.axvspan(39, 60, alpha=0.2, color='green', label='Service box target')
            
            # Mark critical heights
            ax.plot(39, height_at_net, 'yo', markersize=8, label=f'Height at net: {height_at_net:.1f} ft')
            if height_at_service > -5:
                ax.plot(60, max(0, height_at_service), 'bo', markersize=8, label=f'Height at service line: {height_at_service:.1f} ft')
            
            ax.set_xlabel('Distance (feet)')
            ax.set_ylabel('Height (feet)')
            ax.set_title(f'Tennis Serve Analysis - {serve_speed} mph, {serve_angle}° angle')
            ax.grid(True, alpha=0.3)
            ax.legend()
            ax.set_xlim(0, 80)
            ax.set_ylim(-2, max(serve_height + 2, k_vertex_tennis + 2))
            
            st.pyplot(fig)
    
    with tab4:
        st.subheader("Football Field Goal Analysis")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🏈 Field Goal Attempt**
            
            **Setup:**
            - **Goalposts**: 10 feet high
            - **Kick distance**: Variable (20-60 yards)
            - **Wind effects**: Can modify trajectory
            - **Pressure**: Game-winning scenarios
            """)
            
            # Football parameters
            kick_distance_yards = st.slider("Kick distance (yards)", 20, 60, 35, 5)
            kick_distance_feet = kick_distance_yards * 3
            kicker_angle = st.slider("Kick angle (degrees)", 25, 55, 35, 2)
            kick_velocity = st.slider("Kick velocity (ft/s)", 50, 90, 70, 2)
            wind_effect = st.slider("Wind effect (ft/s)", -10, 10, 0, 1)
            
            # Adjust velocity for wind
            effective_velocity = kick_velocity + wind_effect
            
            # Calculate trajectory
            angle_rad_football = math.radians(kicker_angle)
            v0x_football = effective_velocity * math.cos(angle_rad_football)
            v0y_football = effective_velocity * math.sin(angle_rad_football)
            
            g = 32.2
            a_football = -g / (2 * effective_velocity**2 * math.cos(angle_rad_football)**2)
            b_football = math.tan(angle_rad_football)
            c_football = 0  # Ground level kick
            
            # Complete the square
            h_vertex_football = -b_football / (2 * a_football)
            k_vertex_football = a_football * h_vertex_football**2 + b_football * h_vertex_football
            
            # Check if field goal is good
            height_at_goal = a_football * kick_distance_feet**2 + b_football * kick_distance_feet
            field_goal_good = height_at_goal > 10
            
            # Calculate range
            range_football = -b_football / a_football * 2
            
            st.markdown(f"""
            **Kick Analysis:**
            - **Distance**: {kick_distance_yards} yards ({kick_distance_feet} feet)
            - **Angle**: {kicker_angle}°
            - **Velocity**: {kick_velocity} ft/s (wind: {wind_effect:+d} ft/s)
            - **Trajectory**: $h(x) = {a_football:.6f}x^2 + {b_football:.3f}x$
            
            **Completing the Square:**
            $h(x) = {a_football:.6f}(x - {h_vertex_football:.1f})^2 + {k_vertex_football:.1f}$
            
            **Result:**
            - **Peak height**: {k_vertex_football:.1f} feet
            - **Height at goalposts**: {height_at_goal:.1f} feet
            - **Clears crossbar**: {'✅ GOOD!' if field_goal_good else '❌ NO GOOD'}
            - **Total range**: {range_football:.0f} feet ({range_football/3:.0f} yards)
            """)
        
        with col2:
            # Plot football trajectory
            fig, ax = plt.subplots(figsize=(10, 8))
            
            x_football = np.linspace(0, range_football, 400)
            h_football = a_football * x_football**2 + b_football * x_football
            
            # Only plot non-negative heights
            valid_football = h_football >= 0
            x_football_valid = x_football[valid_football]
            h_football_valid = h_football[valid_football]
            
            ax.plot(x_football_valid, h_football_valid, 'brown', linewidth=4, label='Ball trajectory')
            
            # Mark key points
            ax.plot(0, 0, 'go', markersize=10, label='Kick point')
            ax.plot(h_vertex_football, k_vertex_football, 'ro', markersize=10, label=f'Peak ({h_vertex_football:.0f}, {k_vertex_football:.1f})')
            ax.plot(kick_distance_feet, height_at_goal, 'yo', markersize=12, label=f'At goalposts: {height_at_goal:.1f} ft')
            
            # Draw field elements
            ax.axhline(0, color='green', linewidth=8, alpha=0.7, label='Field')
            ax.axhline(10, xmin=kick_distance_feet/(range_football+20)-0.02, xmax=kick_distance_feet/(range_football+20)+0.02, 
                      color='yellow', linewidth=12, label='Crossbar (10 ft)')
            ax.axvline(kick_distance_feet, color='yellow', linestyle=':', alpha=0.8, label=f'Goalposts ({kick_distance_yards} yd)')
            
            # Add uprights
            ax.plot([kick_distance_feet, kick_distance_feet], [10, 25], 'yellow', linewidth=6, alpha=0.8)
            
            # Color code the result
            if field_goal_good:
                ax.fill_between([kick_distance_feet-5, kick_distance_feet+5], [10, 10], [30, 30], 
                               alpha=0.3, color='green', label='GOOD!')
            else:
                ax.fill_between([kick_distance_feet-5, kick_distance_feet+5], [0, 0], [10, 10], 
                               alpha=0.3, color='red', label='NO GOOD')
            
            ax.set_xlabel('Distance (feet)')
            ax.set_ylabel('Height (feet)')
            ax.set_title(f'Field Goal Attempt - {kick_distance_yards} yards, {kicker_angle}°')
            ax.grid(True, alpha=0.3)
            ax.legend()
            ax.set_xlim(0, max(range_football + 20, kick_distance_feet + 30))
            ax.set_ylim(0, max(k_vertex_football + 5, 30))
            
            st.pyplot(fig)

elif section == "📝 Problem Solving":
    st.header("📝 Real-World Problem Solving")
    
    problem_type = st.selectbox("Choose a sports scenario:", [
        "🏀 Basketball Shot Optimization", 
        "🏌️ Golf Drive Analysis", 
        "🎯 Archery Precision", 
        "🚀 Rocket League Physics"
    ])
    
    if problem_type == "🏀 Basketball Shot Optimization":
        st.subheader("Basketball Three-Point Shot Analysis")
        
        st.markdown("""
        **Problem:** A basketball player is attempting a three-point shot from 25 feet away. 
        The ball's trajectory follows: $h(x) = -0.03x^2 + 0.75x + 6.5$
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            # Problem parameters
            shot_distance = st.slider("Shot distance (feet)", 20, 30, 25)
            a_shot = st.slider("Trajectory coefficient a", -0.05, -0.01, -0.03, 0.005)
            b_shot = st.slider("Initial velocity component b", 0.5, 1.0, 0.75, 0.05)
            c_shot = st.slider("Release height (feet)", 6.0, 8.0, 6.5, 0.1)
            
            # Complete the square
            h_optimal = -b_shot / (2 * a_shot)
            k_optimal = a_shot * h_optimal**2 + b_shot * h_optimal + c_shot
            
            # Check shot success
            basket_height = 10.0
            shot_height_at_basket = a_shot * shot_distance**2 + b_shot * shot_distance + c_shot
            shot_success = abs(shot_height_at_basket - basket_height) < 0.5
            
            if st.button("Complete the Square Step-by-Step"):
                st.markdown(f"""
                **Step-by-Step Solution:**
                
                **Given:** $h(x) = {a_shot}x^2 + {b_shot}x + {c_shot}$
                
                **Step 1:** Identify coefficients
                - $a = {a_shot}$, $b = {b_shot}$, $c = {c_shot}$
                
                **Step 2:** Find vertex x-coordinate
                - $h = -\\frac{{b}}{{2a}} = -\\frac{{{b_shot}}}{{2({a_shot})}} = {h_optimal:.2f}$ feet
                
                **Step 3:** Find vertex y-coordinate
                - $k = {a_shot}({h_optimal:.2f})^2 + {b_shot}({h_optimal:.2f}) + {c_shot} = {k_optimal:.2f}$ feet
                
                **Step 4:** Write vertex form
                - $h(x) = {a_shot}(x - {h_optimal:.2f})^2 + {k_optimal:.2f}$
                
                **Analysis:**
                - **Peak height:** {k_optimal:.2f} feet at {h_optimal:.2f} feet distance
                - **Ball height at basket:** {shot_height_at_basket:.2f} feet
                - **Shot result:** {'🎯 SWISH!' if shot_success else '🚫 MISS'}
                """)
        
        with col2:
            # Plot basketball shot
            fig, ax = plt.subplots(figsize=(10, 8))
            
            x_range = np.linspace(0, 30, 400)
            h_trajectory = a_shot * x_range**2 + b_shot * x_range + c_shot
            
            # Only plot above ground
            valid_trajectory = h_trajectory >= 0
            x_valid = x_range[valid_trajectory]
            h_valid = h_trajectory[valid_trajectory]
            
            ax.plot(x_valid, h_valid, 'orange', linewidth=4, label='Shot trajectory')
            
            # Mark key points
            ax.plot(0, c_shot, 'go', markersize=10, label=f'Release ({c_shot} ft)')
            ax.plot(h_optimal, k_optimal, 'ro', markersize=10, label=f'Peak ({h_optimal:.1f}, {k_optimal:.1f})')
            ax.plot(shot_distance, 10, 'bs', markersize=12, label=f'Basket ({shot_distance}, 10)')
            ax.plot(shot_distance, shot_height_at_basket, 'yo', markersize=10, 
                   label=f'Ball at basket: {shot_height_at_basket:.1f} ft')
            
            # Draw court elements
            ax.axhline(0, color='brown', linewidth=6, alpha=0.7, label='Court')
            ax.axvline(shot_distance, color='blue', linestyle='--', alpha=0.7)
            
            # Success zone
            ax.axhspan(9.5, 10.5, xmin=shot_distance/30-0.02, xmax=shot_distance/30+0.02, 
                      alpha=0.3, color='green', label='Success zone')
            
            ax.set_xlabel('Distance (feet)')
            ax.set_ylabel('Height (feet)')
            ax.set_title('Three-Point Shot Analysis')
            ax.grid(True, alpha=0.3)
            ax.legend()
            ax.set_xlim(0, 30)
            ax.set_ylim(0, max(k_optimal + 2, 15))
            
            st.pyplot(fig)
    
    elif problem_type == "🏌️ Golf Drive Analysis":
        st.subheader("Golf Drive Distance Optimization")
        
        st.markdown("""
        **Problem:** A golfer wants to maximize driving distance while avoiding a water hazard 
        located 280 yards away. The ball trajectory is: $h(d) = -0.002d^2 + 0.8d$
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            # Golf parameters
            hazard_distance = st.slider("Water hazard distance (yards)", 250, 320, 280)
            a_golf = st.slider("Trajectory coefficient", -0.005, -0.001, -0.002, 0.0005)
            b_golf = st.slider("Launch coefficient", 0.5, 1.2, 0.8, 0.05)
            
            # Complete the square for golf trajectory
            h_max_golf = -b_golf / (2 * a_golf)
            k_max_golf = a_golf * h_max_golf**2 + b_golf * h_max_golf
            
            # Calculate total distance (where ball lands)
            total_distance = -b_golf / a_golf
            
            # Safety analysis
            height_at_hazard = a_golf * hazard_distance**2 + b_golf * hazard_distance
            clears_hazard = height_at_hazard > 0
            
            st.markdown(f"""
            **Golf Drive Analysis:**
            
            **Trajectory:** $h(d) = {a_golf}d^2 + {b_golf}d$
            
            **Completing the Square:**
            1. **Find peak distance:** $d = -\\frac{{{b_golf}}}{{2({a_golf})}} = {h_max_golf:.0f}$ yards
            2. **Find peak height:** $h = {k_max_golf:.1f}$ yards
            3. **Vertex form:** $h(d) = {a_golf}(d - {h_max_golf:.0f})^2 + {k_max_golf:.1f}$
            
            **Performance Metrics:**
            - **Maximum height:** {k_max_golf:.1f} yards ({k_max_golf*3:.0f} feet)
            - **Total distance:** {total_distance:.0f} yards
            - **Clears water hazard:** {'✅ Safe' if clears_hazard else '❌ Water ball!'}
            - **Distance rating:** {'🔥 Long drive!' if total_distance > 300 else '⚠️ Short drive' if total_distance < 250 else '👍 Good drive'}
            """)
        
        with col2:
            # Plot golf trajectory
            fig, ax = plt.subplots(figsize=(10, 8))
            
            d_golf = np.linspace(0, total_distance, 400)
            h_golf = a_golf * d_golf**2 + b_golf * d_golf
            
            # Only plot non-negative heights
            valid_golf = h_golf >= 0
            d_valid = d_golf[valid_golf]
            h_valid = h_golf[valid_golf]
            
            ax.plot(d_valid, h_valid, 'white', linewidth=4, label='Ball flight')
            
            # Mark key points
            ax.plot(0, 0, 'go', markersize=10, label='Tee')
            ax.plot(h_max_golf, k_max_golf, 'ro', markersize=10, label=f'Peak ({h_max_golf:.0f}, {k_max_golf:.1f})')
            ax.plot(total_distance, 0, 'bo', markersize=10, label=f'Landing ({total_distance:.0f} yards)')
            
            # Draw course elements
            ax.axhline(0, color='green', linewidth=8, alpha=0.8, label='Fairway')
            
            # Water hazard
            hazard_width = 40
            ax.axvspan(hazard_distance, hazard_distance + hazard_width, alpha=0.4, color='blue', label='Water hazard')
            ax.text(hazard_distance + hazard_width/2, k_max_golf/2, 'WATER\nHAZARD', 
                   ha='center', va='center', fontsize=12, fontweight='bold', color='blue')
            
            # Safety check at hazard
            if height_at_hazard > 0:
                ax.plot(hazard_distance, height_at_hazard, 'yo', markersize=8, 
                       label=f'Height at hazard: {height_at_hazard:.2f} yards')
            
            ax.set_xlabel('Distance (yards)')
            ax.set_ylabel('Height (yards)')
            ax.set_title('Golf Drive Analysis - Distance vs Safety')
            ax.grid(True, alpha=0.3)
            ax.legend()
            ax.set_xlim(0, max(total_distance + 50, hazard_distance + 80))
            ax.set_ylim(0, k_max_golf + 10)
            
            st.pyplot(fig)

elif section == "🎯 Performance Analysis":
    st.header("🎯 Advanced Performance Analysis")
    
    st.markdown("""
    **Use completing the square to optimize athletic performance across multiple sports!**
    This section demonstrates how vertex form reveals optimal conditions for peak performance.
    """)
    
    analysis_type = st.selectbox("Choose analysis type:", [
        "Multi-Sport Comparison",
        "Optimal Angle Calculator", 
        "Wind Effect Analysis",
        "Performance Trends"
    ])
    
    if analysis_type == "Multi-Sport Comparison":
        st.subheader("Cross-Sport Trajectory Comparison")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Configure multiple sports scenarios:**")
            
            # Basketball
            st.markdown("**🏀 Basketball:**")
            bb_a = st.slider("Basketball a", -0.1, -0.01, -0.05, 0.005, key="bb_a")
            bb_b = st.slider("Basketball b", 0.3, 1.0, 0.6, 0.05, key="bb_b")
            bb_c = st.slider("Basketball release height", 6.0, 8.0, 6.5, 0.1, key="bb_c")
            
            # Soccer
            st.markdown("**⚽ Soccer:**")
            soccer_a = st.slider("Soccer a", -0.02, -0.005, -0.01, 0.001, key="soccer_a")
            soccer_b = st.slider("Soccer b", 0.5, 1.5, 0.8, 0.05, key="soccer_b")
            soccer_c = 0  # Ground level
            
            # Football
            st.markdown("**🏈 Football:**")
            fb_a = st.slider("Football a", -0.015, -0.005, -0.008, 0.001, key="fb_a")
            fb_b = st.slider("Football b", 0.4, 1.0, 0.7, 0.05, key="fb_b")
            fb_c = 0  # Ground level
            
            # Calculate vertices for each sport
            sports_data = {
                'Basketball': {'a': bb_a, 'b': bb_b, 'c': bb_c, 'color': 'orange'},
                'Soccer': {'a': soccer_a, 'b': soccer_b, 'c': soccer_c, 'color': 'green'},
                'Football': {'a': fb_a, 'b': fb_b, 'c': fb_c, 'color': 'brown'}
            }
            
            st.markdown("**Vertex Analysis:**")
            for sport, data in sports_data.items():
                h_vertex = -data['b'] / (2 * data['a'])
                k_vertex = data['a'] * h_vertex**2 + data['b'] * h_vertex + data['c']
                st.write(f"**{sport}:** Peak at ({h_vertex:.1f}, {k_vertex:.1f})")
        
        with col2:
            # Plot all sports trajectories
            fig, ax = plt.subplots(figsize=(12, 8))
            
            for sport, data in sports_data.items():
                # Calculate range for each sport
                if data['c'] == 0:  # Ground level sports
                    x_max = -data['b'] / data['a']
                else:  # Elevated sports
                    # Solve for where trajectory hits ground: ax² + bx + c = 0
                    discriminant = data['b']**2 - 4*data['a']*data['c']
                    if discriminant > 0:
                        x_max = (-data['b'] + math.sqrt(discriminant)) / (2*data['a'])
                    else:
                        x_max = 50  # Default range
                
                x_range = np.linspace(0, min(x_max, 100), 400)
                y_trajectory = data['a'] * x_range**2 + data['b'] * x_range + data['c']
                
                # Only plot non-negative heights
                valid_indices = y_trajectory >= 0
                x_valid = x_range[valid_indices]
                y_valid = y_trajectory[valid_indices]
                
                ax.plot(x_valid, y_valid, color=data['color'], linewidth=3, label=f'{sport} trajectory')
                
                # Mark vertex
                h_vertex = -data['b'] / (2 * data['a'])
                k_vertex = data['a'] * h_vertex**2 + data['b'] * h_vertex + data['c']
                ax.plot(h_vertex, k_vertex, 'o', color=data['color'], markersize=8, 
                       markeredgecolor='black', markeredgewidth=2)
            
            ax.set_xlabel('Distance (feet/yards)')
            ax.set_ylabel('Height (feet/yards)')
            ax.set_title('Multi-Sport Trajectory Comparison')
            ax.grid(True, alpha=0.3)
            ax.legend()
            ax.set_xlim(0, 100)
            ax.set_ylim(0, 50)
            
            st.pyplot(fig)

# Educational Standards and Resources Section
st.markdown("---")
st.header("📋 Educational Standards & Cognitive Development")

# Common Core Standards breakdown
with st.expander("📚 Common Core Standards Alignment"):
    st.markdown("""
    ### High School Algebra Standards:
    
    **A-SSE (Seeing Structure in Expressions):**
    - A-SSE.A.2: Use the structure of an expression to identify ways to rewrite it
    - A-SSE.B.3: Choose and produce equivalent forms of an expression to reveal properties
    - A-SSE.B.3.a: Factor a quadratic expression and complete the square in a quadratic expression
    
    **A-CED (Creating Equations):**
    - A-CED.A.1: Create equations in one variable and use them to solve problems
    - A-CED.A.2: Create equations in two or more variables to represent relationships
    - A-CED.A.3: Represent constraints by systems of equations and interpret solutions
    
    **A-REI (Reasoning with Equations and Inequalities):**
    - A-REI.B.4: Solve quadratic equations by completing the square, factoring, and quadratic formula
    - A-REI.B.4.a: Use the method of completing the square to transform any quadratic equation
    - A-REI.D.11: Explain why the x-coordinates of intersection points are solutions
    
    **F-IF (Interpreting Functions):**
    - F-IF.C.7: Graph functions and show key features including vertex of a parabola
    - F-IF.C.8: Write a function in different but equivalent forms to reveal properties
    - F-IF.C.8.a: Use completing the square to show zeros, extreme values, and symmetry
    
    **F-BF (Building Functions):**
    - F-BF.A.1: Write a function that describes a relationship between two quantities
    - F-BF.B.3: Identify the effect on the graph of replacing f(x) by f(x) + k, k f(x), f(kx), and f(x + k)
    
    **Mathematical Practices:**
    - MP1: Make sense of problems and persevere in solving them
    - MP2: Reason abstractly and quantitatively  
    - MP3: Construct viable arguments and critique reasoning of others
    - MP4: Model with mathematics
    - MP5: Use appropriate tools strategically
    - MP6: Attend to precision
    - MP7: Look for and make use of structure
    - MP8: Look for and express regularity in repeated reasoning
    """)

# Cognitive Abilities Development
with st.expander("🧠 Cognitive Abilities Development"):
    st.markdown("""
    ### Algebraic Reasoning:
    - **Pattern Recognition**: Identifying perfect square trinomials and their structure
    - **Symbolic Manipulation**: Transforming expressions while maintaining equivalence
    - **Structural Thinking**: Understanding how algebraic forms reveal mathematical properties
    
    ### Spatial-Mathematical Intelligence:
    - **Visual-Algebraic Connection**: Linking completing the square to parabola vertex
    - **Geometric Interpretation**: Understanding area models for algebraic expressions
    - **Transformation Visualization**: Seeing how algebraic changes affect graph shapes
    
    ### Problem-Solving Strategies:
    - **Method Selection**: Choosing when completing the square is most effective
    - **Multi-Step Reasoning**: Following complex algebraic procedures systematically
    - **Optimization Thinking**: Using vertex form to find maximum/minimum values
    
    ### Critical Thinking Skills:
    - **Analysis**: Breaking down quadratic expressions into component parts
    - **Synthesis**: Combining algebraic techniques with real-world applications
    - **Evaluation**: Assessing the efficiency of different solution methods
    
    ### Sports Performance Analysis:
    - **Data Interpretation**: Reading trajectory graphs and extracting performance metrics
    - **Predictive Modeling**: Using mathematics to forecast sports outcomes
    - **Optimization Strategies**: Finding ideal angles, speeds, and positions
    
    ### Executive Function Development:
    - **Sequential Processing**: Following multi-step algebraic procedures accurately
    - **Working Memory**: Maintaining multiple algebraic relationships simultaneously
    - **Attention to Detail**: Precision in sign changes and coefficient manipulation
    - **Cognitive Flexibility**: Switching between different representations and methods
    """)

# Educational Resource Links
with st.expander("🔗 Educational Resources & Practice"):
    st.markdown("""
    ### Khan Academy Resources:
    
    **Completing the Square Foundation:**
    - [Introduction to Completing the Square](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:completing-the-square-intro/v/completing-the-square)
    - [Completing the Square (Leading Coefficient ≠ 1)](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:completing-the-square-intro/v/example-completing-the-square-leading-coefficient-not-1)
    - [Vertex Form and Completing the Square](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:quadratic-standard-form/v/quadratic-functions-vertex-form)
    - [Solving Quadratics by Completing the Square](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:solving-quadratics-completing-square/v/solving-quadratics-by-completing-the-square)
    
    **Advanced Applications:**
    - [Quadratic Word Problems](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:quadratic-word-problems/v/projectile-motion-problem-solving)
    - [Projectile Motion](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:quadratic-word-problems/v/projectile-motion-problem-solving)
    - [Optimizing Quadratic Functions](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:quad/x2ec2f6f830c9fb89:quad-standard-form/v/vertex-of-a-parabola)
    
    ### IXL Practice Modules:
    
    **Algebra 1 Level:**
    - [Complete the Square](https://www.ixl.com/math/algebra-1/complete-the-square)
    - [Solve Quadratics by Completing the Square](https://www.ixl.com/math/algebra-1/solve-a-quadratic-equation-by-completing-the-square)
    - [Convert to Vertex Form](https://www.ixl.com/math/algebra-1/convert-a-quadratic-function-to-vertex-form)
    - [Find the Vertex of a Parabola](https://www.ixl.com/math/algebra-1/find-the-vertex-of-a-parabola)
    
    **Algebra 2 Level:**
    - [Complete the Square with Leading Coefficients](https://www.ixl.com/math/algebra-2/complete-the-square-for-quadratic-expressions)
    - [Quadratic Applications](https://www.ixl.com/math/algebra-2/solve-a-quadratic-equation-using-the-zero-product-property)
    - [Projectile Motion Problems](https://www.ixl.com/math/algebra-2/projectile-motion-find-the-maximum-height)
    - [Optimization Problems](https://www.ixl.com/math/algebra-2/solve-quadratic-inequalities)
    
    **Precalculus Level:**
    - [Advanced Quadratic Models](https://www.ixl.com/math/precalculus/write-a-quadratic-function-from-its-zeros)
    - [Conic Sections and Completing the Square](https://www.ixl.com/math/precalculus/convert-equations-of-parabolas-from-general-to-vertex-form)
    
    ### The Organic Chemistry Tutor (YouTube):
    
    **Completing the Square Videos:**
    - [Completing the Square - Basic Examples](https://www.youtube.com/watch?v=XNJyDg3_lKA) - Clear step-by-step method with multiple examples
    - [Completing the Square When A ≠ 1](https://www.youtube.com/watch?v=wLJyaDWN7_E) - Advanced cases with leading coefficients
    - [Solving Quadratic Equations by Completing the Square](https://www.youtube.com/watch?v=UaXyMGpKTaI) - Problem-solving applications
    - [Vertex Form and Completing the Square](https://www.youtube.com/watch?v=FNPhPay7rjY) - Connection to graphing parabolas
    - [Quadratic Word Problems](https://www.youtube.com/watch?v=I_uFx3otvbs) - Real-world applications and projectile motion
    
    **Sports Physics Applications:**
    - [Projectile Motion Problems](https://www.youtube.com/watch?v=R09i_Gjnhv8) - Physics applications in sports
    - [Optimization Problems](https://www.youtube.com/watch?v=ZnqXU1tc7Io) - Finding maximum and minimum values
    
    ### McGraw Hill Connect & ALEKS:
    
    **Textbook Resources:**
    - **McGraw Hill Algebra 1**: Chapter 9 - Quadratic Functions and Equations
    - **McGraw Hill Algebra 2**: Chapter 4 - Quadratic Functions and Relations
    - **McGraw Hill Precalculus**: Chapter 3 - Polynomial and Rational Functions
    
    **ALEKS Modules:**
    - Completing the Square (Basic)
    - Completing the Square with Leading Coefficient
    - Converting to Vertex Form
    - Solving by Completing the Square
    - Applications of Quadratic Functions
    
    **Connect Assignments:**
    - Interactive completing the square practice
    - Sports trajectory modeling assignments
    - Real-world optimization problems
    - Graphing calculator integration exercises
    
    ### Additional Educational Resources:
    
    **Textbook Publishers:**
    - **Pearson MyMathLab**: Interactive completing the square modules
    - **Cengage WebAssign**: Quadratic function applications
    - **Wiley WileyPLUS**: Sports mathematics connections
    
    **Professional Development:**
    - **NCTM (National Council of Teachers of Mathematics)**: Sports in Mathematics Education
    - **MAA (Mathematical Association of America)**: Authentic Applications in Algebra
    - **Desmos Classroom Activities**: Parabola Vertex Form explorations
    
    **Technology Integration:**
    - **Desmos Graphing Calculator**: Interactive vertex form exploration
    - **GeoGebra**: Dynamic completing the square demonstrations  
    - **Wolfram Alpha**: Step-by-step completing the square solutions
    - **TI-84 Calculator**: Programming quadratic analysis functions
    - **Excel/Google Sheets**: Sports data analysis and modeling
    
    **Sports Analytics Resources:**
    - **ESPN Sport Science**: Mathematical analysis of athletic performance
    - **NBA.com Stats**: Basketball trajectory data for real-world problems
    - **Pro Football Focus**: Football analytics and physics applications
    - **Tennis Abstract**: Tennis serve analysis and optimization data
    
    ### Assessment Resources:
    
    **Formative Assessment Tools:**
    - **Kahoot**: Interactive completing the square quizzes
    - **Quizizz**: Gamified practice with sports themes
    - **Padlet**: Collaborative sports math problem collections
    - **Flipgrid**: Student video explanations of completing the square
    
    **Summative Assessment Options:**
    - **Performance Tasks**: Sports optimization projects
    - **Portfolio Assessments**: Collection of real-world applications
    - **Digital Presentations**: Student-created sports math videos
    - **Authentic Assessments**: Consulting projects for local sports teams
    """)

# Assessment and Progress Tracking
with st.expander("📊 Assessment & Progress Tracking"):
    st.markdown("""
    ### Formative Assessment Strategies:
    - **Exit Tickets**: Quick vertex form conversions and sports scenario analysis
    - **Think-Pair-Share**: Collaborative problem-solving with sports applications
    - **Digital Whiteboards**: Real-time completing the square demonstrations
    - **Sports Data Analysis**: Ongoing projects tracking athlete performance optimization
    
    ### Summative Assessment Options:
    - **Sports Consulting Project**: Students act as performance analysts for local teams
    - **Trajectory Optimization Challenge**: Design optimal paths for various sports scenarios
    - **Cross-Curricular Portfolio**: Connecting completing the square to physics and sports science
    - **Peer Teaching Videos**: Students create tutorials explaining completing the square with sports examples
    
    ### Differentiation Strategies:
    - **Visual Learners**: Algebra tiles, geometric models, trajectory graphing, color-coded steps
    - **Kinesthetic Learners**: Physical sports demonstrations, hands-on manipulatives, movement activities
    - **Analytical Learners**: Step-by-step algebraic derivations, multiple solution methods, proof-based approaches
    - **Creative Learners**: Sports story problems, artistic trajectory displays, game-based learning
    - **English Language Learners**: Visual step guides, multilingual sports terminology, collaborative group work
    
    ### Technology-Enhanced Assessment:
    - **Graphing Calculator Programs**: Custom functions for sports trajectory analysis
    - **Spreadsheet Models**: Data analysis and optimization calculations
    - **Interactive Simulations**: Real-time parameter adjustment and outcome prediction
    - **Video Analysis Tools**: Frame-by-frame sports footage examination with mathematical overlay
    
    ### Real-World Performance Metrics:
    - **Accuracy Measures**: How close predictions match actual sports performance
    - **Optimization Success**: Improvement in athlete performance using mathematical insights
    - **Transfer Skills**: Application of completing the square to novel sports scenarios
    - **Communication Skills**: Explaining mathematical concepts to coaches and athletes
    
    ### Progress Monitoring Tools:
    - **Skill Progression Charts**: Tracking mastery from basic to advanced completing the square
    - **Sports Application Rubrics**: Evaluating real-world problem-solving effectiveness
    - **Peer Assessment Protocols**: Students evaluating each other's sports math solutions
    - **Self-Reflection Journals**: Metacognitive awareness of learning process and sports connections
    """)

# Professional Development and Advanced Resources
with st.expander("👨‍🎓 Professional Development & Advanced Resources"):
    st.markdown("""
    ### Teacher Professional Development:
    
    **Organizations & Conferences:**
    - **NCTM Annual Conference**: Sessions on sports mathematics and authentic applications
    - **MAA MathFest**: Research presentations on mathematics in athletics
    - **ICTM (Illinois Council of Teachers of Mathematics)**: State-level sports math workshops
    - **Regional Math Teacher Circles**: Collaborative problem-solving with sports themes
    
    **Graduate Programs & Courses:**
    - **M.Ed. in Mathematics Education**: Specialization in authentic applications and sports integration
    - **Mathematical Modeling Courses**: University-level courses connecting math to real-world scenarios
    - **Sports Analytics Certificates**: Professional development in data analysis for athletics
    - **STEM Integration Workshops**: Cross-curricular approaches to mathematics education
    
    **Research and Publications:**
    - **Journal for Research in Mathematics Education**: Articles on contextual learning and sports applications
    - **Mathematics Teacher (NCTM)**: Classroom-ready activities and sports-based lessons
    - **School Science and Mathematics**: Interdisciplinary approaches to STEM education
    - **International Journal of Mathematical Education**: Global perspectives on applied mathematics
    
    ### Advanced Mathematical Connections:
    
    **Calculus Extensions:**
    - **Optimization Calculus**: Using derivatives to find maximum trajectory heights and distances
    - **Related Rates**: How changing launch angles affect trajectory parameters
    - **Integration Applications**: Calculating areas under trajectory curves for hang time analysis
    
    **Statistics and Data Science:**
    - **Sports Analytics**: Large-scale data analysis of professional sports performance
    - **Regression Analysis**: Fitting quadratic models to real sports trajectory data
    - **Hypothesis Testing**: Validating theoretical models against actual performance data
    
    **Physics Integration:**
    - **Projectile Motion**: Complete physics derivation of trajectory equations
    - **Air Resistance Models**: Modified quadratic equations accounting for drag forces
    - **Energy Conservation**: Connecting kinetic and potential energy to trajectory optimization
    
    ### Industry Partnerships:
    
    **Professional Sports Teams:**
    - **Analytics Departments**: Collaboration opportunities for authentic data access
    - **Performance Coaching**: Real-world optimization problem validation
    - **Technology Integration**: Access to advanced measurement and analysis tools
    
    **Equipment Manufacturers:**
    - **Research and Development**: Mathematical modeling in sports equipment design
    - **Testing Protocols**: Validation of theoretical models with actual product performance
    - **Educational Partnerships**: Curriculum development with industry expertise
    
    **Academic Research Centers:**
    - **Sports Science Institutes**: Collaboration on mathematical modeling research
    - **Engineering Departments**: Biomechanics and trajectory analysis partnerships
    - **Education Schools**: Research on effectiveness of sports-based mathematics instruction
    """)

st.markdown("---")
st.markdown("""
### 🎯 Learning Extensions:
- **Create Sports Highlight Reels**: Analyze real game footage and add mathematical trajectory overlays
- **Design Performance Apps**: Program calculators or spreadsheets for athlete optimization
- **Conduct Original Research**: Partner with local teams to test mathematical predictions
- **Explore Career Connections**: Interview sports analysts, coaches, and performance specialists
- **Build Physical Models**: Construct trajectory demonstration devices for different sports
- **Cross-Curricular Projects**: Connect to physics, health, statistics, and computer science classes

### 🏆 Assessment Portfolio Ideas:
- **Sport-Specific Optimization Reports**: Detailed analysis of performance improvement strategies
- **Video Tutorial Creation**: Student-produced instructional content explaining completing the square through sports
- **Real Data Analysis Projects**: Working with actual sports performance data from local teams
- **Mathematical Modeling Competitions**: Participating in contests that apply mathematics to athletic scenarios
- **Peer Consulting Services**: Students advising teammates on performance optimization using mathematics

*MathCraft modules are designed to meet rigorous academic standards while fostering deep conceptual understanding through hands-on exploration and real-world applications. This completing the square module specifically connects abstract algebraic concepts to the exciting world of sports, making mathematics relevant and engaging for all students.*
""")
