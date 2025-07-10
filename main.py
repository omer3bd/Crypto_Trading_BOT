from random import randint
import pandas as pd
import ccxt
import sys
import os
BOT_STATUS = True
import statistics
import requests
from dotenv import load_dotenv


class CT_BOT:
    def __init__(self): #, exchange_name):
        self.scraper = False
        # Load environment variables
        load_dotenv()
        self.STATUS_URL = os.getenv("URL_GIST")
        # self.exchange_name = exchange_name
        # Initialize the exchange here if needed
        # self.exchange = getattr(ccxt, exchange_name)()

    # def __repr__(self):
        # return f'CT_BOT(exchange_name={self.exchange_name})'

    # def __str__(self):
        # return f'CT_BOT for {self.exchange_name}'

    def menu(self):
        print("\nWelcome to Crypto Trading BOT")
        print("Press 'a' to check Available commands\n")

        # use kwargs to trade. Example: b/s btc 0.01 stop 2 tp 6 (buy/sell)
        # also add a feature that chases the price

        # ------------- Command selection -------------
        self.choice = input(">>>>Enter a command: ").lower()    # ENTER COMMAND HERE


        # ------------- Display Features or Handle choices -------------
        if self.choice == 'a':
            self.commands_available()
        else:
            self.handle_choice(self.choice)

    def commands_available(self):
        print("\n***** Available commands *****")
        print("Start Bot: 'start'")
        print("Stop Bot: 'stop'")
        print("BOT Features: 'f'")
        print("Exit: 'e'")

    def handle_choice(self, choice):
        if choice == 'e':
            print("Exiting the bot. Goodbye!")
            sys.exit()
        elif choice == 'a':
            self.commands_available()
        elif choice == 'f':
            self.features_status()
        elif choice == 'start':
            self.start()
        elif choice == 'stop':
            print("Stopping all bots. Now on stand-by. Trading bot still is active.")

    def features_status(self):

        # ------------- Display available features -------------
        print("\nBOT Features:")
        print("1. Scraping data from Coin telegraph for news:", "[Enabled]" if self.scraper else "[Disabled]")
        print(". Trade auto-execution: Enabled")

        print(". SMS alerts: Enabled")
        print(". Email alerts: Enabled")
        print(". Push notifications: Enabled")
        print(". Telegram alerts: Enabled")

        print(". Technical Indicators: Enabled")

        # print(". Portfolio management: Enabled")
        # print(". Risk management strategies: Enabled")
        # print(". Performance analytics: Enabled")
        print("n. Back to Menu")


        # ------------- Feature selection -------------
        self.choice_feature = int(input(">>>>Enter a command: "))


        # ------------- Redirect Menu -------------
        if self.choice not in [1, 2, 3, 4, 5]:
            self.handle_features(self.choice_feature)

    def handle_features(self, choice_feature):

        if choice_feature == 1:
            op1 = input(">>>>Press 'e' to enable, 'd' to disable: ").lower()
            try:
                if op1 == 'e':
                    print("Enabling Coin Telegraph scraper...")
                    self.scraper = True
                elif op1 == 'd':
                    print("Disabling Coin Telegraph scraper...")
                    self.scraper = False
            finally: print("Scraper status: ", "Enabled" if self.scraper else "Disabled")
        elif choice_feature == 2:
            pass
        elif choice_feature == 3:
            pass
        elif choice_feature == 4:
            pass
        elif choice_feature == 5:
            pass
        elif choice_feature == 6:
            self.menu()




    def start(self):
        print(f'Starting bot')
        while True:
            self.scrape()

    # def stop(self):
    # print(f'Stopping bot for {self.exchange_name}')

    # --------------------- BOT functions -----------------
    def scrape(self):
    #     if not self.scraper:
    #         pass
    #     else:
    #         pass
        # print(f'Scraping data from {self.exchange_name}')
        print(f'Scraping data from Coin Telegraph')

    def sms_alert(self, message):
        # print(f'Sending SMS alert: {message}')
        pass

    def email_alert(self, message):
        # print(f'Sending email alert: {message}')
        pass

    def push_notification(self, message):
        # print(f'Sending push notification: {message}')
        pass

    def telegram_alert(self, message):
        # print(f'Sending Telegram alert: {message}')
        pass

    # ----------------- Trader tools -----------------
    def get_pos(self):
        pass
    
    def get_balance(self):
        # print(f'Getting balance for {self.exchange_name}')
        pass

    def get_portfolio(self):
        # print(f'Getting portfolio for {self.exchange_name}')
        pass

    def close_pos(self):
        # print(f'Closing position for {self.exchange_name}')
        pass

    def open_pos(self):
        # print(f'Opening position for {self.exchange_name}')
        pass

    def set_stop_loss(self):
        # print(f'Setting stop loss for {self.exchange_name}')
        pass

    def get_trade_history(self):
        # print(f'Getting trade history for {self.exchange_name}')
        pass

    # ----------------- Trader indicators -----------------
    def get_rsi(self):
        # print(f'Getting RSI for {self.exchange_name}')
        pass
    
    def get_rsi_divergence(self):
        # print(f'Getting RSI divergence for {self.exchange_name}')
        pass
    
    def get_candles(self):
        # print(f'Getting candles for {self.exchange_name}')
        pass
    
    def get_volume(self):
        # print(f'Getting volume for {self.exchange_name}')
        # get volume ema also
        pass
    
    def get_ema(self):
        # print(f'Getting EMA for {self.exchange_name}')
        pass

    def prev_day_OHLC(self):
        # print(f'Getting previous day OHLC for {self.exchange_name}')
        pass

    def prev_week_OHLC(self):
        # print(f'Getting previous week OHLC for {self.exchange_name}')
        pass

    def prev_month_OHLC(self):
        # print(f'Getting previous month OHLC for {self.exchange_name}')
        pass

    def prev_year_OHLC(self):
        # print(f'Getting previous year OHLC for {self.exchange_name}')
        pass

    def prev_day_value_area(self):
        # print(f'Getting previous day value area for {self.exchange_name}')
        # VAH
        # VAL
        # POC
        pass

    def vwap(self):
        # print(f'Getting VWAP for {self.exchange_name}')
        pass

    def get_fibonacci_levels(self):
        # print(f'Getting Fibonacci levels for {self.exchange_name}')
        pass

    def volatility_calculator(self):
        # print(f'Calculating volatility for {self.exchange_name}')
        # check volatility that checks up to 3 days of data
        # use ATR (Average True Range) or standard deviation
        # Volatility = (high - low) / low * 100
        # volatility: +3%
        pass

    def get_fear_and_greed_index(self):
        # print(f'Getting Fear and Greed Index for {self.exchange_name}')
        pass



    # ----------------- Main function that initiates  -----------------
    # Remote kill switch
    def gate(self):
        patience = 0
        if not self.STATUS_URL:
            print("❌ Kill switch URL not found in environment.")
            sys.exit()
        try:
            response = requests.get(self.STATUS_URL, timeout=5)
            if response.status_code == 200:
                status = response.text.strip().lower()
                if patience == 3:
                    print('⚠️ Remote kill switch is not responding. Proceeding with caution...')
                    # self_destruct()
                if status == 'off':
                    print("🚫 DISABLED BY ADMIN. Bot is allowed to run")
                    sys.exit()
                elif status == 'wait':
                    print("\n\n\n⏳ Remote kill switch is in WAIT mode by admin. Bot will not run.")
                    sys.exit()
                elif status == 'on':
                    print("✅ Remote kill switch: Bot is allowed to run.")
                    # BOT_STATUS = True
                    # self.menu()
                else:
                    pass
            else:
                print("⚠️ Could not verify kill switch status. Proceeding anyway.")
        except Exception as e:
            print(f"⚠️ Kill switch check failed: {e}. Proceeding...")

    def main_bot_run(self):
        while BOT_STATUS:
            self.menu()

    # delete the main.py file
    def self_destruct(self):
        print("☠️ Kill switch triggered. self-destructing...")
        try:
            os.remove(__file__)
            print("Successfully self-destructed")
        except Exception as e:
            print(f"❌ Could not delete main.py: {e}")
        sys.exit()


