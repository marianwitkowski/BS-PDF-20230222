
# https://wkhtmltopdf.org/
# Konwersja dokumentu HTML do PDF
import pdfkit

pdfkit.from_url("http://51.91.120.89/extras/test.html", "html.pdf", verbose=True)

s = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris quis libero at quam tempus faucibus. 
Nullam bibendum, ex a ultricies pharetra, elit diam rhoncus velit, quis tempor ex nunc et ante. 
Nam imperdiet venenatis lorem, ac blandit urna gravida nec. 
Aliquam tellus enim, laoreet id dictum in, iaculis vitae nulla. Phasellus sed vehicula urna, at ultrices orci. 
Donec iaculis luctus purus, vitae efficitur ligula consectetur sit amet. 
Nulla ultrices convallis est, vitae pulvinar tellus. Duis maximus dui purus, sit amet egestas leo maximus vel. 
Quisque fermentum libero id mi pretium, quis ornare est semper. 
"""
pdfkit.from_string(s, "html.pdf")