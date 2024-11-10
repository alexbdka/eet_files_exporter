import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class FileProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EET Files Exporter")
        self.root.geometry("550x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#f2f2f2")

        # Titre
        title = tk.Label(root, text="EET Exportateur de Fichiers", font=("Arial", 18, "bold"), bg="#f2f2f2", fg="#333")
        title.pack(pady=10)

        # Description avec un cadre
        frame = tk.Frame(root, bg="#e6e6e6", padx=10, pady=10)
        frame.pack(pady=10, padx=15, fill="x")
        description = tk.Label(
            frame, text="Ce programme copie les fichiers .esp et .esm ayant une sauvegarde (.OLD000) "
                        "depuis le dossier source vers le dossier de destination.\n"
                        "Les fichiers originaux seront supprimés et la sauvegarde sera renommée pour conserver le nom original.",
            wraplength=500, justify="left", bg="#e6e6e6", fg="#555"
        )
        description.pack()

        # Boutons de sélection de dossiers avec cadre
        buttons_frame = tk.Frame(root, bg="#f2f2f2")
        buttons_frame.pack(pady=10)
        select_source_button = ttk.Button(buttons_frame, text="Sélectionner le dossier source", command=self.select_source_folder)
        select_source_button.grid(row=0, column=0, padx=10, pady=5)

        select_destination_button = ttk.Button(buttons_frame, text="Sélectionner le dossier de destination", command=self.select_destination_folder)
        select_destination_button.grid(row=0, column=1, padx=10, pady=5)

        # Bouton pour lancer le traitement
        process_button = ttk.Button(root, text="Lancer le traitement", command=self.process_files)
        process_button.pack(pady=20)

        # Variables de dossier
        self.source_folder = None
        self.destination_folder = None

    def select_source_folder(self):
        self.source_folder = filedialog.askdirectory(title="Sélectionnez le dossier source")
        if self.source_folder:
            messagebox.showinfo("Dossier source sélectionné", f"Dossier source : {self.source_folder}")

    def select_destination_folder(self):
        self.destination_folder = filedialog.askdirectory(title="Sélectionnez le dossier de destination")
        if self.destination_folder:
            messagebox.showinfo("Dossier de destination sélectionné", f"Dossier de destination : {self.destination_folder}")

    def process_files(self):
        if not self.source_folder or not self.destination_folder:
            messagebox.showerror("Erreur", "Veuillez sélectionner les dossiers source et de destination.")
            return

        if not os.path.exists(self.source_folder):
            messagebox.showerror("Erreur", f"Le dossier source '{self.source_folder}' n'existe pas.")
            return

        # Crée le dossier de destination s'il n'existe pas
        os.makedirs(self.destination_folder, exist_ok=True)
        files_found = False

        # Parcourir les fichiers .esp et .esm
        for root, _, files in os.walk(self.source_folder):
            for file in files:
                if file.endswith(('.esp', '.esm')):
                    file_path = os.path.join(root, file)
                    backup_file_path = f"{file_path}.OLD000"

                    # Vérifie si une sauvegarde existe
                    if os.path.exists(backup_file_path):
                        try:
                            files_found = True
                            # Copier le fichier
                            shutil.copy(file_path, self.destination_folder)
                            # Supprimer l'original
                            os.remove(file_path)
                            # Renommer la sauvegarde
                            os.rename(backup_file_path, file_path)
                        except Exception as e:
                            messagebox.showerror("Erreur", f"Erreur lors du traitement de '{file}': {e}")
                            return

        # Vérification finale
        if not files_found:
            messagebox.showinfo("Aucun fichier trouvé", f"Aucun fichier avec sauvegarde .OLD000 trouvé dans le dossier source '{self.source_folder}'.")
        else:
            messagebox.showinfo("Succès", "Tous les fichiers ont été traités avec succès.")

# Initialisation de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = FileProcessorApp(root)
    root.mainloop()
