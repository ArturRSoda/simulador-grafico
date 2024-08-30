import tkinter as tk
from tkinter import ttk

class Frame(tk.Frame):
    def __init__(self, parent, width: int, height: int):
        super().__init__(parent, width=width, height=height, borderwidth=3, relief="groove")


class Label(tk.Label):
    def __init__(self, parent, text: str, size: int):
        super().__init__(parent, text=text, font=("Helvetica", size))

class Tab(ttk.Frame):
    def __init__(self, parent, width: int, height: int):
        super().__init__(parent, width=width, height=height, borderwidth=3, relief="ridge")

class NewObjWindow:
    def __init__(self):
        self.app = tk.Toplevel()
        self.app.title("New Object")
        self.app.geometry("400x400")

        self.tab_menu        : ttk.Notebook
        self.point_tab       : Tab
        self.line_tab        : Tab
        self.wireframe_tab   : Tab
        self.curve_tab       : Tab
        self.color_opt_frame : Frame
        self.color_opt_var   : tk.StringVar
        self.obj_name_var    : tk.StringVar
        self.tab_width       : int
        self.tab_height      : int

        self.add_name_obj_entry()
        self.add_color_buttons()
        self.add_tabs()
        self.add_button()


    def add_name_obj_entry(self):
        Label(self.app, "Name:", 10).place(x=10, y=15)

        self.obj_name_var = tk.StringVar()
        tk.Entry(self.app, textvariable=self.obj_name_var, width=35).place(x=60, y=10)

    def add_color_buttons(self):
        self.app.update()
        self.color_opt_frame = Frame(self.app, self.app.winfo_width()-20, 60)
        self.color_opt_frame.place(x=10, y=40)

        Label(self.color_opt_frame, "Color:", 10).place(x=10, y=10)

        self.color_opt_var = tk.StringVar(self.color_opt_frame, "Red")
        tk.Radiobutton(self.color_opt_frame, text="Red", variable=self.color_opt_var, value="Red").place(x=10, y=30)
        tk.Radiobutton(self.color_opt_frame, text="Blue", variable=self.color_opt_var, value="Blue").place(x=70, y=30)
        tk.Radiobutton(self.color_opt_frame, text="Green", variable=self.color_opt_var, value="Green").place(x=130, y=30)

    def add_tabs(self):
        self.tab_menu = ttk.Notebook(self.app)

        self.tab_width = self.app.winfo_width()-20
        self.tab_height = self.app.winfo_height()-self.color_opt_frame.winfo_height()-180

        self.add_point_tab()
        self.add_line_tab()
        self.add_wireframe_tab()
        self.add_curve_tab()

        self.tab_menu.place(x=10, y=105)

    def add_coord_frame(self, parent, x: int, y: int):
        fm = Frame(parent, width=160, height=50)
        fm.place(x=x, y=y)

        Label(fm, "X:", 10).place(x=10, y=15)
        tk.Entry(fm, width=4).place(x=30, y=10)
        
        Label(fm, "Y:", 10).place(x=80, y=15)
        tk.Entry(fm, width=4).place(x=100, y=10)


    def add_point_tab(self):
        self.point_tab = Tab(self.tab_menu, width=self.tab_width, height=self.tab_height)

        ttk.Label(self.point_tab, text="Coordinates").place(x=10, y=10)
        self.add_coord_frame(self.point_tab, 10, 30)

        self.tab_menu.add(self.point_tab, text="Point")

    def add_line_tab(self):
        self.line_tab = Tab(self.tab_menu, width=self.tab_width, height=self.tab_height)

        ttk.Label(self.line_tab, text="Start Coordinates").place(x=10, y=10)
        self.add_coord_frame(self.line_tab, 10, 30)

        ttk.Label(self.line_tab, text="End Coordinates").place(x=10, y=90)
        self.add_coord_frame(self.line_tab, 10, 110)

        self.tab_menu.add(self.line_tab, text="Line")

    def add_wireframe_tab(self):
        self.wireframe_tab = Tab(self.tab_menu, width=self.tab_width, height=self.tab_height)
        self.tab_menu.add(self.wireframe_tab, text="WireFrame")

    def add_curve_tab(self):
        self.curve_tab = Tab(self.tab_menu, width=self.tab_width, height=self.tab_height)
        self.tab_menu.add(self.curve_tab, text="Curve")

    def add_button(self):
        tk.Button(self.app, text="Add", command=self.add_object).place(x=100, y=self.app.winfo_height()-40)
        tk.Button(self.app, text="Cancel", command=self.cancel).place(x=230, y=self.app.winfo_height()-40)

    def add_object(self):
        pass

    def cancel(self):
        self.app.destroy()

