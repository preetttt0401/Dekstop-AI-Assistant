from automation.app_controller import AppController

controller = AppController()

print("=" * 50)
print("Desktop AI Assistant - App Launcher Test")
print("Type 'exit' to quit.")
print("=" * 50)

while True:
    app_name = input("\nEnter application name: ").strip()

    if app_name.lower() == "exit":
        print("Exiting test...")
        break

    result = controller.open_app(app_name)

    print(result)