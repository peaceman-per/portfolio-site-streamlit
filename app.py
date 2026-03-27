
# libraries
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# -- CONFIG --
st.set_page_config(page_title="William | Data Scientist", layout="wide")

# -- SIDEBAR NAVIGATION --
st.sidebar.image("photo.jpg", width=150)
st.sidebar.title("William")
st.sidebar.markdown("MSc Data Science · University of London")
st.sidebar.markdown("[GitHub](https://github.com/peaceman-per) · [Kaggle](https://kaggle.com/peaceman1) · [LinkedIn](https://linkedin.com/in/ws-r)")

page = st.sidebar.radio("Navigate", [
    "🏠 About Me",
    "🧠 Neural Network Explorer",
    "📂 Projects",
    "🏅 Kaggle Competitions",
    "📜 CV & Certifications",
    "📬 Contact"
])

# -- ABOUT ME --
if page == "🏠 About Me":
    st.title("Hi, I'm William")
    st.write("""
    I'm a data scientist with a Masters in Data Science (University of London)
    and a BSc in Maths, Stats & Data Science (University of Bath).

    I'm passionate about deep learning, statistical modelling, and turning
    complex data into actionable insight. I've worked as a data analyst at
    Optimized Project Partners and completed 3 Kaggle competitions.

    When I'm not coding, I'm swimming, climbing mountains, or listening
    to music on my hi-fi.
    """)
    st.download_button("📥 Download my CV", data=open("cv.pdf", "rb"), file_name="CV.pdf")

# -- INTERACTIVE NEURAL NETWORK EXPLORER --
elif page == "🧠 Neural Network Explorer":
    st.title("How Neural Networks Learn")
    st.write("Adjust the sliders and watch a neural network train in real time.")

    col1, col2 = st.columns(2)
    with col1:
        neurons = st.slider("Hidden layer neurons", 2, 64, 16)
        learning_rate = st.select_slider("Learning rate", [0.001, 0.01, 0.05, 0.1])
        epochs = st.slider("Training epochs", 10, 300, 100)
        activation = st.selectbox("Activation function", ["relu", "sigmoid", "tanh"])

    # Generate toy data (e.g., spiral classification)
    np.random.seed(42)
    N = 200
    t = np.linspace(0, 4 * np.pi, N)
    X = np.vstack([
        np.column_stack([t * np.cos(t), t * np.sin(t)]),
        np.column_stack([t * np.cos(t + np.pi), t * np.sin(t + np.pi)])
    ]) + np.random.randn(2 * N, 2) * 0.5
    y = np.array([0]*N + [1]*N)

    # Build and train
    model = Sequential([
        Dense(neurons, input_shape=(2,), activation=activation),
        Dense(neurons, activation=activation),
        Dense(1, activation='sigmoid')
    ])
    from tensorflow.keras.optimizers import Adam
    model.compile(optimizer=Adam(learning_rate=learning_rate),
                  loss='binary_crossentropy', metrics=['accuracy'])
    history = model.fit(X, y, epochs=epochs, verbose=0, validation_split=0.2)

    with col2:
        # Decision boundary
        xx, yy = np.meshgrid(np.linspace(X[:,0].min()-1, X[:,0].max()+1, 200),
                             np.linspace(X[:,1].min()-1, X[:,1].max()+1, 200))
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()], verbose=0).reshape(xx.shape)
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.contourf(xx, yy, Z, alpha=0.4, cmap='RdBu')
        ax.scatter(X[:,0], X[:,1], c=y, cmap='RdBu', s=10, edgecolors='k', linewidths=0.3)
        ax.set_title(f"Decision Boundary ({neurons} neurons, {activation})")
        st.pyplot(fig)

    # Loss curve
    fig2, ax2 = plt.subplots(figsize=(8, 3))
    ax2.plot(history.history['loss'], label='Train Loss')
    ax2.plot(history.history['val_loss'], label='Val Loss')
    ax2.legend()
    ax2.set_xlabel("Epoch")
    ax2.set_ylabel("Loss")
    st.pyplot(fig2)

    st.success(f"Final accuracy: {history.history['accuracy'][-1]:.1%}")
    st.write("💡 **Try it:** Set neurons to 2, then 64. See how capacity affects the boundary!")

# -- PROJECTS --
elif page == "📂 Projects":
    st.title("Projects")
    projects = [
        {
            "title": "🏆 CIFAR-10: 96.15% with Ensembled Transfer ResNets",
            "desc": "3-model ensemble using transfer learning on non-linear ResNet architectures with data augmentation.",
            "tags": ["Deep Learning", "Keras", "Transfer Learning", "Computer Vision"],
            "github": "https://github.com/yourname/cifar10-resnet"
        },
        {
            "title": "📊 Big Data Pipeline with Spark & Hadoop",
            "desc": "Distributed data processing pipeline using MapReduce and Spark for large-scale analytics.",
            "tags": ["Big Data", "Spark", "Hadoop", "Distributed Computing"],
            "github": "https://github.com/yourname/spark-pipeline"
        },
        # Add more projects...
    ]
    for p in projects:
        with st.expander(p["title"]):
            st.write(p["desc"])
            st.markdown(" · ".join([f"`{t}`" for t in p["tags"]]))
            st.markdown(f"[🔗 GitHub Repo]({p['github']})")
            st.download_button(f"📥 Download Report", data=b"placeholder", file_name="report.pdf",
                               key=p["title"])

# -- Add Kaggle, CV, Contact pages similarly --