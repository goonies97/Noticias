# Import the required modules
import os
import openai
import feedparser
import asyncio
import datetime
import pywhatkit

print("Cobot 0.4.3")
print("Desarrollado por Raul Angel Cobos Fuantos")
# Set the OpenAI API key as an environment variable
openai.api_key = "API" 


# Define the RSS feed URL that you want to use
rss_url = "https://noticiasaguascalientes.com/category/prueba/feed" 

# Define the path where you want to save the rewritten titles
path = "C:/Users/Raúl Angel Cobos/OneDrive/Documentos/GPT/Titles" 

# Define a global variable to store the previous number of entries in the feed
prev_num_entries = 0

# Define a coroutine function that fetches the RSS feed, rewrites the titles, and saves them to new txt files
async def rewrite_titles():
  # Declare the global variable
  global prev_num_entries
  # Fetch the RSS feed using feedparser
  feed = feedparser.parse(rss_url)
  # Get the current number of entries in the feed
  curr_num_entries = len(feed.entries)
  # Check if the current number of entries is greater than the previous one
  if curr_num_entries > prev_num_entries:
    # Sort the entries by date using the sorted function and a lambda function
    sorted_entries = sorted(feed.entries, key=lambda e: e.published_parsed)
    # Loop through the new entries of the feed (from prev_num_entries to curr_num_entries)
    for index in range(prev_num_entries, curr_num_entries):
      # Get the title of each entry from the sorted list
      title = sorted_entries[index].title
      # Use ChatGPT to rewrite the title using the Completion API
      response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=title,
        max_tokens=200,
        temperature=0.1,
        frequency_penalty=1.0,
        stop="."
      )
      # Get the rewritten title from the text attribute of the first choice
      rewritten_title = response.choices[0].text
      # Create a file name for each rewritten title using the path and index
      file_name = os.path.join(path, "rewritten_title_" + str(index) + ".txt")
      # Create and write to a new txt file for each rewritten title
      with open(file_name, "w") as f:
        f.write(rewritten_title)
      # Print the rewritten title, along with the date and time, in the command prompt
      print(f"Rewritten title: {rewritten_title}")
      print(f"Date and time: {datetime.datetime.now()}")
      print()
    # Update the previous number of entries with the current one
    prev_num_entries = curr_num_entries

    # Change the default browser to Firefox
    pywhatkit.change_browser(True)
    pywhatkit.change_browser("firefox")

    # Grupo de WhatsApp
    group_link = "https://chat.whatsapp.com/DxNsQSERT7r9BZH8mqjVMC"

    # Loop through the rewritten titles and send them to the group
    for rewritten_title in rewritten_titles:
    # Use the sendwhatmsg function to send a message to the group
    pywhatkit.sendwhatmsg(group_link, rewritten_title, 12, 30)
    # Wait for some time before sending the next message
    time.sleep(10)

# Define another coroutine function that runs the rewrite_titles function every certain interval of time (for example, every 10 seconds)
async def main():
  while True:
    # Run the rewrite_titles function
    await rewrite_titles()
    # Wait for 10 seconds before running it again
    await asyncio.sleep(10)

# Run the main function using asyncio
asyncio.run(main())
