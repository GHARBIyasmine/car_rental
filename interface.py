import tkinter
import customtkinter
import os
from manager_module import LocationManager

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class CustomFrame(customtkinter.CTkFrame):
    def __init__(self, master, row, column, title, icon, number_of_rows, command, include_btn=True, **kwargs):
        super().__init__(master, corner_radius=20, fg_color="#FFFFFF",
                         border_color="#EDEFF8", border_width=4, **kwargs)
        self.grid_rowconfigure((1), weight=1)
        self.grid_columnconfigure((0), weight=1)
        self.grid(row=row, column=column, ipady=10, padx=30, pady=10, ipadx=10)
        self.title = customtkinter.CTkLabel(master=self, corner_radius=20,
                                            fg_color="transparent",
                                            text=title,
                                            font=customtkinter.CTkFont(size=20, weight="bold"),
                                            image=icon,
                                            compound="left"
                                            )
        self.title.grid(row=1, column=0, pady=20, sticky="nsew", padx=20)
        self.button = customtkinter.CTkButton(master=self, corner_radius=30, fg_color="#FFCB42",
                                              text="Submit",
                                              text_color="black", hover_color="#FFB200",
                                              bg_color="transparent",
                                              command=command)
        if include_btn:
            self.button.grid(row=number_of_rows - 1, column=0, padx=10, pady=20)

    def grid_remove(self):
        super().grid_remove()

    def grid_appear(self):
        super().grid()


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, text, *args, **kwargs):
        super().__init__(fg_color="#FFFFFF", *args, **kwargs)
        self.geometry("500x200")
        self.grid_rowconfigure((1), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.label = customtkinter.CTkLabel(self,
                                            text=text,
                                            font=customtkinter.CTkFont(size=20, weight="bold"),
                                            fg_color="transparent", )
        self.label.grid(row=1, column=0, pady=20, sticky="nsew", padx=20)


class App(customtkinter.CTk):
    WIDTH = 1000
    HEIGHT = 700
    global quantity_matrix

    def __init__(self):
        super().__init__()
        self.switch_var = customtkinter.StringVar()

        self.title("Location de voiture")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.manager = LocationManager()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")

        # ======================== TopLevel window ================

        self.toplevel_window = None

        # ============ create main frames ============

        # configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0,
                                                 fg_color="#EDEFF8")
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self, fg_color="#F9FAFF")
        self.frame_right.grid(row=0, column=1, sticky="nswe")

        self.frame_PL_intro = customtkinter.CTkFrame(master=self, fg_color="#F9FAFF")
        self.frame_PL_intro.grid(row=0, column=1, sticky="nswe")
        self.frame_PL_intro.grid_remove()

        # ============ frame_left ============

        # configure grid layout
        self.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing

        self.label = customtkinter.CTkLabel(master=self.frame_left, text=" Menu Principal",
                                            fg_color="transparent", bg_color="transparent",
                                            font=("Roboto Medium", -25)
                                            )
        self.label.grid(row=1, column=0, sticky="nswe")

        self.home_button = customtkinter.CTkButton(master=self.frame_left,
                                                   text="Home",
                                                   font=("Roboto Medium", -14),
                                                   corner_radius=40,
                                                   fg_color="#3E89C7",
                                                   command=self.go_to_home)
        self.home_button.grid(row=2, column=0, pady=10, padx=10, sticky="ew")

        self.add_voiture_btn = customtkinter.CTkButton(master=self.frame_left, corner_radius=30, fg_color="#FFCB42",
                                                       text="Ajouter une voiture",
                                                       text_color="black", hover_color="#FFB200",
                                                       bg_color="transparent",
                                                       command=self.activate_add_voiture)
        self.add_voiture_btn.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.edit_voiture_btn = customtkinter.CTkButton(master=self.frame_left, corner_radius=30, fg_color="#FFCB42",
                                                        text="Modifier une voiture",
                                                        text_color="black", hover_color="#FFB200",
                                                        bg_color="transparent",
                                                        command=self.activate_edit_voiture)
        self.edit_voiture_btn.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        self.delete_voiture_btn = customtkinter.CTkButton(master=self.frame_left, corner_radius=30, fg_color="#FFCB42",
                                                          text="Supprimer une voiture",
                                                          text_color="black", hover_color="#FFB200",
                                                          bg_color="transparent",
                                                          command=self.activate_delete_voiture)
        self.delete_voiture_btn.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

        self.add_locataire_btn = customtkinter.CTkButton(master=self.frame_left, corner_radius=30, fg_color="#FFCB42",
                                                         text="Ajouter un locataire",
                                                         text_color="black", hover_color="#FFB200",
                                                         bg_color="transparent",
                                                         command=self.activate_add_locataire)
        self.add_locataire_btn.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

        self.edit_locataire_btn = customtkinter.CTkButton(master=self.frame_left, corner_radius=30, fg_color="#FFCB42",
                                                          text="Modifier un locataire",
                                                          text_color="black", hover_color="#FFB200",
                                                          bg_color="transparent",
                                                          command=self.activate_edit_locataire)
        self.edit_locataire_btn.grid(row=7, column=0, padx=10, pady=10, sticky="ew")

        self.delete_locataire_btn = customtkinter.CTkButton(master=self.frame_left, corner_radius=30,
                                                            fg_color="#FFCB42",
                                                            text="Supprimer un locataire",
                                                            text_color="black", hover_color="#FFB200",
                                                            bg_color="transparent",
                                                            command=self.activate_delete_locataire)
        self.delete_locataire_btn.grid(row=8, column=0, padx=10, pady=10, sticky="ew")

        self.chercher_locataire_btn = customtkinter.CTkButton(master=self.frame_left, corner_radius=30,
                                                              fg_color="#FFCB42",
                                                              text="chercher un locataire",
                                                              text_color="black", hover_color="#FFB200",
                                                              bg_color="transparent",
                                                              command=self.activate_chercher_locataire)
        self.chercher_locataire_btn.grid(row=9, column=0, padx=10, pady=10, sticky="ew")

        self.rent_car_btn = customtkinter.CTkButton(master=self.frame_left, corner_radius=30, fg_color="#FFCB42",
                                                    text="Louer une voiture",
                                                    text_color="black", hover_color="#FFB200",
                                                    bg_color="transparent",
                                                    command=self.activate_rent_car)
        self.rent_car_btn.grid(row=10, column=0, padx=10, pady=10, sticky="ew")

        self.return_car_btn = customtkinter.CTkButton(master=self.frame_left, corner_radius=20, fg_color="#FFCB42",
                                                      text="Rendre une voiture",
                                                      text_color="black", hover_color="#FFB200",
                                                      bg_color="transparent",
                                                      command=self.activate_return_car)
        self.return_car_btn.grid(row=11, column=0, padx=10, pady=10, sticky="ew")

        self.check_status_car_btn = customtkinter.CTkButton(master=self.frame_left, corner_radius=30,
                                                            fg_color="#FFCB42",
                                                            text="Vérifier le statut d'une voiture",
                                                            text_color="black", hover_color="#FFB200",
                                                            bg_color="transparent",
                                                            command=self.activate_check_car_status)
        self.check_status_car_btn.grid(row=12, column=0, padx=10, pady=10, sticky="ew")

        self.check_car_parc_btn = customtkinter.CTkButton(master=self.frame_left, corner_radius=30,
                                                          fg_color="#FFCB42",
                                                          text="Afficher le parc automobile",
                                                          text_color="black", hover_color="#FFB200",
                                                          bg_color="transparent",
                                                          command=self.activate_check_car_parc)
        self.check_car_parc_btn.grid(row=13, column=0, padx=10, pady=10, sticky="ew")

        self.check_list_locataire_btn = customtkinter.CTkButton(master=self.frame_left, corner_radius=30,
                                                                fg_color="#FFCB42",
                                                                text="Afficher la liste des locataires",
                                                                text_color="black", hover_color="#FFB200",
                                                                bg_color="transparent",
                                                                command=self.activate_list_locataire)
        self.check_list_locataire_btn.grid(row=14, column=0, padx=10, pady=10, sticky="ew")

        # ============ frame_right ============

        # configure grid layout (1x2)
        self.frame_right.rowconfigure(2, weight=1)
        self.frame_right.columnconfigure(0, weight=1)
        self.frame_right.grid_rowconfigure(0, minsize=10)

        self.home_label = customtkinter.CTkLabel(master=self.frame_right, corner_radius=20,
                                                 fg_color="transparent",
                                                 text="⭐ Bienvenue au programme de location de voiture! ⭐",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))

        self.home_label.grid(row=1, column=0, pady=20, padx=40, sticky="nsew")

        self.frame_cards = customtkinter.CTkFrame(master=self.frame_right, fg_color="transparent")

        self.frame_cards.grid(row=2, column=0, pady=20, padx=20, sticky="nsew")
        self.frame_cards.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing

        # ============ frame_cards ============

        # configure grid layout
        self.frame_cards.rowconfigure((1,), weight=1)
        self.frame_cards.columnconfigure((1,), weight=1)

        # ============ frame_for_menu_options ============

        self.add_voiture_frame = CustomFrame(self.frame_cards, 1, 1, "Ajouter une voiture", None,
                                             8, None)
        self.add_voiture_frame.grid_remove()

        self.edit_voiture_frame = CustomFrame(self.frame_cards, 1, 1, "Modifier une voiture", None,
                                              9, None)
        self.edit_voiture_frame.grid_remove()

        self.delete_voiture_frame = CustomFrame(self.frame_cards, 1, 1, "Supprimer une voiture", None,
                                                7, None)
        self.delete_voiture_frame.grid_remove()

        # *****************

        self.add_locataire_frame = CustomFrame(self.frame_cards, 1, 1, "Ajouter un locataire", None,
                                               7, None)
        self.add_locataire_frame.grid_remove()

        self.edit_locataire_frame = CustomFrame(self.frame_cards, 1, 1, "Modifier un locataire", None,
                                                9, None)
        self.edit_locataire_frame.grid_remove()

        self.delete_locataire_frame = CustomFrame(self.frame_cards, 1, 1, "Supprimer un locataire", None,
                                                  7, None)
        self.delete_locataire_frame.grid_remove()

        self.search_locataire_frame = CustomFrame(self.frame_cards, 1, 1, "chercher un locataire", None,
                                                  7, None)
        self.search_locataire_frame.grid_remove()

        # **************************

        self.rent_car_frame = CustomFrame(self.frame_cards, 1, 1, "Louer une voiture", None,
                                          7, None)
        self.rent_car_frame.grid_remove()

        self.return_car_frame = CustomFrame(self.frame_cards, 1, 1, "Rendre une voiture", None,
                                            7, None)
        self.return_car_frame.grid_remove()

        # ***********************

        self.check_car_status_frame = CustomFrame(self.frame_cards, 1, 1, "Verifier le statut d'une voiture", None,
                                                  7, None)
        self.check_car_status_frame.grid_remove()

        # ************************

        self.check_car_parc_frame = CustomFrame(self.frame_cards, 1, 1, "Afficher le parc automobile", None,
                                                7, None, False)
        self.check_car_parc_frame.grid_remove()
        self.result_frame = customtkinter.CTkFrame(master=self.check_car_parc_frame, fg_color="transparent")
        self.result_frame.grid(row=2, column=0, sticky="nsew", padx=15, pady=5)

        # ************************

        self.list_locataire_frame = CustomFrame(self.frame_cards, 1, 1, "Afficher la liste des locataires", None,
                                                7, None, False)
        self.list_locataire_frame.grid_remove()
        self.result_locataire_frame = customtkinter.CTkScrollableFrame(master = self.list_locataire_frame, fg_color="transparent")
        self.result_locataire_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        self.result_locataire_frame.grid_columnconfigure(0, weight=1)


        # ========== functions =============

    # =============== Frame Activation functions =================
    def activate_add_voiture(self):
        self.hide_all_frames()
        self.frame_cards.grid()
        self.add_voiture_frame.grid_appear()

        entry1 = customtkinter.CTkEntry(self.add_voiture_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Numéro d'immatriculation ")
        entry1.grid(row=2, column=0, padx=15, pady=5, sticky="nsew")

        entry2 = customtkinter.CTkEntry(self.add_voiture_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Marque ")
        entry2.grid(row=3, column=0, padx=15, pady=5, sticky="nsew")

        entry3 = customtkinter.CTkEntry(self.add_voiture_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Modèle ")
        entry3.grid(row=4, column=0, padx=15, pady=5, sticky="nsew")

        entry4 = customtkinter.CTkEntry(self.add_voiture_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Kilométrage")
        entry4.grid(row=5, column=0, padx=15, pady=5, sticky="nsew")

        entry5 = customtkinter.CTkEntry(self.add_voiture_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Prix de location ")
        entry5.grid(row=6, column=0, padx=15, pady=5, sticky="nsew")

        self.add_voiture_frame.button.configure(
            command=lambda: self.add_car(
                int(entry1.get().strip()),
                entry2.get(),
                entry3.get(),
                int(entry4.get().strip()),
                int(entry5.get().strip())
            )
        )

    def activate_edit_voiture(self):
        self.hide_all_frames()
        self.frame_cards.grid()
        self.edit_voiture_frame.grid_appear()
        label = customtkinter.CTkLabel(master=self.edit_voiture_frame, corner_radius=20,
                                       fg_color="transparent",
                                       text="Saisir le numero de voiture a modifier\nPour garder l'ancienne valeur,\ngarder la case vide.",
                                       font=customtkinter.CTkFont(size=17, weight="bold"),
                                       compound="left"
                                       )
        label.grid(row=2, column=0, pady=20, sticky="nsew", padx=20)

        entry1 = customtkinter.CTkEntry(self.edit_voiture_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Numéro d'immatriculation ")
        entry1.grid(row=3, column=0, padx=15, pady=5, sticky="nsew")

        entry2 = customtkinter.CTkEntry(self.edit_voiture_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Marque ")
        entry2.grid(row=4, column=0, padx=15, pady=5, sticky="nsew")

        entry3 = customtkinter.CTkEntry(self.edit_voiture_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Modèle ")
        entry3.grid(row=5, column=0, padx=15, pady=5, sticky="nsew")

        entry4 = customtkinter.CTkEntry(self.edit_voiture_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Kilométrage")
        entry4.grid(row=6, column=0, padx=15, pady=5, sticky="nsew")

        entry5 = customtkinter.CTkEntry(self.edit_voiture_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Prix de location ")
        entry5.grid(row=7, column=0, padx=15, pady=5, sticky="nsew")

        self.edit_voiture_frame.button.configure(
            command=lambda: self.edit_car(
                int(entry1.get().strip()),
                entry2.get(),
                entry3.get(),
                entry4.get(),
                entry5.get()
            )
        )



    def activate_delete_voiture(self):
        self.hide_all_frames()
        self.frame_cards.grid()
        self.delete_voiture_frame.grid_appear()

        entry1 = customtkinter.CTkEntry(self.delete_voiture_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Numéro d'immatriculation ")
        entry1.grid(row=2, column=0, padx=15, pady=5, sticky="nsew")

        self.delete_voiture_frame.button.configure(
            command=lambda: self.delete_car(
                int(entry1.get().strip()),

            ))

    def activate_add_locataire(self):
        self.hide_all_frames()
        self.frame_cards.grid()
        self.add_locataire_frame.grid_appear()

        entry1 = customtkinter.CTkEntry(self.add_locataire_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="ID Locataire ")
        entry1.grid(row=2, column=0, padx=15, pady=5, sticky="nsew")

        entry2 = customtkinter.CTkEntry(self.add_locataire_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Nom ")
        entry2.grid(row=3, column=0, padx=15, pady=5, sticky="nsew")

        entry3 = customtkinter.CTkEntry(self.add_locataire_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Prénom ")
        entry3.grid(row=4, column=0, padx=15, pady=5, sticky="nsew")

        entry4 = customtkinter.CTkEntry(self.add_locataire_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Adresse ")
        entry4.grid(row=5, column=0, padx=15, pady=5, sticky="nsew")

        self.add_locataire_frame.button.configure(
            command=lambda: self.add_locataire(
                int(entry1.get().strip()),
                entry2.get(),
                entry3.get(),
                entry4.get()

            ))

    def activate_edit_locataire(self):
        self.hide_all_frames()
        self.frame_cards.grid()
        self.edit_locataire_frame.grid_appear()
        label = customtkinter.CTkLabel(master=self.edit_locataire_frame, corner_radius=20,
                                       fg_color="transparent",
                                       text="Saisir l'ID de locataire a modifier\nPour garder l'ancienne valeur,\ngarder la case vide.",
                                       font=customtkinter.CTkFont(size=17, weight="bold"),
                                       compound="left"
                                       )
        label.grid(row=2, column=0, pady=20, sticky="nsew", padx=20)

        entry1 = customtkinter.CTkEntry(self.edit_locataire_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="ID Locataire ")
        entry1.grid(row=3, column=0, padx=15, pady=5, sticky="nsew")

        entry2 = customtkinter.CTkEntry(self.edit_locataire_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Nom ")
        entry2.grid(row=4, column=0, padx=15, pady=5, sticky="nsew")

        entry3 = customtkinter.CTkEntry(self.edit_locataire_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Prénom ")
        entry3.grid(row=5, column=0, padx=15, pady=5, sticky="nsew")

        entry4 = customtkinter.CTkEntry(self.edit_locataire_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Adresse ")
        entry4.grid(row=6, column=0, padx=15, pady=5, sticky="nsew")

        self.edit_locataire_frame.button.configure(
            command=lambda: self.edit_locataire(
                int(entry1.get().strip()),
                entry2.get(),
                entry3.get(),
                entry4.get()

            ))


    def activate_delete_locataire(self):
        self.hide_all_frames()
        self.frame_cards.grid()
        self.delete_locataire_frame.grid_appear()

        entry1 = customtkinter.CTkEntry(self.delete_locataire_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="ID Locataire ")
        entry1.grid(row=2, column=0, padx=15, pady=5, sticky="nsew")

        self.delete_locataire_frame.button.configure(
            command=lambda: self.delete_locataire(
                int(entry1.get().strip()),

            ))

    def activate_chercher_locataire(self):
        self.hide_all_frames()
        self.frame_cards.grid()
        self.search_locataire_frame.grid_appear()

        radio_var = tkinter.IntVar(value=0)

        radiobutton_1 = customtkinter.CTkRadioButton(master=self.search_locataire_frame, text="Recherche par ID",
                                                      variable=radio_var, value=1)
        radiobutton_1.grid(row=2, column=0, padx=15, pady=5, sticky="nsew")

        radiobutton_2 = customtkinter.CTkRadioButton(master=self.search_locataire_frame, text="Recherche par Nom",
                                                      variable=radio_var, value=2)
        radiobutton_2.grid(row=3, column=0, padx=15, pady=5,sticky="nsew")
        # radiobutton_1.select()
        entry1 = customtkinter.CTkEntry(self.search_locataire_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="saisir valeur ")
        entry1.grid(row=4, column=0, padx=15, pady=5, sticky="nsew")


        if radio_var.get() == 1:
            self.search_locataire_frame.button.configure(
                command=lambda: self.search_locataire_by_ID(
                    int(entry1.get().strip()),

                ))

        else:
            self.search_locataire_frame.button.configure(
                command=lambda: self.search_locataire_by_nom(
                   entry1.get()
                ))





    def activate_rent_car(self):
        self.hide_all_frames()
        self.frame_cards.grid()
        self.rent_car_frame.grid_appear()

        entry1 = customtkinter.CTkEntry(self.rent_car_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="ID Locataire ")
        entry1.grid(row=2, column=0, padx=15, pady=5, sticky="nsew")

        entry2 = customtkinter.CTkEntry(self.rent_car_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Numéro d'immatriculation ")
        entry2.grid(row=3, column=0, padx=15, pady=5, sticky="nsew")

        self.rent_car_frame.button.configure(
            command=lambda: self.rent_car(
                int(entry1.get().strip()),
                int(entry2.get().strip()),

            ))

    def activate_return_car(self):
        self.hide_all_frames()
        self.frame_cards.grid()
        self.return_car_frame.grid_appear()

        entry1 = customtkinter.CTkEntry(self.return_car_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="ID Locataire ")
        entry1.grid(row=2, column=0, padx=15, pady=5, sticky="nsew")

        entry2 = customtkinter.CTkEntry(self.return_car_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Numéro d'immatriculation ")
        entry2.grid(row=3, column=0, padx=15, pady=5, sticky="nsew")

        self.return_car_frame.button.configure(
            command=lambda: self.return_car(
                int(entry1.get().strip()),
                int(entry2.get().strip()),

            ))

    def activate_check_car_status(self):
        self.hide_all_frames()
        self.frame_cards.grid()
        self.check_car_status_frame.grid_appear()

        entry1 = customtkinter.CTkEntry(self.check_car_status_frame, state="normal", fg_color="#FFFFFF",
                                        placeholder_text="Numéro d'immatriculation ")
        entry1.grid(row=2, column=0, padx=15, pady=5, sticky="nsew")

        self.check_car_status_frame.button.configure(
            command=lambda: self.check_car(
                int(entry1.get().strip()),

            ))

    def activate_check_car_parc(self):
        self.hide_all_frames()
        self.frame_cards.grid()
        self.check_car_parc_frame.grid_appear()
        self.check_car_parc()

    def activate_list_locataire(self):
        self.hide_all_frames()
        self.frame_cards.grid()
        self.list_locataire_frame.grid_appear()
        self.list_locataire()

    # =============== Submit button functions =================
    def add_car(self, num_matriculation, marque, model, kilometrage, prix):
        result = self.manager.ajouter_voiture(num_matriculation, marque, model, kilometrage, prix)
        self.open_toplevel(result)

    def edit_car(self, num_matriculation, marque, model, kilometrage, prix):
        result = self.manager.modifier_voiture(num_matriculation, marque, model, kilometrage, prix)
        self.open_toplevel(result)

    def delete_car(self, num_matriculation):
        result = self.manager.supprimer_voiture(num_matriculation)
        self.open_toplevel(result)

    def add_locataire(self, id, nom, prenom, add):
        result = self.manager.ajouter_locataire(id, nom, prenom, add)
        self.open_toplevel(result)

    def edit_locataire(self, id, nom, prenom, add):
        result = self.manager.modifier_locataire(id, nom, prenom, add)
        self.open_toplevel(result)

    def delete_locataire(self, id):
        result = self.manager.supprimer_locataire(id)
        self.open_toplevel(result)


    def search_locataire_by_ID(self, id):
        loc = self.manager.recherche_locataire_par_id(id)
        if loc is None :
            self.open_toplevel("locataire introuvable")
        else:
            self.open_toplevel("ID "+ str(loc.id_loc) + " : " + loc.nom + " " + loc.prenom )

    def search_locataire_by_nom(self, nom):
        loc = self.manager.rechercher_locataire_par_nom(nom)
        if loc is None :
            self.open_toplevel("locataire introuvable")
        else:
            self.open_toplevel(loc.nom + " " + loc.prenom + " ( ID: " + str(loc.id_loc) + " )" )


    def check_car(self, num_matriculation):
        result = self.manager.verifier_statut_voiture(num_matriculation)
        self.open_toplevel(result)

    def rent_car(self, id, num_matriculation):
        result = self.manager.louer_voiture(num_matriculation, id)
        self.open_toplevel(result)

    def return_car(self, id, num_matriculation):
        result = self.manager.rendre_voiture(num_matriculation, id)
        self.open_toplevel(result)

    def check_car_parc(self):
        result = self.manager.afficher_parc_voitures()
        for widget in self.result_frame.winfo_children():
            widget.grid_remove()

        if result is None:
            label = customtkinter.CTkLabel(master=self.result_frame, corner_radius=20,
                                           fg_color="transparent",
                                           text="❌ il n'y a pas encore de voitures enregistrées.\n⭐ Enregistrez votre première voiture pour commencer!",
                                           font=customtkinter.CTkFont(size=20, weight="bold"),
                                           compound="left"
                                           )
            label.grid(row=2, column=0, pady=20, sticky="nsew", padx=20)

        else:
            label1 = customtkinter.CTkLabel(master=self.result_frame, corner_radius=20,
                                            fg_color="transparent",
                                            text="Nombre total de voiture est " + str(result["nbr_voiture"]),
                                            font=customtkinter.CTkFont(size=20, weight="bold"),
                                            compound="left"
                                            )
            label1.grid(row=2, column=0, pady=20, sticky="nsew", padx=20)

            label2 = customtkinter.CTkLabel(master=self.result_frame, corner_radius=20,
                                            fg_color="transparent",
                                            text="kilometrage moyen est " + str(result["kilometrage_moyen"]),
                                            font=customtkinter.CTkFont(size=20, weight="bold"),
                                            compound="left"
                                            )
            label2.grid(row=3, column=0, pady=20, sticky="nsew", padx=20)

    def list_locataire(self):
        result = self.manager.afficher_locataires()
        for widget in self.result_locataire_frame.winfo_children():
            widget.grid_remove()

        if result is None:
            label = customtkinter.CTkLabel(master=self.result_locataire_frame, corner_radius=20,
                                           fg_color="transparent",
                                           text="❌ Aucun locataire pour\nle moment",
                                           font=customtkinter.CTkFont(size=20, weight="bold"),
                                           compound="left"
                                           )
            label.grid(row=2, column=0, pady=20, sticky="nsew", padx=20)

        else:
            for index,loc in enumerate(result):
                label = customtkinter.CTkLabel(master=self.result_locataire_frame, corner_radius=20,
                                                fg_color="transparent",
                                                text= "✅ " + loc.nom + " " + loc.prenom,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                compound="left"
                                                )
                label.grid(row=index, column=0, pady=20, sticky="nsew", padx=20)




    # ================== Loopback functions ===============

    def open_toplevel(self, text):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(text)  # create window if its None or destroyed
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def go_to_home(self):
        self.hide_all_frames()
        self.frame_right.grid()
        self.frame_cards.grid()

    def hide_all_frames(self):
        for widget in self.frame_cards.winfo_children():
            widget.grid_remove()

        # self.frame_right.grid_remove()

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