class CGSystem():
    def __init__(self) -> None:
        self.app = tk.Tk()
        self.app.title("Computer Graphics System")
        self.app.geometry("1000x700")

        self.menu_frame        : Frame
        self.object_menu_frame : Frame
        self.window_menu_frame : Frame
        self.viewport_frame    : Frame
        self.messageBox_frame  : Frame
        self.messageBox        : tk.Listbox
        self.objects_list      : tk.Listbox
        self.canvas            : tk.Canvas
        self.pace_var          : tk.StringVar
        self.pace_entry        : tk.Entry
        self.viewport_width    : int
        self.viewport_height   : int

        self.add_menu()
        self.add_viewport()
        self.add_messagesBox()

    def run(self):
        self.app.mainloop()

    def add_viewport(self):
        self.app.update()
        width = self.app.winfo_width()-self.menu_frame.winfo_width()-20
        self.viewport_frame = Frame(self.app, width, 500)
        self.viewport_frame.place(x=self.menu_frame.winfo_width()+20, y=10)

        Label(self.viewport_frame, "Viewport", 10).place(x=10, y=10)

        self.app.update()
        self.viewport_height = self.viewport_frame.winfo_height()-70
        self.viewport_width = self.viewport_frame.winfo_width()-35
        self.canvas = tk.Canvas(self.viewport_frame, width=self.viewport_width, height=self.viewport_height, bg="white", borderwidth=5, relief="groove")
        self.canvas.place(x=10, y=30)

    def add_messagesBox(self):
        self.app.update()
        width = self.app.winfo_width()-self.menu_frame.winfo_width()-20
        height = self.app.winfo_height()-self.viewport_frame.winfo_height()-30
        self.messageBox_frame = Frame(self.app, width, height)
        self.messageBox_frame.place(x=self.menu_frame.winfo_width()+20, y=self.viewport_frame.winfo_height()+20)

        self.app.update()
        self.messageBox = tk.Listbox(self.messageBox_frame, width=72, height=8)
        self.messageBox.place(x=10, y=10)


    def add_menu(self):
        self.app.update()
        self.menu_frame = Frame(self.app, 300, self.app.winfo_height()-20)
        self.menu_frame.place(x=10, y=10)

        self.app.update()
        self.add_object_menu()
        self.add_window_menu()

    def add_object_menu(self):
        self.object_menu_frame = Frame(self.menu_frame, self.menu_frame.winfo_width()-26, 180)
        self.object_menu_frame.place(x=10, y=10)

        Label(self.object_menu_frame, "Objects", 10).place(x=10, y=10)

        self.objects_list = tk.Listbox(self.object_menu_frame, width=26, height=5)
        self.objects_list.place(x=10, y=30)

        tk.Button(self.object_menu_frame, text="Add", command=self.add_object).place(x=45, y=135)
        tk.Button(self.object_menu_frame, text="Del", command=self.del_object).place(x=145, y=135)

    def add_object(self):
        new_obj_window = NewObjWindow()
        self.add_message("Added object")

    def del_object(self):
        self.add_message("Deleted object")


    def add_window_menu(self):
        self.window_menu_frame = Frame(self.menu_frame, self.menu_frame.winfo_width()-26, 180)
        self.window_menu_frame.place(x=10, y=200)

        Label(self.window_menu_frame, "Window", 10).place(x=10, y=10)

        tk.Button(self.window_menu_frame, text="Up", command=self.move_window_up).place(x=40, y=40)
        tk.Button(self.window_menu_frame, text="Left", command=self.move_window_left).place(x=10, y=70)
        tk.Button(self.window_menu_frame, text="Right", command=self.move_window_right).place(x=62, y=70)
        tk.Button(self.window_menu_frame, text="Down", command=self.move_window_down).place(x=30, y=100)

        tk.Button(self.window_menu_frame, text="Zoom In", command=self.zoom_window_in).place(x=150, y=50)
        tk.Button(self.window_menu_frame, text="Zoom Out", command=self.zoom_window_out).place(x=150, y=90)

        Label(self.window_menu_frame, "Pace", 10).place(x=10, y=145)
        self.pace_var = tk.StringVar()
        self.pace_var.set("10")
        self.pace_entry = tk.Entry(self.window_menu_frame, textvariable=self.pace_var, width=4)
        self.pace_entry.place(x=50, y=140)


    def move_window_up(self):
        pace = self.pace_var.get()
        self.add_message("window moved up by %s" % pace)

    def move_window_down(self):
        pace = self.pace_var.get()
        self.add_message("window moved down by %s" % pace)

    def move_window_left(self):
        pace = self.pace_var.get()
        self.add_message("window moved left by %s" % pace)

    def move_window_right(self):
        pace = self.pace_var.get()
        self.add_message("window moved right by %s" % pace)

    def zoom_window_in(self):
        pace = self.pace_var.get()
        self.add_message("window zoomed in by %s" % pace)

    def zoom_window_out(self):
        pace = self.pace_var.get()
        self.add_message("window zoomed out by %s" % pace)

    def add_message(self, message: str):
        self.messageBox.insert(0, message)



sys = CGSystem()
sys.run()