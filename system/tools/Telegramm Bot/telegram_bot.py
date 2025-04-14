import os
import telebot
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from fuzzywuzzy import fuzz
import markdown
from github import Github
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')  # e.g., 'username/repo'
THESAURUS_PATH = 'Тезаурус'

# Initialize bot with state storage
bot = telebot.TeleBot(TELEGRAM_TOKEN, state_storage=StateMemoryStorage())

# Initialize GitHub client
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

class ThesaurusStates(StatesGroup):
    SEARCHING = State()

def clean_text(text):
    """Clean markdown text for display."""
    # Remove markdown syntax
    text = re.sub(r'[#*_\[\]]', '', text)
    return text.strip()

def get_thesaurus_files():
    """Retrieve all markdown files from Thesaurus directory."""
    try:
        contents = repo.get_contents(THESAURUS_PATH)
        files = []
        for content_file in contents:
            if content_file.type == 'file' and content_file.name.endswith('.md'):
                files.append({
                    'name': content_file.name.replace('.md', ''),
                    'path': content_file.path,
                    'content': content_file.decoded_content.decode('utf-8')
                })
        return files
    except Exception as e:
        print(f"Error accessing GitHub: {e}")
        return []

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот тезауруса. Напиши слово или фразу, и я найду определение из нашей базы знаний.")
    bot.set_state(message.from_user.id, ThesaurusStates.SEARCHING, message.chat.id)

@bot.message_handler(state=ThesaurusStates.SEARCHING)
def search_thesaurus(message):
    query = message.text.strip()
    if not query:
        bot.reply_to(message, "Пожалуйста, введите слово или фразу для поиска.")
        return

    files = get_thesaurus_files()
    if not files:
        bot.reply_to(message, "Не удалось загрузить данные тезауруса. Попробуйте позже.")
        return

    # Exact match search
    for file in files:
        if file['name'].lower() == query.lower():
            content = clean_text(file['content'])
            bot.reply_to(message, f"**{file['name']}**\n\n{content}")
            return

    # Fuzzy search with scoring
    results = []
    for file in files:
        # Score by filename
        name_score = fuzz.ratio(query.lower(), file['name'].lower())
        # Score by content
        content_score = fuzz.partial_ratio(query.lower(), file['content'].lower())
        # Combined score (weighted)
        total_score = max(name_score, content_score * 0.8)
        
        if total_score > 50:  # Threshold for relevance
            results.append({
                'name': file['name'],
                'content': file['content'],
                'score': total_score
            })

    # Sort by score
    results.sort(key=lambda x: x['score'], reverse=True)

    if not results:
        bot.reply_to(message, "Ничего не найдено. Попробуйте переформулировать запрос.")
        return

    # Format response
    response = "Возможные совпадения:\n\n"
    for result in results[:5]:  # Limit to 5 results
        content_preview = clean_text(result['content'])[:200] + '...' if len(result['content']) > 200 else clean_text(result['content'])
        response += f"**{result['name']}** (совпадение: {int(result['score'])}%)\n{content_preview}\n\n"
    
    bot.reply_to(message, response)

# Error handler
@bot.message_handler(content_types=['text'])
def handle_errors(message):
    bot.reply_to(message, "Пожалуйста, используйте текстовые запросы в теме Тезаурус.")

# Polling
if __name__ == '__main__':
    bot.infinity_polling()