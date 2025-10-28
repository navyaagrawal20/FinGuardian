import plotly.graph_objs as go

def compute_risk(age, income, dependents, loans):
    score = 0
    score += 1 if age > 50 else 0
    score += 2 if income < 300000 else 0
    score += dependents
    score += 2 if loans else 0
    return score

def get_risk_level(score):
    if score <= 2: return "Low", "green"
    elif score <= 4: return "Medium", "orange"
    else: return "High", "red"

def generate_risk_profile(age, income, dependents, loans):
    score = compute_risk(age, income, dependents, loans)
    level, color = get_risk_level(score)

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        title = {'text': f"Financial Risk: {level}"},
        gauge = {
            'axis': {'range': [0, 10]},
            'bar': {'color': color},
        }
    ))
    return fig
