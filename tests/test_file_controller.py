from automation.file_controller import FileController

controller = FileController()

print("=" * 50)
print("File Controller Test")
print("=" * 50)

desktop = input("Enter Desktop path: ").strip()

folder_name = input("Folder name: ").strip()

folder_path = desktop + "\\" + folder_name

created = controller.create_folder(folder_path)

print("Created:", created)

opened = controller.open_folder(folder_path)

print("Opened:", opened)
