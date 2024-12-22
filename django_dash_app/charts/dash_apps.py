from django_plotly_dash import DjangoDash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Создаём приложение Dash
app = DjangoDash("ChartBuilder")  # Название должно совпадать с тем, что указано в HTML

# Пример данных
df = pd.DataFrame({
    "Фрукты": ["Яблоки", "Апельсины", "Бананы", "Вишня"],
    "Количество": [4, 3, 2, 5]
})

# Пример графика
fig = px.bar(df, x="Фрукты", y="Количество", title="Пример графика")

# Layout Dash
app.layout = html.Div([
    html.H1("Пример Dash-приложения"),
    dcc.Graph(figure=fig)
])
