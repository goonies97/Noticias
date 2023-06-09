# Import the required modules
import os
import openai
import feedparser
import asyncio

# Set the OpenAI API key as an environment variable
openai.api_key = "API" # Replace with your actual API key

# Define the RSS feed URL that you want to use
rss_url = "https://noticiasaguascalientes.com/category/prueba/feed/" # Replace with your actual RSS feed URL

# Define the path where you want to save the rewritten titles
path = "C:/Users/Raúl Angel Cobos/OneDrive/Documentos/GPT" # Replace with your desired path

# Define a coroutine function that fetches the RSS feed, rewrites the titles, and saves them to new txt files
async def rewrite_titles():
  # Fetch the RSS feed using feedparser
  feed = feedparser.parse(rss_url)
  # Loop through the entries of the feed
  for index, entry in enumerate(feed.entries):
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
    # Create a file name for each rewritten title using the path and index
    file_name = os.path.join(path, "rewritten_title_" + str(index) + ".txt")
    # Create and write to a new txt file for each rewritten title
    with open(file_name, "w") as f:
      f.write(rewritten_title)

# Define another coroutine function that runs the rewrite_titles function every certain interval of time (for example, every 10 seconds)
async def main():
  while True:
    # Run the rewrite_titles function
    await rewrite_titles()
    # Wait for 10 seconds before running it again
    await asyncio.sleep(10)

# Run the main function using asyncio
asyncio.run(main())
