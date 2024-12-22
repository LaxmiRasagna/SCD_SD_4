import requests
from bs4 import BeautifulSoup
import csv

# URL of the e-commerce website
url = "(link unavailable)"

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to retrieve the webpage")
    exit(1)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all product elements on the webpage
products = soup.find_all('div', class_='product')

# Create a CSV file and write the header
with open('products.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Price', 'Rating']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Iterate over each product and extract the information
    for product in products:
        name = product.find('h2', class_='product-name').text.strip()
        price = product.find('span', class_='price').text.strip()
        rating = product.find('span', class_='rating').text.strip()

        # Write the product information to the CSV file
        writer.writerow({'Name': name, 'Price': price, 'Rating': rating})

print("Product information extracted and saved to products.csv")

