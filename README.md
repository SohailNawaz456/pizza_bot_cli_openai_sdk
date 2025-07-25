# 🍕 Pizza Restaurant Chat Bot

A terminal-based chat bot simulation for a pizza restaurant, built using agent-based architecture. Customers can:

- Greet the bot and be welcomed
- View the pizza menu
- Place a pizza order

---

## 🧠 Agents Included

1. **Welcome Agent**  
   Responds to greetings like "hi", "hello", or "hey" with a warm welcome.

2. **Waiter Agent**  
   Displays a pizza menu when the user asks for it (e.g., "show menu").

3. **Order Agent**  
   Takes the order when a customer mentions a pizza name like "Margherita", "Pepperoni", or "Veggie".

---

## 🚀 Getting Started

### Prerequisites

Make sure you have:

- Python 3.8+
- `rich` for colored terminal output  
- Your own `Agent`, `Runner`, and `config` modules

---

### 📦 Install Dependencies

```bash
pip install rich

📁 Project Structure

.
├── main.py             # Main chatbot logic
├── conection/config.py # Configurations for running agents
└── README.md           # This file


▶️ Run the App

python main.py
💬 Example Interaction

🍕 Pizza Ordering Chat Started!
Type 'exit' to quit.

User: hello
welcome_agent:
Hello! Welcome to the pizza place. Please have a seat.

User: show menu
waiter_agent:
Here's our menu:
- 🍅 Margherita
- 🍖 Pepperoni
- 🥦 Veggie

User: I want a Pepperoni pizza
order_agent:
Great! Your Pepperoni pizza has been ordered.
🛠 Customization
You can:

Add more pizzas in the Waiter and Order agents

Improve the NLP logic to detect more flexible user input

Connect it to a backend or database for real orders

📄 License
MIT License — free to use and modify.

👨‍🍳 Built for Fun & Practice
This project demonstrates basic agent routing using Python and simple AI interaction logic.


Let me know if you want to include badges (like Python version), a GIF demo, or convert it for use wi
