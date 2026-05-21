from spawn_agent import spawn_agent

if __name__ == "__main__":
    prompt = input("Enter agent prompt: ")

    result = spawn_agent(prompt)

    print("\n=== RESULT ===")
    print(result)
