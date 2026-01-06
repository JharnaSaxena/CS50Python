import os
import sys
import requests
import webbrowser
import random
import cowsay
import pandas as pd
import matplotlib.pyplot as plt
import pyjokes
import pyfiglet
import pendulum as p

def joke():
    return pyjokes.get_joke()

def fig():
    art = pyfiglet.figlet_format("Bye Ms. Saxena", font="slant")
    print(art)

def good():
    now = p.now("local")
    hr = now.hour

    greeting = (
        "Well, well, well... look who decided to show up. "
        "I’m S.T.A.R.K—Strategic Tactical and Analytical Resource Knowledge. "
        "But let’s keep it simple. You can call me Stark."
    )
    print(greeting)

    if 7 <= hr < 12:
        greet = f"Good Morning, Ms. Saxena. Today is {now.format('dddd')}"
    elif 12 <= hr < 17:
        greet = f"Good Afternoon, Ms. Saxena! Hope you had your lunch. Today is {now.format('dddd')}"
    elif 17 <= hr < 22:
        greet = f"Good Evening, Ms. Saxena! Hope your day was productive. Today is {now.format('dddd')}"
    else:
        greet = f"Good Night, Ms. Saxena. Let's finish what you got on your plate. Today is {now.format('dddd')}"

    cowsay.cow(greet)

def speech():
    user_input = input("Ms. Saxena: ").strip().lower()
    return user_input


def main():
    good()

    while True:
        try:
            test = speech()
            if not test:
                continue

            if "youtube" in test:
                webbrowser.open("https://youtube.com/")
            elif "google" in test:
                webbrowser.open("https://www.google.com/")
            elif "whatsapp" in test:
                webbrowser.open("https://web.whatsapp.com/")
            elif "exit" in test:
                fig()
                sys.exit()
            elif "joke" in test:
                print(joke())
            elif "chatgpt" in test:
                webbrowser.open("https://chatgpt.com/?model=auto")
                print("OK Ma'am, Here's your ChatGPT. But maybe take a break from AI and try something yourself?")
            elif "play endgame" in test or "play ironman 3" in test:
                webbrowser.open("https://drive.google.com/drive/my-drive")
                print("At your service, Ma'am. Here's your movie.")
            elif "playlist" in test:
                webbrowser.open("https://www.youtube.com/watch?v=w0VvmB6ayBw&list=RDw0VvmB6ayBw&start_radio=1")
                print("At your service, Ma'am. Enjoy your playlist!")
            elif "stark" in test:
                print("At your service, Ma'am")
            elif "analyze" in test or "deploy" in test:
                url = input("Enter URL Ma'am: ")
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    contenttype = response.headers.get("Content-Type", "")
                    if "csv" in contenttype:
                        df = pd.read_csv(url)
                        if "X" in df.columns and "Y" in df.columns:
                            plt.plot(df["X"], df["Y"])
                            plt.grid()
                            plt.xlabel("X-axis")
                            plt.ylabel("Y-axis")
                            plt.show()
                        print(df)
                    elif "json" in contenttype:
                        df = pd.json_normalize(response.json())
                        print(df)
                    else:
                        print("Sorry, Ms. Saxena. The data format is not suitable.")
                except Exception as e:
                    print("Error processing the data.", e)
            elif "time" in test:
                now = p.now("local")
                print(f"The current time is {now.format('HH:mm A')}.")
            else:
                print("I'm not sure how to respond to that, Ms. Saxena.")
        except KeyboardInterrupt:
            print("\nGoodbye, Ms. Saxena!")
            fig()
            break
        except Exception as e:
            print("Sorry Ms. Saxena, I encountered an issue.")
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
