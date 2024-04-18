import dash
from dash import dcc,html,callback,Output,Input,State

app = dash.Dash(__name__)

# Sample list of image URLs
image_urls = [
    'assets\AMIT.jpg',
    'assets\Anindya.jpg',
    'assets\WhatsApp Image 2024-04-17 at 21.13.26_248fb876.jpg'
]

image=html.Div([
        html.Img(src=image_url, style={'width': '300px', 'height': '300px'})
        for image_url in image_urls
    ])

app.layout = html.Div([
    html.H1("Display Images from a List"),
    html.Button('Click Me', id='my-input'),
    html.Div(id="my-output")

])


@app.callback(
    Output('my-output', 'children'),
    [Input('my-input', 'n_clicks')]
)
def display_image(n_clicks):
    if n_clicks is None:
        return html.Div()  # No image displayed initially
    else:
        return image

if __name__ == '__main__':
    app.run_server(debug=True)                                     