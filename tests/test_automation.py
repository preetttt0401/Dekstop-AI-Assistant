from automation.app_controller import AppController

controller = AppController()

print(controller.open_app("calculator"))

print(controller.open_app("calc"))

print(controller.open_app("math"))

print(controller.open_app("paint"))