# # live_price = 100












# ----------------- Main function that initiates  -----------------

class TradingBot:
    def __init__(self):
        # self.exchange_name = exchange_name
        # self.bot = CT_BOT()  # Initialize the CT_BOT instance
        # self.bot.gate()  # Check the remote kill switch

        # ----------------- Kelly data -----------------
        self.win_trades = [300, 500, 200, 400, 600, 10]  # Example winning trades
        self.lose_trades = [100, 150, 200, 50]
        self.bank_roll:float = 10000
        self.stop_loss:float = 0.10  # 10% stop loss
        # self.live_price = 100

        # ----------------- Sharpe data -----------------
        self.monthly_return = [5, 2, -3, 7, 1, 4, -2, 6, 3, -1, 8, 2]

        # ------------------ Monte Carlo data -----------------
        self.win_amt = 2  # $2 profit per win
        self.loss_amt = -1  # $1 loss per loss
        self.n_sim = 100  # Number of simulations to show (first n simulations)

    def run(self):
        # print(f"Running trading bot for {self.exchange_name}")
        # self.bot.main_bot_run()

        # Estimate profitability per trade
        self.expected_value()
        # optimal bet size
        self.kelly_criterion()
        pass

    def monte_carlo_simulation(self):       # Statistical arbitrage & Market modeling
        results = []
        for i in range(self.n_sim):
            random_win: int = randint(1, 100)  # Random percentage for win distribution
            radom_loss: int = (random_win - 100)  # Random percentage for loss distribution

            sim_win: float = (random_win * self.win_amt)  # Simulated win amount
            sim_loss: float = (radom_loss * self.loss_amt)  # Simulated loss amount

            sim_net_profit: float = sim_win + sim_loss  # Net profit from all trades
            results.append([i + 1, sim_win, sim_loss, sim_net_profit])  # [1, 114, 43, 157]
        # print(results)
        print(" ")
        df = pd.DataFrame(results, columns=['Sim #', 'Wins', 'Losses', 'Profit'])

        # Print first 10 and last 10 simulations
        print(df.head(4))

        # Summary stats
        print("\n=== Summary Statistics ===")
        print(f"Average Profit: ${df['Profit'].mean():.2f}")
        print(f"Best Profit: ${df['Profit'].max():.2f} (Sim #{df['Profit'].idxmax() + 1})")
        print(f"Worst Profit: ${df['Profit'].min():.2f} (Sim #{df['Profit'].idxmin() + 1})")
        print(f"5th Percentile: ${df['Profit'].quantile(0.05):.2f}")

    def kelly_criterion(self):      # Position sizing strategy & Risk management
        # ----------------- Win prob -----------------
        # trades in profit
        num_winning_trades:int = len(self.win_trades)
        # trades in profit + loss
        total_trades:int = (len(self.win_trades) + len(self.lose_trades))
        win_prob:float = num_winning_trades / total_trades if total_trades > 0 else 0
        print(f'Your win prob: {win_prob * 100:.2f}%')

        # ----------------- Win/Loss Ratio calculation -----------------
        # avg win
        avg_win:float = sum(self.win_trades) / len(self.win_trades) if self.win_trades else 0
        # avg loss
        avg_loss:float = sum(self.lose_trades) / len(self.lose_trades) if self.lose_trades else 0

        # avg win/loss ratio
        if avg_loss != 0:
            winloss_ratio: float = avg_win / avg_loss
            print(f'Your win ratio: {winloss_ratio:.2f}%')
        else:
            winloss_ratio: float = float('inf')  # Handle division by zero

        # ----------------- Kelly Criterion calculation -----------------
        win_probability: float = win_prob  # Probability of winning a trade
        win_loss_ratio: float = winloss_ratio  # Ratio of average win to average loss

        kf = (win_probability * (win_loss_ratio + 1) - 1) / win_loss_ratio
        # print(kf)

        # amount to risk
        risk_amt: float = kf * self.bank_roll
        # print(risk_amt)
        pos_size: float = (risk_amt / self.stop_loss)
        # print(pos_size)

        print(f"\nYou took a trade of '${pos_size:.2f}',"
              f" optimal Capital to risk is '{kf * 100:.2f}%'..."
              f"\nYour stop-loss of '{self.stop_loss * 100:.2f}%' may lose you ${risk_amt:.2f} of your Capital.")

    def sharp_ratio(self):          # Trade performance metrics
        # > 0.1 generally considered good
        # > 2.0 considered excellent
        # < 0.0 considered bad
        # print(f"\n> 0.1 generally considered good"
        #       f"\n> 2.0 considered excellent"
        #       f"\n< 0.0 considered bad\n")

        # assuming the risk-free rate is 0%
        avg_return: float = sum(self.monthly_return) / len(self.monthly_return)

        # -------------- calculate the standard deviation --------------
        # deviation mean
        std_dev: float = statistics.stdev(self.monthly_return)
        print(f"{std_dev:.2f} is the standard deviation")

        # Sharpe Ratio calculation
        sharpe_ratio: float = avg_return / std_dev if std_dev != 0 else float('inf')
        print(f"{sharpe_ratio:.2f} is the Sharpe Ratio")

        if sharpe_ratio >= 2.0:
            print("The Sharpe Ratio indicates a good risk-adjusted return.")
        elif sharpe_ratio >= 1.0:
            print("The Sharpe Ratio indicates an excellent risk-adjusted return.")
        elif sharpe_ratio > 0.0:
            print("The Sharpe Ratio indicates a bad risk-adjusted return.")
        else:
            print("Unknown Sharpe Ratio")

    def expected_value(self):       # Probability of winning a trade
        # Placeholder for Expected Value calculation logic
        print("Calculating Expected Value...")

    def backtest_strategy(self):
        # Placeholder for backtesting logic
        print("Backtesting trading strategy...")





