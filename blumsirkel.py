import requests
import json
from colorama import init, Fore, Style
import time
import datetime
import random
init(autoreset=True)

# Define color variables
RED = Fore.RED + Style.BRIGHT
GREEN = Fore.GREEN + Style.BRIGHT
YELLOW = Fore.YELLOW + Style.BRIGHT
BLUE = Fore.BLUE + Style.BRIGHT
MAGENTA = Fore.MAGENTA + Style.BRIGHT
CYAN = Fore.CYAN + Style.BRIGHT
WHITE = Fore.WHITE + Style.BRIGHT
 
 

bot_token = "MEMEK_TOKEN"
chat_id = "ID_MEMEK"
def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"{GREEN}Notification sent successfully.")
        else:
            print(f"{RED}Failed to send notification. Status code: {response.status_code}")
    except Exception as e:
        print(f"{RED}Error sending notification: {str(e)}")

def get_headers(access_token=None):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://telegram.blum.codes",
        "priority": "u=1, i",
        "referer": "https://telegram.blum.codes/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Pragma": "no-cache",
        "Expires": "0"
    }

    if access_token:
        headers["authorization"] = f"Bearer {access_token}"
    return headers

def auth(init_data, retries=3, delay=2):
    url = "https://user-domain.blum.codes/api/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"
    headers = get_headers()
    body = {
        "query": init_data
    }
    
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers, data=json.dumps(body))
            response.raise_for_status()
            response_json = response.json()
            if response.status_code == 200:
                return response_json
            else:
                print(f"{RED}Error: QUERY INVALID / MATI", flush=True)
                return None
        except (requests.RequestException, ValueError) as e:
            print(f"{RED}Error getting token: {e}", flush=True)
            if attempt < retries - 1:
                print(f"{YELLOW}Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None

def get_user_info(access_token,retries=3,delay=2):
    url = f"https://user-domain.blum.codes/api/v1/user/me"
    headers = get_headers(access_token)
    
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response_json = response.json()
            if response.status_code == 200:
                return response_json
            else:
                print(f"{RED}[ Balance ] : Error: Gagal mendapatkan balance", flush=True)
                return None
        except (requests.RequestException, ValueError) as e:
            if attempt < retries - 1:
                print(f"{YELLOW}[ Balance ] : Error Retrying {e} ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None
def get_balance(access_token,retries=3,delay=2):
    url = f"https://game-domain.blum.codes/api/v1/user/balance"
    headers = get_headers(access_token)
    
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response_json = response.json()
            if response.status_code == 200:
                return response_json
            else:
                print(f"{RED}[ Balance ] : Error: Gagal mendapatkan balance", flush=True)
                return None
        except (requests.RequestException, ValueError) as e:
            if attempt < retries - 1:
                print(f"{YELLOW}[ Balance ] : Error Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None

def check_tribe(access_token, retries=3, delay=2):
    url = f"https://tribe-domain.blum.codes/api/v1/tribe/my"
    headers = get_headers(access_token)
    
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response_json = response.json()
            if response.status_code == 200:
                return response_json
            elif response.status_code == 404:
                # print(f"{RED}[ Tribe ] : Error: Not Found (404) - {response.text}", flush=True)
                return response_json
            else:
                print(f"{RED}[ Tribe ] : Error: Gagal mendapatkan tribe - {response.text}", flush=True)
                return None
        except (requests.RequestException, ValueError) as e:
            if response.status_code == 404:
                return response.json()
      
            if attempt < retries - 1:
                print(f"{YELLOW}[ Tribe ] : Error Retrying... {e} ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                print(f"{RED}[ Tribe ] : Failed after {retries} attempts - {e}", flush=True)
                return None  
 
def join_tribe(access_token, tribe_id, retries=3, delay=2):
    url = f"https://tribe-domain.blum.codes/api/v1/tribe/{tribe_id}/join"
    headers = get_headers(access_token)
    
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers)
            # response_json = response.json()  # Parse JSON response before raising for status
      
            if response.status_code == 200:
                print(f"{GREEN}[ Tribe ] Joined Tribe             ", flush=True)
                return True
            else:
                print(f"{RED}[ Tribe ] : Failed to Join Tribe", flush=True)
        except (requests.RequestException, ValueError) as e:
            # print(f"{RED}Error spin: {e}", flush=True)
            if attempt < retries - 1:
                print(f"{RED}[ Tribe ] : Error Retrying...{e} ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                print(f"{RED}[ Tribe ] : Failed to Join Tribe", flush=True)

def claim_balance(access_token, retries=3, delay=2):
    url = f"https://game-domain.blum.codes/api/v1/farming/claim"
    headers = get_headers(access_token)
    
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers)
            response_json = response.json()  # Parse JSON response before raising for status
            return response_json
        except (requests.RequestException, ValueError) as e:
            if attempt < retries - 1:
                print(f"{RED}[ Farming ] : Error Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                print(f"{RED}[ Farming ] : Failed to claim", flush=True)
                return None
 

def start_farming(access_token, retries=3, delay=2):
    url = f"https://game-domain.blum.codes/api/v1/farming/start"
    headers = get_headers(access_token)
    
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers)
            response_json = response.json()  # Parse JSON response before raising for status
            return response_json
        except (requests.RequestException, ValueError) as e:
            if attempt < retries - 1:
                print(f"{RED}[ Farming ] : Error Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                print(f"{RED}[ Farming ] : Failed to start", flush=True)
                return None


def check_daily_reward(access_token, retries=3, delay=2):
    url = f"https://game-domain.blum.codes/api/v1/daily-reward?offset=-420"
    headers = get_headers(access_token)
    
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers)
            if response.status_code == 400:
                try:
                    return response.json()
                except json.JSONDecodeError:
                    if response.text == "OK":
                        return response.text
                    # print(f"{RED}Json Error: {response.text}")
                    return None
            else:
                try:
                    return response.json()
                except json.JSONDecodeError:
                    print(f"{RED}[ Daily Reward ]:  {response.text}")
                    return None
        except (requests.RequestException, ValueError) as e:
            if attempt < retries - 1:
                print(f"{RED}[ Daily Reward  ] : Error Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                print(f"{RED}[ Daily Reward ] : Failed to check", flush=True)
                return None

def check_task(access_token,retries=3,delay=2):
    url = f"https://earn-domain.blum.codes/api/v1/tasks"
    headers = get_headers(access_token)
    
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response_json = response.json()
            if response.status_code == 200:
                return response_json
            else:
                print(f"{RED}[ Task ] : Error: Gagal mendapatkan Task", flush=True)
                return None
        except (requests.RequestException, ValueError) as e:
            if attempt < retries - 1:
                print(f"{YELLOW}[ Task ] : Error Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None   

def check_balance_friend(access_token,retries=3,delay=2):
    url = f"https://user-domain.blum.codes/api/v1/friends/balance"
    headers = get_headers(access_token)
    
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response_json = response.json()
            if response.status_code == 200:
                return response_json
            else:
                
                return None
        except (requests.RequestException, ValueError) as e:
            if attempt < retries - 1:
                print(f"{YELLOW}[ Refferal ] : Error Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None   

def play_game(access_token,retries=3,delay=2):
    url = f"https://game-domain.blum.codes/api/v1/game/play"
    headers = get_headers(access_token)
    
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers)
            # print(response.json())
            response.raise_for_status()
            response_json = response.json()
            if response.status_code == 200:
                return response_json
            else:
          
                return None
        except (requests.RequestException, ValueError) as e:
            if attempt < retries - 1:
                print(f"{YELLOW}[ Play Game ] : Error Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None            


def claim_game(access_token, game_id, points, retries=3, delay=2):
    url = f"https://game-domain.blum.codes/api/v1/game/claim"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {access_token}",
        "content-type": "application/json",
        "origin": "https://telegram.blum.codes",
        "priority": "u=1, i",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
    }
    body = {
        "gameId": game_id,
        "points": points
    }
    
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers, data=json.dumps(body))
            return response
        except (requests.RequestException, ValueError) as e:
            if attempt < retries - 1:
                print(f"{YELLOW}[ Play Game ] : Error Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None

def claim_balance_friend(access_token,retries=3,delay=2):
    url = f"https://user-domain.blum.codes/api/v1/friends/claim"
    headers = get_headers(access_token)
    
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers)
            response.raise_for_status()
            response_json = response.json()
            if response.status_code == 200:
                return response_json
            else:
                print(f"{RED}[ Refferal ] : Error: Gagal mendapatkan Task", flush=True)
                return None
        except (requests.RequestException, ValueError) as e:
            if attempt < retries - 1:
                print(f"{YELLOW}[ Refferal ] : Error Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None   
            

def validate(access_token, task_id, retries=3, delay=2):
    url = f"https://earn-domain.blum.codes/api/v1/tasks/{task_id}/validate"
    headers = get_headers(access_token)
 
    for attempt in range(3):
        try:
            response = requests.get("https://raw.githubusercontent.com/adearmanwijaya/blum_combo/main/jawaban").text
            answers = dict(line.split(':') for line in response.splitlines())
          
            jawaban = answers.get(task_id, 'DEFAULT_VALUE')  # Use 'DEFAULT_VALUE' if task_id not found
            body = {
                "keyword": jawaban.strip()  # Ensure no extra whitespace
            }
            break  # Exit the loop if successful
        except requests.exceptions.RequestException as e:
            if attempt < 2:  # Retry if not the last attempt
                print(f"Failed to fetch answer. Retrying... ({attempt + 1}/3)", end="\r", flush=True)
                time.sleep(1)  # Wait a bit before retrying
            else:
                print(f"Failed to fetch answer after {attempt + 1} attempts.", flush=True)
                return None  # Exit the function if all retries fail
        
    for attempt in range(retries):
        try:
            # print(body)
            response = requests.post(url, headers=headers, data=json.dumps(body))
            response.raise_for_status()
            response_json = response.json()
            
            if response.status_code == 200:
                return response_json 
            elif response.status_code == 412:
                return response_json 
            else:
                status = response_json.get('message')
                if status == 'Task is not validating':
                    return response_json
                if status == 'Task is already claimed':
                    return response_json
                else:
                    print(f"{RED}    ->  : Error: Gagal mendapatkan data  {response_json}              ", flush=True)
                    return None
        except (requests.RequestException, ValueError) as e:
            # print(e)
            if attempt < retries - 1:
                print(f"{YELLOW}    ->  : Error Retrying... ({attempt + 1}/{retries})", end="\r", flush=True)
                time.sleep(delay)
            else:
                return None
            
def claim_task(access_token, task_id,retries=3,delay=2):
    url = f"https://earn-domain.blum.codes/api/v1/tasks/{task_id}/claim"
    headers = get_headers(access_token)
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers)
            response_json = response.json()  # Parse JSON response before raising for status
            if response.status_code == 200:
                return response_json 
            elif response.status_code == 412:
                return response_json 
            else:
                status = response_json.get('message')
                if status == 'Task is not done':
                    return response_json
                else:
                    print(f"{RED}    ->  : Error: Gagal mendapatkan data  {response_json}              ", flush=True)
                    return None
        except (requests.RequestException, ValueError) as e:
            print(f"{RED}    ->  Error : {e}", flush=True)
            if attempt < retries - 1:
                print(f"{RED}    ->  : Retrying... ({attempt + 1}/{retries})        ",end="\r",  flush=True)
                time.sleep(delay)
            else:
                return None
def start_task(access_token, task_id,retries=3,delay=2):
    url = f"https://earn-domain.blum.codes/api/v1/tasks/{task_id}/start"
    headers = get_headers(access_token)
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers)
            response_json = response.json()  # Parse JSON response before raising for status
            if response.status_code == 200:
                return response_json 
            elif response.status_code == 400:
                return response_json 
            else:
                print(f"{RED}    -> Gagal mendapatkan data", flush=True)
                return None
        except (requests.RequestException, ValueError) as e:
            print(f"{RED}    ->  Error : {e}", flush=True)
            if attempt < retries - 1:
                print(f"{RED}    ->  Retrying... ({attempt + 1}/{retries})",end="\r",  flush=True)
                time.sleep(delay)
            else:
                return None                 
def print_welcome_message():
    print(Fore.WHITE + r"""
          
🆂🅸🆁🅺🅴🅻
          
█▀▀ █▀▀ █▄░█ █▀▀ █▀█ █▀█ █░█ █▀
█▄█ ██▄ █░▀█ ██▄ █▀▄ █▄█ █▄█ ▄█
          """)
    print(Fore.GREEN + Style.BRIGHT + "BlumCrypto BOT")
    print(Fore.BLUE + Style.BRIGHT + "Buy me a coffee :) 0823 2367 3487 GOPAY / DANA\n\n")
  

def main():
    while True:
        try:
            print_welcome_message()
            mode = input(Fore.YELLOW + f"Only Check Balance? (y/n): ").strip().upper()
            notif_tele_enable = input(Fore.YELLOW + f"Sent notification to Telegram? (y/n): ").strip().upper()
            cek_task_enable = input(Fore.YELLOW + f"Check Task? (y/n): ").strip().upper()
            while True:                
                total_balance = 0 
                total_connect = 0
                # Read data from query.txt and perform authentication for each line
                with open('query.txt', 'r') as file:
                    init_data_lines = file.readlines()
                    total_accounts = len(init_data_lines) 
                
                for index, init_data in enumerate(init_data_lines, start=1):
                    init_data = init_data.strip()  # Remove any extra whitespace
                    if not init_data:
                        continue
                    print(f"{YELLOW}Getting access token...", end="\r", flush=True)
                    ghalibie = auth(init_data)
                    time.sleep(1)
                    if ghalibie is None:
                        continue
                    token = ghalibie['token']['refresh']
                    print(f"{YELLOW}Getting user info...", end="\r", flush=True)
                    user_info = get_user_info(token)
                    if user_info is None:
                        continue
                    print(f"{Fore.BLUE+Style.BRIGHT}====[{Fore.WHITE+Style.BRIGHT} Account {index} - {total_accounts} | {user_info['username']}{Fore.BLUE+Style.BRIGHT} ]====",flush=True) 
                    balance_info = get_balance(token) 
                    print(f"{YELLOW}Getting Balance..", end="\r", flush=True)
                    if balance_info is not None:
                        available_balance_before = balance_info.get('availableBalance', 0)
                        balance_before = f"{float(available_balance_before):,.0f}".replace(",", ".")
                        total_balance += float(available_balance_before) 
                        print(f"{YELLOW}[ Balance ]: {balance_before}             ", flush=True)
                        print(f"{YELLOW}[ Tribe ]: Checking Tribe..", end="\r", flush=True)
                        if mode == 'Y':
                            continue
                        tribe_info = check_tribe(token)
                        # print(tribe_info)
                        if tribe_info and tribe_info.get("message") == "NOT_FOUND":
                            print(f"{YELLOW}[ Tribe ]: Joining tribe...", end="\r", flush=True)
                            join_tribe(token, "4cc96181-1cd3-4494-ae49-7b7cb0e81eff")
                            print(f"{YELLOW}[ Tribe ]: Checking Tribe...", end="\r", flush=True)
                            tribe_info = check_tribe(token)
                            if tribe_info and tribe_info.get("id"):
                                print(f"{YELLOW}[ Tribe ]: {tribe_info['title']}                ", flush=True)
                            else:
                                print(f"{RED}[ Tribe ]: Gagal mendapatkan informasi tribe", flush=True)
                        elif tribe_info and tribe_info.get("id"):
                            print(f"{YELLOW}[ Tribe ]: {tribe_info['title']}        ", flush=True)
                        else:
                            print(f"{RED}[ Tribe ]: Gagal mendapatkan informasi tribe", flush=True)
                        
                        print(f"{Fore.MAGENTA+Style.BRIGHT}[ Tiket Game ]: {balance_info['playPasses']}")
                        print(f"{YELLOW}[ Farming ]: Getting Farming..", end="\r", flush=True)
                        farming_info = balance_info.get('farming')
                        if farming_info:
                            end_time_ms = farming_info['endTime']
                            end_time_s = end_time_ms / 1000.0
                            end_utc_date_time = datetime.datetime.fromtimestamp(end_time_s, datetime.timezone.utc)
                            current_utc_time = datetime.datetime.now(datetime.timezone.utc)
                            time_difference = end_utc_date_time - current_utc_time
                            hours_remaining = int(time_difference.total_seconds() // 3600)
                            minutes_remaining = int((time_difference.total_seconds() % 3600) // 60)
                            farming_balance = farming_info['balance']
                            farming_balance_formated = f"{float(farming_balance):,.0f}".replace(",", ".")
                            print(f"{RED}[ Farming ] : {hours_remaining} Hours {minutes_remaining} Minutes | Balance: {farming_balance_formated}", flush=True)
                            if hours_remaining < 0:
                                print(f"{GREEN}[ Farming ] : Claiming balance...", end="\r", flush=True)
                                claim_response = claim_balance(token)
                                if claim_response:
                                    print(f"{GREEN}[ Farming ] : Claimed: {claim_response.get('availableBalance')}                ", flush=True)
                                    print(f"{GREEN}[ Farming ] : Starting farming...", end="\r", flush=True)
                                    start_response = start_farming(token)
                                    if start_response:
                                        print(f"{GREEN}[ Farming ] : Farming started.     ", flush=True)
                                    else:
                                        print(f"{RED}[ Farming ] : Gagal start farming", flush=True)
                                else:
                                    print(f"{RED}[ Farming ] : Gagal claim                ",   flush=True)
                        else:
                            # print(f"{RED}[ Farming ] : Gagal mendapatkan informasi farming", flush=True)
                            print(f"{GREEN}[ Farming ] : Claiming balance...", end="\r", flush=True)
                            claim_response = claim_balance(token)
                            if claim_response:
                                print(f"{GREEN}[ Farming ] : Claimed               ", flush=True)
                                print(f"{GREEN}[ Farming ] : Starting farming...", end="", flush=True)
                                start_response = start_farming(token)
                                if start_response:
                                    print(f"{GREEN}[ Farming ] : Farming started.     ", flush=True)
                                else:
                                    print(f"{RED}[ Farming ] : Gagal start farming", flush=True)
                            else:
                                print(f"{RED}[ Farming ] : Gagal claim                ",   flush=True)
                        
                        print(f"{CYAN}[ Daily Reward ] : Checking daily reward...", end="\r", flush=True)
                        daily_reward_response = check_daily_reward(token)
                    
                        if daily_reward_response is None:
                            print(f"{RED}[ Daily Reward ] : Gagal cek hadiah harian", flush=True)
                        else:
                            if daily_reward_response.get('message') == 'same day':
                                print(f"{CYAN}[ Daily Reward ] : Already Claimed Today          ", flush=True)
                            elif daily_reward_response.get('message') == 'OK':
                                print(f"{CYAN}[ Daily Reward ] : Claimed!          ", flush=True)
                            else:
                                print(f"{RED}[ Daily Reward ] : {daily_reward_response}                                    ", flush=True)
                        available_colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
                        tiket = balance_info.get('playPasses',0)
                        while tiket > 0:
                            print(f"{Fore.CYAN+Style.BRIGHT}[ Play Game ] : Playing game..." ,end ="\r", flush=True)
                            for attempt in range(5):
                                print(f"{Fore.CYAN+Style.BRIGHT}[ Play Game ] : Checking game...", end="\r", flush=True)
                                game_response = play_game(token)
                                if game_response and 'gameId' in game_response:
                                    break
                                else:
                                    print(f"{Fore.RED+Style.BRIGHT}[ Play Game ] : Gagal memainkan game, mencoba lagi...", end="\r",flush=True)
                                    time.sleep(5)
                            if game_response is None or 'gameId' not in game_response:
                                print(f"\r{Fore.RED+Style.BRIGHT}[ Play Game ] : Gagal memainkan game setelah 5 percobaan", flush=True)
                                break

                            time.sleep(10)
                            claim_response = claim_game(token, game_response.get('gameId'), random.randint(1000, 2000))
                            while True:
                                if claim_response is None:
                                    print(f"{Fore.RED+Style.BRIGHT}[ Play Game ] : Gagal mengklaim game, mencoba lagi...", flush=True)
                                    claim_response = claim_game(token, game_response.get('gameId'), random.randint(1000, 2000))
                                    time.sleep(5)
                                elif claim_response.text == '{"message":"game session not finished"}':
                                    time.sleep(5)  # Tunggu sebentar sebelum mencoba lagi
                                    random_color = random.choice(available_colors)
                                    print(f"{random_color+Style.BRIGHT}[ Play Game ] : Game belum selesai.. mencoba lagi                ", end="\r", flush=True)
                                    claim_response = claim_game(token, game_response.get('gameId'), random.randint(1000, 2000))
                                    if claim_response is None:
                                        print(f"{Fore.RED+Style.BRIGHT}[ Play Game ] : Gagal mengklaim game, mencoba lagi...", end="\r", flush=True)
                                elif claim_response.text == '{"message":"game session not found"}':
                                    print(f"{Fore.RED+Style.BRIGHT}[ Play Game ] : Game sudah berakhir", flush=True)
                                    break
                                else:
                                    print(f"{Fore.YELLOW+Style.BRIGHT}[ Play Game ] : Game selesai: {claim_response.text}", flush=True)
                                    break
                            
                            balance_info = get_balance(token) 
                            if balance_info is None: # Refresh informasi saldo untuk mendapatkan tiket terbaru
                                    print(f"{Fore.RED+Style.BRIGHT}[ Play Game ] : Gagal mendapatkan informasi tiket", flush=True)
                            else:
                                available_balance_after = balance_info['availableBalance']  # asumsikan ini mengambil nilai dari JSON
                                before = float(available_balance_before) 
                                after =  float(available_balance_after)
                                total_game = after - before
                            
                                print(f"{Fore.YELLOW+Style.BRIGHT}[ Play Game ]: You Got {total_game} From Playing Game", flush=True)
                                if balance_info['playPasses'] > 0:
                                    print(f"{Fore.GREEN+Style.BRIGHT}[ Play Game ] : Tiket masih tersedia, memainkan game lagi...", flush=True)
                                    continue  # Lanjutkan loop untuk memainkan game lagi
                                else:
                                    print(f"{Fore.RED+Style.BRIGHT}[ Play Game ] : Tidak ada tiket tersisa.", flush=True)
                                    break
                    
                        if cek_task_enable == 'Y':
                            print(f"{YELLOW}[ Task ] : Checking tasks...", end="\r", flush=True)
                            ghalibie = check_task(token)
                            if ghalibie is not None:
                                for section in ghalibie:
                                    for task in section.get('tasks', []):
                                        # print(task)
                                        
                                        print(f"{YELLOW}[ Task ] : {task['title']} - Reward: {task['reward']}")
                                        if task.get('status') == 'NOT_STARTED':
                                            # start_task(token, task['id'])
                                            for subtask in task.get('subTasks', []):
                                                title_promo = subtask['title']
                                                if subtask['status'] == 'NOT_STARTED':
                                                    print(f"{YELLOW}    -> {title_promo}{Style.RESET_ALL}{Fore.YELLOW} {CYAN}Starting{Style.RESET_ALL}                 ", end="\r", flush=True)
                                                    start_promo = start_task(token, subtask['id'])
                                                    if start_promo is not None:
                                                        status_promo = start_promo.get('status')
                                                        message_promo = start_promo.get('message')
                                                        if message_promo == "Task is already started" or status_promo == "STARTED":
                                                            print(f"{Fore.GREEN+Style.BRIGHT}    -> {title_promo}{Style.RESET_ALL}{Fore.GREEN}. {CYAN}Started{Style.RESET_ALL}           ", flush=True)
                                                            claim_promo = claim_task(token, subtask['id'])
                                                            if claim_promo is not None:
                                                                status_promo = claim_promo.get('status')
                                                                message_promo = claim_promo.get('message')
                                                                if message_promo == "Task is already claimed" or status_promo == "FINISHED": 
                                                                    print(f"{Fore.GREEN+Style.BRIGHT}    -> {title_promo}{Style.RESET_ALL}{Fore.GREEN}. {CYAN}Claimed{Style.RESET_ALL}           ", flush=True)
                                                            else:
                                                                print(f"{Fore.RED+Style.BRIGHT}    -> {title_promo}{Style.RESET_ALL}{Fore.RED}. Failed{Style.RESET_ALL}              ", flush=True)
                                                    else:
                                                        print(f"{Fore.RED+Style.BRIGHT}    -> {title_promo}{Style.RESET_ALL}{Fore.RED}. Failed{Style.RESET_ALL}              ", flush=True)
                                                                        
                                                elif subtask['status'] in ['READY_FOR_CLAIM', 'STARTED']:
                                                    print(f"{YELLOW}    -> {title_promo}{Style.RESET_ALL}{Fore.YELLOW}{CYAN}Claiming{Style.RESET_ALL}                 ", end="\r", flush=True)
                                                    claim_promo = claim_task(token, subtask['id'])
                                                    
                                                    if claim_promo is not None:
                                                        status_promo = claim_promo.get('status')
                                                        message_promo = claim_promo.get('message')
                                                        if message_promo == "Task is already claimed" or status_promo == "FINISHED": 
                                                            print(f"{Fore.GREEN+Style.BRIGHT}    -> {title_promo}{Style.RESET_ALL}{Fore.GREEN}. {CYAN}Claimed{Style.RESET_ALL}           ", flush=True)
                                                        elif message_promo == "Task is not done":
                                                            print(f"{Fore.GREEN+Style.BRIGHT}    -> {title_promo}{Style.RESET_ALL}{Fore.RED}. {CYAN}Not Done / Pending{Style.RESET_ALL}          ", flush=True)
                                                        else:
                                                            print(f"{Fore.RED+Style.BRIGHT}    -> {title_promo}{Style.RESET_ALL}{Fore.RED}. Failed{Style.RESET_ALL}              ", flush=True)
                                            
                                        elif task.get('status')  == 'READY_FOR_CLAIM':
                                            print(f"{YELLOW}[ Task ] : {task['title']} - Reward: {task['reward']}. Claiming", end="\r", flush=True)
                                            claim_promo = claim_task(token, task['id'])
                                            if claim_promo is not None:
                                                status_promo = claim_promo.get('status')
                                                message_promo = claim_promo.get('message')
                                                if message_promo == "Task is already claimed" or status_promo == "FINISHED": 
                                                    print(f"{Fore.GREEN+Style.BRIGHT}    -> {title_promo}{Style.RESET_ALL}{Fore.GREEN}. {CYAN}Claimed{Style.RESET_ALL}           ", flush=True)
                                                else:
                                                    print(f"{Fore.RED+Style.BRIGHT}    -> {title_promo}{Style.RESET_ALL}{Fore.RED}. Failed{Style.RESET_ALL}              ", flush=True)
                                                  

                                    subSections = section.get('subSections', [])
                                    for subSection in subSections:
                                        titlenya = subSection['title']
                                        print(f"{YELLOW}[ Task ] : {titlenya}                         ", flush=True)
                                        for tasks in subSection['tasks']:
                                            title = tasks.get('title')
                                            reward = tasks.get('reward')
                                            status = tasks.get('status')
                                            task_type = tasks.get('type')
                                            id_task = tasks.get('id')
                                            validasi = tasks.get('validationType')

                                            if id_task == '39391eb2-f031-4954-bd8a-e7aecbb1f192':
                                                if status == 'FINISHED':
                                                    total_connect += 1
                                                
                                                
                                            if validasi == 'KEYWORD' and status == 'FINISHED':
                                                print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {GREEN}Completed{Style.RESET_ALL}                 ", flush=True)
                                                continue
                                            if status == 'FINISHED':
                                                print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {GREEN}Completed{Style.RESET_ALL}                 ", flush=True)
                                                continue
                                            
                                            if status == 'READY_FOR_VERIFY':
                                                print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {CYAN}Answering{Style.RESET_ALL}       ", end="\r", flush=True)
                                                ghalibie_validate = validate(token, id_task)
                                                time.sleep(1)
                                                # print(ghalibie_validate)
                                                if ghalibie_validate is not None:
                                                    valid_status = ghalibie_validate.get('status')
                                                    valid_message = ghalibie_validate.get('message')
                                                    if valid_status == 'READY_FOR_CLAIM':
                                                        print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {GREEN}Answered. Claiming..{Style.RESET_ALL}            ", end="\r", flush=True)
                                                    if valid_message == 'Task is already claimed':
                                                        print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {GREEN}Completed.{Style.RESET_ALL}            ", end="\r", flush=True)
                                                        continue
                                                    if valid_message == 'Task is not validating':
                                                        print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {GREEN}Already Answer. Claiming..{Style.RESET_ALL}            ", end="\r", flush=True)
                                                    ghalibie = claim_task(token, id_task)
                                                    time.sleep(1)
                                                    if ghalibie is not None:
                                                        status = ghalibie.get('status')
                                                        message = ghalibie.get('message')
                                                        if status == 'FINISHED':
                                                            print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Award: {reward} {GREEN}Completed{Style.RESET_ALL}           ", flush=True)
                                                        elif message == 'Task is not done':
                                                            print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {RED}Not Done{Style.RESET_ALL}               ", flush=True)
                                                        else:
                                                            print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {RED}Failed{Style.RESET_ALL}                ", flush=True)

                                            if status == 'READY_TO_CLAIM':
                                                print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {CYAN}Claiming{Style.RESET_ALL}                 ", flush=True)
                                                ghalibie = claim_task(token, id_task)
                                                time.sleep(1)
                                                if ghalibie is not None:
                                                    status = ghalibie.get('status')
                                                    message = ghalibie.get('message')
                                                    if status == 'FINISHED':
                                                        print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Award: {reward} {GREEN}Completed{Style.RESET_ALL}           ", flush=True)
                                                    elif message == 'Task is not done':
                                                            print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {RED}Not Done{Style.RESET_ALL}               ", flush=True)
                                                    else:
                                                            print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {RED}Failed{Style.RESET_ALL}    ", flush=True)


                                            if task_type in ['PROGRESS_TARGET', 'OTHER_TYPES_THAT_DO_NOT_SUPPORT_START']:
                                                print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {CYAN}Claiming{Style.RESET_ALL}                 ", flush=True)
                                                ghalibie = claim_task(token, id_task)
                                                time.sleep(1)
                                                if ghalibie is not None:
                                                    status = ghalibie.get('status')
                                                    message = ghalibie.get('message')
                                                    if status == 'FINISHED':
                                                        print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Award: {reward} {GREEN}Completed{Style.RESET_ALL}           ", flush=True)
                                                    elif message == 'Task is not done':
                                                        print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {RED}Not Done{Style.RESET_ALL}               ", flush=True)
                                                    else:
                                                        print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {RED}Failed{Style.RESET_ALL}                ", flush=True)
                                            else:
                                                print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {CYAN}Starting{Style.RESET_ALL}     ", end="\r", flush=True)
                                                ghalibie = start_task(token, id_task)
                                                time.sleep(1)
                                                if ghalibie is not None: 
                                                    print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Award: {reward} {MAGENTA}Started{Style.RESET_ALL}           ", end="\r", flush=True)
                                                    time.sleep(1)
                                                    print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Award: {reward} {CYAN}Claming..{Style.RESET_ALL}           ", end="\r" , flush=True)
                                                    ghalibie = claim_task(token, id_task)
                                                    if ghalibie is not None:
                                                        status = ghalibie.get('status')
                                                        message = ghalibie.get('message')
                                                        if status == 'FINISHED':
                                                            print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Award: {reward} {GREEN}Completed{Style.RESET_ALL}           ", flush=True)
                                                        elif message == 'Task is not done':
                                                            print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {RED}Not Done{Style.RESET_ALL}               ", flush=True)
                                                        else:
                                                            print(f"{YELLOW}    -> {title} -{Style.RESET_ALL}{Fore.YELLOW} Reward: {reward} {RED}Failed{Style.RESET_ALL}                ", flush=True)
                        
                        print(f"{YELLOW}[ Refferal ] : Checking..", end="\r", flush=True)
                        friend_balance = check_balance_friend(token)
                        
                        if friend_balance:
                            if friend_balance['canClaim']:
                                print(f"{GREEN}[ Refferal ] : {friend_balance['amountForClaim']}                        ", flush=True)
                                print(f"{GREEN}[ Refferal ] : Claiming...", end="\r", flush=True)
                                claim_friend_balance = claim_balance_friend(token)
                                if claim_friend_balance:
                                    claimed_amount = claim_friend_balance['claimBalance']
                                    print(f"{GREEN}[ Refferal ] : Success", flush=True)
                                else:
                                    print(f"{RED}[ Refferal ] : Failed to claim", flush=True)
                            else:
                                # Periksa apakah 'canClaimAt' ada sebelum mengaksesnya
                                can_claim_at = friend_balance.get('canClaimAt')
                                if can_claim_at:
                                    claim_time = datetime.datetime.fromtimestamp(int(can_claim_at) / 1000)
                                    current_time = datetime.datetime.now()
                                    time_diff = claim_time - current_time
                                    hours, remainder = divmod(int(time_diff.total_seconds()), 3600)
                                    minutes, seconds = divmod(remainder, 60)
                                    print(f"{RED}[ Refferal ] : Claim in {hours} hours {minutes} minutes              ", flush=True)
                                else:
                                    print(f"{RED}[ Refferal ] : False                                 ", flush=True)
                        else:
                            print(f"{RED}[ Refferal ] : Failed to Check           ", flush=True)
                        
                        

                
                print(f"\n{Fore.GREEN+Style.BRIGHT}Total Wallet  Connected: {total_connect} From {total_accounts}")  # Print total balance
                print(f"\n{Fore.GREEN+Style.BRIGHT}Total Balance from all accounts: {total_balance:,.0f}".replace(",", "."))  # Print total balance
                print(f"\n{Fore.GREEN+Style.BRIGHT}========={Fore.WHITE+Style.BRIGHT}Semua akun berhasil di proses{Fore.GREEN+Style.BRIGHT}=========", end="", flush=True)
                if notif_tele_enable == 'Y':
                    message = f"""          
                            ₿ <b>BLUM Report</b>

                    📁  <b>Total Accounts:</b> {total_accounts}
                    🔗 <b>Wallet Connected:</b> {total_connect}
                    💰 <b>Total Balance:</b> {total_balance:,.0f}


                    == Sirkel Generous ==
                    """
                    send_telegram_message(bot_token, chat_id, message)
                animated_loading(200)
        except Exception as e:
            print(f"{RED}An error occurred: {e}. Restarting script...", flush=True)
            time.sleep(5)  #
def animated_loading(duration):
    frames = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        for frame in frames:
            print(f"\rMenunggu waktu claim berikutnya {frame} - Tersisa {remaining_time} detik         ", end="", flush=True)
            time.sleep(0.25)
    print("\rMenunggu waktu claim berikutnya selesai.                            ", flush=True)
# Execute the main function
if __name__ == "__main__":
    main()
