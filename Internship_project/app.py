import streamlit as st
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons

st.sidebar.markdown("# Streamlit Dashboard")

dataset=st.sidebar.selectbox(
    'Dataset',
    ('DS1','DS2')
)

algorithm=st.sidebar.selectbox(
    'Algorithm',
    ('Gradient Boosting for Classification','XgBoost for Classification')
)

loss=st.sidebar.selectbox(
    'Loss Function',
    ('deviance','exponential')
)

learning_rate=st.sidebar.number_input('Learning Rate')

n_estimators=st.sidebar.slider('Boosting Stages')

subsample=st.sidebar.number_input('Subsample')

criterion=st.sidebar.selectbox(
    'Criterion',
    ('friedman_mse','mse','mae')
)

min_samples_split=st.sidebar.number_input('Minimum Samples Split')

min_samples_leaf=st.sidebar.number_input('Minimum Samples Leaf')

min_weight_fraction_leaf=st.sidebar.number_input('Minimum Weight Fraction')

max_depth=st.sidebar.slider('Maximum Depth')

min_impurity_decrease=st.sidebar.number_input('Minimum Impurity Decrease')

min_impurity_split=st.sidebar.number_input('Minimum Impurity Split')

init=st.sidebar.selectbox(
    'Init (Have to think)',
    ('estimator','zero')
)

random_state=st.sidebar.selectbox(
    'Random State (Have to think)',
    (' ',' ')
)

max_features=st.sidebar.selectbox(
    'Max Features',
    ('auto','sqrt','log2')
)

verbose=st.sidebar.slider('Verbose')

max_leaf_nodes=st.sidebar.slider('Maximum Leaf Nodes')

warm_start=st.sidebar.selectbox(
    'Warm Start',
    ('True','False')
)

validation_fraction=st.sidebar.number_input('Validation Fraction')

n_iter_no_change= st.sidebar.slider('n Iteration No Change')

tol=st.sidebar.number_input('Tolerance')

ccp_alpha=st.sidebar.number_input('Cost-Complexity Pruning Alpha')

st.pyplot(fig='')

st.sidebar.button('Set to Default')

if st.sidebar.button('Run Algorithm'):
    print('Hello! world')