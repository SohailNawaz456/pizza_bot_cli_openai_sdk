# Import required modules and components
from agents import Agent, Runner  # Import Agent and Runner classes
from conection import config       # Import the config for running agents
import asyncio                     # For asynchronous input/output handling
from rich.console import Console   # For colored terminal output

console = Console()  # Initialize rich console for pretty printing

# -------------------- Define Agents --------------------

# Order Agent: Handles pizza orders when a pizza name is mentioned
order_agent = Agent(
    name="order_agent",
    instructions="""
You are an order agent in a pizza restaurant.
When a customer mentions a pizza name (like "Margherita", "Pepperoni", "Veggie"), take the order.
Example:
"I want a Margherita pizza"
"""
)

# Waiter Agent: Responds with the pizza menu when user asks for it
waiter_agent = Agent(
    name="waiter_agent",
    instructions="""
You are a waiter in a pizza restaurant and provide a list of pizzas to the customer.

## 🍕 Pizza Menu:
- 🍅 Margherita
- 🍖 Pepperoni
- 🥦 Veggie

Only respond when the user asks to show the menu.
"""
)

# Welcome Agent: Greets the customer when they say hi/hello/hey
welcome_agent = Agent(
    name="welcome_agent",
    instructions="""
You are a welcome agent in a pizza restaurant.
Greet the customer warmly.
Ask them to have a seat.
Only respond to greetings like 'hi', 'hello', 'hey'.
"""
)

# -------------------- Main Event Loop --------------------

async def main():
    console.print("🍕 [bold magenta]Pizza Ordering Chat Started![/bold magenta]\nType '[red]exit[/red]' to quit.\n")

    while True:
        # Get user input, convert to lowercase, and strip whitespace
        msg = console.input("[bold cyan]User:[/bold cyan] ").lower().strip()

        # Exit condition
        if msg == "exit":
            console.print("👋 [bold yellow]Goodbye![/bold yellow]")
            break

        # Route greeting to Welcome Agent
        elif any(word in msg for word in ["hi", "hello", "hey"]):
            result = await Runner.run(welcome_agent, msg, run_config=config)

        # Route menu requests to Waiter Agent
        elif "menu" in msg or "show menu" in msg:
            result = await Runner.run(waiter_agent, msg, run_config=config)

        # Route pizza orders to Order Agent
        elif any(pizza in msg for pizza in ["margherita", "pepperoni", "veggie"]):
            result = await Runner.run(order_agent, msg, run_config=config)

        # If input doesn't match any known pattern
        else:
            console.print("🤖 [italic red]Unknown input.[/italic red] Try: 'hello', 'show menu', or a pizza name.")
            continue

        # Display the responding agent's name and output
        console.print(f"\n[bold green]{result.last_agent.name}:[/bold green]")
        console.print(f"[white]{result.final_output}[/white]")

# Run the main loop if this script is executed directly
if __name__ == "__main__":
    asyncio.run(main())
