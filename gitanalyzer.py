from tkinter import *
import requests

BASE_URL = "https://api.github.com/users/"

def get_github_profile():
    username = username_entry.get().strip()
    if not username:
        result_label.config(text="Enter a valid username!", fg="red")
        return

    url = f"{BASE_URL}{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        profile_text = f"""
👤 Name: {data.get('name', 'N/A')}
📍 Location: {data.get('location', 'N/A')}
📌 Bio: {data.get('bio', 'N/A')}
🔗 Profile: {data['html_url']}
📦 Public Repos: {data['public_repos']}
👥 Followers: {data['followers']} | Following: {data['following']}
"""
        result_label.config(text=profile_text, fg="black", bg="white")
    else:
        result_label.config(text="User not found. Check the username.")


# Tkinter GUI Setup
window = Tk()
window.title("GitHub Profile Viewer")
window.geometry("500x500")  # Set window size

# Load Background Image
bg_image = PhotoImage(file="download (17).png")  # Make sure the image exists in the same folder
bg_label = Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)  # Cover the entire window

# Entry for GitHub username
entry_frame = Frame(window, bg="#ffffff", bd=5)
entry_frame.pack(pady=20)

Label(entry_frame, text="Enter GitHub Username:", font=("Arial", 12), bg="white").pack()
username_entry = Entry(entry_frame, width=30)
username_entry.pack()

# Search Button
search_button = Button(window, text="Get Profile", command=get_github_profile, bg="lightblue", font=("Arial", 10))
search_button.pack(pady=10)

# Result Label
result_label = Label(window, text="", justify=LEFT, font=("Arial", 10), wraplength=400, bg="white")
result_label.pack(pady=20)

# Run Tkinter event loop
window.mainloop()





