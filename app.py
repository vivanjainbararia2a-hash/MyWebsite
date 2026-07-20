from flask import Flask

app = Flask(__name__)

def page(title, content, background=None):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>software</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: Arial, sans-serif;
            }}

            body {{
    {"background-image: url('/static/" + background + "');" if background else ""}
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    background-attachment: fixed;
}}

            nav {{
                background: #0d6efd;
                padding: 15px;
                text-align: center;
            }}

            nav a {{
                color: white;
                text-decoration: none;
                margin: 0 20px;
                font-size: 18px;
                font-weight: bold;
            }}

            .container {{
                width: 90%;
                margin: auto;
                padding: 40px;
            }}

            .hero {{
                text-align: center;
                padding: 80px;
                background: white;
                border-radius: 15px;
                box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
                margin-top: 30px;
            }}

            .hero h1 {{
                color: #0d6efd;
                font-size: 50px;
                margin-bottom: 20px;
            }}

            .cards {{
                display: grid;
                grid-template-columns: repeat(auto-fit,minmax(250px,1fr));
                gap: 20px;
                margin-top: 40px;
            }}

            .card {{
                background: white;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
                text-align: center;
            }}

            .btn {{
                display: inline-block;
                margin-top: 15px;
                background: #0d6efd;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 8px;
            }}

            footer {{
                text-align: center;
                padding: 25px;
                margin-top: 50px;
                background: #111;
                color: white;
            }}
        </style>
    </head>
    <body>

        <nav>
            <a href="/">Home</a>
            <a href="/product1">Product 1</a>
            <a href="/product2">Product 2</a>
            <a href="/product3">Product 3</a>
            <a href="/product4">Product 4</a>
        </nav>

        <div class="container">
            {content}
        </div>

        <footer>
            © 2026 Your Business | All Rights Reserved
        </footer>

    </body>
    </html>
    """

@app.route("/")
def home():
    return page(
        "Home",
        """
        <div class="hero">
            <h1>Welcome To My Business</h1>

            <img src="/static/home.png" width="300">

            <p>Professional solutions for modern customers.</p>
        </div>

        <div class="cards">
            <div class="card">
                <h2>Product 1</h2>
                <p>Premium Quality Product</p>
                <a class="btn" href="/product1">View</a>
            </div>

            <div class="card">
                <h2>Product 2</h2>
                <p>Smart Business Solution</p>
                <a class="btn" href="/product2">View</a>
            </div>

            <div class="card">
                <h2>Product 3</h2>
                <p>Advanced Technology</p>
                <a class="btn" href="/product3">View</a>
            </div>

            <div class="card">
                <h2>Product 4</h2>
                <p>Reliable Services</p>
                <a class="btn" href="/product4">View</a>
            </div>
        </div>
        """
    )

@app.route("/product1")
def product1():
    return page(
        "Product 1",
        """
        <div class="hero">
            <h1>Product 1</h1>

            <img src="/static/product1.png"
                 alt="Product 1"
                 width="150">

            <p>High-quality product for your business.</p>
        </div>
        """
    )
@app.route("/product2")
def product2():
    return page(
        "Product 2",
        """
        <div class="hero">
            <h1>Product 2</h1>

            <img src="/static/product2.png"
                 alt="Product 2"
                 width="150">

            <p>High-quality product for your business.</p>
        </div>
        """
    )
@app.route("/product3")
def product3():
    return page(
        "Product 3",
        """
        <div class="hero">
            <h1>Product 3</h1>

            <img src="/static/product3.png"
                 alt="Product 3"
                 width="150">

            <p>High-quality product for your business.</p>
        </div>
        """
    )
@app.route("/product4")
def product4():
    return page(
        "Product 4",
        """
        <div class="hero">
            <h1>Product 4</h1>

            <img src="/static/product4.png"
                 alt="Product 4"
                 width="150">

            <p>High-quality product for your business.</p>
        </div>
        """
    )
if __name__ == "__main__":
    app.run(debug=True)