# Instantiate and start the bot
ctp = CT_BOT()
# ctp.gate()
ctp.main_bot_run()
# ------------- classes -----------------
# tb = TradingBot()
# tb.monte_carlo_simulation()

import requests
import os
import sys
import datetime

KEY_FILE = "activation.key"
REMOTE_KEYS_URL = "https://raw.githubusercontent.com/omer3bd/CTB-switch/main/keys.txt"

def fetch_remote_keys():
    try:
        res = requests.get(REMOTE_KEYS_URL)
        if res.status_code == 200:
            raw_lines = res.text.strip().splitlines()
            keys = {}
            for line in raw_lines:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    key, expiry = parts[0].strip(), parts[1].strip()
                    keys[key] = expiry
            return keys
        else:
            print("❌ Couldn't fetch key list.")
            return {}
    except Exception as e:
        print(f"❌ Error fetching key list: {e}")
        return {}

def is_valid(key, remote_keys):
    if key not in remote_keys:
        return False, None
    expiry_date = datetime.datetime.strptime(remote_keys[key], "%Y-%m-%d").date()
    today = datetime.date.today()
    return today <= expiry_date, expiry_date

def check_local_activation(remote_keys):
    if not os.path.exists(KEY_FILE):
        return False

    try:
        with open(KEY_FILE, 'r') as f:
            data = f.read().strip().split(',')
            if len(data) != 2:
                return False
            saved_key, activation_date_str = data
            activation_date = datetime.datetime.strptime(activation_date_str, "%Y-%m-%d").date()
            today = datetime.date.today()

            # Check if within 2-day window
            if (today - activation_date).days <= 2:
                valid, expiry = is_valid(saved_key, remote_keys)
                if valid:
                    print(f"✅ Activated key still valid (expires: {expiry})")
                    return True
                else:
                    print("🔒 Key expired remotely.")
                    return False
            else:
                print("🔒 Local activation expired (over 2 days).")
                return False
    except Exception as e:
        print("⚠️ Error checking activation:", e)
        return False

def request_activation(remote_keys):
    for _ in range(3):
        entered_key = input("🔐 Enter your activation key: ").strip()
        valid, expiry = is_valid(entered_key, remote_keys)
        if valid:
            with open(KEY_FILE, 'w') as f:
                today = datetime.date.today().strftime("%Y-%m-%d")
                f.write(f"{entered_key},{today}")
            print("✅ Activation successful.")
            return True
        else:
            print("❌ Invalid or expired key.")
    print("⛔ Too many invalid attempts. Exiting.")
    return False

def check_activation():
    remote_keys = fetch_remote_keys()
    if check_local_activation(remote_keys):
        return
    else:
        if not request_activation(remote_keys):
            sys.exit()

# Place this at the top of your main.py
# check_activation()