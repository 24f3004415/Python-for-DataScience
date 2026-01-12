import streamlit as st
import random
import time

# Page configuration
st.set_page_config(
    page_title="CYBER GUESS",
    page_icon="🎮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for futuristic design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1a2e 50%, #16213e 100%);
        font-family: 'Orbitron', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Title styling */
    .cyber-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(45deg, #00f5ff, #00ff88, #00f5ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 0 30px rgba(0, 245, 255, 0.5);
        margin-bottom: 1rem;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { filter: drop-shadow(0 0 10px #00f5ff); }
        to { filter: drop-shadow(0 0 20px #00ff88); }
    }
    
    /* Stats container */
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
        gap: 1rem;
    }
    
    .stat-box {
        background: linear-gradient(135deg, rgba(0, 245, 255, 0.1), rgba(0, 255, 136, 0.1));
        border: 2px solid #00f5ff;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        flex: 1;
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .stat-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 30px rgba(0, 245, 255, 0.5);
    }
    
    .stat-label {
        color: #00f5ff;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 0.5rem;
    }
    
    .stat-value {
        color: #00ff88;
        font-size: 2rem;
        font-weight: 900;
        text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
    }
    
    /* Message styling */
    .message-box {
        background: linear-gradient(135deg, rgba(0, 245, 255, 0.15), rgba(0, 255, 136, 0.15));
        border-left: 4px solid #00f5ff;
        padding: 1.5rem;
        margin: 2rem 0;
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.2);
    }
    
    .message-high {
        border-left-color: #ff006e;
        background: linear-gradient(135deg, rgba(255, 0, 110, 0.15), rgba(255, 0, 110, 0.05));
    }
    
    .message-low {
        border-left-color: #00f5ff;
        background: linear-gradient(135deg, rgba(0, 245, 255, 0.15), rgba(0, 245, 255, 0.05));
    }
    
    .message-success {
        border-left-color: #00ff88;
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.15), rgba(0, 255, 136, 0.05));
    }
    
    .message-text {
        color: #ffffff;
        font-size: 1.5rem;
        text-align: center;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 3px;
    }
    
    /* Input styling */
    .stNumberInput > div > div > input {
        background: rgba(0, 245, 255, 0.1);
        border: 2px solid #00f5ff;
        border-radius: 10px;
        color: #00ff88;
        font-size: 1.5rem;
        font-weight: 700;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        box-shadow: inset 0 0 10px rgba(0, 245, 255, 0.2);
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #00ff88;
        box-shadow: 0 0 20px rgba(0, 255, 136, 0.4);
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(45deg, #00f5ff, #00ff88);
        color: #0a0e27;
        font-family: 'Orbitron', sans-serif;
        font-size: 1.2rem;
        font-weight: 900;
        padding: 1rem 2rem;
        border: none;
        border-radius: 10px;
        text-transform: uppercase;
        letter-spacing: 2px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.4);
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 30px rgba(0, 245, 255, 0.7);
    }
    
    /* History styling */
    .history-item {
        background: rgba(0, 245, 255, 0.05);
        border-left: 3px solid #00f5ff;
        padding: 0.8rem;
        margin: 0.5rem 0;
        border-radius: 5px;
        color: #ffffff;
        font-size: 0.9rem;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #00f5ff, transparent);
        margin: 2rem 0;
    }
    
    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #00f5ff;
        font-size: 1rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.history = []
    st.session_state.game_won = False
    st.session_state.last_guess = None
    st.session_state.message = ""
    st.session_state.message_type = ""

def reset_game():
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.history = []
    st.session_state.game_won = False
    st.session_state.last_guess = None
    st.session_state.message = ""
    st.session_state.message_type = ""

def make_guess(guess):
    if st.session_state.game_won:
        return
    
    st.session_state.attempts += 1
    st.session_state.last_guess = guess
    
    if guess < st.session_state.target_number:
        st.session_state.message = "📈 TOO LOW! INCREASE POWER!"
        st.session_state.message_type = "low"
        st.session_state.history.append(f"Attempt {st.session_state.attempts}: {guess} → TOO LOW")
    elif guess > st.session_state.target_number:
        st.session_state.message = "📉 TOO HIGH! DECREASE POWER!"
        st.session_state.message_type = "high"
        st.session_state.history.append(f"Attempt {st.session_state.attempts}: {guess} → TOO HIGH")
    else:
        st.session_state.message = f"🎯 SYSTEM BREACHED! YOU WON IN {st.session_state.attempts} ATTEMPTS!"
        st.session_state.message_type = "success"
        st.session_state.game_won = True
        st.session_state.history.append(f"Attempt {st.session_state.attempts}: {guess} → ✓ CORRECT!")

# Main UI
st.markdown('<h1 class="cyber-title">⚡ CYBER GUESS ⚡</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Neural Network Challenge: Decode the Number</p>', unsafe_allow_html=True)

# Stats display
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-label">Range</div>
        <div class="stat-value">1-100</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-label">Attempts</div>
        <div class="stat-value">{st.session_state.attempts}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    status = "ACTIVE" if not st.session_state.game_won else "COMPLETE"
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-label">Status</div>
        <div class="stat-value" style="font-size: 1.3rem;">{status}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Display message
if st.session_state.message:
    message_class = f"message-{st.session_state.message_type}"
    st.markdown(f"""
    <div class="message-box {message_class}">
        <div class="message-text">{st.session_state.message}</div>
    </div>
    """, unsafe_allow_html=True)

# Game interface
if not st.session_state.game_won:
    st.markdown("<br>", unsafe_allow_html=True)
    guess = st.number_input(
        "ENTER YOUR GUESS",
        min_value=1,
        max_value=100,
        value=50,
        step=1,
        key="guess_input",
        label_visibility="visible"
    )
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("🚀 SUBMIT GUESS", use_container_width=True):
            make_guess(guess)
            st.rerun()
    
    with col2:
        if st.button("🔄 RESET", use_container_width=True):
            reset_game()
            st.rerun()
else:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🎮 PLAY AGAIN", use_container_width=True):
        reset_game()
        st.rerun()

# History
if st.session_state.history:
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Mission Log</p>', unsafe_allow_html=True)
    
    for item in reversed(st.session_state.history[-10:]):  # Show last 10 attempts
        st.markdown(f'<div class="history-item">{item}</div>', unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #00f5ff; font-size: 0.8rem; opacity: 0.6;">
    CYBER GUESS v2.0 | NEURAL NETWORK GAMING SYSTEM
</div>
""", unsafe_allow_html=True)