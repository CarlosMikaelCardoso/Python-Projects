import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Word Frequency")
root.geometry("300x200")

def resultado():
    global label, result
    result = tk.Tk()
    result.title("Result")
    result.geometry("300x200")
    count_letters()

def fetch_url_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch URL content: {e}")
        return ""

def count_letters():
    global sorted_letter_counts, result, text_widget
    text_widget = tk.Text(result, wrap='word')
    text_widget.pack(expand=True, fill='both')
    text = entry.get()
    if text.startswith("http://") or text.startswith("https://"):
        text = fetch_url_content(text)
    letter_counts = {}
    for char in text:
        if char.isalpha():
            char = char.lower()  # Considerar letras maiúsculas e minúsculas como iguais
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    sorted_letter_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
        
    texto_final = ""
    for char, count in sorted_letter_counts:
        texto_final += f"{char}: {count}\n"

    text_widget.insert('1.0', texto_final)
    plot_graph(sorted_letter_counts)
    
def plot_graph(letter_counts):
    letters, counts = zip(*letter_counts)
    plt.bar(letters, counts)
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency')
    plt.show()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Count letters", command=resultado)
button.pack()

root.mainloop()