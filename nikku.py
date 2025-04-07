import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="nikku's love book", layout="centered")

book_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .book {
            width: 600px;
            height: 400px;
            margin: auto;
            position: relative;
            perspective: 1500px;
        }
        .page {
            width: 100%;
            height: 100%;
            background: #fff;
            position: absolute;
            transform-origin: left;
            transition: transform 1s;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
            border: 1px solid #ddd;
            box-sizing: border-box;
            font-family: "Georgia", serif;
        }
        .page.back {
            transform: rotateY(-180deg);
            z-index: 0;
        }
        .page.front {
            z-index: 1;
            background: url('https://media-hosting.imagekit.io/6d6bd377abeb47b4/WhatsApp%20Image%202025-04-07%20at%2009.38.30_47bf7a8e.jpg?Expires=1838620892&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=1JD2IPgZCAo~Dj053beX91EfGHtiYGfi9~UntedWDwKGHEomg43nNGbyhWICvLG0PyCmh7wkjAcFl7FFtqe4XZOndg4L2LQkT2zMwmX8mOTxp7XNnkQIjA0FsAZ0OZeud-VH2KyJD~mDqlXXstcPPCjsjj1mx46l1Jy9LXyQjHBR~7mxGR-Dc0FyrozrDT-H2rxZ4d2baf9fg8HoobRFa21Xa4oG7JFWeeLzogTcGMiESDHrJTJBQzc8x7ChdEq3xM4THuxO9Cjb7vPHZ373WhpTxAUTTIylZTlNDR70ognnFCfbMLm45pWlPKteL9HnIrmtxJzRIng1AYoCQCG9UA__') no-repeat center center;
            background-size: contain; /* Ensure the entire image is visible */
            background-color: black; /* Add a background color to fill empty space */
            padding: 0; /* Remove padding to make the image full-page */
            color: white;
            text-shadow: 1px 1px 2px black;
        }
        .page.turn {
            transform: rotateY(-180deg);
        }
        .page.unturn {
            transform: rotateY(0deg);
        }
        .button-container {
            margin-top: 20px;
        }
        .button {
            padding: 10px 20px;
            background-color: #ff4081;
            border: none;
            color: white;
            font-size: 16px;
            cursor: pointer;
            border-radius: 8px;
            margin-right: 10px;
        }
        textarea {
            width: 100%;
            height: 120px;
            font-size: 16px;
            padding: 10px;
            border: 1px solid #ccc;
            resize: none;
        }
    </style>
</head>
<body>
    <div class="book">
        <div id="page1" class="page front">
            <h2>Hello!! cutie NIKKU!</h2>
            <p>This is a special little book for you. With love, Swarup</p>
            <div class="button-container">
                <button class="button" onclick="turnpage()">Next</button>
            </div>
        </div>
        <div id="page2" class="page back">
            <p><strong>How do you feel about me?</strong></p>
            <textarea placeholder="Write your opinion here..."></textarea>
            <div class="button-container">
                <button class="button" onclick="unturnpage()">Previous</button>
            </div>
        </div>
    </div>
    <script>
        function turnpage() {
            document.getElementById("page1").style.transform = "rotateY(-180deg)";
            document.getElementById("page2").style.transform = "rotateY(0deg)";
        }
        function unturnpage() {
            document.getElementById("page1").style.transform = "rotateY(0deg)";
            document.getElementById("page2").style.transform = "rotateY(-180deg)";
        }
    </script>
</body>
</html>
"""

components.html(book_html, height=550)