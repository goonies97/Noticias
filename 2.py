# Import the required modules
import os
import openai
import feedparser
import asyncio

# Set the OpenAI API key as an environment variable
openai.api_key = "API"
#openai.api_key = os.getenv("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") # Replace with your actual API key

# Define the RSS feed URL that you want to use
rss_url = "https://rss.app/feeds/Co8Y81kx7ysKRKYO.xml" # Replace with your actual RSS feed URL

# Define the file name and path where you want to save the rewritten titles
file_name = "rewritten_titles.txt" # Replace with your desired file name and path

# Define a coroutine function that fetches the RSS feed, rewrites the titles, and saves them to a file
async def rewrite_titles():
  # Fetch the RSS feed using feedparser
  feed = feedparser.parse(rss_url)
  # Open the file in write mode
  file = open(file_name, "w")
  # Loop through the entries of the feed
  for entry in feed.entries:
    # Get the title of each entry
    title = entry.title
    # Use ChatGPT to rewrite the title using the Completion API
    response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=title,
  max_tokens=200,
  temperature=0.7,
  frequency_penalty=0.5,
  stop="."
)
    # Get the rewritten title from the text attribute of the first choice
    rewritten_title = response.choices[0].text
    # Write the rewritten title to the file on a new line
    file.write(rewritten_title + "\n")
  # Close the file when done
  file.close()

# Define another coroutine function that runs the rewrite_titles function every certain interval of time (for example, every 10 seconds)
async def main():
  while True:
    # Run the rewrite_titles function
    await rewrite_titles()
    # Wait for 10 seconds before running it again
    await asyncio.sleep(10)

# Run the main function using asyncio
asyncio.run(main())
