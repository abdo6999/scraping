import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string

chrome_options = Options()

# Add the extension
extension_path = r'./extension_4_1_55_0.crx'  # Replace with the actual path
chrome_options.add_extension(extension_path)

# Create a directory to store the JSON files
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Generate the list of English letters excluding 'a'
english_letters = list(string.ascii_lowercase)
english_letters.remove('a')
english_letters.remove('b')
english_letters.remove('c')
english_letters.remove('d')


# Set up the web driver with the custom options
driver = webdriver.Chrome(options=chrome_options)
for english_letter in english_letters:
    # Create the directory for the letter
    letter_dir = os.path.join(output_dir, english_letter.upper())
    os.makedirs(letter_dir, exist_ok=True)

    # Navigate to the form URL
    driver.get(f"https://babysignlanguage.com/dictionary-letter/?letter={english_letter}")

    # Find all the .single-letter-card elements
    parent_elements = driver.find_elements("css selector", ".single-letter-card")

    # Retrieve the word titles from each parent element
    word_titles = [parent_element.text for parent_element in parent_elements]

    # Loop through each parent element
    for i, parent_element in enumerate(word_titles):
        word_title = word_titles[i]

        parent_elements = driver.find_elements("css selector", ".single-letter-card")
        
        parent_element = parent_elements[i]
        # Find the <a> element within the parent element
        link_element = parent_element.find_element("css selector", "a")
        # Click on the <a> element
        link_element.click()

        # Wait for the page to finish loading
        wait = WebDriverWait(driver, 10)
        description_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".hero-content")))
        description_text = description_element.text

        # Create a dictionary for the word and description
        data = {"word": word_title, "description": description_text}

        # Generate the filename based on the word title
        filename = f"{i+1}_{word_title}.json"

        filepath = os.path.join(letter_dir, filename)
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)

        # Use JavaScript to navigate back in the browser's history
        driver.back()
        # Wait for the page to finish loading
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".single-letter-card")))

# Close the browser
driver.quit()
