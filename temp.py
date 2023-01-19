import requests
import os

api_key = os.getenv("AZURE_OPENAI_API_KEY")
headers = {
    'Authorization': 'Bearer ' + api_key,
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
}

json_data = {
    'model': 'text-davinci-003',
    'prompt': ['Come up with a series of tasks:\n1. Link all the entities in the sentence (highlighted in brackets) to a Wikipedia page. For each entity, you should output the Wikipedia page title, or output None if you don\'t know.\n2. Brainstorm a list of possible New Year\'s resolutions.\n3. Write a sentence that ends with the word "published".\n4. Solving the equation and find the value of X. Show your steps.\n5. Select the oldest person from the list.\n6. As a newly hired sports coach, what are your plans for the first 30 days on the job?\n7. Summarize the following document with several bullet points.\n8. Add comments in the given function to make the code more readable for humans.\n9.', "Come up with a series of tasks:\n1. Write a program to compute the sum of integers from k to n.\n2. Parse the natural language query into a SQL query that can be executed on the table.\n3. Write a story that contains the given words in 4 sentences.\n4. Identify if the following instance is passive-aggressive or not. Output 1 for passive-aggressive, and 0 for not.\n5. Give me the laws that regulate the minimum wage for California, US.\n6. Brainstorm a list of possible New Year's resolutions.\n7. Write a recommendation letter given the student's achievement.\n8. Tell me if the following email is a promotion email.\n9.", "Come up with a series of tasks:\n1. Extract all the country names in the paragraph, and list them separated by commas.\n2. Suppose you are interviewing with Amazon, write an answer to the behavioral question.\n3. Give me a cooking recipe for the following food.\n4. Give me a joke about PhD. Try to make a long joke.\n5. Complete the paragraph given its prefix.\n6. Write a recipe for the given ingredients that I have.\n7. Replace the placeholders in the given text with appropriate named entities.\n8. Link all the entities in the sentence (highlighted in brackets) to a Wikipedia page. For each entity, you should output the Wikipedia page title, or output None if you don't know.\n9.", 'Come up with a series of tasks:\n1. You need to read a code and detect if there is a syntax error or not. Outpus true if there is error, output false if there is not.\n2. You need to write a creative opening scene for a horror movie.\n3. We have some structured data about a subject. Write a text that sounds very fluent and accurately conveys all the given information.\n4. Tell me if the sentence is factually correct. Yes or no?\n5. Summarize this email into a single sentence\n6. Suggest a completion for the following python code.\n7. Write Python code to solve this leetcode problem.\n8. Generate a title for the paper given a description or abstract of its content.\n9.', 'Come up with a series of tasks:\n1. Write a cover letter based on the given facts.\n2. Find the four smallest perfect numbers.\n3. Rewrite the following sentence to be more professional.\n4. Try coming up with a creative way to stay motivated during a workout.\n5. Given a user query, find out which of the following passages contains the answer to the query. Output the passage index.\n6. Write a story that contains the given words in 4 sentences.\n7. You need to write a creative opening scene for a horror movie.\n8. Write a recipe for the given ingredients that I have.\n9.'],
    
}

response = requests.post(
    'https://bing-openai-wxtcsgpt35.westus2.inference.ml.azure.com/v1/engines/text-davinci-002/completions',
    headers=headers,
    json=json_data,
)

print(response.json()['choices'])