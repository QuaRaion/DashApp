
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# Пример данных
df = pd.DataFrame({
    "Фрукты": ["Яблоки", "Апельсины", "Бананы", "Вишня"],
    "Количество": [4, 3, 2, 5]
})

# Пример графика
fig = px.bar(df, x="Фрукты", y="Количество", title="Пример графика")

# Приложение Dash
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Пример Dash-приложения"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
